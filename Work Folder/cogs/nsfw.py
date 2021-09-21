import discord, json
from discord.ext import commands
from json import load as loadjson
from random import randint as randomint
from platform import system as systemtype
from os import system as systemruncmnd
try:
    import requests
except:
    if systemtype().lower().startswith('win'):
        systemruncmnd("pip install requests")
    else:
        systemruncmnd("pip3 install requests")
    import requests

import database.retrieve_embeds as getembed


class NSFW(commands.Cog, description="NSFW `images`/`gifs`/`videos`/`link`"):
    def __init__(self, client: commands.Bot):
        self.client = client

        # Loading config.json and its important content for this file
        self.botconfigdata = loadjson(open("config.json", "r"))
        self.bot_prefix = self.botconfigdata["msg-prefix"]
        self.bot_creator_id = self.botconfigdata["ownerid"]

        # This is the please-wait/Loading embed
        self.please_wait_emb = discord.Embed(title=getembed.PleaseWait.TITLE, description=f"``` {getembed.PleaseWait.DESCRIPTION} ```", color=getembed.PleaseWait.COLOR)
        self.please_wait_emb.set_author(name=getembed.PleaseWait.AUTHOR_NAME, icon_url=getembed.PleaseWait.AUTHOR_LINK)
        self.please_wait_emb.set_thumbnail(url=getembed.PleaseWait.THUMBNAIL)
        self.please_wait_emb.set_footer(text=getembed.PleaseWait.FOOTER)


    @commands.command(breif="Lesbain Images/GIFs",
    description="Send lesbian Images/GIFs!",
    help="Send lesbian Images/GIFs!")
    async def lesbian(self, ctx):
        loading_message = await ctx.send(embed=self.please_wait_emb)

        try:
            r = requests.get("https://nekos.life/api/v2/img/les")
            res = r.json()
            em = discord.Embed(color=getembed.Common.COLOR)
            em.set_image(url=res['url'])
            em.set_footer(text=f"Requested by {ctx.author.name}")
            em.set_author(name=getembed.Common.AUTHOR, icon_url=getembed.Common.AUTHOR_LINK)
            await loading_message.delete()
            await ctx.send(embed=em)

        except Exception as e:
            embed3=discord.Embed(getembed.ErrorEmbeds.TITLE, description=getembed.ErrorEmbeds.DESCRIPTION, color=getembed.ErrorEmbeds.COLOR)
            embed3.set_author(name=getembed.Common.AUTHOR, icon_url=getembed.Common.AUTHOR_LINK)
            embed3.set_thumbnail(url=getembed.ErrorEmbeds.THUMBNAIL)
            embed3.add_field(name="Error:", value=f"{e}", inline=False)
            embed3.set_footer(text=f"Requested by {ctx.author.name}")
            await loading_message.delete()
            await ctx.send(embed=embed3)


    @commands.command(breif="Anal Images/GIFs",
    description="Send anal Images/GIFs!",
    help="Send anal Images/GIFs!")
    async def anal(self, ctx):
        loading_message = await ctx.send(embed=self.please_wait_emb)

        try:
            r = requests.get("https://nekos.life/api/v2/img/anal")
            res = r.json()
            em = discord.Embed(color=getembed.Common.COLOR)
            em.set_footer(text=f"Requested by {ctx.author.name}")
            em.set_author(name=getembed.Common.AUTHOR, icon_url=getembed.Common.AUTHOR_LINK)
            em.set_image(url=res['url'])
            await loading_message.delete()
            await ctx.send(embed=em)
        
        except Exception as e:
            embed3=discord.Embed(getembed.ErrorEmbeds.TITLE, description=getembed.ErrorEmbeds.DESCRIPTION, color=getembed.ErrorEmbeds.COLOR)
            embed3.set_author(name=getembed.Common.AUTHOR, icon_url=getembed.Common.AUTHOR_LINK)
            embed3.set_thumbnail(url=getembed.ErrorEmbeds.THUMBNAIL)
            embed3.add_field(name="Error:", value=f"{e}", inline=False)
            embed3.set_footer(text=f"Requested by {ctx.author.name}")
            await loading_message.delete()
            await ctx.send(embed=embed3)

    @commands.command(breif="Feet Images/GIFs",
    description="Send feet Images/GIFs!",
    help="Send feet Images/GIFs!")
    async def feet(self, ctx):
        loading_message = await ctx.send(embed=self.please_wait_emb)
        
        try:
            r = requests.get("https://nekos.life/api/v2/img/feetg")
            res = r.json()
            em = discord.Embed(color=getembed.Common.COLOR)
            em.set_footer(text=f"Requested by {ctx.author.name}")
            em.set_author(name=getembed.Common.AUTHOR, icon_url=getembed.Common.AUTHOR_LINK)
            em.set_image(url=res['url'])
            await loading_message.delete()
            await ctx.send(embed=em)

        except Exception as e:
            embed3=discord.Embed(getembed.ErrorEmbeds.TITLE, description=getembed.ErrorEmbeds.DESCRIPTION, color=getembed.ErrorEmbeds.COLOR)
            embed3.set_author(name=getembed.Common.AUTHOR, icon_url=getembed.Common.AUTHOR_LINK)
            embed3.set_thumbnail(url=getembed.ErrorEmbeds.THUMBNAIL)
            embed3.add_field(name="Error:", value=f"{e}", inline=False)
            embed3.set_footer(text=f"Requested by {ctx.author.name}")
            await loading_message.delete()
            await ctx.send(embed=embed3)

    @commands.command(breif="Hentai Images/GIFs",
    description="Send hentai Images/GIFs!",
    help="Send hentai Images/GIFs!")
    async def hentai(self, ctx):
        loading_message = await ctx.send(embed=self.please_wait_emb)

        try:
            r = requests.get("https://nekos.life/api/v2/img/Random_hentai_gif")
            res = r.json()
            em = discord.Embed(color=getembed.Common.COLOR)
            em.set_footer(text=f"Requested by {ctx.author.name}")
            em.set_author(name=getembed.Common.AUTHOR, icon_url=getembed.Common.AUTHOR_LINK)
            em.set_image(url=res['url'])
            await loading_message.delete()
            await ctx.send(embed=em)
        
        except Exception as e:
            embed3=discord.Embed(getembed.ErrorEmbeds.TITLE, description=getembed.ErrorEmbeds.DESCRIPTION, color=getembed.ErrorEmbeds.COLOR)
            embed3.set_author(name=getembed.Common.AUTHOR, icon_url=getembed.Common.AUTHOR_LINK)
            embed3.set_thumbnail(url=getembed.ErrorEmbeds.THUMBNAIL)
            embed3.add_field(name="Error:", value=f"{e}", inline=False)
            embed3.set_footer(text=f"Requested by {ctx.author.name}")
            await loading_message.delete()
            await ctx.send(embed=embed3)


    @commands.command(breif="Boobs Images/GIFs",
    description="Send boobs Images/GIFs!",
    help="Send boobs Images/GIFs!")
    async def boobs(self, ctx):
        loading_message = await ctx.send(embed=self.please_wait_emb)

        try:
            r = requests.get("https://nekos.life/api/v2/img/boobs")
            res = r.json()
            em = discord.Embed(color=getembed.Common.COLOR)
            em.set_image(url=res['url'])
            em.set_footer(text=f"Requested by {ctx.author.name}")
            em.set_author(name=getembed.Common.AUTHOR, icon_url=getembed.Common.AUTHOR_LINK)
            await loading_message.delete()
            await ctx.send(embed=em)

        except Exception as e:
            embed3=discord.Embed(getembed.ErrorEmbeds.TITLE, description=getembed.ErrorEmbeds.DESCRIPTION, color=getembed.ErrorEmbeds.COLOR)
            embed3.set_author(name=getembed.Common.AUTHOR, icon_url=getembed.Common.AUTHOR_LINK)
            embed3.set_thumbnail(url=getembed.ErrorEmbeds.THUMBNAIL)
            embed3.add_field(name="Error:", value=f"{e}", inline=False)
            embed3.set_footer(text=f"Requested by {ctx.author.name}")
            await loading_message.delete()
            await ctx.send(embed=embed3)


    @commands.command(breif="Tits Images/GIFs",
    description="Send tits Images/GIFs!",
    help="Send tits Images/GIFs!")
    async def tits(self, ctx):
        loading_message = await ctx.send(embed=self.please_wait_emb)

        try:
            r = requests.get("https://nekos.life/api/v2/img/tits")
            res = r.json()
            em = discord.Embed(color=getembed.Common.COLOR)
            em.set_image(url=res['url'])
            em.set_footer(text=f"Requested by {ctx.author.name}")
            em.set_author(name=getembed.Common.AUTHOR, icon_url=getembed.Common.AUTHOR_LINK)
            await loading_message.delete()
            await ctx.send(embed=em)

        except Exception as e:
            embed3=discord.Embed(getembed.ErrorEmbeds.TITLE, description=getembed.ErrorEmbeds.DESCRIPTION, color=getembed.ErrorEmbeds.COLOR)
            embed3.set_author(name=getembed.Common.AUTHOR, icon_url=getembed.Common.AUTHOR_LINK)
            embed3.set_thumbnail(url=getembed.ErrorEmbeds.THUMBNAIL)
            embed3.add_field(name="Error:", value=f"{e}", inline=False)
            embed3.set_footer(text=f"Requested by {ctx.author.name}")
            await loading_message.delete()
            await ctx.send(embed=embed3)


    @commands.command(breif="Blowjob Images/GIFs",
    description="Send blowjob Images/GIFs!",
    help="Send blowjob Images/GIFs!")
    async def blowjob(self, ctx):
        loading_message = await ctx.send(embed=self.please_wait_emb)

        try:
            r = requests.get("https://nekos.life/api/v2/img/blowjob")
            res = r.json()
            em = discord.Embed(color=getembed.Common.COLOR)
            em.set_footer(text=f"Requested by {ctx.author.name}")
            em.set_author(name=getembed.Common.AUTHOR, icon_url=getembed.Common.AUTHOR_LINK)
            em.set_image(url=res['url'])
            await loading_message.delete()
            await ctx.send(embed=em)
        
        except Exception as e:
            embed3=discord.Embed(getembed.ErrorEmbeds.TITLE, description=getembed.ErrorEmbeds.DESCRIPTION, color=getembed.ErrorEmbeds.COLOR)
            embed3.set_author(name=getembed.Common.AUTHOR, icon_url=getembed.Common.AUTHOR_LINK)
            embed3.set_thumbnail(url=getembed.ErrorEmbeds.THUMBNAIL)
            embed3.add_field(name="Error:", value=f"{e}", inline=False)
            embed3.set_footer(text=f"Requested by {ctx.author.name}")
            await loading_message.delete()
            await ctx.send(embed=embed3)


    @commands.command(breif="Lewd Images/GIFs",
    description="Send lewd Images/GIFs!",
    help="Send lewd Images/GIFs!")
    async def lewd(self, ctx):
        loading_message = await ctx.send(embed=self.please_wait_emb)

        try:
            r = requests.get("https://nekos.life/api/v2/img/nsfw_neko_gif")
            res = r.json()
            em = discord.Embed(color=getembed.Common.COLOR)
            em.set_image(url=res['url'])
            em.set_footer(text=f"Requested by {ctx.author.name}")
            em.set_author(name=getembed.Common.AUTHOR, icon_url=getembed.Common.AUTHOR_LINK)
            await loading_message.delete()
            await ctx.send(embed=em)

        except Exception as e:
            embed3=discord.Embed(getembed.ErrorEmbeds.TITLE, description=getembed.ErrorEmbeds.DESCRIPTION, color=getembed.ErrorEmbeds.COLOR)
            embed3.set_author(name=getembed.Common.AUTHOR, icon_url=getembed.Common.AUTHOR_LINK)
            embed3.set_thumbnail(url=getembed.ErrorEmbeds.THUMBNAIL)
            embed3.add_field(name="Error:", value=f"{e}", inline=False)
            embed3.set_footer(text=f"Requested by {ctx.author.name}")
            await loading_message.delete()
            await ctx.send(embed=embed3)


    @commands.command(breif="a funny text - NSFW",
    description="Send an hilarious perverty text!",
    help="Send an hilarious perverty text!")
    async def pervert(self, ctx):
        # Just a text
        await ctx.send("```" + """Can I get a booty pic with your panties on? And one without them on? Can I also get 3 different pics of your boobs in any position. Also can I get a pic of your pussy from the front and one where it’s spread open. Can I get a picture of you fingering your self? Can I get a pic of you doing a kissing face but with your boobs in it? Can I get a picture of your pussy and ass from behind in one shot? Can I also get a pic of your full front body in just a bra and panties? And can I get a pic of your ass when your pants are all the way up? Also can I get a pic of your boobs when you’re in the shower? Also can I get another pussy pic while you’re in the shower? For the rest of the pics can you just send whatever other sexy things you want? For the videos can I get a video of you twerking in really short shorts? And one of you fingering yourself? One of you actually cumming? Also can I get a video of you playing with your tits while not wearing a shirt? u be squirtin? or u on the cream team? what color the inside? your booty real wet? do it clap? do it fart? do it grip the meat? it’s tight? how many fingers u use? what it taste like? can i smell it? is it warm? it’s real juicy? do it drip? you be moaning?""" + "```")


    @commands.command(aliases=['dong', 'penis', 'pp', 'psize', 'dicksize', 'penissize'],
    breif="Random dick size - NSFW",
    description="Send a random dick size between 2-inches to 19-inches. You can also mention `user` as `@user` by tagging him/her if its being used in a server.",
    help="Send a random dick size between 2-inches to 19-inches. You can also mention `user` as `@user` by tagging him/her if its being used in a server.")
    async def dick(self, ctx, *, user: discord.User = None):
        loading_message = await ctx.send(embed=self.please_wait_emb)
        
        try:
            if user is None:
                user = ctx.author
                size = randomint(2, 20) # this is the random dick size!
                inch = size
                centim = inch * 2.54
                embed=discord.Embed(title="D!ck size", description=f"of {user}", color=getembed.Common.COLOR)
                embed.set_author(name=getembed.Common.AUTHOR, icon_url=getembed.Common.AUTHOR_LINK)
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
                embed=discord.Embed(title="D!ck size", description=f"of {user}", color=getembed.Common.COLOR)
                embed.set_author(name=getembed.Common.AUTHOR, icon_url=getembed.Common.AUTHOR_LINK)
                embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/877796755234783273/879744998805999656/download.png")
                embed.add_field(name="inches", value=f"{inch}", inline=False)
                embed.add_field(name="centimeters ", value=f"{centim}", inline=True)
                embed.set_footer(text=f"Requested by {ctx.author.name}")
                await loading_message.delete()
                await ctx.send(embed=embed)
            # if size < 6:
            #   await ctx.send(f"{user.mention} - Your dick is very small that a girl will not just feel theres something in, Just get a new life!")

        except Exception as e:
            embed3=discord.Embed(getembed.ErrorEmbeds.TITLE, description=getembed.ErrorEmbeds.DESCRIPTION, color=getembed.ErrorEmbeds.COLOR)
            embed3.set_author(name=getembed.Common.AUTHOR, icon_url=getembed.Common.AUTHOR_LINK)
            embed3.set_thumbnail(url=getembed.ErrorEmbeds.THUMBNAIL)
            embed3.add_field(name="Error:", value=f"{e}", inline=False)
            embed3.set_footer(text=f"Requested by {ctx.author.name}")
            await loading_message.delete()
            await ctx.send(embed=embed3)


    @commands.command(breif="HEHE BOI..",
    description="buhahahahaha",
    help="buhahahahaha")
    async def daddy(self, ctx):
        loading_message = await ctx.send(embed=self.please_wait_emb)

        try:
            await ctx.send(f'{ctx.author.mention}a femboi caught in 4k requesting for dick pics!')
            r = requests.get("https://nekos.life/api/v2/img/Random_hentai_gif")
            res = r.json()

            em = discord.Embed(title="YOU LIL PERVERT!", color=getembed.Common.COLOR)
            em.set_author(name=getembed.Common.AUTHOR, icon_url=getembed.Common.AUTHOR_LINK)
            em.set_footer(text=f"Requested by {ctx.author.name}")
            em.set_image(url=res['url'])

            await loading_message.delete()
            await ctx.send(embed=em)
            await ctx.send(f'{ctx.author.mention} my dear mate, go fap for this! you will never get dick pics!')

        except Exception as e:
            embed3=discord.Embed(getembed.ErrorEmbeds.TITLE, description=getembed.ErrorEmbeds.DESCRIPTION, color=getembed.ErrorEmbeds.COLOR)
            embed3.set_author(name=getembed.Common.AUTHOR, icon_url=getembed.Common.AUTHOR_LINK)
            embed3.set_thumbnail(url=getembed.ErrorEmbeds.THUMBNAIL)
            embed3.add_field(name="Error:", value=f"{e}", inline=False)
            embed3.set_footer(text=f"Requested by {ctx.author.name}")
            await loading_message.delete()
            await ctx.send(embed=embed3)
    

    @commands.command(breif="Find one porn vieo",
    description="You can find a porn video link. `querywhatsearch` is what to search for and send the link. the result will be sent to the channel in the server or if used in dm, will work without any issue",
    help="You can find a porn video link. `querywhatsearch` is what to search for and send the link. the result will be sent to the channel in the server or if used in dm, will work without any issue")
    async def pornlink(self, ctx, *, querywhatsearch: str = "hardcore"):
        loading_message = await ctx.send(embed=self.please_wait_emb)

        try:
            r = requests.get(f"https://www.eporner.com/api/v2/video/search/?query={querywhatsearch}&per_page=60&thumbsize=big&order=top-weekly&format=json")
            resultjson = r.json()
            index_to_give = randomint(1, 60)
            em = discord.Embed(title="Pornographic Content", description="Here is a video for you!", color=getembed.Common.COLOR)
            em.set_author(name=getembed.Common.AUTHOR, icon_url=getembed.Common.AUTHOR_LINK)
            em.set_image(url=resultjson["videos"][index_to_give]["default_thumb"]["src"])
            # em.set_image(url=resultjson["videos"][0]["embed"])
            em.add_field(name="Title", value=f'{resultjson["videos"][index_to_give]["title"]}', inline=False)
            em.add_field(name="Keywords", value=f'{resultjson["videos"][index_to_give]["keywords"]}', inline=False)
            em.add_field(name="Views", value=f'{resultjson["videos"][index_to_give]["views"]}', inline=False)
            em.add_field(name="Rating", value=f'{resultjson["videos"][index_to_give]["rate"]}', inline=False)
            em.add_field(name="Uploaded on", value=f'{resultjson["videos"][index_to_give]["added"]}', inline=False)
            em.add_field(name="Length", value=f'{resultjson["videos"][index_to_give]["length_min"]}', inline=False)
            em.add_field(name="URL", value=f'{resultjson["videos"][index_to_give]["url"]}', inline=False)
            em.set_footer(text=f"Requested by {ctx.author.name}")
            await loading_message.delete()
            await ctx.send(embed=em)

        except Exception as e:
            embed3=discord.Embed(getembed.ErrorEmbeds.TITLE, description=getembed.ErrorEmbeds.DESCRIPTION, color=getembed.ErrorEmbeds.COLOR)
            embed3.set_author(name=getembed.Common.AUTHOR, icon_url=getembed.Common.AUTHOR_LINK)
            embed3.set_thumbnail(url=getembed.ErrorEmbeds.THUMBNAIL)
            embed3.add_field(name="Error:", value=f"{e}", inline=False)
            embed3.set_footer(text=f"Requested by {ctx.author.name}")
            await loading_message.delete()
            await ctx.send(embed=embed3)


    @commands.command(breif="Find one porn vieo",
    description="You can find a porn video link. `querywhatsearch` is what to search for and send the links. `howmany` is how many video links you want the bot to send you to DM. You can use this command anywhere, but the results will be sent to DM. Max value for `howmany` is 45. searching the same thing will send the same results in the given number of times.",
    help="You can find a porn video link. `querywhatsearch` is what to search for and send the links. `howmany` is how many video links you want the bot to send you to DM. You can use this command anywhere, but the results will be sent to DM. Max value for `howmany` is 45. searching the same thing will send the same results in the given number of times.")
    async def pornlinks(self, ctx, howmany: int = 5, *, querywhatsearch: str = "hardcore"):
        loading_message = await ctx.send(embed=self.please_wait_emb)

        try:
            r = requests.get(f"https://www.eporner.com/api/v2/video/search/?query={querywhatsearch}&per_page=40&thumbsize=big&order=top-weekly&format=json")
            resultjson = r.json()

            if int(howmany) <= 20: 
                emchannels = discord.Embed(title="Pornographic Content", description="```Please check your Direct Messages```",color=getembed.Common.COLOR)
                emchannels.set_author(name=getembed.Common.AUTHOR, icon_url=getembed.Common.AUTHOR_LINK)
                emchannels.set_footer(text=f"Requested by {ctx.author.name}")
                await loading_message.delete()
                await ctx.send(embed=emchannels)
                
                for index_to_give in range(int(howmany)):
                    em = discord.Embed(title="Pornographic Content", description="Here are some videos for you!",color=getembed.Common.COLOR)
                    em.set_author(name=getembed.Common.AUTHOR, icon_url=getembed.Common.AUTHOR_LINK)
                    em.set_image(url=resultjson["videos"][index_to_give]["default_thumb"]["src"])
                    # em.set_image(url=resultjson["videos"][0]["embed"])
                    em.add_field(name="Title", value=f'{resultjson["videos"][index_to_give]["title"]}', inline=False)
                    em.add_field(name="Keywords", value=f'{resultjson["videos"][index_to_give]["keywords"]}', inline=False)
                    em.add_field(name="Views", value=f'{resultjson["videos"][index_to_give]["views"]}', inline=False)
                    em.add_field(name="Rating", value=f'{resultjson["videos"][index_to_give]["rate"]}', inline=False)
                    em.add_field(name="Uploaded on", value=f'{resultjson["videos"][index_to_give]["added"]}', inline=False)
                    em.add_field(name="Length", value=f'{resultjson["videos"][index_to_give]["length_min"]}', inline=False)
                    em.add_field(name="URL", value=f'{resultjson["videos"][index_to_give]["url"]}', inline=False)
                    em.set_footer(text=f"Requested by {ctx.author.name}")
                    await ctx.author.send(embed=em)
            else:
                embed3=discord.Embed(getembed.ErrorEmbeds.TITLE, description=getembed.ErrorEmbeds.DESCRIPTION, color=getembed.ErrorEmbeds.COLOR)
                embed3.set_author(name=getembed.Common.AUTHOR, icon_url=getembed.Common.AUTHOR_LINK)
                embed3.set_thumbnail(url=getembed.ErrorEmbeds.THUMBNAIL)
                embed3.add_field(name="Error:", value=f"High value", inline=False)
                embed3.add_field(name="Possible Fix", value=f"Enter a number below 40", inline=False)
                embed3.set_footer(text=f"Requested by {ctx.author.name}")
                await loading_message.delete()
                await ctx.send(embed=embed3)

        except Exception as e:
            embed3=discord.Embed(getembed.ErrorEmbeds.TITLE, description=getembed.ErrorEmbeds.DESCRIPTION, color=getembed.ErrorEmbeds.COLOR)
            embed3.set_author(name=getembed.Common.AUTHOR, icon_url=getembed.Common.AUTHOR_LINK)
            embed3.set_thumbnail(url=getembed.ErrorEmbeds.THUMBNAIL)
            embed3.add_field(name="Error:", value=f"{e}", inline=False)
            embed3.set_footer(text=f"Requested by {ctx.author.name}")
            await loading_message.delete()
            await ctx.send(embed=embed3)





def setup(client: commands.Bot):
    client.add_cog(NSFW(client))
