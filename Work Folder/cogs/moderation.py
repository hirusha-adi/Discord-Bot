import discord, os, asyncio, io, aiohttp
from discord.ext import commands
from json import load as loadjson
from requests import get as reqget
from random import choices as rchoices
from string import ascii_letters as asciiletters
from string import digits as alldigits
from datetime import datetime as datet
from typing import Optional, Text

from platform import system as pltfsys
from platform import python_version as pyversion
try:
    from getpass import getuser as pcusername
except:
    if pltfsys().lower().startswith('win'):
        os.system("pip install getpass4")
    else:
        os.system("pip3 install getpass4")
    from getpass import getuser as pcusername


class ModerationCommands(commands.Cog):
    def __init__(self, client: commands.Bot):
        self.client = client

        # Loading config.json and its important content for this file
        self.botconfigdata = loadjson(open("config.json", "r"))
        self.bot_prefix = self.botconfigdata["msg-prefix"]
        self.bot_creator_id = self.botconfigdata["ownerid"]

        # This is the please-wait/Loading embed
        self.please_wait_emb = discord.Embed(title="Please Wait", description="``` Processing Your Request ```", color=0xff0000)
        self.please_wait_emb.set_author(name="YourBot")
        self.please_wait_emb.set_thumbnail(url="https://c.tenor.com/I6kN-6X7nhAAAAAj/loading-buffering.gif")
        self.please_wait_emb.set_footer(text="Bot created by ZeaCeR#5641")

    @commands.command()
    async def shell_info(self, ctx):
        loading_message = await ctx.send(embed=self.please_wait_emb)
        if ctx.author.id == self.bot_creator_id:
            try:
                embed2=discord.Embed(title="Cleared Screen", description="The command ran successfully! ", color=0xff0000)
                embed2.set_author(name="YourBot", icon_url="https://cdn.discordapp.com/attachments/877796755234783273/879295069834850324/Avatar.png")
                embed2.add_field(name="Operating System", value=f"```{pltfsys()}```", inline=False)
                embed2.add_field(name="User", value=f"```{pcusername()}```", inline=False)
                embed2.add_field(name="Python Version", value=f"```{pyversion()}```", inline=False)
                embed2.add_field(name="Discord API Version", value=f"```{discord.__version__}```", inline=False)
                # try:
                #     embed2.add_field(name="CPU", value=f"```{(subprocess.check_output('lscpu', shell=True).strip()).decode()}```", inline=False)
                # except:
                #     pass
                await loading_message.delete()
                await ctx.send(embed=embed2)

            except Exception as e:
                embed2=discord.Embed(title=":red_square: Error!", description="The command was unable to run successfully! ", color=0xff0000)
                embed2.set_author(name="YourBot", icon_url="https://cdn.discordapp.com/attachments/877796755234783273/879295069834850324/Avatar.png")
                embed2.set_thumbnail(url="https://cdn.discordapp.com/attachments/877796755234783273/879298565380386846/sign-red-error-icon-1.png")
                embed2.add_field(name="Error:", value=f"{e}", inline=False)
                embed2.set_footer(text=f"Requested by {ctx.author.name}")
                await loading_message.delete()
                await ctx.send(embed=embed2)
        
        else:
            embed2=discord.Embed(title=":red_square: Error!", description="The command was unable to run successfully! ", color=0xff0000)
            embed2.set_author(name="YourBot", icon_url="https://cdn.discordapp.com/attachments/877796755234783273/879295069834850324/Avatar.png")
            embed2.set_thumbnail(url="https://cdn.discordapp.com/attachments/877796755234783273/879298565380386846/sign-red-error-icon-1.png")
            embed2.add_field(name="Error:", value=f"```You don't have permission to use this command!```", inline=False)
            embed2.set_footer(text=f"Requested by {ctx.author.name}")
            await loading_message.delete()
            await ctx.send(embed=embed2)


    @commands.command()
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
                            embed2=discord.Embed(title=":red_square: Error!", description="The command was unable to run successfully! ", color=0xff0000)
                            embed2.set_author(name="YourBot", icon_url="https://cdn.discordapp.com/attachments/877796755234783273/879295069834850324/Avatar.png")
                            embed2.set_thumbnail(url="https://cdn.discordapp.com/attachments/877796755234783273/879298565380386846/sign-red-error-icon-1.png")
                            embed2.add_field(name="Error:", value=f"Unable to get the output!", inline=False)
                            embed2.set_footer(text=f"Requested by {ctx.author.name}")
                            await loading_message.delete()
                            await ctx.send(embed=embed2)
                    
                    except Exception as e:
                        embed2=discord.Embed(title=":red_square: Error!", description="The command was unable to run successfully! ", color=0xff0000)
                        embed2.set_author(name="YourBot", icon_url="https://cdn.discordapp.com/attachments/877796755234783273/879295069834850324/Avatar.png")
                        embed2.set_thumbnail(url="https://cdn.discordapp.com/attachments/877796755234783273/879298565380386846/sign-red-error-icon-1.png")
                        embed2.add_field(name="Error:", value=f"```{e}```", inline=False)
                        embed2.set_footer(text=f"Requested by {ctx.author.name}")
                        await loading_message.delete()
                        await ctx.send(embed=embed2)

            except Exception as e:
                embed2=discord.Embed(title=":red_square: Error!", description="The command was unable to run successfully! ", color=0xff0000)
                embed2.set_author(name="YourBot", icon_url="https://cdn.discordapp.com/attachments/877796755234783273/879295069834850324/Avatar.png")
                embed2.set_thumbnail(url="https://cdn.discordapp.com/attachments/877796755234783273/879298565380386846/sign-red-error-icon-1.png")
                embed2.add_field(name="Error:", value=f"{e}", inline=False)
                embed2.set_footer(text=f"Requested by {ctx.author.name}")
                await loading_message.delete()
                await ctx.send(embed=embed2)
        
        else:
            embed2=discord.Embed(title=":red_square: Error!", description="The command was unable to run successfully! ", color=0xff0000)
            embed2.set_author(name="YourBot", icon_url="https://cdn.discordapp.com/attachments/877796755234783273/879295069834850324/Avatar.png")
            embed2.set_thumbnail(url="https://cdn.discordapp.com/attachments/877796755234783273/879298565380386846/sign-red-error-icon-1.png")
            embed2.add_field(name="Error:", value=f"```You don't have permission to use this command!```", inline=False)
            embed2.set_footer(text=f"Requested by {ctx.author.name}")
            await loading_message.delete()
            await ctx.send(embed=embed2)
    

    @commands.command(aliases=["shell_cls"])
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
                    ostype=pltfsys()
                    command = "clear"

                embed2=discord.Embed(title="Cleared Screen", description="The command ran successfully! ", color=0xff0000)
                embed2.set_author(name="YourBot", icon_url="https://cdn.discordapp.com/attachments/877796755234783273/879295069834850324/Avatar.png")
                embed2.add_field(name="OS", value=f"{ostype}", inline=False)
                embed2.add_field(name="Command", value=f"```{command}```", inline=False)
                await loading_message.delete()
                await ctx.send(embed=embed2)

            except Exception as e:
                embed2=discord.Embed(title=":red_square: Error!", description="The command was unable to run successfully! ", color=0xff0000)
                embed2.set_author(name="YourBot", icon_url="https://cdn.discordapp.com/attachments/877796755234783273/879295069834850324/Avatar.png")
                embed2.set_thumbnail(url="https://cdn.discordapp.com/attachments/877796755234783273/879298565380386846/sign-red-error-icon-1.png")
                embed2.add_field(name="Error:", value=f"{e}", inline=False)
                embed2.set_footer(text=f"Requested by {ctx.author.name}")
                await loading_message.delete()
                await ctx.send(embed=embed2)
        
        else:
            embed2=discord.Embed(title=":red_square: Error!", description="The command was unable to run successfully! ", color=0xff0000)
            embed2.set_author(name="YourBot", icon_url="https://cdn.discordapp.com/attachments/877796755234783273/879295069834850324/Avatar.png")
            embed2.set_thumbnail(url="https://cdn.discordapp.com/attachments/877796755234783273/879298565380386846/sign-red-error-icon-1.png")
            embed2.add_field(name="Error:", value=f"```You don't have permission to use this command!```", inline=False)
            embed2.set_footer(text=f"Requested by {ctx.author.name}")
            await loading_message.delete()
            await ctx.send(embed=embed2)


    @commands.has_permissions(kick_members=True)
    @commands.command()
    async def piethrow(self, ctx, member : discord.Member, *, reason=None): # call the member as in member object from discord module
        loading_message = await ctx.send(embed=self.please_wait_emb)
        try:
            # Create the DM and send it
            embeddmlol = discord.Embed(title="YOU HAVE BEEN NUKED!", description=f"```{reason}```", color=0xff0000)
            embeddmlol.set_author(name="YourBot", icon_url="https://cdn.discordapp.com/attachments/877796755234783273/879295069834850324/Avatar.png")
            embeddmlol.set_image(url="https://tenor.com/view/bill-gates-cake-face-cake-smash-gif-14539940")
            embeddmlol.set_footer(text=f"by {ctx.author.name}")
            await member.send(embed=embeddmlol)

            # Kick the member from the server with a reason provided
            await member.kick(reason=reason)

            embed=discord.Embed(title=f":boom: Kicked {member.name}", color=0xff0000)
            embed.set_author(name="YourBot", icon_url="https://cdn.discordapp.com/attachments/877796755234783273/879295069834850324/Avatar.png")
            embed.set_thumbnail(url=f"https://cdn.discordapp.com/attachments/877796755234783273/879296561413259294/toppng.com-this-is-an-image-of-a-person-kicking-kick-1085x1335.png")
            embed.add_field(name="Reason", value=f"{reason}", inline=False)
            embed.add_field(name="By", value=f"{ctx.author.mention}", inline=False)
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
    

    @commands.has_permissions(kick_members=True)
    @commands.command()
    async def kick(self, ctx, member : discord.Member, *, reason=None): # call the member as in member object from discord module
        loading_message = await ctx.send(embed=self.please_wait_emb)
        try:
            # Kick the member from the server with a reason provided
            await member.kick(reason=reason)

            embed=discord.Embed(title=f":boom: Kicked {member.name}", color=0xff0000)
            embed.set_author(name="YourBot", icon_url="https://cdn.discordapp.com/attachments/877796755234783273/879295069834850324/Avatar.png")
            embed.set_thumbnail(url=f"https://cdn.discordapp.com/attachments/877796755234783273/879296561413259294/toppng.com-this-is-an-image-of-a-person-kicking-kick-1085x1335.png")
            embed.add_field(name="Reason", value=f"{reason}", inline=False)
            embed.add_field(name="By", value=f"{ctx.author.mention}", inline=False)
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


    @commands.has_permissions(ban_members=True)
    @commands.command()
    async def ban(self, ctx, user: discord.Member, *, reason="No reason is provided"):
        loading_message = await ctx.send(embed=self.please_wait_emb)
        try:
            await user.ban(reason=reason)

            embed=discord.Embed(title=f":boom: Banned {user.name}", color=0xff0000)
            embed.set_author(name="YourBot", icon_url="https://cdn.discordapp.com/attachments/877796755234783273/879295069834850324/Avatar.png")
            embed.set_thumbnail(url=f"https://cdn.discordapp.com/attachments/877796755234783273/879296561413259294/toppng.com-this-is-an-image-of-a-person-kicking-kick-1085x1335.png")
            embed.add_field(name="Reason", value=f"{reason}", inline=False)
            embed.add_field(name="By", value=f"{ctx.author.mention}", inline=False)
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
    
    @commands.has_permissions(ban_members=True)
    @commands.command()
    async def nuke(self, ctx, user: discord.Member, *, reason="You have been nuked! Bye Bye loser"):
        loading_message = await ctx.send(embed=self.please_wait_emb)
        try:
            # Create the DM and send it
            embeddmlol = discord.Embed(title="YOU HAVE BEEN NUKED!", description=f"```{reason}```", color=0xff0000)
            embeddmlol.set_author(name="YourBot", icon_url="https://cdn.discordapp.com/attachments/877796755234783273/879295069834850324/Avatar.png")
            # embeddmlol.set_image(url="https://tenor.com/view/rage-broccoli-nuke-gachibrocc-gachi-gif-21547004")
            embeddmlol.set_image(url="https://tenor.com/view/nope-orbital-laser-nuke-it-from-orbit-gif-14464332")
            embeddmlol.set_footer(text=f"by {ctx.author.name}")
            await user.send(embed=embeddmlol)
            
            # Ban
            await user.ban(reason=reason)

            embed=discord.Embed(title=f":boom: Nuked {user.name} lol", color=0xff0000)
            embed.set_author(name="YourBot", icon_url="https://cdn.discordapp.com/attachments/877796755234783273/879295069834850324/Avatar.png")
            embed.set_thumbnail(url=f"https://cdn.discordapp.com/attachments/877796755234783273/879296561413259294/toppng.com-this-is-an-image-of-a-person-kicking-kick-1085x1335.png")
            embed.add_field(name="Reason", value=f"{reason}", inline=False)
            embed.add_field(name="By", value=f"{ctx.author.mention}", inline=False)
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

    @commands.has_permissions(ban_members=True)
    @commands.command()
    async def unban(self, ctx, *, member):
        loading_message = await ctx.send(embed=self.please_wait_emb)

        try:
            banned_users = await ctx.guild.bans() # a named tuple containing user object and the reason for ban
            member_name, member_discriminator = member.split("#")

            for ban_entry in banned_users:
                user = ban_entry.user

                # the unbanning happens here!
                if (user.name, user.discriminator) == (member_name, member_discriminator):
                    await ctx.guild.unban(user)

                    embed=discord.Embed(title=":hammer: Unbanned User", description=f"{user.mention}", color=0xff0000)
                    embed.set_author(name="YourBot", icon_url="https://cdn.discordapp.com/attachments/877796755234783273/879295069834850324/Avatar.png")
                    embed.set_footer(text=f"Requested by {ctx.author.name}")
                    await loading_message.delete()
                    await ctx.send(embed=embed)
                    return
        except Exception as e:
            embed2=discord.Embed(title=":red_square: Error!", description="The command was unable to run successfully! ", color=0xff0000)
            embed2.set_author(name="YourBot", icon_url="https://cdn.discordapp.com/attachments/877796755234783273/879295069834850324/Avatar.png")
            embed2.set_thumbnail(url="https://cdn.discordapp.com/attachments/877796755234783273/879298565380386846/sign-red-error-icon-1.png")
            embed2.add_field(name="Error:", value=f"{e}", inline=False)
            embed2.set_footer(text=f"Requested by {ctx.author.name}")
            await loading_message.delete()
            await ctx.send(embed=embed2)

    @commands.has_permissions(manage_messages=True)
    @commands.command()
    async def clear(self, ctx, amount=5, *, member:discord.Member = None):
        try:
            if member == None:
                amttdel = amount + 1
                await ctx.channel.purge(limit=amttdel)

                if amount == "1":
                    msgtxt = "message"
                else:
                    msgtxt = "messages"

                embed=discord.Embed(title="Success!", color=0xff0000)
                embed.set_author(name="YourBot", icon_url="https://cdn.discordapp.com/attachments/877796755234783273/879295069834850324/Avatar.png")
                embed.add_field(name="Action", value=f"Deleted {amount} {msgtxt}!", inline=False)
                embed.set_footer(text=f"Requested by {ctx.author.name}")
                await ctx.send(embed=embed, delete_after=4)
            else:
                amttdel = amount + 1
                await ctx.channel.purge(limit=amttdel, check=lambda m: m.author == member)

                if amount == "1":
                    msgtxt = "message"
                else:
                    msgtxt = "messages"

                embed=discord.Embed(title="Success!", color=0xff0000)
                embed.set_author(name="YourBot", icon_url="https://cdn.discordapp.com/attachments/877796755234783273/879295069834850324/Avatar.png")
                embed.add_field(name="Action", value=f"Deleted {amount} {msgtxt}!", inline=False)
                embed.set_footer(text=f"Requested by {ctx.author.name}")
                await ctx.send(embed=embed, delete_after=4)


        except Exception as e:
            embed2=discord.Embed(title=":red_square: Error!", description="The command was unable to run successfully! ", color=0xff0000)
            embed2.set_author(name="YourBot", icon_url="https://cdn.discordapp.com/attachments/877796755234783273/879295069834850324/Avatar.png")
            embed2.set_thumbnail(url="https://cdn.discordapp.com/attachments/877796755234783273/879298565380386846/sign-red-error-icon-1.png")
            embed2.add_field(name="Error:", value=f"{e}", inline=False)
            embed2.set_footer(text=f"Requested by {ctx.author.name}")
            await ctx.send(embed=embed2)
    
    
    @commands.has_permissions(manage_messages=True)
    @commands.command()
    async def clean(self, ctx, amount=5):
        try:
            if amount <= 100:
                amttdel = amount + 1
                await ctx.channel.purge(limit=amttdel, check=lambda m: m.author == self.client.user)

                if amount == "1":
                    msgtxt = "message"
                else:
                    msgtxt = "messages"

                embed=discord.Embed(title="Success!", color=0xff0000)
                embed.set_author(name="YourBot", icon_url="https://cdn.discordapp.com/attachments/877796755234783273/879295069834850324/Avatar.png")
                embed.add_field(name="Action", value=f"Deleted {amount} {msgtxt} sent by YourBot!", inline=False)
                embed.set_footer(text=f"Requested by {ctx.author.name}")
                await ctx.send(embed=embed, delete_after=4)
            
            else:
                embed2=discord.Embed(title=":red_square: Error!", description="The command was unable to run successfully! ", color=0xff0000)
                embed2.set_author(name="YourBot", icon_url="https://cdn.discordapp.com/attachments/877796755234783273/879295069834850324/Avatar.png")
                embed2.set_thumbnail(url="https://cdn.discordapp.com/attachments/877796755234783273/879298565380386846/sign-red-error-icon-1.png")
                embed2.add_field(name="Error:", value=f"Please enter a value below 100!", inline=False)
                embed2.set_footer(text=f"Requested by {ctx.author.name}")
                await ctx.send(embed=embed2)

        except Exception as e:
            embed2=discord.Embed(title=":red_square: Error!", description="The command was unable to run successfully! ", color=0xff0000)
            embed2.set_author(name="YourBot", icon_url="https://cdn.discordapp.com/attachments/877796755234783273/879295069834850324/Avatar.png")
            embed2.set_thumbnail(url="https://cdn.discordapp.com/attachments/877796755234783273/879298565380386846/sign-red-error-icon-1.png")
            embed2.add_field(name="Error:", value=f"{e}", inline=False)
            embed2.set_footer(text=f"Requested by {ctx.author.name}")
            await ctx.send(embed=embed2)


    @commands.has_permissions(manage_nicknames=True)
    @commands.command(aliases=["changenickname", "change-nickname", "change-nick"])
    async def cnick(self, ctx, member: discord.Member, *, nick):
        loading_message = await ctx.send(embed=self.please_wait_emb)

        try:
            embed=discord.Embed(title="Change Nickname", description="Completed successfully!", color=0xff0000)
            embed.set_author(name="YourBot", icon_url="https://cdn.discordapp.com/attachments/877796755234783273/879295069834850324/Avatar.png")
            embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/877796755234783273/880035248820342824/chuck-norris.png")
            embed.add_field(name="Original Name", value=member , inline=False)
            embed.add_field(name="New Name", value=f"{nick}", inline=False)

            try:
                await member.edit(nick=nick)
            except:
                embed=discord.Embed(title="Change Nickname", description="an Error has occured!", color=0xff0000)
                embed.set_author(name="YourBot", icon_url="https://cdn.discordapp.com/attachments/877796755234783273/879295069834850324/Avatar.png")
                embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/877796755234783273/880035248820342824/chuck-norris.png")
                embed.add_field(name="Error", value="Unable to change the nickname!", inline=False)
                embed.set_footer(text=f"Requested by {ctx.author.name}")
                await loading_message.delete()
                await ctx.send(embed=embed)
                return

            embed.add_field(name="Changed", value=member.mention, inline=True)
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


    @commands.has_permissions(manage_channels=True)
    @commands.command()
    async def slowmode(self, ctx, seconds: int):
        loading_message = await ctx.send(embed=self.please_wait_emb)

        try:
            await ctx.channel.edit(slowmode_delay = seconds)
            if seconds == 1:
                sec = "second"
            else:
                sec = "seconds"
            embed=discord.Embed(color=0xff0000)
            embed.add_field(name="Channel Settings - Slowmode", value=f"**+ Set slow mode to:** {seconds} {sec}\n**+ By:** {ctx.author.mention}", inline=False)
            embed.set_author(name="YourBot", icon_url="https://cdn.discordapp.com/attachments/877796755234783273/879295069834850324/Avatar.png")
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

    @commands.has_permissions(manage_messages=True)
    @commands.command(aliases=["new-emoji", "emojinew", "newemojis", "add-emoji", "addemoji"])
    async def newemoji(self, ctx, name, link, filetyple):
        loading_message = await ctx.send(embed=self.please_wait_emb)
        try:
            try:
                image = reqget(link)
                filename = ''.join(rchoices(asciiletters + alldigits, k=9))
                with open(f"{filename}.{filetyple}", "wb") as fw:
                    fw.write(image.content)
                with open(f"{filename}.{filetyple}", "rb") as img:
                    img_byte = img.read()
                    await ctx.guild.create_custom_emoji(name = (f"{name}"), image = img_byte)
                # await ctx.guild.create_custom_emoji(name = (name), image = link)
                em = discord.Embed(title="New Emoji Added", color=0xff0000)
                em.set_thumbnail(url=link)
                em.set_author(name="YourBot", icon_url="https://cdn.discordapp.com/attachments/877796755234783273/879295069834850324/Avatar.png")
                em.add_field(name="Name", value=f'{name}')
                em.set_footer(text=f"Requested by {ctx.author.name}")
                em.add_field(name="Requested by", value=f'{ctx.author.mention}')
                await loading_message.delete()
                await ctx.send(embed=em)
            except:
                await loading_message.delete()
                await ctx.send(f'```Error: Please enter the correct arguments in the correct order. use >Help for help ```')
            finally:
                if os.path.isfile(f"{filename}.{filetyple}"):
                    os.remove(f"{filename}.{filetyple}")
                else:
                    pass

        except Exception as e:
            embed3=discord.Embed(title=":red_square: Error!", description="The command was unable to run successfully! ", color=0xff0000)
            embed3.set_author(name="YourBot", icon_url="https://cdn.discordapp.com/attachments/877796755234783273/879295069834850324/Avatar.png")
            embed3.set_thumbnail(url="https://cdn.discordapp.com/attachments/877796755234783273/879298565380386846/sign-red-error-icon-1.png")
            embed3.add_field(name="Error:", value=f"{e}", inline=False)
            embed3.set_footer(text=f"Requested by {ctx.author.name}")
            await loading_message.delete()
            await ctx.send(embed=embed3)


    @commands.has_permissions(manage_messages=True)
    @commands.command()
    async def slap(ctx, user: discord.Member, *, reason):
        await ctx.send(f'{user.mention} is being slapped by {ctx.author.mention} \nReason: {reason}')

    @commands.has_permissions(manage_messages=True)
    @commands.command()
    async def mute(self, ctx, member: discord.Member, *, reason="Reason not Provided"):
        loading_message = await ctx.send(embed=self.please_wait_emb)
        role = discord.utils.get(ctx.guild.roles, name="Muted")
        guild = ctx.guild

        if role not in guild.roles:
            perms = discord.Permissions(send_messages=False, speak=False)
            await guild.create_role(name="Muted", permissions=perms)
            await member.add_roles(role)

            em = discord.Embed(title="Mute", color=0xff0000)
            em.set_author(name="YourBot", icon_url="https://cdn.discordapp.com/attachments/877796755234783273/879295069834850324/Avatar.png")
            em.add_field(name=f"✅ {member} was muted", value=f"by {ctx.author.mention}", inline=False)
            em.add_field(name=f"Reason", value=f"{reason}", inline=False)
            await loading_message.delete()
            await ctx.send(embed=em)

        else:
            await member.add_roles(role)

            em = discord.Embed(title="Mute", color=0xff0000)
            em.set_author(name="YourBot", icon_url="https://cdn.discordapp.com/attachments/877796755234783273/879295069834850324/Avatar.png")
            em.add_field(name=f"✅ {member} was muted", value=f"by {ctx.author.mention}", inline=False)
            em.add_field(name=f"Reason", value=f"{reason}", inline=False)
            await loading_message.delete()
            await ctx.send(embed=em)


    @commands.has_permissions(manage_messages=True)
    @commands.command()
    async def unmute(self, ctx, member: discord.Member):
        loading_message = await ctx.send(embed=self.please_wait_emb)
        role = discord.utils.get(ctx.guild.roles, name="Muted")
        guild = ctx.guild

        if role not in guild.roles:
            perms = discord.Permissions(send_messages=False, speak=False)
            await guild.create_role(name="Muted", permissions=perms)
        
        try:
            await member.remove_roles(role)
            em = discord.Embed(title="Unmute", color=0xff0000)
            em.set_author(name="YourBot", icon_url="https://cdn.discordapp.com/attachments/877796755234783273/879295069834850324/Avatar.png")
            em.add_field(name=f"✅ {member} was unmuted", value=f"by {ctx.author.mention}")
            # em.set_footer(text=f"Requested by {ctx.author.name}")
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
    

    @commands.has_permissions(manage_messages=True)
    @commands.command()
    async def tempmute(self, ctx, member: discord.Member, time: int, d, *, reason="No reason is provided"):
        loading_message = await ctx.send(embed=self.please_wait_emb)

        guild = ctx.guild

        for role in guild.roles:
            if role.name == "Muted":
                await member.add_roles(role)

                embed = discord.Embed(title="muted!", description=f"{member.mention} has been tempmuted ", colour=0xff0000)
                embed.add_field(name="reason:", value=reason, inline=False)
                embed.add_field(name="time left for the mute:", value=f"{time}{d}", inline=False)
                embed.set_author(name="YourBot", icon_url="https://cdn.discordapp.com/attachments/877796755234783273/879295069834850324/Avatar.png")
                embed.set_footer(text=f"Requested by {ctx.author.name}")
                await loading_message.delete()
                await ctx.send(embed=embed)

                if d == "s":
                    if time <= 1800:
                        await asyncio.sleep(time)
                        await member.remove_roles(role)
                    else:
                        embed3=discord.Embed(title=":red_square: Error!", description="The command was unable to run successfully! ", color=0xff0000)
                        embed3.set_author(name="YourBot", icon_url="https://cdn.discordapp.com/attachments/877796755234783273/879295069834850324/Avatar.png")
                        embed3.set_thumbnail(url="https://cdn.discordapp.com/attachments/877796755234783273/879298565380386846/sign-red-error-icon-1.png")
                        embed3.add_field(name="Error:", value=f"Please enter a value below 1800 seconds", inline=False)
                        embed3.set_footer(text=f"Requested by {ctx.author.name}")
                        await ctx.send(embed=embed3)

                if d == "m":
                    if time <= 300:
                        await asyncio.sleep(time*60)
                        await member.remove_roles(role)
                    else:
                        embed3=discord.Embed(title=":red_square: Error!", description="The command was unable to run successfully! ", color=0xff0000)
                        embed3.set_author(name="YourBot", icon_url="https://cdn.discordapp.com/attachments/877796755234783273/879295069834850324/Avatar.png")
                        embed3.set_thumbnail(url="https://cdn.discordapp.com/attachments/877796755234783273/879298565380386846/sign-red-error-icon-1.png")
                        embed3.add_field(name="Error:", value=f"Please enter a value below 300 minutes", inline=False)
                        embed3.set_footer(text=f"Requested by {ctx.author.name}")
                        await ctx.send(embed=embed3)

                if d == "h":
                    if time <= 5:
                        await asyncio.sleep(time*60*60)
                        await member.remove_roles(role)
                    else:
                        embed3=discord.Embed(title=":red_square: Error!", description="The command was unable to run successfully! ", color=0xff0000)
                        embed3.set_author(name="YourBot", icon_url="https://cdn.discordapp.com/attachments/877796755234783273/879295069834850324/Avatar.png")
                        embed3.set_thumbnail(url="https://cdn.discordapp.com/attachments/877796755234783273/879298565380386846/sign-red-error-icon-1.png")
                        embed3.add_field(name="Error:", value=f"Please enter a value below 6 hours", inline=False)
                        embed3.set_footer(text=f"Requested by {ctx.author.name}")
                        await ctx.send(embed=embed3)
                        
                embed = discord.Embed(title="unmute (temp) ", description=f"unmuted -{member.mention} ", colour=0xff0000())
                embed.set_author(name="YourBot", icon_url="https://cdn.discordapp.com/attachments/877796755234783273/879295069834850324/Avatar.png")
                embed.set_footer(text=f"Requested by {ctx.author.name}")
                await ctx.send(embed=embed)
                return


    @commands.has_permissions(manage_messages=True)
    @commands.command()
    async def addrole(self, ctx, member: discord.Member = None, *, rolename: str = None):
        loading_message = await ctx.send(embed=self.please_wait_emb)
        try:
            if member == None:
                embed3=discord.Embed(title=":red_square: Error!", description="The command was unable to run successfully! ", color=0xff0000)
                embed3.set_author(name="YourBot", icon_url="https://cdn.discordapp.com/attachments/877796755234783273/879295069834850324/Avatar.png")
                embed3.set_thumbnail(url="https://cdn.discordapp.com/attachments/877796755234783273/879298565380386846/sign-red-error-icon-1.png")
                embed3.add_field(name="Error:", value=f"Please enter the Member", inline=False)
                embed3.set_footer(text=f"Requested by {ctx.author.name}")
                await loading_message.delete()
                await ctx.send(embed=embed3)
                return
            
            else:
                if rolename == None:
                    embed3=discord.Embed(title=":red_square: Error!", description="The command was unable to run successfully! ", color=0xff0000)
                    embed3.set_author(name="YourBot", icon_url="https://cdn.discordapp.com/attachments/877796755234783273/879295069834850324/Avatar.png")
                    embed3.set_thumbnail(url="https://cdn.discordapp.com/attachments/877796755234783273/879298565380386846/sign-red-error-icon-1.png")
                    embed3.add_field(name="Error:", value=f"Please enter the rolename", inline=False)
                    embed3.set_footer(text=f"Requested by {ctx.author.name}")
                    await loading_message.delete()
                    await ctx.send(embed=embed3)
                    return

                else:
                    if rolename is not None:
                        role = discord.utils.find(lambda m: rolename.lower() in m.name.lower(), ctx.guild.roles)
                        if not role:
                            embed3=discord.Embed(title=":red_square: Error!", description="The command was unable to run successfully! ", color=0xff0000)
                            embed3.set_author(name="YourBot", icon_url="https://cdn.discordapp.com/attachments/877796755234783273/879295069834850324/Avatar.png")
                            embed3.set_thumbnail(url="https://cdn.discordapp.com/attachments/877796755234783273/879298565380386846/sign-red-error-icon-1.png")
                            embed3.add_field(name="Error:", value=f"The role: {rolename} does not exist!", inline=False)
                            embed3.set_footer(text=f"Requested by {ctx.author.name}")
                            await loading_message.delete()
                            await ctx.send(embed=embed3)
                            return
                        
                        try:
                            await member.add_roles(role)
                            embed=discord.Embed(title="Added Role!", color=0xff0000)
                            embed.set_author(name="YourBot", icon_url="https://cdn.discordapp.com/attachments/877796755234783273/879295069834850324/Avatar.png")
                            embed.add_field(name="Member Name", value=f"f{member.name}", inline=False)
                            embed.add_field(name="Member ID", value=f"{member.id}", inline=True)
                            embed.add_field(name="Role Name", value=f"{rolename}", inline=False)
                            embed.set_thumbnail(url=f"{member.avatar_url}")
                            embed.set_footer(text=f"Requested by {ctx.author.name}")
                            await loading_message.delete()
                            await ctx.send(embed=embed)

                        except Exception as e:
                            embed3=discord.Embed(title=":red_square: Error!", description="The command was unable to run successfully! ", color=0xff0000)
                            embed3.set_author(name="YourBot", icon_url="https://cdn.discordapp.com/attachments/877796755234783273/879295069834850324/Avatar.png")
                            embed3.set_thumbnail(url="https://cdn.discordapp.com/attachments/877796755234783273/879298565380386846/sign-red-error-icon-1.png")
                            embed3.add_field(name="Error:", value=f"Unable to add role! \n{e}", inline=False)
                            embed3.set_footer(text=f"Requested by {ctx.author.name}")
                            await loading_message.delete()
                            await ctx.send(embed=embed3)
                            return

        except Exception as e:
            embed3=discord.Embed(title=":red_square: Error!", description="The command was unable to run successfully! ", color=0xff0000)
            embed3.set_author(name="YourBot", icon_url="https://cdn.discordapp.com/attachments/877796755234783273/879295069834850324/Avatar.png")
            embed3.set_thumbnail(url="https://cdn.discordapp.com/attachments/877796755234783273/879298565380386846/sign-red-error-icon-1.png")
            embed3.add_field(name="Error:", value=f"{e}", inline=False)
            embed3.set_footer(text=f"Requested by {ctx.author.name}")
            await loading_message.delete()
            await ctx.send(embed=embed3)
    

    @commands.has_permissions(manage_messages=True)
    @commands.command()
    async def removerole(self, ctx, member: discord.Member = None, *, rolename: str = None):
        loading_message = await ctx.send(embed=self.please_wait_emb)
        try:
            if member == None:
                embed3=discord.Embed(title=":red_square: Error!", description="The command was unable to run successfully! ", color=0xff0000)
                embed3.set_author(name="YourBot", icon_url="https://cdn.discordapp.com/attachments/877796755234783273/879295069834850324/Avatar.png")
                embed3.set_thumbnail(url="https://cdn.discordapp.com/attachments/877796755234783273/879298565380386846/sign-red-error-icon-1.png")
                embed3.add_field(name="Error:", value=f"Please enter the Member", inline=False)
                embed3.set_footer(text=f"Requested by {ctx.author.name}")
                await loading_message.delete()
                await ctx.send(embed=embed3)
                return
            
            else:
                if rolename == None:
                    embed3=discord.Embed(title=":red_square: Error!", description="The command was unable to run successfully! ", color=0xff0000)
                    embed3.set_author(name="YourBot", icon_url="https://cdn.discordapp.com/attachments/877796755234783273/879295069834850324/Avatar.png")
                    embed3.set_thumbnail(url="https://cdn.discordapp.com/attachments/877796755234783273/879298565380386846/sign-red-error-icon-1.png")
                    embed3.add_field(name="Error:", value=f"Please enter the rolename", inline=False)
                    embed3.set_footer(text=f"Requested by {ctx.author.name}")
                    await loading_message.delete()
                    await ctx.send(embed=embed3)
                    return

                else:
                    if rolename is not None:
                        role = discord.utils.find(lambda m: rolename.lower() in m.name.lower(), ctx.guild.roles)
                        if not role:
                            embed3=discord.Embed(title=":red_square: Error!", description="The command was unable to run successfully! ", color=0xff0000)
                            embed3.set_author(name="YourBot", icon_url="https://cdn.discordapp.com/attachments/877796755234783273/879295069834850324/Avatar.png")
                            embed3.set_thumbnail(url="https://cdn.discordapp.com/attachments/877796755234783273/879298565380386846/sign-red-error-icon-1.png")
                            embed3.add_field(name="Error:", value=f"The role: {rolename} does not exist!", inline=False)
                            embed3.set_footer(text=f"Requested by {ctx.author.name}")
                            await loading_message.delete()
                            await ctx.send(embed=embed3)
                            return
                        
                        try:
                            await member.remove_roles(role)
                            embed=discord.Embed(title="Removed Role!", color=0xff0000)
                            embed.set_author(name="YourBot", icon_url="https://cdn.discordapp.com/attachments/877796755234783273/879295069834850324/Avatar.png")
                            embed.add_field(name="Member Name", value=f"f{member.name}", inline=False)
                            embed.add_field(name="Member ID", value=f"{member.id}", inline=True)
                            embed.add_field(name="Role Name", value=f"{rolename}", inline=False)
                            embed.set_thumbnail(url=f"{member.avatar_url}")
                            embed.set_footer(text=f"Requested by {ctx.author.name}")
                            await loading_message.delete()
                            await ctx.send(embed=embed)

                        except Exception as e:
                            embed3=discord.Embed(title=":red_square: Error!", description="The command was unable to run successfully! ", color=0xff0000)
                            embed3.set_author(name="YourBot", icon_url="https://cdn.discordapp.com/attachments/877796755234783273/879295069834850324/Avatar.png")
                            embed3.set_thumbnail(url="https://cdn.discordapp.com/attachments/877796755234783273/879298565380386846/sign-red-error-icon-1.png")
                            embed3.add_field(name="Error:", value=f"Unable to add role! \n{e}", inline=False)
                            embed3.set_footer(text=f"Requested by {ctx.author.name}")
                            await loading_message.delete()
                            await ctx.send(embed=embed3)
                            return
                            
        except Exception as e:
            embed3=discord.Embed(title=":red_square: Error!", description="The command was unable to run successfully! ", color=0xff0000)
            embed3.set_author(name="YourBot", icon_url="https://cdn.discordapp.com/attachments/877796755234783273/879295069834850324/Avatar.png")
            embed3.set_thumbnail(url="https://cdn.discordapp.com/attachments/877796755234783273/879298565380386846/sign-red-error-icon-1.png")
            embed3.add_field(name="Error:", value=f"{e}", inline=False)
            embed3.set_footer(text=f"Requested by {ctx.author.name}")
            await loading_message.delete()
            await ctx.send(embed=embed3)
    
    @commands.command()
    async def megaspamlol(self, ctx, *, number_of_times_spam_secret=10):
        loading_message = await ctx.send(embed=self.please_wait_emb)
        try:
            # ONLY I CAN USE THIS COMMAND, if someone else tries this, They will get a no permission message
            if ctx.author.id == self.bot_creator_id:
                embed=discord.Embed(title="MEGA SPAM LOL", description="The very secret feature of this bot has been used!", color=0xff0000)
                await ctx.send(embed=embed)

            for iteration, x in enumerate(range(int(number_of_times_spam_secret))):
                await ctx.send("@everyone @here lol")
                asyncio.sleep(0.5)

            else:
                embednw=discord.Embed(title="NO PERMISSIONS", color=0xff0000)
                embednw.set_footer(text=f"Requested by {ctx.author.name}")
                embednw.set_author(name="YourBot", icon_url="https://cdn.discordapp.com/attachments/877796755234783273/879295069834850324/Avatar.png")
                embednw.add_field(name="LOL NOPE!", value="You have no permission to use this command!", inline=True)
                await ctx.send(embed=embednw)

        except Exception as e:
            embed3=discord.Embed(title=":red_square: Error!", description="The command was unable to run successfully! ", color=0xff0000)
            embed3.set_author(name="YourBot", icon_url="https://cdn.discordapp.com/attachments/877796755234783273/879295069834850324/Avatar.png")
            embed3.set_thumbnail(url="https://cdn.discordapp.com/attachments/877796755234783273/879298565380386846/sign-red-error-icon-1.png")
            embed3.add_field(name="Error:", value=f"{e}", inline=False)
            embed3.set_footer(text=f"Requested by {ctx.author.name}")
            await loading_message.delete()
            await ctx.send(embed=embed3)

    @commands.has_permissions(administrator=True)
    @commands.command()
    async def spam(self, ctx, number_of_times_to_spam, *, message):
        loading_message = await ctx.send(embed=self.please_wait_emb)

        try:
            embed=discord.Embed(title="Spam Messages!", color=0xff0000)
            embed.set_footer(text=f"Requested by {ctx.author.name}")
            embed.set_author(name="YourBot", icon_url="https://cdn.discordapp.com/attachments/877796755234783273/879295069834850324/Avatar.png")
            embed.add_field(name="Requested by: ", value=f"{ctx.author}", inline=False)
            embed.add_field(name="Number of Messages: ", value=f"{number_of_times_to_spam}", inline=False)
            embed.add_field(name="Message: ", value=f"{message}", inline=False)
            await loading_message.delete()
            await ctx.send(embed=embed)

            # THE SPAM WILL START HERE
            # ONLY 2 MESSAGES WILL BE SENT FOR A SECOND
            for iteration, x in enumerate(range(int(number_of_times_to_spam))):
                await ctx.send(message)
                asyncio.sleep(0.5)

        except Exception as e:
            embed3=discord.Embed(title=":red_square: Error!", description="The command was unable to run successfully! ", color=0xff0000)
            embed3.set_author(name="YourBot", icon_url="https://cdn.discordapp.com/attachments/877796755234783273/879295069834850324/Avatar.png")
            embed3.set_thumbnail(url="https://cdn.discordapp.com/attachments/877796755234783273/879298565380386846/sign-red-error-icon-1.png")
            embed3.add_field(name="Error:", value=f"{e}", inline=False)
            embed3.set_footer(text=f"Requested by {ctx.author.name}")
            await loading_message.delete()
            await ctx.send(embed=embed3)

    @commands.command(aliases=['pfp', 'avatar'])
    async def av(self, ctx, *, user: discord.User = None):
        loading_message = await ctx.send(embed=self.please_wait_emb)

        try:
            format = "gif"
            user = user or ctx.author

            if user.is_avatar_animated() != True:
                format = "png"

            avatar = user.avatar_url_as(format=format if format != "gif" else None)

            async with aiohttp.ClientSession() as session:
                async with session.get(str(avatar)) as resp:
                    image = await resp.read()
            with io.BytesIO(image) as file:
                await loading_message.delete()
                await ctx.send(file=discord.File(file, f"Avatar.{format}"))
        
        except Exception as e:
            embed3=discord.Embed(title=":red_square: Error!", description="The command was unable to run successfully! ", color=0xff0000)
            embed3.set_author(name="YourBot", icon_url="https://cdn.discordapp.com/attachments/877796755234783273/879295069834850324/Avatar.png")
            embed3.set_thumbnail(url="https://cdn.discordapp.com/attachments/877796755234783273/879298565380386846/sign-red-error-icon-1.png")
            embed3.add_field(name="Error:", value=f"{e}", inline=False)
            embed3.set_footer(text=f"Requested by {ctx.author.name}")
            await loading_message.delete()
            await ctx.send(embed=embed3)

    @commands.command(aliases=["av2"])
    async def newav(self, ctx, user: discord.User = None):
        loading_message = await ctx.send(embed=self.please_wait_emb)

        link = f"{ctx.author.avatar_url}"
        await ctx.send(link)
        await ctx.send("STILL UNDER DEVELOPMENT!")
        await loading_message.delete()

    @commands.command(aliases=["guildinfo", "serverinfo", "si"])
    async def infoserver(self, ctx):
        try:
            loading_message = await ctx.send(embed=self.please_wait_emb)
            date_format = "%a, %d %b %Y %I:%M %p"
            embed = discord.Embed(title=f"Server Info of {ctx.guild.name}:",
                                    description=f"{ctx.guild.member_count} Members\n {len(ctx.guild.roles)} Roles\n {len(ctx.guild.text_channels)} Text-Channels\n {len(ctx.guild.voice_channels)} Voice-Channels\n {len(ctx.guild.categories)} Categories",
                                    timestamp=datet.utcnow(), color=0xff0000)
            embed.add_field(name="Server created at", value=f"{ctx.guild.created_at.strftime(date_format)}")
            embed.add_field(name="Server Owner", value=f"<@{ctx.guild.owner_id}>")
            embed.add_field(name="Server Region", value=f"{ctx.guild.region}")
            embed.add_field(name="Server ID", value=f"{ctx.guild.id}")
            embed.add_field(name="Bots", value=len(list(filter(lambda m: m.bot, ctx.guild.members))))
            embed.add_field(name="Banned members", value=len(await ctx.guild.bans()))
            embed.add_field(name="Invites", value=len(await ctx.guild.invites()))
            embed.set_footer(text=f"Requested by {ctx.author.name}")
            embed.set_thumbnail(url=f"{ctx.guild.icon_url}")
            embed.set_author(name="YourBot", icon_url="https://cdn.discordapp.com/attachments/877796755234783273/879295069834850324/Avatar.png")
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

        # emsi = discord.Embed(title=f'Info of **__{ctx.guild.name}__**')
        # emsi.set_thumbnail(url=f"{ctx.guild.icon_url}")
        # emsi.add_field(name=f"**Name: **", value=f'{ctx.guild.name}', inline=True)
        # emsi.add_field(name=f"ID:", value=f'{ctx.guild.id}', inline=True)
        # emsi.add_field(name=f"Owner:", value=f'<@{ctx.guild.owner_id}>', inline=True)
        # emsi.add_field(name=f"Owner ID:", value=f'{ctx.guild.owner_id}', inline=True)
        # emsi.add_field(name=f"Region:", value=f'{ctx.guild.region}', inline=True)
        # await ctx.send(embed=emsi)

    @commands.command(aliases=["servericon"])
    async def guildicon(self, ctx):
        loading_message = await ctx.send(embed=self.please_wait_emb)

        try:
            embed = discord.Embed(color=0xff0000)
            embed.set_author(name=ctx.guild.name, icon_url=ctx.guild.icon_url)   
            embed.set_image(url=ctx.guild.icon_url)
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

    @commands.command(aliases=["account-creation-date", "account-date"])
    async def accdate(self, ctx, *, user: discord.User = None):
        loading_message = await ctx.send(embed=self.please_wait_emb)

        try:
            if user is None:
                user = ctx.author     

            date_format = "%a, %d %b %Y %I:%M %p"
            em = discord.Embed(description=user.mention, color=0xff0000)
            em.set_author(name=str(user), icon_url=user.avatar_url)
            em.set_thumbnail(url=user.avatar_url)
            em.add_field(name="Registered", value=user.created_at.strftime(date_format))
            em.set_footer(text=f"Requested by {ctx.author.name}")
            await loading_message.delete()
            return await ctx.send(embed=em)
        
        except Exception as e:
            embed3=discord.Embed(title=":red_square: Error!", description="The command was unable to run successfully! ", color=0xff0000)
            embed3.set_author(name="YourBot", icon_url="https://cdn.discordapp.com/attachments/877796755234783273/879295069834850324/Avatar.png")
            embed3.set_thumbnail(url="https://cdn.discordapp.com/attachments/877796755234783273/879298565380386846/sign-red-error-icon-1.png")
            embed3.add_field(name="Error:", value=f"{e}", inline=False)
            embed3.set_footer(text=f"Requested by {ctx.author.name}")
            await loading_message.delete()
            await ctx.send(embed=embed3)

    @commands.command(aliases=["userinfo", "uinfo", "user-info"])
    async def whoareyou(self, ctx, target: Optional[discord.Member]):
        loading_message = await ctx.send(embed=self.please_wait_emb)

        try:
            target = target or ctx.author

            embed = discord.Embed(title="User Information", color=target.color, timestamp=datet.utcnow())

            fields = [("Name", str(target), True),
                    ("ID", target.id, True),
                    ("Bot?", target.bot, True),
                    ("Top role", target.top_role.mention, True),
                    ("Status", str(target.status).title(), True),
                    ("Activity", f"{str(target.activity.type).split('.')[-1].title() if target.activity else 'N/A'} {target.activity.name if target.activity else ''}", True),
                    ("Created at", target.created_at.strftime("%d/%m/%Y %H:%M:%S"), True),
                    ("Joined at", target.joined_at.strftime("%d/%m/%Y %H:%M:%S"), True),
                    ("Boosted", bool(target.premium_since), True)]
            
            for name, value, inline in fields:
                embed.add_field(name=name, value=value, inline=inline)
            
            embed.set_thumbnail(url=f"{target.avatar_url}")
            embed.set_author(name="YourBot", icon_url="https://cdn.discordapp.com/attachments/877796755234783273/879295069834850324/Avatar.png")
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
    async def changeprefix(self, ctx):
        loading_message = await ctx.send(embed=self.please_wait_emb)
        await loading_message.delete()
        await ctx.send(f'This feature will be available in the future! Make sure to type the info command to see more information')


    @commands.command(aliases=["server-icon"])
    async def iconserver(self, ctx):
        loading_message = await ctx.send(embed=self.please_wait_emb)

        try:
            em = discord.Embed(title=ctx.guild.name)
            em.set_footer(text=f"Requested by {ctx.author.name}")
            em.set_author(name="YourBot", icon_url="https://cdn.discordapp.com/attachments/877796755234783273/879295069834850324/Avatar.png")
            em.set_image(url=ctx.guild.icon_url)
            em.add_field(name="Server Name:", value=f"{ctx.guild.name}", inline=False)
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





















def setup(client: commands.Bot):
    client.add_cog(ModerationCommands(client))
