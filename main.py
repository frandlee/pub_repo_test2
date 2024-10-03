import os
from slack_sdk.webhook import WebhookClient

# Define slackMsg as a dictionary to store the send function
slackMsg = {}

# Get the Slack Webhook URL from environment variables
webhook_url = os.getenv('SLACK_WEBHOOK_URL')
webhook = WebhookClient(webhook_url)

# Define the send function to send a message to the Slack webhook
async def send_message(msg):
    response = await webhook.send(
        text=msg
    )
    if response.status_code != 200:
        raise Exception(f"Failed to send message: {response.status_code}, {response.body}")

# Assign the function​⬤