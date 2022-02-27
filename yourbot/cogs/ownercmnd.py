import discord
import os
import asyncio
from discord.ext import commands
import yourbot.database.embeds.retrieve_embeds as getembed
import yourbot.database.main.retrieve_base as getbase
import yourbot.others.installerm as ybinstaller
import yourbot.database.blacklist.blacklistmgr as blacklistmgr

from platform import system as pltfsys
from platform import python_version as pyversion
try:
    from getpass import getuser as pcusername
except:
    ybinstaller.pip_install("getpass4")
    from getpass import getuser as pcusername


class OwnerOnly(commands.Cog, description="These commands can only be used by the creator of this bot!"):
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

    @commands.command(breif="Built for Owner",
                      description="Get shell info of the server where the bot is deployed",
                      help="Get shell info of the server where the bot is deployed")
    async def shell_info(self, ctx):
        loading_message = await ctx.send(embed=self.please_wait_emb)
        if ctx.author.id == self.bot_creator_id:
            try:
                embed2 = discord.Embed(
                    title="Cleared Screen", description="The command ran successfully! ", color=getembed.Common.COLOR)
                embed2.set_author(name=str(self.client.user.name),
                                  icon_url=getembed.Common.AUTHOR_LINK)
                embed2.add_field(name="Operating System",
                                 value=f"```{pltfsys()}```", inline=False)
                embed2.add_field(
                    name="User", value=f"```{pcusername()}```", inline=False)
                embed2.add_field(name="Python Version",
                                 value=f"```{pyversion()}```", inline=False)
                embed2.add_field(name="Discord API Version",
                                 value=f"```{discord.__version__}```", inline=False)
                # try:
                #     embed2.add_field(name="CPU", value=f"```{(subprocess.check_output('lscpu', shell=True).strip()).decode()}```", inline=False)
                # except:
                #     pass
                await loading_message.delete()
                await ctx.send(embed=embed2)

            except Exception as e:
                embed2 = discord.Embed(title=getembed.ErrorEmbeds.TITLE,
                                       description=getembed.ErrorEmbeds.DESCRIPTION, color=getembed.ErrorEmbeds.COLOR)
                embed2.set_author(name=str(self.client.user.name),
                                  icon_url=getembed.Common.AUTHOR_LINK)
                embed2.set_thumbnail(url=getembed.ErrorEmbeds.THUMBNAIL)
                embed2.add_field(name="Error:", value=f"{e}", inline=False)
                embed2.set_footer(text=f"Requested by {ctx.author.name}")
                await loading_message.delete()
                await ctx.send(embed=embed2)

        else:
            embed2 = discord.Embed(title=getembed.ErrorEmbeds.TITLE,
                                   description=getembed.ErrorEmbeds.DESCRIPTION, color=getembed.ErrorEmbeds.COLOR)
            embed2.set_author(name=str(self.client.user.name),
                              icon_url=getembed.Common.AUTHOR_LINK)
            embed2.set_thumbnail(url=getembed.ErrorEmbeds.THUMBNAIL)
            embed2.add_field(
                name="Error:", value=f"```You don't have permission to use this command!```", inline=False)
            embed2.set_footer(text=f"Requested by {ctx.author.name}")
            await loading_message.delete()
            await ctx.send(embed=embed2)

    @commands.command(breif="Built for Owner",
                      description="Run a command and send the output",
                      help="Run a command and send the output")
    async def shell_run(self, ctx, *, cnmd: str = None):
        loading_message = await ctx.send(embed=self.please_wait_emb)
        if ctx.author.id == self.bot_creator_id:
            try:
                if cnmd is None:
                    process = await asyncio.create_subprocess_shell(cnmd, stdout=asyncio.subprocess.PIPE)
                    stdout, stderr = await process.communicate()
                    try:
                        if stdout:
                            await loading_message.delete()
                            await ctx.send(f'`{cnmd}`\n```{stdout.decode().strip()}```')
                        elif stderr:
                            await loading_message.delete()
                            await ctx.send(f'`{cnmd}`\n```{stderr.decode().strip()}```')
                        else:
                            embed2 = discord.Embed(
                                title=getembed.ErrorEmbeds.TITLE, description=getembed.ErrorEmbeds.DESCRIPTION, color=getembed.ErrorEmbeds.COLOR)
                            embed2.set_author(
                                name=str(self.client.user.name), icon_url=getembed.Common.AUTHOR_LINK)
                            embed2.set_thumbnail(
                                url=getembed.ErrorEmbeds.THUMBNAIL)
                            embed2.add_field(
                                name="Error:", value=f"Unable to get the output!", inline=False)
                            embed2.set_footer(
                                text=f"Requested by {ctx.author.name}")
                            await loading_message.delete()
                            await ctx.send(embed=embed2)

                    except Exception as e:
                        embed2 = discord.Embed(
                            title=getembed.ErrorEmbeds.TITLE, description=getembed.ErrorEmbeds.DESCRIPTION, color=getembed.ErrorEmbeds.COLOR)
                        embed2.set_author(
                            name=str(self.client.user.name), icon_url=getembed.Common.AUTHOR_LINK)
                        embed2.set_thumbnail(
                            url=getembed.ErrorEmbeds.THUMBNAIL)
                        embed2.add_field(
                            name="Error:", value=f"```{e}```", inline=False)
                        embed2.set_footer(
                            text=f"Requested by {ctx.author.name}")
                        await loading_message.delete()
                        await ctx.send(embed=embed2)

            except Exception as e:
                embed2 = discord.Embed(title=getembed.ErrorEmbeds.TITLE,
                                       description=getembed.ErrorEmbeds.DESCRIPTION, color=getembed.ErrorEmbeds.COLOR)
                embed2.set_author(name=str(self.client.user.name),
                                  icon_url=getembed.Common.AUTHOR_LINK)
                embed2.set_thumbnail(url=getembed.ErrorEmbeds.THUMBNAIL)
                embed2.add_field(name="Error:", value=f"{e}", inline=False)
                embed2.set_footer(text=f"Requested by {ctx.author.name}")
                await loading_message.delete()
                await ctx.send(embed=embed2)

        else:
            embed2 = discord.Embed(title=getembed.ErrorEmbeds.TITLE,
                                   description=getembed.ErrorEmbeds.DESCRIPTION, color=getembed.ErrorEmbeds.COLOR)
            embed2.set_author(name=str(self.client.user.name),
                              icon_url=getembed.Common.AUTHOR_LINK)
            embed2.set_thumbnail(url=getembed.ErrorEmbeds.THUMBNAIL)
            embed2.add_field(
                name="Error:", value=f"```You don't have permission to use this command!```", inline=False)
            embed2.set_footer(text=f"Requested by {ctx.author.name}")
            await loading_message.delete()
            await ctx.send(embed=embed2)

    @commands.command(aliases=["shell_cls"],
                      breif="Built for Owner",
                      description="Clear the shell / run 'clear' or 'cls' by identidying the OS",
                      help="Clear the shell / run 'clear' or 'cls' by identidying the OS")
    async def shell_clear(self, ctx):
        loading_message = await ctx.send(embed=self.please_wait_emb)
        if ctx.author.id == self.bot_creator_id:
            try:

                if pltfsys().lower().startswith('win'):
                    os.system('cls')
                    ostype = "Microsoft Windows"
                    command = "cls"
                else:
                    os.system('clear')
                    ostype = pltfsys()
                    command = "clear"

                embed2 = discord.Embed(
                    title="Cleared Screen", description="The command ran successfully! ", color=getembed.Common.COLOR)
                embed2.set_author(name=str(self.client.user.name),
                                  icon_url=getembed.Common.AUTHOR_LINK)
                embed2.add_field(name="OS", value=f"{ostype}", inline=False)
                embed2.add_field(
                    name="Command", value=f"```{command}```", inline=False)
                await loading_message.delete()
                await ctx.send(embed=embed2)

            except Exception as e:
                embed2 = discord.Embed(title=getembed.ErrorEmbeds.TITLE,
                                       description=getembed.ErrorEmbeds.DESCRIPTION, color=getembed.ErrorEmbeds.COLOR)
                embed2.set_author(name=str(self.client.user.name),
                                  icon_url=getembed.Common.AUTHOR_LINK)
                embed2.set_thumbnail(url=getembed.ErrorEmbeds.THUMBNAIL)
                embed2.add_field(name="Error:", value=f"{e}", inline=False)
                embed2.set_footer(text=f"Requested by {ctx.author.name}")
                await loading_message.delete()
                await ctx.send(embed=embed2)

        else:
            embed2 = discord.Embed(title=getembed.ErrorEmbeds.TITLE,
                                   description=getembed.ErrorEmbeds.DESCRIPTION, color=getembed.ErrorEmbeds.COLOR)
            embed2.set_author(name=str(self.client.user.name),
                              icon_url=getembed.Common.AUTHOR_LINK)
            embed2.set_thumbnail(url=getembed.ErrorEmbeds.THUMBNAIL)
            embed2.add_field(
                name="Error:", value=f"```You don't have permission to use this command!```", inline=False)
            embed2.set_footer(text=f"Requested by {ctx.author.name}")
            await loading_message.delete()
            await ctx.send(embed=embed2)

    @commands.command(
        breif="Built for Owner",
        description="Blacklist a user from using the bot",
        help="Blacklist a user from using the bot")
    async def blacklist_user(self, ctx, member: discord.Member = None):
        loading_message = await ctx.send(embed=self.please_wait_emb)
        if ctx.author.id == self.bot_creator_id:
            try:
                if member == None:
                    embed2 = discord.Embed(
                        title=getembed.ErrorEmbeds.TITLE, description=getembed.ErrorEmbeds.DESCRIPTION, color=getembed.ErrorEmbeds.COLOR)
                    embed2.set_author(name=str(self.client.user.name),
                                      icon_url=getembed.Common.AUTHOR_LINK)
                    embed2.set_thumbnail(url=getembed.ErrorEmbeds.THUMBNAIL)
                    embed2.add_field(
                        name="Error:", value=f"No user is mentioned", inline=False)
                    embed2.add_field(
                        name="Possible Fix:", value=f"Enter the member-id or tag the member at the end of the message", inline=False)
                    embed2.set_footer(text=f"Requested by {ctx.author.name}")
                    await loading_message.delete()
                    await ctx.send(embed=embed2)
                    return

                await ctx.send(f"[+] Blacklisting the user with id: **{member.id}**")
                blacklistmgr.blacklist_user(int(member.id))
                await loading_message.delete()
                await ctx.send(f"[+] Added **{member.id}** to the blacklist - This user can no longer use any command of this bot!")

            except Exception as e:
                embed2 = discord.Embed(title=getembed.ErrorEmbeds.TITLE,
                                       description=getembed.ErrorEmbeds.DESCRIPTION, color=getembed.ErrorEmbeds.COLOR)
                embed2.set_author(name=str(self.client.user.name),
                                  icon_url=getembed.Common.AUTHOR_LINK)
                embed2.set_thumbnail(url=getembed.ErrorEmbeds.THUMBNAIL)
                embed2.add_field(name="Error:", value=f"{e}", inline=False)
                embed2.set_footer(text=f"Requested by {ctx.author.name}")
                await loading_message.delete()
                await ctx.send(embed=embed2)

        else:
            embed2 = discord.Embed(title=getembed.ErrorEmbeds.TITLE,
                                   description=getembed.ErrorEmbeds.DESCRIPTION, color=getembed.ErrorEmbeds.COLOR)
            embed2.set_author(name=str(self.client.user.name),
                              icon_url=getembed.Common.AUTHOR_LINK)
            embed2.set_thumbnail(url=getembed.ErrorEmbeds.THUMBNAIL)
            embed2.add_field(
                name="Error:", value=f"```You don't have permission to use this command!```", inline=False)
            embed2.set_footer(text=f"Requested by {ctx.author.name}")
            await loading_message.delete()
            await ctx.send(embed=embed2)

    @commands.command(
        breif="Built for Owner",
        description="Blacklist the current server from using the bot",
        help="Blacklist the current server from using the bot")
    async def blacklist_this_server(self, ctx):
        loading_message = await ctx.send(embed=self.please_wait_emb)
        if ctx.author.id == self.bot_creator_id:
            try:
                await ctx.send(f"[+] Blacklisting the current server! {ctx.guild.id} - {ctx.guild.name} - {ctx.guild.region} - Made by {ctx.guild.owner_id}")
                blacklistmgr.blacklist_server(int(ctx.guild.id))
                await loading_message.delete()
                await ctx.send(f"[+] Added **{ctx.guild.id}** to the blacklist - This server can no longer use any command of this bot!")

            except Exception as e:
                embed2 = discord.Embed(title=getembed.ErrorEmbeds.TITLE,
                                       description=getembed.ErrorEmbeds.DESCRIPTION, color=getembed.ErrorEmbeds.COLOR)
                embed2.set_author(name=str(self.client.user.name),
                                  icon_url=getembed.Common.AUTHOR_LINK)
                embed2.set_thumbnail(url=getembed.ErrorEmbeds.THUMBNAIL)
                embed2.add_field(name="Error:", value=f"{e}", inline=False)
                embed2.set_footer(text=f"Requested by {ctx.author.name}")
                await loading_message.delete()
                await ctx.send(embed=embed2)

        else:
            embed2 = discord.Embed(title=getembed.ErrorEmbeds.TITLE,
                                   description=getembed.ErrorEmbeds.DESCRIPTION, color=getembed.ErrorEmbeds.COLOR)
            embed2.set_author(name=str(self.client.user.name),
                              icon_url=getembed.Common.AUTHOR_LINK)
            embed2.set_thumbnail(url=getembed.ErrorEmbeds.THUMBNAIL)
            embed2.add_field(
                name="Error:", value=f"```You don't have permission to use this command!```", inline=False)
            embed2.set_footer(text=f"Requested by {ctx.author.name}")
            await loading_message.delete()
            await ctx.send(embed=embed2)

    @commands.command(
        breif="Built for Owner",
        description="Blacklist a server from using the bot",
        help="Blacklist a server from using the bot")
    async def blacklist_server(self, ctx, id=None):
        loading_message = await ctx.send(embed=self.please_wait_emb)
        if ctx.author.id == self.bot_creator_id:
            try:
                if id == None:
                    embed2 = discord.Embed(
                        title=getembed.ErrorEmbeds.TITLE, description=getembed.ErrorEmbeds.DESCRIPTION, color=getembed.ErrorEmbeds.COLOR)
                    embed2.set_author(name=str(self.client.user.name),
                                      icon_url=getembed.Common.AUTHOR_LINK)
                    embed2.set_thumbnail(url=getembed.ErrorEmbeds.THUMBNAIL)
                    embed2.add_field(
                        name="Error:", value=f"No user is mentioned", inline=False)
                    embed2.add_field(
                        name="Possible Fix:", value=f"Enter the member-id or tag the member at the end of the message", inline=False)
                    embed2.set_footer(text=f"Requested by {ctx.author.name}")
                    await loading_message.delete()
                    await ctx.send(embed=embed2)
                    return

                await ctx.send(f"[+] Blacklisting the server with id: {id}")
                blacklistmgr.blacklist_server(int(id))
                await loading_message.delete()
                await ctx.send(f"[+] Added **{id}** to the blacklist - This server can no longer use any command of this bot!")

            except Exception as e:
                embed2 = discord.Embed(title=getembed.ErrorEmbeds.TITLE,
                                       description=getembed.ErrorEmbeds.DESCRIPTION, color=getembed.ErrorEmbeds.COLOR)
                embed2.set_author(name=str(self.client.user.name),
                                  icon_url=getembed.Common.AUTHOR_LINK)
                embed2.set_thumbnail(url=getembed.ErrorEmbeds.THUMBNAIL)
                embed2.add_field(name="Error:", value=f"{e}", inline=False)
                embed2.set_footer(text=f"Requested by {ctx.author.name}")
                await loading_message.delete()
                await ctx.send(embed=embed2)

        else:
            embed2 = discord.Embed(title=getembed.ErrorEmbeds.TITLE,
                                   description=getembed.ErrorEmbeds.DESCRIPTION, color=getembed.ErrorEmbeds.COLOR)
            embed2.set_author(name=str(self.client.user.name),
                              icon_url=getembed.Common.AUTHOR_LINK)
            embed2.set_thumbnail(url=getembed.ErrorEmbeds.THUMBNAIL)
            embed2.add_field(
                name="Error:", value=f"```You don't have permission to use this command!```", inline=False)
            embed2.set_footer(text=f"Requested by {ctx.author.name}")
            await loading_message.delete()
            await ctx.send(embed=embed2)


def setup(client: commands.Bot):
    client.add_cog(OwnerOnly(client))
