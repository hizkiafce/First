import discord
import random

from discord import message

client = discord.Client()

sad_words = ['sedih', 'bete', 'depresi', 'mengsedih', 'nangis', 'ga enak', 'ngambek']

starter_cheer = ['yaela cengeng', 'lemah kau cok', 'yaela gitu doang, lah gua', 'ccd bet', 'trus gua harus apa???', 'bajingan buang-buang waktu gua']

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    msg = message.content

    if message.content.startswith(';Halo'):
        await message.channel.send('Halo')

    if message.content.startswith('pacaran yuuu'):
        await message.channel.send('Gaskeun boii') 

    if message.content.startswith("Katanya si jamie mo beli no man's sky"):
        await message.channel.send('bacot aja itu bang')

    if any(word in msg for word in sad_words):
        await message.channel.send(random.choice(starter_cheer))

client.run('OTEzNzQ2OTYwMTk5MDgxOTk1.YaC_Kw.5kdtLdsRBxWIMKoChtvx_hoJYIs')
