# Telegram Channel Bot

This project is a Telegram bot designed to create a new channel, invite a user to the channel, monitor messages from users, and send responses based on user input. The bot is built using the `Telethon` library and telegram API.

## Features

- **Channel Creation**: The bot can create a new Telegram channel.
- **Invite Members**: The bot invites specified users to the channel.
- **Assign Admin**: The bot is automatically added as an admin to the channel with specific permissions.
- **Monitor Messages**: The bot monitors messages in the channel, waiting for specific inputs from users.
- **Conditional Responses**: The bot sends different messages based on the conditions met (e.g., both users sending "ready").

## Prerequisites

- **Python 3.7+**: Ensure you have Python installed.
- **Telegram API Credentials**: You need to have a Telegram API ID, API Hash, and a bot token.

## Installation

1. **Clone the repository**:

   ```bash
     git clone https://github.com/yourusername/telegram-channel-bot.git
     cd telegram-channel-bot
2.**Install the required dependencies**: 
   
      pip install -r requirements.txt

3. **Setup your environment**:
add to your .env file the folowing:
 (YOUR_API_ID, YOUR_API_HASH, YOUR_BOT_TOKEN, YOUR_PHONE_NUMBER, YOUR_BOT_USERNAME, TELEGRAM_USER.) with your actual credentials.

## usage:
-run the command:
```bash
  python main.py


  





