import io
import os
import requests
from datetime import datetime, timezone, timedelta
from PIL import Image, ImageDraw, ImageFont

# ── Configuration ────────────────────────────────────────────────────────────

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
FONT_PATH = os.path.join(SCRIPT_DIR, "assets", "font.ttf")
BANNER_PATH = os.path.join(SCRIPT_DIR, "assets", "banner_base.png")

COUNTDOWN_FONT_SIZE = 250
TEXT_SHADOW_OFFSET = 8
TEXT_Y_NUDGE = -20
SHADOW_COLOR = (0, 0, 0, 150)
TEXT_COLOR = (16, 185, 129, 255)  # Terminal green

# ── Calculate days remaining ─────────────────────────────────────────────────

target_date = datetime(2026, 11, 29, tzinfo=timezone.utc)
ist_now = datetime.now(timezone.utc) + timedelta(hours=5, minutes=30)
days_left = (target_date.date() - ist_now.date()).days

if days_left < 0:
    print("Exam date has passed.")
    exit()

# ── Generate countdown image ─────────────────────────────────────────────────

if not os.path.exists(BANNER_PATH):
    raise FileNotFoundError(
        f"Base banner '{BANNER_PATH}' not found. "
        "Place a banner_base.png in the assets/ directory."
    )

img = Image.open(BANNER_PATH)
draw = ImageDraw.Draw(img)

try:
    font = ImageFont.truetype(FONT_PATH, COUNTDOWN_FONT_SIZE)
except IOError:
    print("WARNING: Custom font not found, falling back to default.")
    font = ImageFont.load_default()

text = str(days_left)
bbox = draw.textbbox((0, 0), text, font=font)
text_w = bbox[2] - bbox[0]
text_h = bbox[3] - bbox[1]
x = (img.width - text_w) / 2
y = (img.height - text_h) / 2 + TEXT_Y_NUDGE

# Drop shadow
draw.text((x + TEXT_SHADOW_OFFSET, y + TEXT_SHADOW_OFFSET), text, font=font, fill=SHADOW_COLOR)
# Main text
draw.text((x, y), text, font=font, fill=TEXT_COLOR)

# ── Send to Discord via webhook ──────────────────────────────────────────────

buf = io.BytesIO()
img.save(buf, format="PNG")
buf.seek(0)

webhook_url = os.getenv("DISCORD_WEBHOOK_URL")
if webhook_url:
    response = requests.post(
        webhook_url,
        files={"file": ("countdown.png", buf, "image/png")},
        data={"content": f"**{days_left} Days until CAT 2026!**\nKeep grinding, stay focused, and make today count. Let's get it! 🚀"}
    )
    print(f"Webhook response: {response.status_code}")
else:
    print("Error: DISCORD_WEBHOOK_URL environment variable missing.")
