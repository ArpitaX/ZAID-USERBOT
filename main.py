import logging
from pyrogram import Client, filters, idle
from pyrogram.types import *
import requests
import os
import re
import asyncio
from datetime import datetime
from config import *

from apscheduler.schedulers.asyncio import AsyncIOScheduler

logging.basicConfig(format='[%(levelname) 5s/%(asctime)s] %(name)s: %(message)s',
                    level=logging.WARNING)

API_ID = API_ID
API_HASH = API_HASH 
SUDO_USERS = SUDO_USERS
DB_URL = DB_URL
cleanmode = {}



if not API_ID:
    logging.error("No Api-ID Found! Exiting!")
    quit(1)

if not MONGO_DB:
    logging.error("No MongoDB Found! Exiting!")
    quit(1)

if not API_HASH:
    logging.error("No ApiHash Found! Exiting!")
    quit(1)

if ALIVE_IMG:
    ALIVE_PIC = ALIVE_IMG
else: 
    ALIVE_PIC = 'https://telegra.ph/file/077f0e0eb681938c6d85f.jpg'

if LOG_CHAT:
    LOG_GROUP = LOG_CHAT
else:
    LOG_GROUP = 777000
Owner = LOG_GROUP


bot1 = Client(session_name= STRING_SESSION, api_id = API_ID, api_hash = API_HASH , plugins=dict(root="handlers"))

scheduler = AsyncIOScheduler()
CMD_HELP = {}
START_TIME = datetime.now()

bot1.start()
idle()

print("🎉 DEPLOYED")
