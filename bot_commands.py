import os
import requests
from telegram import Update
import json 
from dotenv import load_dotenv
from telegram.ext import CallbackContext
from telethon import TelegramClient, events,functions,types
from db.db_manager import save_channel_link
from manage_channel import add_bot_as_admin,send_message_to_channel,invite_members_to_channel,check_users_and_monitor_ready_messages
api_id =os.getenv('API_ID')
api_hash =os.getenv('API_HASH')
bot_token =os.getenv('BOT_TOKEN')
phone = os.getenv('PHONE_NUMBER')
bot_username = os.getenv('BOT_USERNAME')

load_dotenv()
server_url = os.getenv('SERVER_URL')

async def start_command(update: Update, context: CallbackContext) -> None:
    await update.message.reply_text(f'Hi. I\'m {context.bot.first_name}. this is a start message')


async def create(update: Update, context: CallbackContext) -> None:
        client = TelegramClient('user_session13', api_id, api_hash)
        await client.start(phone)
        user_id = update.effective_user.id
        result = await client(functions.channels.CreateChannelRequest(
        title='My_awesome_title22390',
        about='some string here',
        megagroup=True,  
        for_import=False,  
        forum=False,  
    ))

        new_channel = result.chats[0]
    

        username = new_channel.title  
        channel_link = f"https://t.me/{username}"

        invite = await client(functions.messages.ExportChatInviteRequest(
        peer=new_channel.id
    ))
        
        invite_link = invite.link
        save_channel_link(new_channel.id, invite_link,user_id)
        await add_bot_as_admin(client, new_channel.id, bot_username)
        await update.message.reply_text(invite_link)
        await send_message_to_channel(client, new_channel.id,'hello from bot')
        await invite_members_to_channel(client,new_channel.id,'@jawadma14')
        await check_users_and_monitor_ready_messages(client,new_channel.id)
