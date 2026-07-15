---
name: rn-wechat-extract
description: "Extract full text from WeChat public account articles (mp.weixin.qq.com). Use when the user provides a WeChat article URL and asks for 提取文章, 抓取公众号, 读一下这篇, or when another skill needs to read a WeChat article before processing. Bypasses WeChat's access control via MicroMessenger UA spoofing. Stdlib only, no API key required."
---

# RN WeChat Extract

Extract the full text of a WeChat public account article into clean Markdown.

This skill is a **source reader** — it extracts and returns text. It does not summarize, rewrite, translate, or produce video.

## How It Works

WeChat blocks external access to public account articles through User-Agent detection: the server checks for the `MicroMessenger` keyword and rejects normal browser requests.

This skill sends HTTP requests with a genuine WeChat iOS WebView User-Agent and the correct Referer header, which is sufficient to receive the full article HTML. No login, cookie, or API key is needed.

**Extracts:** title, author, publish time, and body text as Markdown.

**Limitations:**
- Some heavily JS-rendered articles may return partial content
- Rapid successive calls from the same IP may trigger CAPTCHA (wait and retry)
- Does not work on login-gated or paid articles

**Enhanced Versions:**
- `fetch_wechat_with_images.py` - Downloads images only
- `fetch_wechat_with_media.py` - Downloads both images and videos
- Images saved to `{title}_images/` directory
- Videos saved to `{title}_videos/` directory
- Markdown references updated to local paths

## Locate The Skill

```bash
WX_HOME="$(
  for d in "$(pwd)/.codex/skills/rn-wechat-extract" \
           "$(pwd)/.agents/skills/rn-wechat-extract" \
           "$(pwd)/.claude/skills/rn-wechat-extract" \
           "$(pwd)/rnskill/skills/rn-wechat-extract" \
           "$HOME/.codex/skills/rn-wechat-extract" \
           "$HOME/.agents/skills/rn-wechat-extract" \
           "$HOME/.claude/skills/rn-wechat-extract"; do
    [ -f "$d/SKILL.md" ] && echo "$d" && break
  done
)"
export WX_HOME
```

## Workflow

1. Health check (optional):

   ```bash
   python3 "$WX_HOME/scripts/fetch_wechat.py" --doctor
   ```

2. Extract article:

   ```bash
   python3 "$WX_HOME/scripts/fetch_wechat.py" "<mp.weixin.qq.com URL>" \
     --output-dir "<desired output directory>"
   ```

3. The script prints a JSON result to stdout:

   ```json
   {
     "status": "ok",
     "title": "文章标题",
     "author": "公众号名称",
     "publish_time": "2026-07-14 00:18",
     "char_count": 7025,
     "output_path": "path/to/extracted.md"
   }
   ```

4. Read the output file and present the full text or pass it to the next skill.

5. On failure:
   - Exit 1 (fetch/CAPTCHA): suggest retry after a few minutes or ask the user to paste text
   - Exit 2 (parse failure): rerun with `--raw` to save HTML for debugging

## Command Reference

### Basic Version (text only)

```
fetch_wechat.py <url> [options]

Arguments:
  url                    mp.weixin.qq.com article URL

Options:
  --output-dir <dir>     Output directory (default: current directory)
  --raw                  Also save the raw HTML alongside the Markdown
  --doctor               Check dependencies and exit
```

### Enhanced Version (images only)

```
fetch_wechat_with_images.py <url> [options]

Arguments:
  url                    mp.weixin.qq.com article URL

Options:
  --output-dir <dir>     Output directory (default: current directory)
  --no-images            Skip image download
  --raw                  Also save the raw HTML alongside the Markdown
  --doctor               Check dependencies and exit
```

### Enhanced Version (images + videos)

```
fetch_wechat_with_media.py <url> [options]

Arguments:
  url                    mp.weixin.qq.com article URL

Options:
  --output-dir <dir>     Output directory (default: current directory)
  --no-images            Skip image download
  --no-videos            Skip video download
  --raw                  Also save the raw HTML alongside the Markdown
  --doctor               Check dependencies and exit
```

**Output structure (with media):**
```
output/
├── 2026-07-15-article-title.md
├── 2026-07-15-article-title.raw.html  (if --raw)
├── 2026-07-15-article-title_images/
│   ├── image_01.jpg
│   ├── image_02.jpg
│   └── ...
└── 2026-07-15-article-title_videos/
    ├── video_01.mp4
    ├── video_02.mp4
    └── ...
```

No external dependencies — Python stdlib only (`urllib`, `re`, `html`, `json`).

## Integration Examples

This skill provides text for any downstream content workflow:

| Scenario | Call chain |
|---|---|
| Rewrite article into video script | rn-wechat-extract → rewrite skill |
| Save article as topic idea | rn-wechat-extract → topic management |
| Read and discuss an article | rn-wechat-extract (standalone) |
| Turn article into image cards | rn-wechat-extract → content adaptation |
| Extract article with images | rn-wechat-extract (with_images) |
| Extract article with full media | rn-wechat-extract (with_media) |

## Enhanced Versions

| Version | Images | Videos | Use Case |
|---------|--------|--------|----------|
| Original | ❌ | ❌ | Text-only extraction |
| with_images | ✅ | ❌ | Articles with important images |
| with_media | ✅ | ✅ | Articles with videos |

### Usage Examples

```bash
# Text only (original)
python3 "$WX_HOME/scripts/fetch_wechat.py" "<url>" --output-dir "./output"

# With images
python3 "$WX_HOME/scripts/fetch_wechat_with_images.py" "<url>" --output-dir "./output"

# With images and videos
python3 "$WX_HOME/scripts/fetch_wechat_with_media.py" "<url>" --output-dir "./output"
```

### Technical Details

**Images:**
- WeChat uses lazy-loaded `data-src` attributes
- Script extracts URLs and downloads with WeChat headers
- Images saved to `{title}_images/` directory

**Videos:**
- Videos hosted on `mpvideo.qpic.cn`
- Script extracts MP4 URLs from JavaScript
- Videos saved to `{title}_videos/` directory
- Some videos may require authentication (403 errors)
