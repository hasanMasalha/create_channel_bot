import os
import requests
from telegram import Update
import json 
from dotenv import load_dotenv
from telegram.ext import CallbackContext
from telethon import TelegramClient, events,functions
api_id = '27293743'
api_hash = 'd10bd374ed20fc4866132cea8f58edfb'
bot_token = '7347498031:AAHyFgo712sWO0yEQc6uGhpA6CbfQxVZ3E0'

load_dotenv()

server_url = os.getenv('SERVER_URL')


async def start_command(update: Update, context: CallbackContext) -> None:
    await update.message.reply_text(f'Hi. I\'m {context.bot.first_name}. How may I help you today?')


async def create(update: Update, context: CallbackContext) -> None:
        client = TelegramClient('user_session13', api_id, api_hash)
        await client.start(phone='+972509010126')
        user_id = update.effective_user.id
        print(user_id)
    # Create a new channel using the CreateChannelRequest function
        result = await client(functions.channels.CreateChannelRequest(
        title='My_awesome_title2231',
        about='some string here',
        megagroup=True,  # True for a supergroup, False for a regular channel
        for_import=False,  # Set to True if you want to create the channel for importing messages
        forum=False,  # Set to True if you want the channel to have forum features (if applicable)
    ))

    # Extract the channel information
        new_channel = result.chats[0]
    

    # Assign a username to the channel
        username = new_channel.title  # Replace with the desired username
        channel_link = f"https://t.me/{username}"

        invite = await client(functions.messages.ExportChatInviteRequest(
        peer=new_channel.id
    ))
    
        # Print and return the invite link
        print(new_channel.id)
        invite_link = invite.link
        save_channel_link(new_channel.id, invite_link,user_id)
        await update.message.reply_text(invite_link)

def save_channel_link(channel_id, link, user_id, filename='channels.json'):
    # Create a dictionary with the channel ID as the key and link as the value
    channel_data = {
        channel_id: {
            "link": link,
            "user_id": user_id
        }
    }

    # Check if the file exists and is not empty
    if os.path.exists(filename) and os.path.getsize(filename) > 0:
        try:
            with open(filename, 'r') as file:
                data = json.load(file)
        except json.JSONDecodeError:
            print(f"Warning: {filename} is not a valid JSON file. Starting with an empty file.")
            data = {}
    else:
        data = {}

    # Update the data with the new channel data
    data.update(channel_data)

    # Save the updated data back to the file
    with open(filename, 'w') as file:
        json.dump(data, file, indent=4)
    
    print(f"Channel {channel_id} with link {link} and user ID {user_id} saved successfully.")