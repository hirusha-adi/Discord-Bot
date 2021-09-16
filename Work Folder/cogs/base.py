import discord, datetime
from discord.ext import commands
from json import load as loadjson
from time import time as nowtime
import platform

class BotMainCommands(commands.Cog):
    def __init__(self, client: commands.Bot):
        self.client = client

        self.start_time = None

        # Loading config.json and its important content for this file
        self.botconfigdata = loadjson(open("config.json", "r"))
        self.bot_prefix = self.botconfigdata["msg-prefix"]
        self.bot_inv_link = self.botconfigdata["invite-link"]
        self.bot_current_version = self.botconfigdata["bot-version"]
        self.bot_creator_name = self.botconfigdata["bot-creator-name"]

        # This is the please-wait/Loading embed
        self.please_wait_emb = discord.Embed(title="Please Wait", description="``` Processing Your Request ```", color=0xff0000)
        self.please_wait_emb.set_author(name="YourBot")
        self.please_wait_emb.set_thumbnail(url="https://c.tenor.com/I6kN-6X7nhAAAAAj/loading-buffering.gif")
        self.please_wait_emb.set_footer(text="Bot created by ZeaCeR#5641")


    @commands.Cog.listener()
    async def on_ready(self):
        print(f'Discord.py API version: {discord.__version__}')
        print(f'Python version: {platform.python_version()}')
        print(f'Logged in as {self.client.user.name}')
        global start_time
        start_time = nowtime()
        await self.client.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name=f"{len(self.client.guilds)} servers!"))
        print('Bot is ready!')
    
    # ERROR HANDLING //////////////////////////////////////////////////////////////////////////////////////////
    # https://stackoverflow.com/questions/62234166/cant-get-discord-py-to-raise-an-error-if-user-doesnt-have-permissions-to-kick
    @commands.Cog.listener()
    async def on_command_error(self, ctx, error):
        if isinstance(error, commands.MissingPermissions):
            embed=discord.Embed(title="ERROR", description="`You don't have the permissions required to use this command!`", color=0xff0000)
            embed.set_author(name="YourBot", icon_url="https://cdn.discordapp.com/attachments/877796755234783273/879295069834850324/Avatar.png")
            embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/877796755234783273/879298565380386846/sign-red-error-icon-1.png")
            await ctx.send(embed=embed)
            return

        if isinstance(error, commands.MissingRequiredArgument):
            embed=discord.Embed(title="Something is wrong!", description="An error has been occured!", color=0xff0000)
            embed.set_author(name="YourBot", icon_url="https://cdn.discordapp.com/attachments/877796755234783273/879295069834850324/Avatar.png")
            embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/877796755234783273/879298565380386846/sign-red-error-icon-1.png")
            embed.add_field(name="Error", value="You haven't passed the needed arguments for this command to run properly", inline=True)
            embed.add_field(name="Possible Fix", value=f"use `{self.bot_prefix}help all` to list out all the command and check the proper usage of the command you used", inline=True)
            await ctx.send(embed=embed)
            return

    @commands.command(aliases=["invite", "botlink", "invitelink"])
    async def inv(self, ctx):
        await ctx.send("```Hey there! Make sure you have me in your server too! Bot Invite link:```" + str(self.bot_inv_link))

    @commands.command() 
    async def ping(self, ctx):
        loading_message = await ctx.send(embed=self.please_wait_emb)
        try:
            embed=discord.Embed(title="Response Time", color=0xff0000)
            embed.set_author(name="YourBot", icon_url="https://cdn.discordapp.com/attachments/877796755234783273/879295069834850324/Avatar.png")
            embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/877796755234783273/879311068097290320/PngItem_1526969.png")
            embed.add_field(name=f"Ping :timer:", value=f"{round(self.client.latency * 1000)} ms", inline=False)
            embed.set_footer(text=f"Requested by {ctx.author.name}")
            await loading_message.delete()
            await ctx.send(embed=embed)

        except Exception as e:
            embed2=discord.Embed(title=":red_square: Error!", description="The command was unable to run successfully! ", color=0xff0000)
            embed2.set_author(name="YourBot", icon_url="https://cdn.discordapp.com/attachments/877796755234783273/879295069834850324/Avatar.png")
            embed2.set_thumbnail(url="https://cdn.discordapp.com/attachments/877796755234783273/879298565380386846/sign-red-error-icon-1.png")
            embed2.add_field(name="Error:", value=f"{e}", inline=False)
            embed2.set_footer(text=f"Requested by {ctx.author.name}")
            await loading_message.delete()
            await ctx.send(embed=embed2)

    @commands.command(aliases=["about"])
    async def info(self, ctx):
        loading_message = await ctx.send(embed=self.please_wait_emb)

        try:
            em = discord.Embed(title="Your Bot", color=0xFF0000)
            em.set_thumbnail(url="https://cdn.discordapp.com/attachments/877796755234783273/879295069834850324/Avatar.png")
            em.set_author(name="YourBot", icon_url="https://cdn.discordapp.com/attachments/877796755234783273/879295069834850324/Avatar.png")
            em.add_field(name="Version", value=f'{self.bot_current_version}')
            em.add_field(name="Creator", value=f'{self.bot_creator_name}')
            em.add_field(name="Servers", value=f'{len(self.client.guilds)}')
            em.add_field(name="Link", value=f'https://github.com/hirusha-adi/Discord-Bot')
            em.set_footer(text=f"Requested by {ctx.author.name}")
            await loading_message.delete()
            await ctx.send(embed=em)

        except Exception as e:
            embed3=discord.Embed(title=":red_square: Error!", description="The command was unable to run successfully! ", color=0xff0000)
            embed3.set_author(name="YourBot", icon_url="https://cdn.discordapp.com/attachments/877796755234783273/879295069834850324/Avatar.png")
            embed3.set_thumbnail(url="https://cdn.discordapp.com/attachments/877796755234783273/879298565380386846/sign-red-error-icon-1.png")
            embed3.add_field(name="Error:", value=f"{e}", inline=False)
            embed3.set_footer(text=f"Requested by {ctx.author.name}")
            await loading_message.delete()
            await ctx.send(embed=embed3)


    @commands.command()
    async def uptime(self, ctx):
        loading_message = await ctx.send(embed=self.please_wait_emb)

        try:
            current_time = nowtime()
            difference = int(round(current_time - start_time))
            text = str(datetime.timedelta(seconds=difference))
            embed=discord.Embed(color=0xff0000)
            embed.add_field(name="The bot was online for: ", value=f":alarm_clock: {text}", inline=False)
            embed.set_footer(text=f"Requested by {ctx.author.name}")
            await loading_message.delete()
            await ctx.send(embed=embed)
        
        except Exception as e:
            embed3=discord.Embed(title=":red_square: Error!", description="The command was unable to run successfully! ", color=0xff0000)
            embed3.set_author(name="YourBot", icon_url="https://cdn.discordapp.com/attachments/877796755234783273/879295069834850324/Avatar.png")
            embed3.set_thumbnail(url="https://cdn.discordapp.com/attachments/877796755234783273/879298565380386846/sign-red-error-icon-1.png")
            embed3.add_field(name="Error:", value=f"{e}", inline=False)
            embed3.set_footer(text=f"Requested by {ctx.author.name}")
            await loading_message.delete()
            await ctx.send(embed=embed3)


    @commands.command()
    async def status(self, ctx):
        loading_message = await ctx.send(embed=self.please_wait_emb)

        try:
            current_time = nowtime()
            difference = int(round(current_time - start_time))
            text = str(datetime.timedelta(seconds=difference))

            embed=discord.Embed(color=0xff0000)
            embed.add_field(name="Announcements", value=f"``` -YourBot {self.bot_current_version}- Hello! Its been nearly two months after the first release of this discord bot. Most of the commands are very stable now, but not all of them. Help me make this bot have 500+ commands. use {self.bot_prefix}help to check all the commands available! ```", inline=False)
            embed.add_field(name="Servers", value=f"{len(self.client.guilds)}", inline=True)
            embed.add_field(name="Uptime", value=f"{text}", inline=True)
            embed.add_field(name="Version", value=f"{self.bot_current_version}", inline=True)
            embed.add_field(name="Source Code", value="https://github.com/hirusha-adi/Discord-Bot", inline=True)
            embed.add_field(name="Creator", value=f"{self.bot_creator_name}", inline=True)
            embed.add_field(name="Errors", value="``` There is bug when the chatbot feature is being used simultaneously in many channels, This issue will be fixed soon!  ```", inline=False)
            embed.set_footer(text=f"Requested by {ctx.author.name}")
            await loading_message.delete()
            await ctx.send(embed=embed)
        
        except Exception as e:
            embed3=discord.Embed(title=":red_square: Error!", description="The command was unable to run successfully! ", color=0xff0000)
            embed3.set_author(name="YourBot", icon_url="https://cdn.discordapp.com/attachments/877796755234783273/879295069834850324/Avatar.png")
            embed3.set_thumbnail(url="https://cdn.discordapp.com/attachments/877796755234783273/879298565380386846/sign-red-error-icon-1.png")
            embed3.add_field(name="Error:", value=f"{e}", inline=False)
            embed3.set_footer(text=f"Requested by {ctx.author.name}")
            await loading_message.delete()
            await ctx.send(embed=embed3)












def setup(client: commands.Bot):
    client.add_cog(BotMainCommands(client))
