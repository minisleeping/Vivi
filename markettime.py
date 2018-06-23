import discord
import asyncio
from discord import Game
from discord.ext.commands import Bot
import datetime
import os
import pytz
tz = pytz.timezone('Asia/Bangkok')

DN = [0,1,0,1,0,1,0,1,0,1,0,1]
time = [[2,40],[3,20],[6,40],[7,20],[10,40],[11,20],[14,40],[15,20],[18,40],[19,20],[22,40],[23,20]]


client = discord.Client()

@client.event
async def on_ready():
    global counter
    print('Logged in')
    print('Name : {}'.format(client.user.name))
    print('ID : {}'.format(client.user.id))
    print(discord.__version__)



async def my_background_task():
	await client.wait_until_ready()
	while not client.is_closed:
		now = datetime.datetime.now(tz)
		hour = (now.hour)
		mine = (now.minute)
		x = 0
		while x < len(time):
			if int(hour) < time[x][0]:
				nexth = time[x][0]
				nextm = time[x][1]
				ck = DN[x]
				x = len(time)
			elif int(hour) == time[x][0] and int(mine) < time[x][1]:
				nexth = time[x][0]
				nextm = time[x][1]
				ck = DN[x]
				x = len(time)
			elif x == len(time) - 1:
				nexth = time[0][0]
				nextm = time[0][1]
				ck = DN[0]
				x = len(time)
			else:
				x += 1

		startlp = 0
		while  startlp == 0:
			now = datetime.datetime.now(tz)
			hour = (now.hour)
			mine = (now.minute)
			if int(hour) == 23 and int(mine) >= 20:
				m1 = int(hour) * 60 + int(mine)
				m2 = 24 * 60 + 160
			else:
				m1 = int(hour) * 60 + int(mine)
				m2 = nexth * 60 + nextm

			m3 = m2 - m1
			if nextm == 0:
				showm = '00'
			else:
				showm = str(nextm)
			if int(m3/60) == 0:
				if ck == 1:
					await client.change_presence(game=discord.Game(name='Day at '+str(nexth)+':'+showm+'(' + str(m3) +'m)'))
				else:
					await client.change_presence(game=discord.Game(name='Night at '+str(nexth)+':'+showm+'(' + str(m3) +'m)'))
			else:
				if ck == 1:
					await client.change_presence(game=discord.Game(name='Day at '+str(nexth)+':'+showm+'('+str(int(m3/60))+'h' + str(m3 - int(m3/60) * 60) +'m)'))
				else:
					await client.change_presence(game=discord.Game(name='Night at '+str(nexth)+':'+showm+'('+str(int(m3/60))+'h' + str(m3 - int(m3/60) * 60) +'m)'))

			await asyncio.sleep(5)
			if int(hour) == nexth and int(mine) == nextm:
				startlp = 1

client.loop.create_task(my_background_task())
client.run(os.getenv('BDOTIME_TOKEN'))
