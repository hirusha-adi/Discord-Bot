import discord, datetime
from discord.ext import commands
from json import load as loadjson
from time import time as nowtime
import platform
import database.retrieve_embeds as getembed
import database.retrieve_base as getbase

class Main(commands.Cog, description="For bot information"):
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
        self.please_wait_emb = discord.Embed(title=getembed.PleaseWait.TITLE, description=f"``` {getembed.PleaseWait.DESCRIPTION} ```", color=getembed.PleaseWait.COLOR)
        self.please_wait_emb.set_author(name=getembed.PleaseWait.AUTHOR_NAME, icon_url=getembed.PleaseWait.AUTHOR_LINK)
        self.please_wait_emb.set_thumbnail(url=getembed.PleaseWait.THUMBNAIL)
        self.please_wait_emb.set_footer(text=getembed.PleaseWait.FOOTER)


    @commands.Cog.listener()
    async def on_ready(self):
        BOT_ACTIVITY = discord.ActivityType.watching, name=f"{len(self.client.guilds)} servers!"
        print(f'Discord.py API version: {discord.__version__}')
        print(f'Python version: {platform.python_version()}')
        print(f'Logged in as {self.client.user} | {self.client.user.id}')
        global start_time
        start_time = nowtime()
        await self.client.change_presence(activity=discord.Activity(type=BOT_ACTIVITY))
        print(getbase.BotBase.BOT_READY_MESSAGE)


    # ERROR HANDLING //////////////////////////////////////////////////////////////////////////////////////////
    # https://stackoverflow.com/questions/62234166/cant-get-discord-py-to-raise-an-error-if-user-doesnt-have-permissions-to-kick
    @commands.Cog.listener()
    async def on_command_error(self, ctx, error):
        if isinstance(error, commands.MissingPermissions):
            embed=discord.Embed(title=getembed.ErrorEmbeds.PERM_TITLEE, description=getembed.ErrorEmbeds.PERM_DESCRIPTION, color=getembed.ErrorEmbeds.PERM_COLOR)
            embed.set_author(name=getembed.ErrorEmbeds.PERM_AUTHOR_NAME, icon_url=getembed.ErrorEmbeds.PERM_AUTHOR_LINK)
            embed.set_thumbnail(url=getembed.ErrorEmbeds.PERM_THUMBNAIL)
            await ctx.send(embed=embed)
            return

        if isinstance(error, commands.MissingRequiredArgument):
            embed=discord.Embed(title=getembed.ErrorEmbeds.ARGS_TITLE, description=getembed.ErrorEmbeds.ARGS_DESCRIPTION, color=getembed.ErrorEmbeds.ARGS_COLOR)
            embed.set_author(name=getembed.ErrorEmbeds.ARGS_AUTHOR_NAME, icon_url=getembed.ErrorEmbeds.ARGS_AUTHOR_LINK)
            embed.set_thumbnail(url=getembed.ErrorEmbeds.ARGS_THUMBNAIL)
            embed.add_field(name=getembed.ErrorEmbeds.ARGS_ERROR, value=getembed.ErrorEmbeds.ARGS_ERROR_VALUE, inline=True)
            embed.add_field(name=getembed.ErrorEmbeds.ARGS_POSSIBLE_FIX, value=getembed.ErrorEmbeds.ARGS_POSSIBLE_FIX, inline=True)
            await ctx.send(embed=embed)
            return


    @commands.command(aliases=["invite", "botlink", "invitelink"],
    breif="Bot Invite Link",
    description="Get the bot invite link",
    help="Get the bot invite link")
    async def inv(self, ctx):
        await ctx.send(getbase.BotBase.INVITE_MESSAGE + " " + str(getbase.BotBase.INVITE_LINK))


    @commands.command(breif="Bot Ping",
    description="Show the response time of the bot",
    help="Show the response time of the bot")
    async def ping(self, ctx):
        loading_message = await ctx.send(embed=self.please_wait_emb)
        try:
            embed=discord.Embed(title="Response Time", color=getembed.Common.COLOR)
            embed.set_author(name=getembed.Common.AUTHOR, icon_url=getembed.Common.AUTHOR_LINK)
            embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/877796755234783273/879311068097290320/PngItem_1526969.png")
            embed.add_field(name=f"Ping :timer:", value=f"{round(self.client.latency * 1000)} ms", inline=False)
            embed.set_footer(text=f"Requested by {ctx.author.name}")
            await loading_message.delete()
            await ctx.send(embed=embed)

        except Exception as e:
            embed2=discord.Embed(title=getembed.ErrorEmbeds.TITLE, description=getembed.ErrorEmbeds.DESCRIPTION, color=getembed.ErrorEmbeds.COLOR)
            embed2.set_author(name=getembed.Common.AUTHOR, icon_url=getembed.Common.AUTHOR_LINK)
            embed2.set_thumbnail(url=getembed.ErrorEmbeds.THUMBNAIL)
            embed2.add_field(name="Error:", value=f"{e}", inline=False)
            embed2.set_footer(text=f"Requested by {ctx.author.name}")
            await loading_message.delete()
            await ctx.send(embed=embed2)


    @commands.command(aliases=["about", "source-code", "soourcecode", "source_code"],
    breif="Bot Information",
    description="Show information about the bot",
    help="Show information about the bot")
    async def info(self, ctx):
        loading_message = await ctx.send(embed=self.please_wait_emb)

        try:
            em = discord.Embed(title=getembed.Common.AUTHOR, color=getembed.Common.COLOR)
            em.set_thumbnail(url="https://cdn.discordapp.com/attachments/877796755234783273/879295069834850324/Avatar.png")
            em.set_author(name=getembed.Common.AUTHOR, icon_url=getembed.Common.AUTHOR_LINK)
            em.add_field(name="Version", value=f'{self.bot_current_version}')
            em.add_field(name="Creator", value=f'{self.bot_creator_name}')
            em.add_field(name="Servers", value=f'{len(self.client.guilds)}')
            em.add_field(name="Link", value=getbase.BotBase.SOURCE_CODE_LINK)
            em.set_footer(text=f"Requested by {ctx.author.name}")
            await loading_message.delete()
            await ctx.send(embed=em)

        except Exception as e:
            embed3=discord.Embed(title=getembed.ErrorEmbeds.TITLE, description=getembed.ErrorEmbeds.DESCRIPTION, color=getembed.ErrorEmbeds.COLOR)
            embed3.set_author(name=getembed.Common.AUTHOR, icon_url=getembed.Common.AUTHOR_LINK)
            embed3.set_thumbnail(url=getembed.ErrorEmbeds.THUMBNAIL)
            embed3.add_field(name="Error:", value=f"{e}", inline=False)
            embed3.set_footer(text=f"Requested by {ctx.author.name}")
            await loading_message.delete()
            await ctx.send(embed=embed3)


    @commands.command(breif="Bot Uptime",
    description="Show the uptime of the bot",
    help="Show the uptime of the bot")
    async def uptime(self, ctx):
        loading_message = await ctx.send(embed=self.please_wait_emb)

        try:
            current_time = nowtime()
            difference = int(round(current_time - start_time))
            text = str(datetime.timedelta(seconds=difference))
            embed=discord.Embed(color=getembed.Common.COLOR)
            embed.add_field(name="The bot was online for: ", value=f":alarm_clock: {text}", inline=False)
            embed.set_footer(text=f"Requested by {ctx.author.name}")
            await loading_message.delete()
            await ctx.send(embed=embed)
        
        except Exception as e:
            embed3=discord.Embed(title=getembed.ErrorEmbeds.TITLE, description=getembed.ErrorEmbeds.DESCRIPTION, color=getembed.ErrorEmbeds.COLOR)
            embed3.set_author(name=getembed.Common.AUTHOR, icon_url=getembed.Common.AUTHOR_LINK)
            embed3.set_thumbnail(url=getembed.ErrorEmbeds.THUMBNAIL)
            embed3.add_field(name="Error:", value=f"{e}", inline=False)
            embed3.set_footer(text=f"Requested by {ctx.author.name}")
            await loading_message.delete()
            await ctx.send(embed=embed3)


    @commands.command(breif="Bot Status",
    description="Show the status of the bot",
    help="Show the status of the bot")
    async def status(self, ctx):
        loading_message = await ctx.send(embed=self.please_wait_emb)

        try:
            current_time = nowtime()
            difference = int(round(current_time - start_time))
            text = str(datetime.timedelta(seconds=difference))

            embed=discord.Embed(color=getembed.Common.COLOR)
            embed.add_field(name="Announcements", value=getbase.BotBase.STATUS_ANNOUNCEMENTS, inline=False)
            embed.add_field(name="Servers", value=f"{len(self.client.guilds)}", inline=True)
            embed.add_field(name="Uptime", value=f"{text}", inline=True)
            embed.add_field(name="Version", value=f"{self.bot_current_version}", inline=True)
            embed.add_field(name="Source Code", value=getbase.BotBase.SOURCE_CODE_LINK, inline=True)
            embed.add_field(name="Creator", value=f"{self.bot_creator_name}", inline=True)
            embed.add_field(name="Errors", value=getbase.BotBase.STATUS_ERRORS, inline=False)
            embed.set_footer(text=f"Requested by {ctx.author.name}")
            await loading_message.delete()
            await ctx.send(embed=embed)
        
        except Exception as e:
            embed3=discord.Embed(title=getembed.ErrorEmbeds.TITLE, description=getembed.ErrorEmbeds.DESCRIPTION, color=getembed.ErrorEmbeds.COLOR)
            embed3.set_author(name=getembed.Common.AUTHOR, icon_url=getembed.Common.AUTHOR_LINK)
            embed3.set_thumbnail(url=getembed.ErrorEmbeds.THUMBNAIL)
            embed3.add_field(name="Error:", value=f"{e}", inline=False)
            embed3.set_footer(text=f"Requested by {ctx.author.name}")
            await loading_message.delete()
            await ctx.send(embed=embed3)





def setup(client: commands.Bot):
    client.add_cog(Main(client))
