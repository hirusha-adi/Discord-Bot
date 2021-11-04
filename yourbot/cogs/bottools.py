import discord
from discord.ext import commands
import yourbot.database.embeds.retrieve_embeds as getembed
import yourbot.database.main.retrieve_base as getbase
from yourbot.assets.tools.utils import getConfig

# Ill deal with this fucking shit later


class BotTools(commands.Cog, description="Configure the bot in here!"):
    def __init__(self, client: commands.Bot):
        self.client = client

        self.bot_prefix = getbase.Main.MSG_PREFIX
        self.bot_inv_link = getbase.Main.INVITE_LINK

        # This is the please-wait/Loading embed
        self.please_wait_emb = discord.Embed(
            title=getembed.PleaseWait.TITLE, description=f"``` {getembed.PleaseWait.DESCRIPTION} ```", color=getembed.PleaseWait.COLOR)
        self.please_wait_emb.set_author(
            name=getembed.PleaseWait.AUTHOR_NAME, icon_url=getembed.PleaseWait.AUTHOR_LINK)
        self.please_wait_emb.set_thumbnail(url=getembed.PleaseWait.THUMBNAIL)
        self.please_wait_emb.set_footer(text=getembed.PleaseWait.FOOTER)

    @commands.has_permissions(administrator=True)
    @commands.command(breif="Change bot prefix",
                      description="Change the bot command prefix. This only affects your server!",
                      help="Change the bot command prefix. This only affects your server!")
    async def change_prefix(self, ctx, custom_prefix):
        loading_message = await ctx.send(embed=self.please_wait_emb)
        try:
            data = getConfig(ctx.guild.id)
            old_prefix = data["prefix"]
            data["prefix"] = custom_prefix
            embed = discord.Embed(
                title="Change Bot Prefix", color=getembed.Common.COLOR)
            embed.set_author(name=getembed.Common.AUTHOR,
                             icon_url=getembed.Common.AUTHOR_LINK)
            embed.set_thumbnail(url=getembed.Common.AUTHOR_LINK)
            embed.add_field(name="Old", value=f"{old_prefix}", inline=True)
            embed.add_field(name="New", value=f"{custom_prefix}", inline=True)
            embed.set_footer(text=f"Requested by {ctx.author.name}")
            await loading_message.delete()
            await ctx.send(embed=embed)

        except Exception as e:
            embed3 = discord.Embed(title=getembed.ErrorEmbeds.TITLE,
                                   description=getembed.ErrorEmbeds.DESCRIPTION, color=getembed.ErrorEmbeds.COLOR)
            embed3.set_author(name=getembed.Common.AUTHOR,
                              icon_url=getembed.Common.AUTHOR_LINK)
            embed3.set_thumbnail(url=getembed.ErrorEmbeds.THUMBNAIL)
            embed3.add_field(name="Error:", value=f"{e}", inline=False)
            embed3.set_footer(text=f"Requested by {ctx.author.name}")
            await loading_message.delete()
            await ctx.send(embed=embed3)

    @commands.has_permissions(manage_messages=True)
    @commands.command(breif="Disable Logging",
                      description="This bot logs every command used by the bot in order to monitor bugs if found! You can disable it here",
                      help="This bot logs every command used by the bot in order to monitor bugs if found! You can disable it here")
    async def disable_logging(self, ctx):
        loading_message = await ctx.send(embed=self.please_wait_emb)
        try:
            data = getConfig(ctx.guild.id)
            data["logServerCommands"] = False
            embed = discord.Embed(
                title="Disable Logging", color=getembed.Common.COLOR)
            embed.set_author(name=getembed.Common.AUTHOR,
                             icon_url=getembed.Common.AUTHOR_LINK)
            embed.set_thumbnail(url=getembed.Common.AUTHOR_LINK)
            embed.add_field(
                name="Server", value=f"{ctx.guild.name} | {ctx.guild.id}", inline=True)
            embed.add_field(
                name="Status", value=f"`False`", inline=True)
            embed.set_footer(text=f"Requested by {ctx.author.name}")
            await loading_message.delete()
            await ctx.send(embed=embed)

        except Exception as e:
            embed3 = discord.Embed(title=getembed.ErrorEmbeds.TITLE,
                                   description=getembed.ErrorEmbeds.DESCRIPTION, color=getembed.ErrorEmbeds.COLOR)
            embed3.set_author(name=getembed.Common.AUTHOR,
                              icon_url=getembed.Common.AUTHOR_LINK)
            embed3.set_thumbnail(url=getembed.ErrorEmbeds.THUMBNAIL)
            embed3.add_field(name="Error:", value=f"{e}", inline=False)
            embed3.set_footer(text=f"Requested by {ctx.author.name}")
            await loading_message.delete()
            await ctx.send(embed=embed3)

    @commands.has_permissions(manage_messages=True)
    @commands.command(breif="Enable Logging",
                      description="This bot logs every command used by the bot in order to monitor bugs if found! You can enable it here. Logging bot commands is enabled by default!",
                      help="This bot logs every command used by the bot in order to monitor bugs if found! You can enable it here. Logging bot commands is enabled by default!")
    async def disable_logging(self, ctx):
        loading_message = await ctx.send(embed=self.please_wait_emb)
        try:
            data = getConfig(ctx.guild.id)
            data["logServerCommands"] = True
            embed = discord.Embed(
                title="Enable Logging", color=getembed.Common.COLOR)
            embed.set_author(name=getembed.Common.AUTHOR,
                             icon_url=getembed.Common.AUTHOR_LINK)
            embed.set_thumbnail(url=getembed.Common.AUTHOR_LINK)
            embed.add_field(
                name="Server", value=f"{ctx.guild.name} | {ctx.guild.id}", inline=True)
            embed.add_field(
                name="Status", value=f"`True`", inline=True)
            embed.set_footer(text=f"Requested by {ctx.author.name}")
            await loading_message.delete()
            await ctx.send(embed=embed)

        except Exception as e:
            embed3 = discord.Embed(title=getembed.ErrorEmbeds.TITLE,
                                   description=getembed.ErrorEmbeds.DESCRIPTION, color=getembed.ErrorEmbeds.COLOR)
            embed3.set_author(name=getembed.Common.AUTHOR,
                              icon_url=getembed.Common.AUTHOR_LINK)
            embed3.set_thumbnail(url=getembed.ErrorEmbeds.THUMBNAIL)
            embed3.add_field(name="Error:", value=f"{e}", inline=False)
            embed3.set_footer(text=f"Requested by {ctx.author.name}")
            await loading_message.delete()
            await ctx.send(embed=embed3)


def setup(client: commands.Bot):
    client.add_cog(BotTools(client))
