import discord
import asyncio
from discord import Game
from discord.ext.commands import Bot
import datetime
import os
import pytz
tz = pytz.timezone('Asia/Bangkok')


ktdate = ["Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday"]
kttime = [[10,18],[14],[18],[0,14],[10,18],[14],[14]]


client = discord.Client()

@client.event
async def on_ready():
    global counter
    print('Logged in')
    print('Name : {}'.format(client.user.name))
    print('ID : {}'.format(client.user.id))
    print(discord.__version__)



async def my_background_task():
	await client.wait_until_ready(tz)
	while not client.is_closed:
		now = datetime.datetime.now()
		date = now.strftime("%A")
		hour = (now.hour)
		mine = (now.minute)
		day = ktdate.index(date)
		alltime = kttime[day]
		next = 99
		nextdate = date
		x = 0
		while x < len(alltime):
			if int(hour) < alltime[x]:
				next = alltime[x]
				x = len(alltime)
			else:
				x += 1
		if next == 99:
			if day+1 < 7:
				nextdate = ktdate[day+1]
				next = kttime[day+1][0]
			else:
				nextdate = ktdate[0]
				next = kttime[0][0]

		startlp = 0
		while  startlp == 0:
			now = datetime.datetime.now(tz)
			date = now.strftime("%A")
			hour = (now.hour)
			mine = (now.minute)
			day = ktdate.index(date)
			alltime = kttime[day]

			if nextdate == date:
				if int(mine) > 0:
					m = 60 - int(mine)
					h = next - int(hour) - 1
				else:
					h = next - int(hour)
					m = 0
			else:
				if int(mine) > 0:
					m = 60 - int(mine)
					h = 24 - int(hour) - 1 + next
				else:
					h = 24 - int(hour) + next
					m = 0

			if int(h/24) == 0:
				await client.change_presence(game=discord.Game(name='Spawn at ' + str(next) + ':01(' + str(h) +'h' + str(m) +'m)'))
			else:
				await client.change_presence(game=discord.Game(name='Spawn at ' + str(next) + ':01('+str(int(h/24))+'d' + str(h - int(h/24) * 24) +'h' + str(m) +'m)'))
			await asyncio.sleep(5)
			if nextdate == date:
				if int(hour) == next and int(mine) == 1:
					startlp = 1

client.loop.create_task(my_background_task())
client.run(os.getenv('KTTOKEN'))
