#!/usr/bin/env python3
"""Compare a reference and candidate video with hashes plus PSNR/SSIM."""

from __future__ import annotations

import argparse
import hashlib
import json
import shutil
import subprocess
from pathlib import Path


def run(cmd: list[str], check: bool = True) -> subprocess.CompletedProcess[str]:
    return subprocess.run(cmd, check=check, text=True, capture_output=True)


def sha256(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as f:
        for chunk in iter(lambda: f.read(1024 * 1024), b""):
            h.update(chunk)
    return h.hexdigest()


def ffprobe(path: Path) -> dict:
    result = run(
        [
            "ffprobe",
            "-v",
            "error",
            "-show_entries",
            "format=duration,size,bit_rate",
            "-show_entries",
            "stream=index,codec_type,codec_name,width,height,r_frame_rate,channels",
            "-of",
            "json",
            str(path),
        ]
    )
    return json.loads(result.stdout)


def videos_cmp(a: Path, b: Path) -> bool:
    return run(["cmp", "-s", str(a), str(b)], check=False).returncode == 0


def metric(reference: Path, candidate: Path, outdir: Path, name: str) -> str:
    log = outdir / f"{name}.log"
    expr = f"[0:v][1:v]{name}=stats_file={log}"
    result = run(
        [
            "ffmpeg",
            "-hide_banner",
            "-nostats",
            "-i",
            str(reference),
            "-i",
            str(candidate),
            "-lavfi",
            expr,
            "-f",
            "null",
            "-",
        ],
        check=False,
    )
    combined = (result.stderr or "") + "\n" + (result.stdout or "")
    lines = [line.strip() for line in combined.splitlines() if name.upper() in line or f"Parsed_{name}" in line]
    return lines[-1] if lines else combined.strip().splitlines()[-1]


def write_report(outdir: Path, data: dict) -> Path:
    report = outdir / "comparison-report.md"
    lines = [
        "# Video Comparison Report",
        "",
        "## Files",
        "",
        f"- Reference: `{data['reference']}`",
        f"- Candidate: `{data['candidate']}`",
        "",
        "## Hash / Bit Exact",
        "",
        f"- Reference SHA-256: `{data['reference_sha256']}`",
        f"- Candidate SHA-256: `{data['candidate_sha256']}`",
        f"- Byte-identical cmp: `{data['bit_exact']}`",
        "",
        "## Video Metrics",
        "",
        f"- PSNR: `{data.get('psnr', 'not run')}`",
        f"- SSIM: `{data.get('ssim', 'not run')}`",
        "",
        "## Media Info",
        "",
        "```json",
        json.dumps({"reference": data["reference_probe"], "candidate": data["candidate_probe"]}, indent=2),
        "```",
        "",
    ]
    report.write_text("\n".join(lines), encoding="utf-8")
    return report


def main() -> None:
    parser = argparse.ArgumentParser(description="Compare reference and candidate video files.")
    parser.add_argument("reference", type=Path)
    parser.add_argument("candidate", type=Path)
    parser.add_argument("--out", type=Path, required=True)
    parser.add_argument("--skip-metrics", action="store_true")
    args = parser.parse_args()

    if shutil.which("ffmpeg") is None or shutil.which("ffprobe") is None:
        raise SystemExit("ffmpeg and ffprobe are required")

    outdir = args.out.expanduser().resolve()
    outdir.mkdir(parents=True, exist_ok=True)
    reference = args.reference.expanduser().resolve()
    candidate = args.candidate.expanduser().resolve()

    data = {
        "reference": str(reference),
        "candidate": str(candidate),
        "reference_sha256": sha256(reference),
        "candidate_sha256": sha256(candidate),
        "bit_exact": videos_cmp(reference, candidate),
        "reference_probe": ffprobe(reference),
        "candidate_probe": ffprobe(candidate),
    }

    if not args.skip_metrics:
        data["psnr"] = metric(reference, candidate, outdir, "psnr")
        data["ssim"] = metric(reference, candidate, outdir, "ssim")

    (outdir / "comparison.json").write_text(json.dumps(data, indent=2), encoding="utf-8")
    report = write_report(outdir, data)
    print(json.dumps({"report": str(report), "bit_exact": data["bit_exact"]}, indent=2))


if __name__ == "__main__":
    main()
