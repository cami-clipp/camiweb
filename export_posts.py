#!/usr/bin/env python3
import subprocess, os, time, re, shutil
from pathlib import Path
from PIL import Image

BASE = Path("/home/camila/Documentos/cami presentacion")
TMP  = BASE / "_tmp_exports"
TMP.mkdir(exist_ok=True)

def chrome_shot(html_path, png_path, w, h):
    subprocess.run([
        "google-chrome", "--headless=new", "--disable-gpu", "--no-sandbox",
        f"--window-size={w},{h}", f"--screenshot={png_path}",
        "--force-device-scale-factor=1", f"file://{html_path}"
    ], capture_output=True, timeout=30)
    time.sleep(1)

def to_jpeg(png, jpg):
    img = Image.open(png).convert("RGB")
    img.save(jpg, "JPEG", quality=95)
    print(f"  ✓ {Path(jpg).name}")

VOID = {'area','base','br','col','embed','hr','img','input','link','meta','param','source','track','wbr'}

def extract_div(html, div_id):
    start = html.find(f'id="{div_id}"')
    if start == -1:
        return None
    open_tag_start = html.rfind('<', 0, start)
    pos = open_tag_start
    depth = 0
    while pos < len(html):
        if html[pos] != '<':
            pos += 1; continue
        if html[pos:pos+4] == '<!--':
            pos = html.index('-->', pos) + 3; continue
        tag_end = html.index('>', pos)
        tag_content = html[pos+1:tag_end].strip()
        full_tag = html[pos:tag_end+1]
        if tag_content.startswith('/'):
            depth -= 1
            if depth == 0:
                return html[open_tag_start:tag_end+1]
        elif full_tag.endswith('/>'):
            pass  # self-closing
        else:
            tag_name = tag_content.split()[0].lower().rstrip('/')
            if tag_name not in VOID:
                depth += 1
        pos = tag_end + 1
    return None

def extract_css(src):
    m = re.search(r'<style>(.*?)</style>', src, re.DOTALL)
    return m.group(1) if m else ""

def standalone(css, div_html, w, h, bg):
    active_div = re.sub(r'class="(post|story)[^"]*"', lambda m: f'class="{m.group(1)} active"', div_html, count=1)
    return f"""<!DOCTYPE html><html><head><meta charset="UTF-8">
<link href="https://fonts.googleapis.com/css2?family=Playfair+Display:ital,wght@0,400;0,700;1,400&family=DM+Sans:wght@300;400;600&display=swap" rel="stylesheet">
<style>
*{{margin:0;padding:0;box-sizing:border-box;}}
body{{width:{w}px;height:{h}px;overflow:hidden;background:{bg};}}
{css}
.post,.story{{width:{w}px!important;height:{h}px!important;transform:none!important;position:relative!important;overflow:hidden!important;}}
.post.active,.story.active{{display:block;}}
</style></head><body>{active_div}</body></html>"""

# ── Posts ──
posts_src = (BASE / "posts/posts_virales_pack.html").read_text()
posts_css  = extract_css(posts_src)
post_bgs   = {1:"#FAF6F1",2:"#ffffff",3:"#ffffff",4:"#C4683A",
              5:"#ffffff",6:"#2B1F1A",7:"#EDE3D6",8:"#ffffff",
              9:"#FAF6F1",10:"#C4683A"}

print("Exportando posts 1–10...")
for n in range(1, 11):
    div = extract_div(posts_src, f"p{n}")
    if not div:
        print(f"  ✗ p{n} no encontrado"); continue
    html = standalone(posts_css, div, 1080, 1080, post_bgs[n])
    tmp_html = TMP / f"post_{n}.html"
    tmp_html.write_text(html)
    tmp_png  = TMP / f"post_{n}.png"
    chrome_shot(str(tmp_html), str(tmp_png), 1080, 1080)
    if tmp_png.exists():
        to_jpeg(str(tmp_png), str(BASE / f"camiclipp_post_{n:02d}.jpg"))
    else:
        print(f"  ✗ screenshot falló post {n}")

# ── Stories ──
story_src = (BASE / "story cami/stories_interactivas.html").read_text()
story_css  = extract_css(story_src)
story_bgs  = {1:"#FAF6F1", 2:"#ffffff", 3:"#2B1F1A"}

print("\nExportando stories 1–3...")
for n in range(1, 4):
    div = extract_div(story_src, f"s{n}")
    if not div:
        print(f"  ✗ s{n} no encontrado"); continue
    if n == 3:
        div = re.sub(r'class="story[^"]*"', 'class="story active step2"', div, count=1)
    html = standalone(story_css, div, 1080, 1920, story_bgs[n])
    tmp_html = TMP / f"story_{n}.html"
    tmp_html.write_text(html)
    tmp_png  = TMP / f"story_{n}.png"
    chrome_shot(str(tmp_html), str(tmp_png), 1080, 1920)
    if tmp_png.exists():
        to_jpeg(str(tmp_png), str(BASE / f"camiclipp_story_{n:02d}.jpg"))
    else:
        print(f"  ✗ screenshot falló story {n}")

shutil.rmtree(TMP)
print("\nListo.")
