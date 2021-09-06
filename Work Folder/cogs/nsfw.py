import discord, os, asyncio, json, requests
from discord.ext import commands
from json import load as loadjson
from random import randint as randomint


class NSFWCommands(commands.Cog):
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
    async def lesbian(self, ctx):
        loading_message = await ctx.send(embed=self.please_wait_emb)

        try:
            r = requests.get("https://nekos.life/api/v2/img/les")
            res = r.json()
            em = discord.Embed(color=0xff0000)
            em.set_image(url=res['url'])
            em.set_footer(text=f"Requested by {ctx.author.name}")
            em.set_author(name="YourBot", icon_url="https://cdn.discordapp.com/attachments/877796755234783273/879295069834850324/Avatar.png")
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
    async def anal(self, ctx):
        loading_message = await ctx.send(embed=self.please_wait_emb)

        try:
            r = requests.get("https://nekos.life/api/v2/img/anal")
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
    async def feet(self, ctx):
        loading_message = await ctx.send(embed=self.please_wait_emb)
        
        try:
            r = requests.get("https://nekos.life/api/v2/img/feetg")
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
    async def hentai(self, ctx):
        loading_message = await ctx.send(embed=self.please_wait_emb)

        try:
            r = requests.get("https://nekos.life/api/v2/img/Random_hentai_gif")
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
    async def boobs(self, ctx):
        loading_message = await ctx.send(embed=self.please_wait_emb)

        try:
            r = requests.get("https://nekos.life/api/v2/img/boobs")
            res = r.json()
            em = discord.Embed(color=0xff0000)
            em.set_image(url=res['url'])
            em.set_footer(text=f"Requested by {ctx.author.name}")
            em.set_author(name="YourBot", icon_url="https://cdn.discordapp.com/attachments/877796755234783273/879295069834850324/Avatar.png")
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
    async def tits(self, ctx):
        loading_message = await ctx.send(embed=self.please_wait_emb)

        try:
            r = requests.get("https://nekos.life/api/v2/img/tits")
            res = r.json()
            em = discord.Embed(color=0xff0000)
            em.set_image(url=res['url'])
            em.set_footer(text=f"Requested by {ctx.author.name}")
            em.set_author(name="YourBot", icon_url="https://cdn.discordapp.com/attachments/877796755234783273/879295069834850324/Avatar.png")
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
    async def blowjob(self, ctx):
        loading_message = await ctx.send(embed=self.please_wait_emb)

        try:
            r = requests.get("https://nekos.life/api/v2/img/blowjob")
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
    async def lewd(self, ctx):
        loading_message = await ctx.send(embed=self.please_wait_emb)

        try:
            r = requests.get("https://nekos.life/api/v2/img/nsfw_neko_gif")
            res = r.json()
            em = discord.Embed(color=0xff0000)
            em.set_image(url=res['url'])
            em.set_footer(text=f"Requested by {ctx.author.name}")
            em.set_author(name="YourBot", icon_url="https://cdn.discordapp.com/attachments/877796755234783273/879295069834850324/Avatar.png")
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
    async def pervert(self, ctx):
        # Just a text
        await ctx.send("```" + """Can I get a booty pic with your panties on? And one without them on? Can I also get 3 different pics of your boobs in any position. Also can I get a pic of your pussy from the front and one where it’s spread open. Can I get a picture of you fingering your self? Can I get a pic of you doing a kissing face but with your boobs in it? Can I get a picture of your pussy and ass from behind in one shot? Can I also get a pic of your full front body in just a bra and panties? And can I get a pic of your ass when your pants are all the way up? Also can I get a pic of your boobs when you’re in the shower? Also can I get another pussy pic while you’re in the shower? For the rest of the pics can you just send whatever other sexy things you want? For the videos can I get a video of you twerking in really short shorts? And one of you fingering yourself? One of you actually cumming? Also can I get a video of you playing with your tits while not wearing a shirt? u be squirtin? or u on the cream team? what color the inside? your booty real wet? do it clap? do it fart? do it grip the meat? it’s tight? how many fingers u use? what it taste like? can i smell it? is it warm? it’s real juicy? do it drip? you be moaning?""" + "```")


    @commands.command(aliases=['dong', 'penis', 'pp', 'psize', 'dicksize', 'penissize'])
    async def dick(self, ctx, *, user: discord.User = None):
        loading_message = await ctx.send(embed=self.please_wait_emb)
        
        try:
            if user is None:
                user = ctx.author
                size = randomint(2, 20) # this is the random dick size!
                inch = size
                centim = inch * 2.54
                embed=discord.Embed(title="D!ck size", description=f"of {user}", color=0xff0000)
                embed.set_author(name="YourBot", icon_url="https://cdn.discordapp.com/attachments/877796755234783273/879295069834850324/Avatar.png")
                embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/877796755234783273/879744998805999656/download.png")
                embed.add_field(name="inches", value=f"{inch}", inline=False)
                embed.add_field(name="centimeters ", value=f"{centim}", inline=True)
                embed.set_footer(text=f"Requested by {ctx.author.name}")
                await loading_message.delete()
                await ctx.send(embed=embed)
            # if size < 6:
            #   await ctx.send(f"{user.mention} - Your dick is very small that a girl will not just feel theres something in, Just get a new life!")
            
            else:
                size = randomint(2, 20)
                inch = size
                centim = inch * 2.54
                embed=discord.Embed(title="D!ck size", description=f"of {user}", color=0xff0000)
                embed.set_author(name="YourBot", icon_url="https://cdn.discordapp.com/attachments/877796755234783273/879295069834850324/Avatar.png")
                embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/877796755234783273/879744998805999656/download.png")
                embed.add_field(name="inches", value=f"{inch}", inline=False)
                embed.add_field(name="centimeters ", value=f"{centim}", inline=True)
                embed.set_footer(text=f"Requested by {ctx.author.name}")
                await loading_message.delete()
                await ctx.send(embed=embed)
            # if size < 6:
            #   await ctx.send(f"{user.mention} - Your dick is very small that a girl will not just feel theres something in, Just get a new life!")

        except Exception as e:
            embed3=discord.Embed(title=":red_square: Error!", description="The command was unable to run successfully! ", color=0xff0000)
            embed3.set_author(name="YourBot", icon_url="https://cdn.discordapp.com/attachments/877796755234783273/879295069834850324/Avatar.png")
            embed3.set_thumbnail(url="https://cdn.discordapp.com/attachments/877796755234783273/879298565380386846/sign-red-error-icon-1.png")
            embed3.add_field(name="Error:", value=f"{e}", inline=False)
            embed3.set_footer(text=f"Requested by {ctx.author.name}")
            await loading_message.delete()
            await ctx.send(embed=embed3)

    @commands.command()
    async def daddy(self, ctx):
        loading_message = await ctx.send(embed=self.please_wait_emb)

        try:
            await ctx.send(f'{ctx.author.mention}a femboi caught in 4k requesting for dick pics!')
            r = requests.get("https://nekos.life/api/v2/img/Random_hentai_gif")
            res = r.json()

            em = discord.Embed(title="YOU LIL PERVERT!", color=0xff0000)
            em.set_author(name="YourBot", icon_url="https://cdn.discordapp.com/attachments/877796755234783273/879295069834850324/Avatar.png")
            em.set_footer(text=f"Requested by {ctx.author.name}")
            em.set_image(url=res['url'])

            await loading_message.delete()
            await ctx.send(embed=em)
            await ctx.send(f'{ctx.author.mention} my dear mate, go fap for this! you will never get dick pics!')

        except Exception as e:
            embed3=discord.Embed(title=":red_square: Error!", description="The command was unable to run successfully! ", color=0xff0000)
            embed3.set_author(name="YourBot", icon_url="https://cdn.discordapp.com/attachments/877796755234783273/879295069834850324/Avatar.png")
            embed3.set_thumbnail(url="https://cdn.discordapp.com/attachments/877796755234783273/879298565380386846/sign-red-error-icon-1.png")
            embed3.add_field(name="Error:", value=f"{e}", inline=False)
            embed3.set_footer(text=f"Requested by {ctx.author.name}")
            await loading_message.delete()
            await ctx.send(embed=embed3)


def setup(client: commands.Bot):
    client.add_cog(NSFWCommands(client))

