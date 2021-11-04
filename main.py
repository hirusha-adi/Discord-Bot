from yourbot.web.keep_alive import keep_alive
import yourbot.others.installerm as ybinstaller
import yourbot.database.main.retrieve_base as getbase
import yourbot.database.embeds.retrieve_embeds as getembeds
import yourbot.database.chatbot.chatbot_channels as getChatBot
import yourbot.database.blacklist.blacklistmgr as blacklistmgr

# The main module
try:
    import discord
    from discord.ext import commands
except:
    ybinstaller.pip_install("discord")
    import discord
    from discord.ext import commands

# OTHERS
import os
import random
import datetime
try:
    from prsaw import RandomStuffV2
except:
    ybinstaller.pip_install("prsaw")
    from prsaw import RandomStuffV2

# Imports for music command!
try:
    import nacl
except:
    ybinstaller.pip_install("PyNaCl")
    import nacl


# From yourbot/database/config.json
bot_prefix = getbase.Main.MSG_PREFIX
bot_owner_id_zeacer = getbase.Main.OWNER_ID
bot_logging_commands_status = getbase.Main.LOG_USER_DATA
bot_logging_channel_id = getbase.Main.LOG_CHANNEL_ID

# From enviroment (as i host in replit)
token = os.environ['TOKEN']
bot_email_addr = os.environ['EMAILA']
bot_email_password = os.environ['EMAILP']


client = commands.Bot(command_prefix=bot_prefix)


@client.command()
async def loadex(ctx, extension):
    if ctx.author.id == bot_owner_id_zeacer:
        client.load_extension(f'yourbot.cogs.{extension}')
        embed = discord.Embed(
            title="SUCCESS", description=f"`ADDED cogs.{extension} from YourBot`", color=getembeds.Common.COLOR)
        embed.set_author(name=getembeds.CogManage.AUTHOR_NAME,
                         icon_url=getembeds.CogManage.AUTHOR_ICON)
        embed.set_thumbnail(url=getembeds.CogManage.THUMBNAIL)
        await ctx.send(embed=embed)
        return
    else:
        embed = discord.Embed(
            title="ERROR", description="`You don't have the permissions required to use this command!`", color=getembeds.ErrorEmbeds.COLOR)
        embed.set_author(name=getembeds.CogManage.AUTHOR_NAME,
                         icon_url=getembeds.CogManage.AUTHOR_ICON)
        embed.set_thumbnail(url=getembeds.CogManage.THUMBNAIL)
        await ctx.send(embed=embed)
        return


@client.command()
async def unloadex(ctx, extension):
    if ctx.author.id == bot_owner_id_zeacer:
        client.unload_extension(f'yourbot.cogs.{extension}')
        embed = discord.Embed(
            title="SUCCESS", description=f"`REMOVED cogs.{extension} from YourBot`", color=getembeds.Common.COLOR)
        embed.set_author(name=getembeds.CogManage.AUTHOR_NAME,
                         icon_url=getembeds.CogManage.AUTHOR_ICON)
        embed.set_thumbnail(url=getembeds.CogManage.THUMBNAIL)
        await ctx.send(embed=embed)
        return
    else:
        embed = discord.Embed(
            title="ERROR", description="`You don't have the permissions required to use this command!`", color=getembeds.ErrorEmbeds.COLOR)
        embed.set_author(name=getembeds.CogManage.AUTHOR_NAME,
                         icon_url=getembeds.CogManage.AUTHOR_ICON)
        embed.set_thumbnail(url=getembeds.CogManage.THUMBNAIL)
        await ctx.send(embed=embed)
        return


# Loading all the cogs at startup
for filename in os.listdir('./yourbot/cogs'):
    if filename.endswith('.py'):  # cogs.musicplayer is not being loded in here
        try:
            client.load_extension(f'yourbot.cogs.{filename[:-3]}')
            print(f"[+] Loaded: yourbot.cogs.{filename[:-3]}")
        except Exception as excl:
            print(
                f"[+] Unable to load: yourbot.cogs.{filename[:-3]}  :  {excl}")


# MUSIC BOT //////////////////////////////////////////////////////////////////////////////////////////
# The lava.link could be a localhost:port, but i chooses these servers and i dont host it manually
# The password can be anything!
client.lava_nodes = [
    {
        'host': "lava.link",
        'port': 80,
        'rest_uri': f'http://lava.link:80',
        'identifier': 'MAIN',
        'password': 'anything',
        'region': 'singapore'
    }
]

# Adding the cog
client.load_extension('yourbot.cogs.musicplayer')
print("[+] Loaded: yourbot.cogs.musicplayer")


# CHAT BOT //////////////////////////////////////////////////////////////////////////////////////////
rs = RandomStuffV2()
credits_wl = (
    "who made you", "developer", "who created you", "creator", "who is your owner", "your owner" "zeacer", "5641", "zeacer5641", "zeacer#5641", "your father", "your mother", "your creator", "develop", "who is your father", "who is your mother", "who is your zeacer", "who is your creator")
credits_reply_wl = ("I was created by ZeaCeR#5641", "ZeaCeR#5641 created me",
                    "ZeaCeR#5641 is the creator of me", "ZeaCeR#5641 is person who created me")
channel_lis = getChatBot.ChatBotChannels.channel_ids

bp = bot_prefix


@client.event
async def on_message(message):
    if client.user == message.author:
        return

    # User Blacklist
    if message.author.id in blacklistmgr.Users.blacklisted_users:
        if message.content.startswith(f'{bp}'):
            message.reply("[-] You are blacklisted from using this bot!")
        return

    # Server Blacklist
    if message.guild.name in blacklistmgr.Servers.blacklisted_servers:
        if message.content.startswith(f'{bp}'):
            message.reply(
                "[-] The server you are trying to use the bot is blaclisted!")
        return

    # ChatBot in specified channels or if the message starts with `cb`
    if (message.channel.id in channel_lis) or (message.content.lower().startswith('cb')):
        if message.content.lower() in credits_wl:
            await message.reply(f"{random.choice(credits_reply_wl)}")
        # so we can use the help command in set channels
        elif message.content.startswith(f'{bp}help'):
            pass
        else:
            try:
                response = rs.get_ai_response(message.content)
                await message.reply(response['message'])
            except Exception as e:
                await message.reply(f'Error: {e}')

    # Logging user messages to YourBot server's log channel (You need a role to see it and only i can give it to others)
    if bot_logging_commands_status == "yes":
        if message.content.startswith('>'):
            channel = client.get_channel(bot_logging_channel_id)
            embed = discord.Embed(title=f"{message.author.name} has used a command!", colour=discord.Colour(
                0xff0000), timestamp=datetime.datetime.utcfromtimestamp(1629281713))
            embed.set_thumbnail(url=f"{message.author.avatar_url}")
            embed.set_author(
                name="YourBot", icon_url="https://cdn.discordapp.com/attachments/861861096512290836/877496519123677195/Avatar.png")
            embed.set_footer(text="Command Logger - YourBot",
                             icon_url="https://cdn.discordapp.com/attachments/861861096512290836/877496519123677195/Avatar.png")
            embed.add_field(
                name="Command", value=f"{message.content}", inline=False)
            embed.add_field(name="User Name",
                            value=f"{message.author.name}", inline=True)
            embed.add_field(
                name="User ID", value=f"{message.author.id}", inline=True)
            try:
                embed.add_field(name="Sever Name",
                                value=f"{message.guild.name}", inline=True)
                embed.add_field(name="Sever ID",
                                value=f"{message.guild.id}", inline=True)
                embed.add_field(name="Channel Name",
                                value=f"{message.channel.name}", inline=True)
                embed.add_field(name="Channel ID",
                                value=f"{message.channel.id}", inline=True)
            except AttributeError:
                embed.add_field(name="Location",
                                value=f"Direct Message", inline=True)
            await channel.send(embed=embed)

    await client.process_commands(message)


keep_alive()
client.run(token)
