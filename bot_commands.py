import os
import requests
from telegram import Update
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

    # Create a new channel using the CreateChannelRequest function
        result = await client(functions.channels.CreateChannelRequest(
        title='My_awesome_title15171',
        about='some string here',
        megagroup=True,  # True for a supergroup, False for a regular channel
        for_import=False,  # Set to True if you want to create the channel for importing messages
        forum=False,  # Set to True if you want the channel to have forum features (if applicable)
    ))

    # Extract the channel information
        new_channel = result.chats[0]
        print(new_channel)
        print(f"Channel ID: {new_channel.id}")
        print(f"Channel Title: {new_channel.title}")

    # Assign a username to the channel
        username = new_channel.title  # Replace with the desired username
        print(new_channel)
        channel_link = f"https://t.me/{username}"
        print(channel_link)


        invite = await client(functions.messages.ExportChatInviteRequest(
        peer=new_channel.id
    ))
    
        # Print and return the invite link
        invite_link = invite.link
        print(f"Invite Link: {invite_link}")
        await update.message.reply_text(invite_link)
