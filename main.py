import discord
from discord.ext import commands
token = "NzQzOTYxNjg4NDc0MTI0MzM4.XzcSUA.hkxJ0juXDCfo44hblAWFbS7smug"

bot = commands.Bot(command_prefix='!')
client = discord.Client()

@bot.event
async def on_ready():
    await bot.change_presence(status=discord.Status.idle, activity=discord.Game('JE SUIS LE BOSS'))
    print("Bot pret")
    print('Fonction on_ready over')
    

@bot.command()
async def regles(ctx):
    await ctx.send('-p https://www.youtube.com/watch?v=lbeUyW6axeA')
    print("Test")

@client.event
async def on_message(message):

    if message.content.startswith('$hello'):
        await message.channel.send('Bien ou quoi ? ')


    print('Fonction on_message prêt')

print('Lancement du bot...')

bot.run(token)
