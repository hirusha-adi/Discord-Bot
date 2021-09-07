import discord, requests, aiohttp
from discord.ext import commands
from json import load as loadjson
from json import loads as loadjsonstring


class OtherCommandsFun(commands.Cog):
    def __init__(self, client: commands.Bot):
        self.client = client

        # Loading config.json and its important content for this file
        self.botconfigdata = loadjson(open("config.json", "r"))
        self.bot_prefix = self.botconfigdata["msg-prefix"]
        self.bot_inv_link = self.botconfigdata["invite-link"]

        # This is the please-wait/Loading embed
        self.please_wait_emb = discord.Embed(title="Please Wait", description="``` Processing Your Request ```", color=0xff0000)
        self.please_wait_emb.set_author(name="YourBot")
        self.please_wait_emb.set_thumbnail(url="https://c.tenor.com/I6kN-6X7nhAAAAAj/loading-buffering.gif")
        self.please_wait_emb.set_footer(text="Bot created by ZeaCeR#5641")







    @commands.command()
    async def feed(self, ctx, user: discord.Member = None):
        loading_message = await ctx.send(embed=self.please_wait_emb)

        try:
            r = requests.get("https://nekos.life/api/v2/img/feed")
            res = r.json()

            if user == None:
                em = discord.Embed(description="User is not mentioned!", color=0xff0000)
                em.set_author(name="YourBot", icon_url="https://cdn.discordapp.com/attachments/877796755234783273/879295069834850324/Avatar.png")
                em.set_footer(text=f"Requested by {ctx.author.name}")
                em.set_image(url=res['url'])
                await loading_message.delete()
                await ctx.send(embed=em)
            
            else:
                em = discord.Embed(description=user.mention, color=0xff0000)
                em.set_author(name="YourBot", icon_url="https://cdn.discordapp.com/attachments/877796755234783273/879295069834850324/Avatar.png")
                em.set_footer(text=f"Requested by {ctx.author.name}")
                em.set_image(url=res['url'])
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
    async def tickle(self, ctx, user: discord.Member = None):
        loading_message = await ctx.send(embed=self.please_wait_emb)
        try:
            r = requests.get("https://nekos.life/api/v2/img/tickle")
            res = r.json()

            if user == None:
                em = discord.Embed(description="User is not mentioned!", color=0xff0000)
                em.set_author(name="YourBot", icon_url="https://cdn.discordapp.com/attachments/877796755234783273/879295069834850324/Avatar.png")
                em.set_footer(text=f"Requested by {ctx.author.name}")
                em.set_image(url=res['url'])
                await loading_message.delete()
                await ctx.send(embed=em)

            else:
                em = discord.Embed(description=user.mention, color=0xff0000)
                em.set_author(name="YourBot", icon_url="https://cdn.discordapp.com/attachments/877796755234783273/879295069834850324/Avatar.png")
                em.set_footer(text=f"Requested by {ctx.author.name}")
                em.set_image(url=res['url'])
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
    async def hit(self, ctx, user: discord.Member = None):
        loading_message = await ctx.send(embed=self.please_wait_emb)
        
        try:
            r = requests.get("https://nekos.life/api/v2/img/slap")
            res = r.json()

            if user == None:
                em = discord.Embed(description="User is not mentioned!", color=0xff0000)
                em.set_image(url=res['url'])
                em.set_author(name="YourBot", icon_url="https://cdn.discordapp.com/attachments/877796755234783273/879295069834850324/Avatar.png")
                em.set_footer(text=f"Requested by {ctx.author.name}")
                await loading_message.delete()
                await ctx.send(embed=em)
            else:
                em = discord.Embed(description=user.mention, color=0xff0000)
                em.set_author(name="YourBot", icon_url="https://cdn.discordapp.com/attachments/877796755234783273/879295069834850324/Avatar.png")
                em.set_footer(text=f"Requested by {ctx.author.name}")
                em.set_image(url=res['url'])
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
    async def hug(self, ctx, user: discord.Member):
        loading_message = await ctx.send(embed=self.please_wait_emb)

        try:
            r = requests.get("https://nekos.life/api/v2/img/hug")
            res = r.json()
            if user == None:
                em = discord.Embed(description="User is not mentioned!", color=0xff0000)
                em.set_author(name="YourBot", icon_url="https://cdn.discordapp.com/attachments/877796755234783273/879295069834850324/Avatar.png")
                em.set_footer(text=f"Requested by {ctx.author.name}")
                em.set_image(url=res['url'])
                await loading_message.delete()
                await ctx.send(embed=em)

            else:
                em = discord.Embed(description="user.mention", color=0xff0000)
                em.set_author(name="YourBot", icon_url="https://cdn.discordapp.com/attachments/877796755234783273/879295069834850324/Avatar.png")
                em.set_footer(text=f"Requested by {ctx.author.name}")
                em.set_image(url=res['url'])
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
    async def smug(self, ctx, user: discord.Member):
        loading_message = await ctx.send(embed=self.please_wait_emb)

        try:
            r = requests.get("https://nekos.life/api/v2/img/smug")
            res = r.json()

            if user == None:
                em = discord.Embed(description="User is not mentioned!", color=0xff0000)
                em.set_image(url=res['url'])
                em.set_author(name="YourBot", icon_url="https://cdn.discordapp.com/attachments/877796755234783273/879295069834850324/Avatar.png")
                em.set_footer(text=f"Requested by {ctx.author.name}")
                await loading_message.delete()
                await ctx.send(embed=em)

            else:
                em = discord.Embed(description=user.mention, color=0xff0000)
                em.set_image(url=res['url'])
                em.set_author(name="YourBot", icon_url="https://cdn.discordapp.com/attachments/877796755234783273/879295069834850324/Avatar.png")
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
    async def pat(self, ctx, user: discord.Member = None):
        loading_message = await ctx.send(embed=self.please_wait_emb)

        try:
            r = requests.get("https://nekos.life/api/v2/img/pat")
            res = r.json()

            if user == None:
                em = discord.Embed(description="User is not mentioned!", color=0xff0000)
                em.set_image(url=res['url'])
                em.set_author(name="YourBot", icon_url="https://cdn.discordapp.com/attachments/877796755234783273/879295069834850324/Avatar.png")
                em.set_footer(text=f"Requested by {ctx.author.name}")
                await loading_message.delete()
                await ctx.send(embed=em)

            else:
                em = discord.Embed(description=user.mention, color=0xff0000)
                em.set_image(url=res['url'])
                em.set_author(name="YourBot", icon_url="https://cdn.discordapp.com/attachments/877796755234783273/879295069834850324/Avatar.png")
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
    async def erofeet(self, ctx):
      loading_message = await ctx.send(embed=self.please_wait_emb)
    
      try:
        r = requests.get("https://nekos.life/api/v2/img/erofeet")
        res = r.json()
        em = discord.Embed(color=0xff0000)
        em.set_footer(text=f"Requested by {ctx.author.name}")
        em.set_author(name="YourBot", icon_url="https://cdn.discordapp.com/attachments/877796755234783273/879295069834850324/Avatar.png")
        em.set_image(url=res['url'])
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
    async def kiss(self, ctx, user: discord.Member = None):
        loading_message = await ctx.send(embed=self.please_wait_emb)

        try:
            r = requests.get("https://nekos.life/api/v2/img/kiss")
            res = r.json()

            if user == None:
                em = discord.Embed(description="User is not mentioned!", color=0xff0000)
                em.set_author(name="YourBot", icon_url="https://cdn.discordapp.com/attachments/877796755234783273/879295069834850324/Avatar.png")
                em.set_footer(text=f"Requested by {ctx.author.name}")
                em.set_image(url=res['url'])
                await loading_message.delete()
                await ctx.send(embed=em)
            
            else:
                em = discord.Embed(description=user.mention, color=0xff0000)
                em.set_author(name="YourBot", icon_url="https://cdn.discordapp.com/attachments/877796755234783273/879295069834850324/Avatar.png")
                em.set_footer(text=f"Requested by {ctx.author.name}")
                em.set_image(url=res['url'])
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
    
    @commands.command(aliases=["lol"])
    async def meme(self, ctx):
        loading_message = await ctx.send(embed=self.please_wait_emb)

        try:
            r = requests.get("https://some-random-api.ml/meme").json()

            embed = discord.Embed(color=0xff0000)
            embed.set_author(name="a Meme.", icon_url="https://freepngimg.com/thumb/internet_meme/3-2-troll-face-meme-png-thumb.png") 
            
            try:
                caption = str(r["caption"])
                embed.add_field(name="Just a random Meme", value=caption)
            except:
                pass
            
            embed.set_image(url=str(r["image"]))
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
    client.add_cog(OtherCommandsFun(client))


