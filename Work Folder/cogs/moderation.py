import discord, os, asyncio
from discord.ext import commands
from json import load as loadjson
from requests import get as reqget
from random import choices as rchoices
from string import ascii_letters as asciiletters
from string import digits as alldigits

class ModerationCommands(commands.Cog):
    def __init__(self, client: commands.Bot):
        self.client = client

        # Loading config.json and its important content for this file
        self.botconfigdata = loadjson(open("config.json", "r"))
        self.bot_prefix = self.botconfigdata["msg-prefix"]

        # This is the please-wait/Loading embed
        self.please_wait_emb = discord.Embed(title="Please Wait", description="``` Processing Your Request ```", color=0xff0000)
        self.please_wait_emb.set_author(name="YourBot")
        self.please_wait_emb.set_thumbnail(url="https://c.tenor.com/I6kN-6X7nhAAAAAj/loading-buffering.gif")
        self.please_wait_emb.set_footer(text="Bot created by ZeaCeR#5641")


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
            # Ban the user from the server with a reason
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
    async def clear(self, ctx, amount=5):
        amttdel = amount + 1
        await ctx.channel.purge(limit=amttdel)

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

                embed = discord.Embed(title="muted!", description=f"{member.mention} has been tempmuted ", colour=discord.Colour.light_gray())
                embed.add_field(name="reason:", value=reason, inline=False)
                embed.add_field(name="time left for the mute:", value=f"{time}{d}", inline=False)
                await ctx.send(embed=embed)

                if d == "s":
                    if time <= 1800:
                        await asyncio.sleep(time)
                    else:
                        embed3=discord.Embed(title=":red_square: Error!", description="The command was unable to run successfully! ", color=0xff0000)
                        embed3.set_author(name="YourBot", icon_url="https://cdn.discordapp.com/attachments/877796755234783273/879295069834850324/Avatar.png")
                        embed3.set_thumbnail(url="https://cdn.discordapp.com/attachments/877796755234783273/879298565380386846/sign-red-error-icon-1.png")
                        embed3.add_field(name="Error:", value=f"Please enter a value below 1800 seconds", inline=False)
                        embed3.set_footer(text=f"Requested by {ctx.author.name}")
                        await loading_message.delete()
                        await ctx.send(embed=embed3)
                        await member.remove_roles(role)

                if d == "m":
                    if time <= 300:
                        await asyncio.sleep(time*60)
                    else:
                        embed3=discord.Embed(title=":red_square: Error!", description="The command was unable to run successfully! ", color=0xff0000)
                        embed3.set_author(name="YourBot", icon_url="https://cdn.discordapp.com/attachments/877796755234783273/879295069834850324/Avatar.png")
                        embed3.set_thumbnail(url="https://cdn.discordapp.com/attachments/877796755234783273/879298565380386846/sign-red-error-icon-1.png")
                        embed3.add_field(name="Error:", value=f"Please enter a value below 300 minutes", inline=False)
                        embed3.set_footer(text=f"Requested by {ctx.author.name}")
                        await loading_message.delete()
                        await ctx.send(embed=embed3)
                        await member.remove_roles(role)

                if d == "h":
                    if time <= 5:
                        await asyncio.sleep(time*60*60)
                    else:
                        embed3=discord.Embed(title=":red_square: Error!", description="The command was unable to run successfully! ", color=0xff0000)
                        embed3.set_author(name="YourBot", icon_url="https://cdn.discordapp.com/attachments/877796755234783273/879295069834850324/Avatar.png")
                        embed3.set_thumbnail(url="https://cdn.discordapp.com/attachments/877796755234783273/879298565380386846/sign-red-error-icon-1.png")
                        embed3.add_field(name="Error:", value=f"Please enter a value below 6 hours", inline=False)
                        embed3.set_footer(text=f"Requested by {ctx.author.name}")
                        await loading_message.delete()
                        await ctx.send(embed=embed3)
                        await member.remove_roles(role)




                embed = discord.Embed(title="unmute (temp) ", description=f"unmuted -{member.mention} ", colour=discord.Colour.light_gray())
                await ctx.send(embed=embed)

                return





def setup(client: commands.Bot):
    client.add_cog(ModerationCommands(client))
