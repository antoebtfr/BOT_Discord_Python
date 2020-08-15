import discord

client = discord.Client()

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if message.content.startswith(('Yo', 'yo')):
        await message.channel.send('Bien ou quoi ? Tu fais un truc aujourd\'hui ?')

client.run('NzQzOTYxNjg4NDc0MTI0MzM4.XzcSUA.hkxJ0juXDCfo44hblAWFbS7smug')