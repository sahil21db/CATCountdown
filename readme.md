# CAT 2026 Daily Discord Countdown Bot

An automated Discord countdown bot that generates a stylized cyber-grid image displaying the exact number of days remaining until the CAT 2026 exam (November 29, 2026). The bot automatically posts the updated graphic to a designated Discord channel every morning at 9:00 AM IST using GitHub Actions.

## Features

- **Automated Scheduling:** Runs completely free on GitHub cloud infrastructure every day at 9:00 AM IST (03:30 UTC).
- **Dynamic Image Generation:** Uses Python's `Pillow` library to construct a custom image with drop-shadow typography and clean design layers on every run.
- **Auto-Sizing Layout:** Dynamically calculates the bounding box of text elements to prevent layout clipping.
- **Secure Configuration:** Keeps your Discord Webhook URL hidden safely using GitHub Repository Secrets.

## File Structure

```text
├── .github/
│   └── workflows/
│       └── daily_reminder.yml   # GitHub Actions automation schedule
├── countdown.py                 # Core image generation and webhook execution logic
└── README.md                    # Setup documentation


Setup Instructions
1. Discord Webhook Setup
Open Discord and go to your server's #general channel settings (gear icon).

Select Integrations > Webhooks > New Webhook.

Name your webhook (e.g., CAT 2026 Countdown) and copy the Webhook URL.

2. GitHub Secrets Configuration
Go to your GitHub repository.

Click Settings > Secrets and variables > Actions.

Click New repository secret.

Name the secret exactly: DISCORD_WEBHOOK_URL

Paste your copied Discord Webhook URL into the value field and save.

3. Adding the Code
Add the codebase into your repository files:

Copy the optimized script code into countdown.py.

Copy the workflow definition into .github/workflows/daily_reminder.yml.

Testing the Bot Manually
You don't have to wait until 9:00 AM to see if it works.

Navigate to the Actions tab in your GitHub repository.

Select Daily CAT Countdown from the left sidebar.

Click the Run workflow dropdown on the right side and click the green Run workflow button.

This will trigger an immediate test broadcast to your Discord channel.
