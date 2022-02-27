import discord
from discord.ext import commands
from os import remove as osremovef
import yourbot.database.embeds.retrieve_embeds as getembed
import yourbot.database.main.retrieve_base as getbase
import yourbot.others.installerm as ybinstaller

try:
    import requests
except:
    ybinstaller.pip_install("requests")
    import requests

try:
    import urllib
except:
    ybinstaller.pip_install("requests")
    import urllib


class Images(commands.Cog, description="Send fun images | Add effects/overlays to images"):
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

    @commands.command(breif="send a Image/GIF",
                      description="send a Image/GIF",
                      help="send a Image/GIF")
    async def feed(self, ctx, user: discord.Member = None):
        loading_message = await ctx.send(embed=self.please_wait_emb)

        try:
            r = requests.get("https://nekos.life/api/v2/img/feed")
            res = r.json()

            if user == None:
                em = discord.Embed(
                    description="User is not mentioned!", color=getembed.Common.COLOR)
                em.set_author(name=getembed.Common.AUTHOR,
                              icon_url=getembed.Common.AUTHOR_LINK)
                em.set_footer(text=f"Requested by {ctx.author.name}")
                em.set_image(url=res['url'])
                await loading_message.delete()
                await ctx.send(embed=em)

            else:
                em = discord.Embed(description=user.mention,
                                   color=getembed.Common.COLOR)
                em.set_author(name=getembed.Common.AUTHOR,
                              icon_url=getembed.Common.AUTHOR_LINK)
                em.set_footer(text=f"Requested by {ctx.author.name}")
                em.set_image(url=res['url'])
                await loading_message.delete()
                await ctx.send(embed=em)

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

    @commands.command(breif="send a Image/GIF",
                      description="send a Image/GIF",
                      help="send a Image/GIF")
    async def tickle(self, ctx, user: discord.Member = None):
        loading_message = await ctx.send(embed=self.please_wait_emb)
        try:
            r = requests.get("https://nekos.life/api/v2/img/tickle")
            res = r.json()

            if user == None:
                em = discord.Embed(
                    description="User is not mentioned!", color=getembed.Common.COLOR)
                em.set_author(name=getembed.Common.AUTHOR,
                              icon_url=getembed.Common.AUTHOR_LINK)
                em.set_footer(text=f"Requested by {ctx.author.name}")
                em.set_image(url=res['url'])
                await loading_message.delete()
                await ctx.send(embed=em)

            else:
                em = discord.Embed(description=user.mention,
                                   color=getembed.Common.COLOR)
                em.set_author(name=getembed.Common.AUTHOR,
                              icon_url=getembed.Common.AUTHOR_LINK)
                em.set_footer(text=f"Requested by {ctx.author.name}")
                em.set_image(url=res['url'])
                await loading_message.delete()
                await ctx.send(embed=em)

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

    @commands.command(breif="send a Image/GIF",
                      description="send a Image/GIF",
                      help="send a Image/GIF")
    async def hit(self, ctx, user: discord.Member = None):
        loading_message = await ctx.send(embed=self.please_wait_emb)

        try:
            r = requests.get("https://nekos.life/api/v2/img/slap")
            res = r.json()

            if user == None:
                em = discord.Embed(
                    description="User is not mentioned!", color=getembed.Common.COLOR)
                em.set_image(url=res['url'])
                em.set_author(name=getembed.Common.AUTHOR,
                              icon_url=getembed.Common.AUTHOR_LINK)
                em.set_footer(text=f"Requested by {ctx.author.name}")
                await loading_message.delete()
                await ctx.send(embed=em)
            else:
                em = discord.Embed(description=user.mention,
                                   color=getembed.Common.COLOR)
                em.set_author(name=getembed.Common.AUTHOR,
                              icon_url=getembed.Common.AUTHOR_LINK)
                em.set_footer(text=f"Requested by {ctx.author.name}")
                em.set_image(url=res['url'])
                await loading_message.delete()
                await ctx.send(embed=em)

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

    @commands.command(breif="send a Image/GIF",
                      description="send a Image/GIF",
                      help="send a Image/GIF")
    async def hug(self, ctx, user: discord.Member):
        loading_message = await ctx.send(embed=self.please_wait_emb)

        try:
            r = requests.get("https://nekos.life/api/v2/img/hug")
            res = r.json()
            if user == None:
                em = discord.Embed(
                    description="User is not mentioned!", color=getembed.Common.COLOR)
                em.set_author(name=getembed.Common.AUTHOR,
                              icon_url=getembed.Common.AUTHOR_LINK)
                em.set_footer(text=f"Requested by {ctx.author.name}")
                em.set_image(url=res['url'])
                await loading_message.delete()
                await ctx.send(embed=em)

            else:
                em = discord.Embed(description="user.mention",
                                   color=getembed.Common.COLOR)
                em.set_author(name=getembed.Common.AUTHOR,
                              icon_url=getembed.Common.AUTHOR_LINK)
                em.set_footer(text=f"Requested by {ctx.author.name}")
                em.set_image(url=res['url'])
                await loading_message.delete()
                await ctx.send(embed=em)

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

    @commands.command(breif="send a Image/GIF",
                      description="send a Image/GIF",
                      help="send a Image/GIF")
    async def smug(self, ctx, user: discord.Member):
        loading_message = await ctx.send(embed=self.please_wait_emb)

        try:
            r = requests.get("https://nekos.life/api/v2/img/smug")
            res = r.json()

            if user == None:
                em = discord.Embed(
                    description="User is not mentioned!", color=getembed.Common.COLOR)
                em.set_image(url=res['url'])
                em.set_author(name=getembed.Common.AUTHOR,
                              icon_url=getembed.Common.AUTHOR_LINK)
                em.set_footer(text=f"Requested by {ctx.author.name}")
                await loading_message.delete()
                await ctx.send(embed=em)

            else:
                em = discord.Embed(description=user.mention,
                                   color=getembed.Common.COLOR)
                em.set_image(url=res['url'])
                em.set_author(name=getembed.Common.AUTHOR,
                              icon_url=getembed.Common.AUTHOR_LINK)
                em.set_footer(text=f"Requested by {ctx.author.name}")
                await loading_message.delete()
                await ctx.send(embed=em)

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

    @commands.command(breif="send a Image/GIF",
                      description="send a Image/GIF",
                      help="send a Image/GIF")
    async def pat(self, ctx, user: discord.Member = None):
        loading_message = await ctx.send(embed=self.please_wait_emb)

        try:
            r = requests.get("https://nekos.life/api/v2/img/pat")
            res = r.json()

            if user == None:
                em = discord.Embed(
                    description="User is not mentioned!", color=getembed.Common.COLOR)
                em.set_image(url=res['url'])
                em.set_author(name=getembed.Common.AUTHOR,
                              icon_url=getembed.Common.AUTHOR_LINK)
                em.set_footer(text=f"Requested by {ctx.author.name}")
                await loading_message.delete()
                await ctx.send(embed=em)

            else:
                em = discord.Embed(description=user.mention,
                                   color=getembed.Common.COLOR)
                em.set_image(url=res['url'])
                em.set_author(name=getembed.Common.AUTHOR,
                              icon_url=getembed.Common.AUTHOR_LINK)
                em.set_footer(text=f"Requested by {ctx.author.name}")
                await loading_message.delete()
                await ctx.send(embed=em)

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

    @commands.command(breif="send a Image/GIF",
                      description="send a Image/GIF",
                      help="send a Image/GIF")
    async def erofeet(self, ctx):
        loading_message = await ctx.send(embed=self.please_wait_emb)

        try:
            r = requests.get("https://nekos.life/api/v2/img/erofeet")
            res = r.json()
            em = discord.Embed(color=getembed.Common.COLOR)
            em.set_footer(text=f"Requested by {ctx.author.name}")
            em.set_author(name=getembed.Common.AUTHOR,
                          icon_url=getembed.Common.AUTHOR_LINK)
            em.set_image(url=res['url'])
            await loading_message.delete()
            await ctx.send(embed=em)

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

    @commands.command(breif="send a Image/GIF",
                      description="send a Image/GIF",
                      help="send a Image/GIF")
    async def kiss(self, ctx, user: discord.Member = None):
        loading_message = await ctx.send(embed=self.please_wait_emb)

        try:
            r = requests.get("https://nekos.life/api/v2/img/kiss")
            res = r.json()

            if user == None:
                em = discord.Embed(
                    description="User is not mentioned!", color=getembed.Common.COLOR)
                em.set_author(name=getembed.Common.AUTHOR,
                              icon_url=getembed.Common.AUTHOR_LINK)
                em.set_footer(text=f"Requested by {ctx.author.name}")
                em.set_image(url=res['url'])
                await loading_message.delete()
                await ctx.send(embed=em)

            else:
                em = discord.Embed(description=user.mention,
                                   color=getembed.Common.COLOR)
                em.set_author(name=getembed.Common.AUTHOR,
                              icon_url=getembed.Common.AUTHOR_LINK)
                em.set_footer(text=f"Requested by {ctx.author.name}")
                em.set_image(url=res['url'])
                await loading_message.delete()
                await ctx.send(embed=em)

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

    @commands.command(aliases=["lol"],
                      breif="a good meme",
                      description="Send a meme to laugh at! ",
                      help="Send a meme to laugh at! ")
    async def meme(self, ctx):
        loading_message = await ctx.send(embed=self.please_wait_emb)

        try:
            r = requests.get("https://some-random-api.ml/meme").json()

            embed = discord.Embed(color=getembed.Common.COLOR)
            embed.set_author(
                name="a Meme.", icon_url="https://freepngimg.com/thumb/internet_meme/3-2-troll-face-meme-png-thumb.png")

            try:
                caption = str(r["caption"])
                embed.add_field(name="Just a random Meme", value=caption)
            except:
                pass

            embed.set_image(url=str(r["image"]))
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

    @commands.command(aliases=["a-pikachu", "pikachuu"],
                      breif="Pikachu images",
                      description="Send a random image of pikachu",
                      help="Send a random image of pikachu")
    async def pikachu(self, ctx):
        loading_message = await ctx.send(embed=self.please_wait_emb)

        try:
            r = requests.get('https://some-random-api.ml/img/pikachu')
            c = r.json()
            fact = c["link"]
            em = discord.Embed(title='a Pickachu', color=getembed.Common.COLOR)
            em.set_author(name=getembed.Common.AUTHOR,
                          icon_url=getembed.Common.AUTHOR_LINK)
            em.set_image(url=fact)
            em.set_footer(text=f"Requested by {ctx.author.name}")
            await loading_message.delete()
            await ctx.send(embed=em)

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

    @commands.command(aliases=["a-wink", "winks"],
                      breif="send a Image/GIF",
                      description="send a Image/GIF",
                      help="send a Image/GIF")
    async def wink(self, ctx):
        loading_message = await ctx.send(embed=self.please_wait_emb)

        try:
            r = requests.get('https://some-random-api.ml/animu/wink')
            c = r.json()
            fact = c["link"]
            em = discord.Embed(title='a wink', color=getembed.Common.COLOR)
            em.set_author(name=getembed.Common.AUTHOR,
                          icon_url=getembed.Common.AUTHOR_LINK)
            em.set_image(url=fact)
            em.set_footer(text=f"Requested by {ctx.author.name}")
            await loading_message.delete()
            await ctx.send(embed=em)

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

    @commands.command(aliases=["gay-colors", "gay-colours"],
                      breif="Add effects/overlays to a image",
                      description="Add effects/overlays to any image given! the link of the image should be direct!",
                      help="Add effects/overlays to any image given! the link of the image should be direct!")
    async def gay(self, ctx, *, messagelink: str):
        loading_message = await ctx.send(embed=self.please_wait_emb)

        try:
            weblink = 'https://some-random-api.ml/canvas/gay?avatar=' + messagelink
            r = requests.get(weblink)
            em = discord.Embed(title='Gay Picture',
                               color=getembed.Common.COLOR)
            em.set_author(name=getembed.Common.AUTHOR,
                          icon_url=getembed.Common.AUTHOR_LINK)
            em.set_image(url=weblink)
            em.set_footer(text=f"Requested by {ctx.author.name}")
            await loading_message.delete()
            await ctx.send(embed=em)

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

    @commands.command(aliases=["glass-colors", "glass-colours", "glassy-colors", "glassy-colours"],
                      breif="Add effects/overlays to a image",
                      description="Add effects/overlays to any image given! the link of the image should be direct!",
                      help="Add effects/overlays to any image given! the link of the image should be direct!")
    async def glass(self, ctx, *, messagelink):
        loading_message = await ctx.send(embed=self.please_wait_emb)

        try:
            weblink = 'https://some-random-api.ml/canvas/glass/?avatar=' + messagelink
            em = discord.Embed(title='Glassy Picture',
                               color=getembed.Common.COLOR)
            em.set_author(name=getembed.Common.AUTHOR,
                          icon_url=getembed.Common.AUTHOR_LINK)
            em.set_image(url=weblink)
            em.set_footer(text=f"Requested by {ctx.author.name}")
            await loading_message.delete()
            await ctx.send(embed=em)

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

    @commands.command(aliases=["wasted-colors", "wasted-colours", "wasted-image", "wasted-img"],
                      breif="Add effects/overlays to a image",
                      description="Add effects/overlays to any image given! the link of the image should be direct!",
                      help="Add effects/overlays to any image given! the link of the image should be direct!")
    async def wasted(self, ctx, *, messagelink, color=getembed.Common.COLOR):
        loading_message = await ctx.send(embed=self.please_wait_emb)

        try:
            weblink = 'https://some-random-api.ml/canvas/glass/?avatar=' + messagelink
            em = discord.Embed(title='a Wasted Picture',
                               color=getembed.Common.COLOR)
            em.set_author(name=getembed.Common.AUTHOR,
                          icon_url=getembed.Common.AUTHOR_LINK)
            em.set_image(url=weblink)
            em.set_footer(text=f"Requested by {ctx.author.name}")
            await loading_message.delete()
            await ctx.send(embed=em)

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

    @commands.command(
        breif="Add effects/overlays to a image",
        description="Add effects/overlays to any image given! the link of the image should be direct!",
        help="Add effects/overlays to any image given! the link of the image should be direct!")
    async def triggered(self, ctx, *, messagelink):
        loading_message = await ctx.send(embed=self.please_wait_emb)

        try:
            weblink = 'https://some-random-api.ml/canvas/triggered?avatar=' + messagelink
            em = discord.Embed(title='a TRIGGERED Picture',
                               color=getembed.Common.COLOR)
            em.set_author(name=getembed.Common.AUTHOR,
                          icon_url=getembed.Common.AUTHOR_LINK)
            em.set_image(url=weblink)
            em.set_footer(text=f"Requested by {ctx.author.name}")
            await loading_message.delete()
            await ctx.send(embed=em)

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

    @commands.command(aliases=["bandw", "black-and-white"],
                      breif="Add effects/overlays to a image",
                      description="Add effects/overlays to any image given! the link of the image should be direct!",
                      help="Add effects/overlays to any image given! the link of the image should be direct!")
    async def grayscale(self, ctx, *, messagelink):
        loading_message = await ctx.send(embed=self.please_wait_emb)

        try:
            weblink = 'https://some-random-api.ml/canvas/greyscale?avatar=' + messagelink
            em = discord.Embed(title='a Black and White Picture',
                               color=getembed.Common.COLOR)
            em.set_author(name=getembed.Common.AUTHOR,
                          icon_url=getembed.Common.AUTHOR_LINK)
            em.set_image(url=weblink)
            em.set_footer(text=f"Requested by {ctx.author.name}")
            await loading_message.delete()
            await ctx.send(embed=em)

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

    @commands.command(aliases=["invert-img", "invert-colors", "invert-image"],
                      breif="Invert colors",
                      description="Invert the colors of any given image! the link of the image should be direct!",
                      help="Invert the colors of any given image! the link of the image should be direct!")
    async def invert(self, ctx, *, messagelink):
        loading_message = await ctx.send(embed=self.please_wait_emb)

        try:
            weblink = 'https://some-random-api.ml/canvas/invert?avatar=' + messagelink
            em = discord.Embed(title='a Inverted Picture',
                               color=getembed.Common.COLOR)
            em.set_author(name=getembed.Common.AUTHOR,
                          icon_url=getembed.Common.AUTHOR_LINK)
            em.set_image(url=weblink)
            em.set_footer(text=f"Requested by {ctx.author.name}")
            await loading_message.delete()
            await ctx.send(embed=em)

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

    @commands.command(aliases=["bright-img", "bright-colors", "bright-image", "brightimg"],
                      breif="Add effects/overlays to a image",
                      description="Add effects/overlays to any image given! the link of the image should be direct!",
                      help="Add effects/overlays to any image given! the link of the image should be direct!")
    async def brighten(self, ctx, *, messagelink):
        loading_message = await ctx.send(embed=self.please_wait_emb)

        try:
            weblink = 'https://some-random-api.ml/canvas/brightness?avatar=' + messagelink
            em = discord.Embed(title='a Brightened Picture',
                               color=getembed.Common.COLOR)
            em.set_author(name=getembed.Common.AUTHOR,
                          icon_url=getembed.Common.AUTHOR_LINK)
            em.set_image(url=weblink)
            em.set_footer(text=f"Requested by {ctx.author.name}")
            await loading_message.delete()
            await ctx.send(embed=em)

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

    @commands.command(aliases=["threshold-img", "threshold-colors", "threshold-image", "thresh"],
                      breif="Add effects/overlays to a image",
                      description="Add effects/overlays to any image given! the link of the image should be direct!",
                      help="Add effects/overlays to any image given! the link of the image should be direct!")
    async def threshold(self, ctx, *, messagelink):
        loading_message = await ctx.send(embed=self.please_wait_emb)

        try:
            weblink = 'https://some-random-api.ml/canvas/threshold?avatar=' + messagelink
            em = discord.Embed(title='a Threshold Picture',
                               color=getembed.Common.COLOR)
            em.set_author(name=getembed.Common.AUTHOR,
                          icon_url=getembed.Common.AUTHOR_LINK)
            em.set_image(url=weblink)
            em.set_footer(text=f"Requested by {ctx.author.name}")
            await loading_message.delete()
            await ctx.send(embed=em)

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

    @commands.command(aliases=["sepia-image", "sepia-color"],
                      breif="Add effects/overlays to a image",
                      description="Add effects/overlays to any image given! the link of the image should be direct!",
                      help="Add effects/overlays to any image given! the link of the image should be direct!")
    async def sepia(self, ctx, *, messagelink):
        loading_message = await ctx.send(embed=self.please_wait_emb)

        try:
            weblink = 'https://some-random-api.ml/canvas/greyscale?avatar=' + messagelink
            em = discord.Embed(title='a Sepia Picture',
                               color=getembed.Common.COLOR)
            em.set_author(name=getembed.Common.AUTHOR,
                          icon_url=getembed.Common.AUTHOR_LINK)
            em.set_image(url=weblink)
            em.set_footer(text=f"Requested by {ctx.author.name}")
            await loading_message.delete()
            await ctx.send(embed=em)

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

    @commands.command(aliases=["red-image", "red-color"],
                      breif="Add effects/overlays to a image",
                      description="Add effects/overlays to any image given! the link of the image should be direct!",
                      help="Add effects/overlays to any image given! the link of the image should be direct!")
    async def red(self, ctx, *, messagelink):
        loading_message = await ctx.send(embed=self.please_wait_emb)

        try:
            weblink = 'https://some-random-api.ml/canvas/red?avatar=' + messagelink
            em = discord.Embed(title='a Red Picture',
                               color=getembed.Common.COLOR)
            em.set_author(name=getembed.Common.AUTHOR,
                          icon_url=getembed.Common.AUTHOR_LINK)
            em.set_image(url=weblink)
            em.set_footer(text=f"Requested by {ctx.author.name}")
            await loading_message.delete()
            await ctx.send(embed=em)

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

    @commands.command(aliases=["green-image", "green-color"],
                      breif="Add effects/overlays to a image",
                      description="Add effects/overlays to any image given! the link of the image should be direct!",
                      help="Add effects/overlays to any image given! the link of the image should be direct!")
    async def green(self, ctx, *, messagelink):
        loading_message = await ctx.send(embed=self.please_wait_emb)

        try:
            weblink = 'https://some-random-api.ml/canvas/green?avatar=' + messagelink
            em = discord.Embed(title='a Green Picture',
                               color=getembed.Common.COLOR)
            em.set_author(name=getembed.Common.AUTHOR,
                          icon_url=getembed.Common.AUTHOR_LINK)
            em.set_image(url=weblink)
            em.set_footer(text=f"Requested by {ctx.author.name}")
            await loading_message.delete()
            await ctx.send(embed=em)

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

    @commands.command(aliases=["blue-image", "blue-color"],
                      breif="Add effects/overlays to a image",
                      description="Add effects/overlays to any image given! the link of the image should be direct!",
                      help="Add effects/overlays to any image given! the link of the image should be direct!")
    async def blue(self, ctx, *, messagelink):
        loading_message = await ctx.send(embed=self.please_wait_emb)

        try:
            weblink = 'https://some-random-api.ml/canvas/blue?avatar=' + messagelink
            em = discord.Embed(title='a Blue Picture',
                               color=getembed.Common.COLOR)
            em.set_author(name=getembed.Common.AUTHOR,
                          icon_url=getembed.Common.AUTHOR_LINK)
            em.set_image(url=weblink)
            em.set_footer(text=f"Requested by {ctx.author.name}")
            await loading_message.delete()
            await ctx.send(embed=em)
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

    @commands.command(aliases=["tint-image", "tint-color"],
                      breif="Add effects/overlays to a image",
                      description="Add color overlays to any image given! the link of the image should be direct! the `colorTotint` should be a hex code",
                      help="Add color overlays to any image given! the link of the image should be direct! the `colorTotint` should be a hex code")
    async def tint(self, ctx, colorTotint, *, messagelink):
        loading_message = await ctx.send(embed=self.please_wait_emb)

        try:
            weblink = 'https://some-random-api.ml/canvas/color?avatar=' + \
                messagelink + "&color=%" + colorTotint
            em = discord.Embed(title='a Tinted Picture',
                               color=getembed.Common.COLOR)
            embed_text = "Picture tinted in " + colorTotint
            em.set_author(name=getembed.Common.AUTHOR,
                          icon_url=getembed.Common.AUTHOR_LINK)
            em.set_image(url=weblink)
            em.set_footer(text=f"Requested by {ctx.author.name}")
            await loading_message.delete()
            await ctx.send(embed=em)

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

    @commands.command(aliases=["pixelate-image"],
                      breif="Add effects/overlays to a image",
                      description="Add effects/overlays to any image given! the link of the image should be direct!",
                      help="Add effects/overlays to any image given! the link of the image should be direct!")
    async def pixelate(self, ctx, *, messagelink):
        loading_message = await ctx.send(embed=self.please_wait_emb)

        try:
            weblink = 'https://some-random-api.ml/canvas/pixelate' + messagelink
            em = discord.Embed(title='a Blue Picture',
                               color=getembed.Common.COLOR)
            em.set_author(name=getembed.Common.AUTHOR,
                          icon_url=getembed.Common.AUTHOR_LINK)
            em.set_image(url=weblink)
            em.set_footer(text=f"Requested by {ctx.author.name}")
            await loading_message.delete()
            await ctx.send(embed=em)

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

    @commands.command(aliases=["ytc", "youtubecomment", "youtube-comment", "yt-comment", "you-tube-comment"],
                      breif="Create a fake YouTube comment",
                      description="Create a real looking image of a youtube comment! in `commentmsg`, please use `_` instead of a space! the pofile picture links is optional, if you give a profile picture link, please give a direct link for it to create the image successfully! ",
                      help="Create a real looking image of a youtube command! in `commentmsg`, please use `_` instead of a space! the pofile picture links is optional, if you give a profile picture link, please give a direct link for it to create the image successfully! ")
    async def ytcomment(self, ctx, usernameofu="ZeaCeR5641", commentmsg="This_is_a_test", profilepictureLink="https://static.wikia.nocookie.net/ba0628fe-3bc1-42c3-9c0c-aa91ba24f03c/scale-to-width/370", mode="dark"):
        loading_message = await ctx.send(embed=self.please_wait_emb)

        try:
            weblink = "https://some-random-api.ml/canvas/youtube-comment?username=" + usernameofu.replace(
                "_", "%20") + "&comment=" + commentmsg.replace("_", "%20") + "&avatar=" + profilepictureLink + "&dark=true"
            # em = discord.Embed(title='a picture of a YouTube Comment')
            # em.set_author(name='Fake YouTube Comment')
            # em.set_image(url=weblink)
            # await ctx.send(embed=em)
            await loading_message.delete()
            await ctx.send(weblink)

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

    @commands.command(aliases=["twc"],
                      breif="Create a fake tweet",
                      description="Create a real looking image of a tweet! please give a direct link of the profile picture' to create the image successfully! you can enter the comment in any way you like",
                      help="Create a real looking image of a tweet! please give a direct link of the profile picture' to create the image successfully! you can enter the comment in any way you like")
    async def twittercomment(self, ctx, usernametw="User1", displaynametw="user", linkpfp="https://media.discordapp.net/attachments/877796755234783273/879295069834850324/Avatar.png?width=300&height=300", *, commenttw="The comment comes here"):
        loading_message = await ctx.send(embed=self.please_wait_emb)

        try:
            if linkpfp.lower() == "no":
                linkpfp = "https://media.discordapp.net/attachments/877796755234783273/879295069834850324/Avatar.png?width=300&height=300"
                urrl = f"https://some-random-api.ml/canvas/tweet?avatar={linkpfp}&username={usernametw}&displayname={displaynametw}&comment={urllib.parse.quote_plus(commenttw)}"
                await loading_message.delete()
                ctx.send(urrl)

            else:
                urrl = f"https://some-random-api.ml/canvas/tweet?avatar={linkpfp}&username={usernametw}&displayname={displaynametw}&comment={urllib.parse.quote_plus(commenttw)}"
                await loading_message.delete()
                ctx.send(urrl)

        except Exception as e:
            embed3 = discord.Embed(
                title=":red_square: Error!", description="The command was unable to run successfully! ", color=getembed.Common.COLOR)
            embed3.set_author(name=getembed.Common.AUTHOR,
                              icon_url=getembed.Common.AUTHOR_LINK)
            embed3.set_thumbnail(
                url="https://media.discordapp.net/attachments/877796755234783273/880745781966037032/new-scrabble-words-2018-beatdown-5657-57124c9f228c0258d65053fe7d3891491x.jpg")
            embed3.add_field(name="Error:", value=f"{e}", inline=False)
            embed3.add_field(
                name="Possible Fix:", value=f"You must have only one '||' part for the whole message for the bot to divide the string", inline=False)
            embed3.set_footer(text=f"Requested by {ctx.author.name}")
            await loading_message.delete()
            await ctx.send(embed=embed3)

    @commands.command(
        breif="A cute monstor image",
        description="This will send a low resolution picture of a monstor. the image is in .png format",
        help="This will send a low resolution picture of a monstor. the image is in .png format")
    async def monstor(self, ctx):
        loading_message = await ctx.send(embed=self.please_wait_emb)

        try:
            websitelink = r'https://app.pixelencounter.com/api/basic/svgmonsters/image/png?primaryColor=%23FC6400&size=100'
            r = requests.get(websitelink)
            c = r.content
            file = open("monstorimg.png", 'wb')
            file.write(c)
            file.close()
            with open("monstorimg.png", 'rb') as f:
                picture = discord.File(f)
                await loading_message.delete()
                await ctx.send(file=picture)
            osremovef("monstorimg.png")

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
    client.add_cog(Images(client))
