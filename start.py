from .. import bot,openai_key
from telethon import events 
import asyncio 
import openai

openai_key="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"
openai.my_api_key = openai_key 

@bot.on(events.NewMessage(incoming=True,pattern = "/start"))
async def start(event):
  await event.reply("Hello this is Himanshu bot")
  
@bot.on(events.NewMessage(incoming=True,pattern = "/get"))
async def start(event):
 a=await event.reply("Hello this is get command")
 await asyncio.sleep(3)
 await a.edit("this is edit message")
  
@bot.on(events.NewMessage(incoming=True,pattern = "/eval"))
async def start(event):
  await event.reply("Hello this is eval command")