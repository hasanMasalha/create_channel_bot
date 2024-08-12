
import os
import requests
from telegram import Update
import json 
from dotenv import load_dotenv
from telegram.ext import CallbackContext
from telethon import TelegramClient, events,functions,types
async def add_bot_as_admin(client, channel_id, bot_username):
    # Invite the bot to the channel
    await client(functions.channels.InviteToChannelRequest(
        channel=channel_id,
        users=[bot_username]
    ))

    # Promote the bot to admin
    await client(functions.channels.EditAdminRequest(
        channel=channel_id,
        user_id=bot_username,
        admin_rights=types.ChatAdminRights(
            post_messages=True,
            add_admins=False,
            change_info=False,
            delete_messages=False,
            ban_users=False,
            invite_users=True,
            pin_messages=True,
            edit_messages=True,
            manage_call=True
        ),
        rank='Admin'  # You can give the bot a rank name (optional)
    ))

    print(f"Bot {bot_username} added as admin")

async def send_message_to_channel(client, channel_id, message):

    async with client:
        await client.send_message(channel_id, message)


async def invite_members_to_channel(bot, channel_id, user):
    # Ensure the bot is connected
    if not bot.is_connected():
        await bot.connect()

    await bot(functions.channels.InviteToChannelRequest(
        channel=channel_id,
        users=[user]
    ))


async def check_users_and_monitor_ready_messages(bot, channel_id):
    # Get the participants in the channel
    participants = await bot.get_participants(channel_id)
    
    if len(participants) != 3:
        await send_message_to_channel(bot, channel_id, "There must be exactly two participants in the channel.")
        return

    user1 = participants[0]
    user2 = participants[1]
    print(f"Monitoring messages from {user1.username} and {user2.username}")

    ready_users = set()

    @bot.on(events.NewMessage(chats=channel_id))
    async def handler(event):
        if event.sender_id in [user1.id, user2.id] and event.text.lower() == "ready":
            ready_users.add(event.sender_id)
            if len(ready_users) == 2:
                await send_message_to_channel(bot, channel_id, "Both users are ready! Proceeding with the next step.")
                ready_users.clear()  # Reset for future checks