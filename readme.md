# CAT 2026 Daily Discord Countdown Bot

An automated Discord countdown that overlays the days remaining until the CAT 2026 exam (November 29, 2026) onto a styled banner template and posts it to a Discord channel every morning at 9:00 AM IST using GitHub Actions.

## Features

- **Automated Scheduling:** Runs completely free on GitHub cloud infrastructure every day at 9:00 AM IST (03:30 UTC).
- **Template-Based Image Generation:** Overlays the countdown number onto a custom banner template (`assets/banner_base.png`) using a bundled font (`assets/font.ttf`), with drop-shadow typography.
- **In-Memory Processing:** Generates and sends the image entirely in memory — no temp files written to disk.
- **Secure Configuration:** Keeps your Discord Webhook URL hidden safely using GitHub Repository Secrets.

## File Structure

```text
├── .github/
│   └── workflows/
│       └── daily_reminder.yml   # GitHub Actions cron schedule
├── assets/
│   ├── banner_base.png          # Base banner template image
│   └── font.ttf                 # Custom font for countdown text
├── countdown.py                 # Webhook-based countdown script (used by GitHub Actions)
└── readme.md                    # This file
```

## Setup Instructions

### 1. Discord Webhook Setup

1. Open Discord and go to your server's channel settings (gear icon).
2. Select **Integrations > Webhooks > New Webhook**.
3. Name your webhook (e.g., `CAT 2026 Countdown`) and copy the **Webhook URL**.

### 2. GitHub Secrets Configuration

1. Go to your GitHub repository.
2. Click **Settings > Secrets and variables > Actions**.
3. Click **New repository secret**.
4. Name the secret exactly: `DISCORD_WEBHOOK_URL`
5. Paste your copied Discord Webhook URL into the value field and save.

### 3. Customizing the Banner

- Replace `assets/banner_base.png` with your own template image. The countdown number will be centered on it.
- Replace `assets/font.ttf` with any `.ttf` font file to change the number styling.

## Testing Manually

You don't have to wait until 9:00 AM to see if it works.

1. Navigate to the **Actions** tab in your GitHub repository.
2. Select **Daily CAT Countdown** from the left sidebar.
3. Click the **Run workflow** dropdown on the right side and click the green **Run workflow** button.

This will trigger an immediate test broadcast to your Discord channel.