from apscheduler.schedulers.asyncio import AsyncIOScheduler
from apscheduler.triggers.cron import CronTrigger
from datetime import datetime
from dotenv import load_dotenv
from discord.ext import commands
import discord
import random
import os

load_dotenv()

client = discord.Client()
dt = datetime.now().strftime("%d/%m/%Y %H:%M:%S")

phrase = ['phrase1', 'phrase2', 'phrase3']

async def func():
    c = client.get_channel(SERVER_CHANNEL_ID_GOES_HERE)
    await c.send(random.choice(phrase))

@client.event
async def on_ready():
    print("[", dt, "] Ready")

    scheduler = AsyncIOScheduler()
    scheduler.add_job(func, CronTrigger(minute="0"))
    scheduler.start()

client.run(os.getenv('TOKEN'))
