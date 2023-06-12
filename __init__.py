from telethon import TelegramClient
import logging
import time


openai_key ="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"
api_id ="1125689"

api_hash="4772d1792ed194020a8fb06a91ffb8fa"

bot_token="5846650068:AAHv89DPjLjAvbMzO6caq50WNHns9inB5UI"

bot = TelegramClient("Himanshu_bot", api_id, api_hash).start(bot_token = bot_token)