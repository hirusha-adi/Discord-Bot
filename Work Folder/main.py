# MY FILES

from keep_alive import keep_alive
import installerm

# OTHERS

import platform
import os

try:
  from prsaw import RandomStuffV2
  os.system("pip3 install prsaw")
except:
  if platform.system().lower().startswith('win'):
    os.system("pip install prsaw")
  else:
    os.system("pip3 install prsaw")
  from prsaw import RandomStuffV2

# The main module
try:
  import discord
except:
  if platform.system().lower().startswith('win'):
    os.system("pip install discord")
  else:
    os.system("pip3 install discord")
  import discord

from discord.ext import commands
import random
import json
import datetime
import database.retrieve_base as getbase

# Imports for music command!
if platform.system().lower().startswith('win'):
  os.system("pip install PyNaCl")
else:
  os.system("pip3 install PyNaCl")

try:
  import nacl
except:
  if platform.system().lower().startswith('win'):
    os.system("pip install PyNaCl")
  else:
    os.system("pip3 install PyNaCl")
  import nacl


try:
    if platform.system().lower().startswith('win'):
            os.system("pip install dismusic==1.0.1")
    else:
            os.system("pip3 install dismusic==1.0.1")
except Exception as e:
  print("Error:", e)


# FOR helpcmd cog
# if platform.system().lower().startswith('win'):
#     os.system("pip install discord-custom-help")
# else:
#     os.system("pip3 install discord-custom-help")


bot_prefix = getbase.Main.MSG_PREFIX
bot_owner_id_zeacer = getbase.Main.OWNER_ID
bot_logging_commands_status = getbase.Main.LOG_USER_DATA
bot_logging_channel_id = getbase.Main.LOG_CHANNEL_ID


token = os.environ['TOKEN']
bot_email_addr = os.environ['EMAILA']
bot_email_password = os.environ['EMAILP']

client = commands.Bot(command_prefix = bot_prefix)


@client.command()
async def loadex(ctx, extension):
  if ctx.author.id == bot_owner_id_zeacer:
    client.load_extension(f'cogs.{extension}')
    embed=discord.Embed(title="SUCCESS", description=f"`ADDED cogs.{extension} from YourBot`", color=0xff0000)
    embed.set_author(name="YourBot", icon_url="https://cdn.discordapp.com/attachments/877796755234783273/879295069834850324/Avatar.png")
    embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/877796755234783273/879298565380386846/sign-red-error-icon-1.png")
    await ctx.send(embed=embed)
    return
  else:
    embed=discord.Embed(title="ERROR", description="`You don't have the permissions required to use this command!`", color=0xff0000)
    embed.set_author(name="YourBot", icon_url="https://cdn.discordapp.com/attachments/877796755234783273/879295069834850324/Avatar.png")
    embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/877796755234783273/879298565380386846/sign-red-error-icon-1.png")
    await ctx.send(embed=embed)
    return


@client.command()
async def unloadex(ctx, extension):
  if ctx.author.id == bot_owner_id_zeacer:
    try:
      client.unload_extension(f'cogs.{extension}')
      embed=discord.Embed(title="SUCCESS", description=f"`REMOVED cogs.{extension} from YourBot`", color=0xff0000)
      embed.set_author(name="YourBot", icon_url="https://cdn.discordapp.com/attachments/877796755234783273/879295069834850324/Avatar.png")
      embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/877796755234783273/879298565380386846/sign-red-error-icon-1.png")
      await ctx.send(embed=embed)
      return
    except:
      embed=discord.Embed(title="ERROR", description="`You don't have the permissions required to use this command!`", color=0xff0000)
      embed.set_author(name="YourBot", icon_url="https://cdn.discordapp.com/attachments/877796755234783273/879295069834850324/Avatar.png")
      embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/877796755234783273/879298565380386846/sign-red-error-icon-1.png")
      await ctx.send(embed=embed)
      return


# Loading all the cogs at startup
for filename in os.listdir('./cogs'):
  if filename.endswith('.py'):
    try:
      client.load_extension(f'cogs.{filename[:-3]}')
      print(f"[+] Loaded: cogs.{filename[:-3]}")
    except Exception as excl:
      print(f"[+] Unable to load: cogs.{filename[:-3]}  :  {excl}")


# MUSIC BOT //////////////////////////////////////////////////////////////////////////////////////////
# The lava.link could be a localhost:port, but i chooses these servers and i dont host it manually
# The password can be anything!
client.lava_nodes = [
  {
    'host':"lava.link",
    'port':80,
    'rest_uri':f'http://lava.link:80',
    'identifier':'MAIN',
    'password':'anything',
    'region':'singapore'
  }
]

# Adding the cog
client.load_extension('dismusic')



# CHAT BOT //////////////////////////////////////////////////////////////////////////////////////////
rs = RandomStuffV2()
credits_wl = (
  "who made you", "developer", "who created you", "creator", "who is your owner", "your owner" "zeacer", "5641", "zeacer5641", "zeacer#5641", "your father", "your mother", "your creator", "develop", "who is your father", "who is your mother", "who is your zeacer", "who is your creator")
credits_reply_wl = ( "I was created by ZeaCeR#5641", "ZeaCeR#5641 created me", "ZeaCeR#5641 is the creator of me", "ZeaCeR#5641 is person who created me")
channel_lis = ( 863706778743341076, 874577378746175508, 874963358254780447, 874964067322822696)

bp = bot_prefix

@client.event
async def on_message(message):
  
  if message.channel.id in channel_lis:
    if client.user == message.author:
      return

    if message.content.lower() in credits_wl:
      await message.reply(f"{random.choice(credits_reply_wl)}")
    elif message.content.startswith(f'{bp}help'):
      pass
    else:
      try:
          response = rs.get_ai_response(message.content)
          await message.reply(response['message'])
      except Exception as e:
        await message.reply(f'Error: {e}')
  
  if client.user == message.author:
    return
  
  # Logging user messages to YourBot log server
  if bot_logging_commands_status == "yes":
    if message.content.startswith('>'):
      channel = client.get_channel(bot_logging_channel_id)
      embed = discord.Embed(title=f"{message.author.name} has used a command!", colour=discord.Colour(0xff0000), timestamp=datetime.datetime.utcfromtimestamp(1629281713))
      embed.set_thumbnail(url=f"{message.author.avatar_url}")
      embed.set_author(name="YourBot", icon_url="https://cdn.discordapp.com/attachments/861861096512290836/877496519123677195/Avatar.png")
      embed.set_footer(text="Command Logger - YourBot", icon_url="https://cdn.discordapp.com/attachments/861861096512290836/877496519123677195/Avatar.png")
      embed.add_field(name="Command", value=f"{message.content}", inline=False)
      embed.add_field(name="User Name", value=f"{message.author.name}", inline=True)
      embed.add_field(name="User ID", value=f"{message.author.id}", inline=True)
      try:
        embed.add_field(name="Sever Name", value=f"{message.guild.name}", inline=True)
        embed.add_field(name="Sever ID", value=f"{message.guild.id}", inline=True)
        embed.add_field(name="Channel Name", value=f"{message.channel.name}", inline=True)
        embed.add_field(name="Channel ID", value=f"{message.channel.id}", inline=True)
      except AttributeError:
        embed.add_field(name="Location", value=f"Direct Message", inline=True)
      await channel.send(embed=embed)

  await client.process_commands(message)


keep_alive()
client.run(token)