
from genericpath import exists
from pyrogram import Client as Bot, filters
from pyrogram import client
import requests
from pyrogram import Client, filters
from pyrogram.types import *
import requests
import re
import urllib
import urllib.parse
import sys
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from pyrogram import Client as Bot, filters
import re
import time 
import requests
from bs4 import BeautifulSoup
from fake_useragent import UserAgent
from pyrogram import Client, filters
from telegraph import upload_file as uf
import requests
from bs4 import BeautifulSoup
import pytz
from datetime import date, datetime
UTC = pytz.utc
IST = pytz.timezone('Asia/Kolkata')
datetime_ist = datetime.now(IST)
dt = datetime_ist.strftime('%Y:%m:%d %H:%M:%S')
from time import sleep
import argparse
from PIL import Image
import asyncio
import os
import aiofiles
# url list to screenshot
from htmlwebshot import WebShot

# defining options manually

# actually launching the function
wait = []
@Bot.on_callback_query()
async def cdata(c, q):
    data = q.data
    wait = "wait bro..."
    if data.startswith("ss|"):
     try:
       if q.from_user.id in wait:
         await q.answer("already a process going on for you!")
       else:
            wait.append(q.from_user.id)
            link = data.split("|", 1)[1]
            await c.send_chat_action(chat_id=q.from_user.id, action="upload_document")
            await q.answer("Start Capturing webpage..", show_alert=True)
            shot = WebShot()
            #await q.answer("Downloading webpage..",)
            shot.create_pic(url=link)
            #await q.answer("Uploading webpage..",)
            await c.send_chat_action(chat_id=q.from_user.id, action="upload_document")
            await c.send_document(q.from_user.id, document="webshot.png")
            while(m.from_user.id in wait):
              wait.remove(K)
     except Exception as e:
         await q.message.edit_text(e)
         #await c.send_document(q.from_user.id, document="webshot.png")
         
     os.remove("webshot.png")
    elif data == "alive":
        ch = q.from_user.mention
        await q.message.edit_text("i am alive\n"+ch+"\n"+dt, reply_markup = InlineKeyboardMarkup([[InlineKeyboardButton(text='CHECK STATUS', callback_data='alive')]]))
        await c.send_message("s4tyendra", ch+"\n pinged me")
