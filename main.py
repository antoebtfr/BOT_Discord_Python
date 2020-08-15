import discord
from discord.ext import commands
token = "NzQzOTYxNjg4NDc0MTI0MzM4.XzcSUA.JBLRJoXTpyj0_47oRxkFxp9hnZ8"

bot = commands.Bot(command_prefix='!')

@bot.event
async def on_ready():
    print("Bot pret")
    await bot.change_presence(status=discord.Status.idle, activity=discord.Game('JE SUIS LE BOSS'))
    print('Fonction on_ready over')
    

@bot.command()
async def regles(ctx):
    print("Test")


print('Lancement du bot...')

bot.run(token)
