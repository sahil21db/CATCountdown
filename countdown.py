import os
import requests
from datetime import datetime, timezone, timedelta

# CAT 2026 Exam Date
target_date = datetime(2026, 11, 29, tzinfo=timezone.utc)
# Current time in IST (UTC+5:30)
ist_now = datetime.now(timezone.utc) + timedelta(hours=5, minutes=30)
days_left = (target_date.date() - ist_now.date()).days

if days_left >= 0:
    payload = {
        "content": f"🚨 **CAT 2026 Countdown** 🚨\n⏳ Only **{days_left} days** left until the exam! Make today count."
    }
    webhook_url = os.getenv("DISCORD_WEBHOOK_URL")
    requests.post(webhook_url, json=payload)
