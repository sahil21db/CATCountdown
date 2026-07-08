import os
import requests
from datetime import datetime, timezone, timedelta
from PIL import Image, ImageDraw, ImageFont

# 1. Calculate days remaining
target_date = datetime(2026, 11, 29, tzinfo=timezone.utc)
ist_now = datetime.now(timezone.utc) + timedelta(hours=5, minutes=30)
days_left = (target_date.date() - ist_now.date()).days

if days_left < 0:
    print("Exam date has passed.")
    exit()

# 2. Image Dimensions & Colors
width, height = 1200, 630
bg_color = (18, 18, 18)        # Dark matte background
card_bg = (13, 13, 13)         # Inner card background
grid_color = (28, 28, 28)      # Thin grid line color
green_text = (15, 196, 126)    # Bright cyber green
white_text = (240, 240, 240)   # Clean off-white
muted_text = (100, 100, 100)   # Status text color

# Create base canvas
img = Image.new("RGB", (width, height), bg_color)
draw = ImageDraw.Draw(img)

# Draw subtle grid lines (background pattern)
grid_size = 40
for x in range(0, width, grid_size):
    draw.line([(x, 0), (x, height)], fill=grid_color, width=1)
for y in range(0, height, grid_size):
    draw.line([(0, y), (width, y)], fill=grid_color, width=1)

# Draw inner border container
margin = 50
draw.rectangle(
    [(margin, margin), (width - margin, height - margin)],
    fill=card_bg,
    outline=(40, 40, 40),
    width=1
)

# 3. Load Fonts
# Using standard system fonts available on Ubuntu GitHub runner
try:
    font_large = ImageFont.truetype("DejaVuSans-Bold.ttf", 220)
    font_sub = ImageFont.truetype("DejaVuSans-Bold.ttf", 42)
    font_header = ImageFont.truetype("DejaVuSans-Bold.ttf", 32)
    font_status = ImageFont.truetype("DejaVuSans.ttf", 18)
except IOError:
    # Fallback if specific truetype isn't found
    font_large = font_sub = font_header = font_status = ImageFont.load_default()

# 4. Draw Header Strings
draw.text((340, 90), "> TARGET: CAT_2026", fill=green_text, font=font_header)
draw.text((440, 145), "STATUS: COUNTDOWN_ACTIVE", fill=muted_text, font=font_status)

# 5. Draw Countdown Numbers (with drop shadow)
num_str = str(days_left)
num_x, num_y = 600, 350

# Draw Drop Shadow
draw.text((num_x + 8, num_y + 8), num_str, fill=(0, 0, 0), font=font_large, anchor="mm")
# Draw Main text
draw.text((num_x, num_y), num_str, fill=green_text, font=font_large, anchor="mm")

# 6. Draw "DAYS REMAINING" pill button at the bottom
pill_w, pill_h = 330, 50
pill_x1 = (width - pill_w) // 2
pill_y1 = 475
pill_x2 = pill_x1 + pill_w
pill_y2 = pill_y1 + pill_h

draw.rectangle([(pill_x1, pill_y1), (pill_x2, pill_y2)], fill=green_text)
draw.text(
    ((pill_x1 + pill_x2) // 2, (pill_y1 + pill_y2) // 2),
    "DAYS REMAINING",
    fill=white_text,
    font=font_sub,
    anchor="mm"
)

# 7. Save Image Locally
image_path = "countdown.png"
img.save(image_path)

# 8. Send Image to Discord via Webhook
webhook_url = os.getenv("DISCORD_WEBHOOK_URL")
if webhook_url:
    with open(image_path, "rb") as f:
        response = requests.post(
            webhook_url,
            files={"file": (image_path, f, "image/png")},
            data={"content": f"📅 **CAT 2026 Daily Check-in:** {days_left} days to go."}
        )
    print(f"Webhook response: {response.status_code}")
else:
    print("Error: DISCORD_WEBHOOK_URL environment variable missing.")
