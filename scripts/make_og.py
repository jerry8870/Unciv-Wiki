#!/usr/bin/env python3
"""生成默认 OG 社交分享图 (1200x630)，供 og:image / twitter:image 使用。

用法:
    python3 scripts/make_og.py
"""
from PIL import Image, ImageDraw, ImageFont
from pathlib import Path

W, H = 1200, 630
OUT = Path(__file__).resolve().parent.parent / "public" / "og-default.png"
FONT = "/System/Library/Fonts/Helvetica.ttc"


def vgrad(top, bottom):
    img = Image.new("RGB", (W, H))
    px = img.load()
    for y in range(H):
        t = y / (H - 1)
        c = tuple(int(top[i] * (1 - t) + bottom[i] * t) for i in range(3))
        for x in range(W):
            px[x, y] = c
    return img


def main():
    img = vgrad((27, 33, 56), (13, 16, 32))
    d = ImageDraw.Draw(img)

    title_font = ImageFont.truetype(FONT, 132, index=0)
    sub_font = ImageFont.truetype(FONT, 46, index=0)
    foot_font = ImageFont.truetype(FONT, 30, index=0)

    GOLD = (245, 197, 66)
    LIGHT = (201, 207, 224)
    MUTE = (150, 160, 190)

    def center(text, font, y, fill):
        bbox = d.textbbox((0, 0), text, font=font)
        w = bbox[2] - bbox[0]
        d.text(((W - w) // 2, y), text, font=font, fill=fill)

    # 顶部装饰短线
    d.rectangle([W // 2 - 60, 188, W // 2 + 60, 192], fill=GOLD)
    center("Unciv Wiki", title_font, 210, GOLD)
    center("Community guide & database for Unciv", sub_font, 378, LIGHT)
    center("Unciv4iOS", foot_font, 562, MUTE)

    OUT.parent.mkdir(parents=True, exist_ok=True)
    img.save(OUT)
    print(f"wrote {OUT} ({W}x{H})")


if __name__ == "__main__":
    main()
