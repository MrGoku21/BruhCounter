import discord
from discord.ext import commands
import asyncio
import os
import time

bot = commands.Bot(command_prefix = "!", help_command=None)
bot.message_counter = 0

@bot.event
async def on_ready():
    print ("Systemet kjører nå!\nKlar til bruk kaptein!")
    await bot.change_presence(activity=discord.Streaming(name="Bruh this is slavery", url="https://www.twitch.tv/Twitch"))

@bot.event
async def on_message(message):
    user = message.author
    if message.content.startswith("bruh"):
        embed=discord.Embed(title="Bruh Counter intensifies", description=f"{user} said the word Bruh! \n Bless this dude!", color=0xb1f1c0)
        embed.set_footer(text="Made by Marceline <3")
        await message.channel.send(embed=embed)
        bot.message_counter += 1
    await bot.process_commands(message)

@bot.command()
async def bruh(ctx):
    embed=discord.Embed(title="Bruh Counter", description="The word bruh has been said {} times!".format(ctx.bot.message_counter) , color=0xefe0b4)
    embed.set_thumbnail(url="https://steamuserimages-a.akamaihd.net/ugc/958603887337454582/7ED14D409F60454623CFC1A6A1DFAEFFDF591460/")
    embed.add_field(name="Conclusion", value="The word bruh is overrated.", inline=True)
    embed.set_footer(text="Made by Marceline <3 (Caasi)")
    await ctx.send(embed=embed)   

bot.run(" YOUR CLIENT_ID GOES HERE! ")                                                                                                                   
