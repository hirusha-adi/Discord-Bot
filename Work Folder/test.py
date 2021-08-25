
import discord, os, time
from discord.ext import commands


bot = commands.Bot(command_prefix = "--")
token = "ODU4Mjk4NjgzMjIwMTY0NjE2.YNcG8A._RcHIYTHk48OL9kKgS1X2oV3Wqw"

@bot.event
async def on_ready():
    print("Auto Bumper Is Online!")



@bot.command()
async def bla(ctx):
    while True:
        await ctx.send("!d bump")
        time.sleep(8125)

@bot.event
async def on_message(message):
  print(message.content)

  await bot.process_commands(message)


bot.run(token)

