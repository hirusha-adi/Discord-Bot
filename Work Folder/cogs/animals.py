import discord, requests, aiohttp
from discord.ext import commands
from json import load as loadjson
from json import loads as loadjsonstring
import database.retrieve as dbEmbed


class Animals(commands.Cog, description="Images/Facts about animals"):
    def __init__(self, client: commands.Bot):
        self.client = client

        # Loading config.json and its important content for this file
        self.botconfigdata = loadjson(open("config.json", "r"))
        self.bot_prefix = self.botconfigdata["msg-prefix"]
        self.bot_inv_link = self.botconfigdata["invite-link"]

        # This is the please-wait/Loading embed
        self.please_wait_emb = discord.Embed(title=dbEmbed.PleaseWait.TITLE, description=f"``` {dbEmbed.PleaseWait.DESCRIPTION} ```", color=dbEmbed.PleaseWait.COLOR)
        self.please_wait_emb.set_author(name=dbEmbed.PleaseWait.AUTHOR_NAME, icon_url=dbEmbed.PleaseWait.AUTHOR_LINK)
        self.please_wait_emb.set_thumbnail(url=dbEmbed.PleaseWait.THUMBNAIL)
        self.please_wait_emb.set_footer(text=dbEmbed.PleaseWait.FOOTER)

        # THIS IS FOR THE EMBEDS
        self.AUTHOR = dbEmbed.Common.AUTHOR
        self.AUTHOR_LINK = dbEmbed.Common.AUTHOR_LINK
        self.COLOR = dbEmbed.Common.COLOR


    @commands.command(breif="Image of a panda", 
    description="Send an image of a panda. Works on both DM and on servers",
    help="Send an image of a panda. Works on both DM and on servers")
    async def panda(self, ctx):
        loading_message = await ctx.send(embed=self.please_wait_emb)
        
        try:
            r = requests.get("https://some-random-api.ml/img/panda").json()

            embed = discord.Embed(color=self.COLOR)
            embed.set_author(name="a Panda.", icon_url="https://cdn.freebiesupply.com/logos/large/2x/panda-7-logo-png-transparent.png") 
            embed.set_image(url=str(r["link"]))
            embed.set_footer(text=f"Requested by {ctx.author.name}")
            await loading_message.delete()
            await ctx.send(embed=embed)

        except Exception as e:
            embed3=discord.Embed(title=":red_square: Error!", description="The command was unable to run successfully! ", color=self.COLOR)
            embed3.set_author(name=self.AUTHOR, icon_url=self.AUTHOR_LINK)
            embed3.set_thumbnail(url="https://cdn.discordapp.com/attachments/877796755234783273/879298565380386846/sign-red-error-icon-1.png")
            embed3.add_field(name="Error:", value=f"{e}", inline=False)
            embed3.set_footer(text=f"Requested by {ctx.author.name}")
            await loading_message.delete()
            await ctx.send(embed=embed3)


    @commands.command(breif="Image of a dog", 
    description="Send an image of a dog. Works on both DM and on servers",
    help="Send an image of a dog. Works on both DM and on servers")
    async def dog(self, ctx):
        loading_message = await ctx.send(embed=self.please_wait_emb)
        try:
            r = requests.get("https://some-random-api.ml/img/dog").json()
            embed = discord.Embed(color=self.COLOR)
            embed.set_author(name="a Dog." , icon_url="https://t4.ftcdn.net/jpg/03/66/78/13/360_F_366781345_oEr9wc8yWhYRPZe6CGyFWS6QolZIf2fJ.jpg") 
            embed.set_image(url=str(r["link"]))
            await loading_message.delete()
            await ctx.send(embed=embed)    
        except Exception as e:
            embed3=discord.Embed(title=":red_square: Error!", description="The command was unable to run successfully! ", color=self.COLOR)
            embed3.set_author(name=self.AUTHOR, icon_url=self.AUTHOR_LINK)
            embed3.set_thumbnail(url="https://cdn.discordapp.com/attachments/877796755234783273/879298565380386846/sign-red-error-icon-1.png")
            embed3.add_field(name="Error:", value=f"{e}", inline=False)
            embed3.set_footer(text=f"Requested by {ctx.author.name}")
            await loading_message.delete()
            await ctx.send(embed=embed3)

    
    @commands.command(breif="Image of a cat", description="Send an image of a cat. Works on both DM and on servers")
    async def cat(self, ctx):
        loading_message = await ctx.send(embed=self.please_wait_emb)
        try:
            r = requests.get("https://some-random-api.ml/img/cat").json()
            embed = discord.Embed(color=self.COLOR)
            embed.set_author(name="a Cat.", icon_url="https://i.pinimg.com/736x/d6/0c/7e/d60c7e8983fdbd7c7a27fd42fb3d61ba.jpg") 
            embed.set_image(url=str(r["link"]))
            await loading_message.delete()
            await ctx.send(embed=embed)   
        
        except Exception as e:
            embed3=discord.Embed(title=":red_square: Error!", description="The command was unable to run successfully! ", color=self.COLOR)
            embed3.set_author(name=self.AUTHOR, icon_url=self.AUTHOR_LINK)
            embed3.set_thumbnail(url="https://cdn.discordapp.com/attachments/877796755234783273/879298565380386846/sign-red-error-icon-1.png")
            embed3.add_field(name="Error:", value=f"{e}", inline=False)
            embed3.set_footer(text=f"Requested by {ctx.author.name}")
            await loading_message.delete()
            await ctx.send(embed=embed3)

    @commands.command(aliases=["dog-facts", "dogfacts", "dog-fact"], 
    breif="Fact about dogs", 
    description="Send a fact about dogs. Works on both DM and on servers",
    help="Send a fact about dogs. Works on both DM and on servers")
    async def dogfact(self, ctx):
        loading_message = await ctx.send(embed=self.please_wait_emb)

        try:
            r = requests.get('https://some-random-api.ml/facts/dog')
            c = r.json()
            fact = c["fact"]

            embed=discord.Embed(title="Dog Fact", color=self.COLOR)
            embed.set_author(name=self.AUTHOR, icon_url=self.AUTHOR_LINK)
            embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/877796755234783273/880010039581102110/322868_1100-800x825.jpg")
            embed.add_field(name="Fact", value=f"{fact}", inline=False)
            embed.set_footer(text=f"Requested by {ctx.author.name}")
            await loading_message.delete()
            await ctx.send(embed=embed)
        
        except Exception as e:
            embed3=discord.Embed(title=":red_square: Error!", description="The command was unable to run successfully! ", color=self.COLOR)
            embed3.set_author(name=self.AUTHOR, icon_url=self.AUTHOR_LINK)
            embed3.set_thumbnail(url="https://cdn.discordapp.com/attachments/877796755234783273/879298565380386846/sign-red-error-icon-1.png")
            embed3.add_field(name="Error:", value=f"{e}", inline=False)
            embed3.set_footer(text=f"Requested by {ctx.author.name}")
            await loading_message.delete()
            await ctx.send(embed=embed3)


    @commands.command(aliases=["cat-facts", "catfacts", "cat-fact"], 
    breif="Fact about cats", 
    description="Send a fact about cats. Works on both DM and on servers",
    help="Send a fact about cats. Works on both DM and on servers")
    async def catfact(self, ctx):
        loading_message = await ctx.send(embed=self.please_wait_emb)

        try:
            r = requests.get('https://some-random-api.ml/facts/cat')
            c = r.json()
            fact = c["fact"]

            embed=discord.Embed(title="Cat Fact", color=self.COLOR)
            embed.set_author(name=self.AUTHOR, icon_url=self.AUTHOR_LINK)
            embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/877796755234783273/880010397392969788/3683.jpg")
            embed.add_field(name="Fact", value=f"{fact}", inline=False)
            embed.set_footer(text=f"Requested by {ctx.author.name}")
            await loading_message.delete()
            await ctx.send(embed=embed)
        
        except Exception as e:
            embed3=discord.Embed(title=":red_square: Error!", description="The command was unable to run successfully! ", color=self.COLOR)
            embed3.set_author(name=self.AUTHOR, icon_url=self.AUTHOR_LINK)
            embed3.set_thumbnail(url="https://cdn.discordapp.com/attachments/877796755234783273/879298565380386846/sign-red-error-icon-1.png")
            embed3.add_field(name="Error:", value=f"{e}", inline=False)
            embed3.set_footer(text=f"Requested by {ctx.author.name}")
            await loading_message.delete()
            await ctx.send(embed=embed3)


    @commands.command(aliases=["elephant-facts", "elephantfacts", "elephant-fact"], 
    breif="Fact about elephants", 
    description="Send a fact about elephants. Works on both DM and on servers",
    help="Send a fact about elephants. Works on both DM and on servers")
    async def elephantfact(self, ctx):
        loading_message = await ctx.send(embed=self.please_wait_emb)

        try:
            r = requests.get('https://some-random-api.ml/facts/elephant')
            c = r.json()
            fact = c["fact"]

            embed=discord.Embed(title="Elephant Fact", color=self.COLOR)
            embed.set_author(name=self.AUTHOR, icon_url=self.AUTHOR_LINK)
            embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/877796755234783273/880010717913309204/WW187785.jpg")
            embed.add_field(name="Fact", value=f"{fact}", inline=False)
            embed.set_footer(text=f"Requested by {ctx.author.name}")
            await loading_message.delete()
            await ctx.send(embed=embed)
        
        except Exception as e:
            embed3=discord.Embed(title=":red_square: Error!", description="The command was unable to run successfully! ", color=self.COLOR)
            embed3.set_author(name=self.AUTHOR, icon_url=self.AUTHOR_LINK)
            embed3.set_thumbnail(url="https://cdn.discordapp.com/attachments/877796755234783273/879298565380386846/sign-red-error-icon-1.png")
            embed3.add_field(name="Error:", value=f"{e}", inline=False)
            embed3.set_footer(text=f"Requested by {ctx.author.name}")
            await loading_message.delete()
            await ctx.send(embed=embed3)


    @commands.command(aliases=["panda-facts", "pandafacts", "panda-fact"], 
    breif="Fact about pandas", 
    description="Send a fact about pandas. Works on both DM and on servers",
    help="Send a fact about pandas. Works on both DM and on servers")
    async def pandafact(self, ctx):
        loading_message = await ctx.send(embed=self.please_wait_emb)

        try:
            r = requests.get('https://some-random-api.ml/facts/panda')
            c = r.json()
            fact = c["fact"]

            embed=discord.Embed(title="Panda Fact", color=self.COLOR)
            embed.set_author(name=self.AUTHOR, icon_url=self.AUTHOR_LINK)
            embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/877796755234783273/880011140816576552/BabyGiantPanda.jpg")
            embed.add_field(name="Fact", value=f"{fact}", inline=False)
            embed.set_footer(text=f"Requested by {ctx.author.name}")
            await loading_message.delete()
            await ctx.send(embed=embed)
        
        except Exception as e:
            embed3=discord.Embed(title=":red_square: Error!", description="The command was unable to run successfully! ", color=self.COLOR)
            embed3.set_author(name=self.AUTHOR, icon_url=self.AUTHOR_LINK)
            embed3.set_thumbnail(url="https://cdn.discordapp.com/attachments/877796755234783273/879298565380386846/sign-red-error-icon-1.png")
            embed3.add_field(name="Error:", value=f"{e}", inline=False)
            embed3.set_footer(text=f"Requested by {ctx.author.name}")
            await loading_message.delete()
            await ctx.send(embed=embed3)


    @commands.command(aliases=["fox-facts", "foxfacts", "fox-fact"], 
    breif="Fact about foxes", 
    description="Send a fact about foxes. Works on both DM and on servers",
    help="Send a fact about foxes. Works on both DM and on servers")
    async def foxfact(self, ctx):
        loading_message = await ctx.send(embed=self.please_wait_emb)

        try:
            r = requests.get('https://some-random-api.ml/facts/fox')
            c = r.json()
            fact = c["fact"]

            embed=discord.Embed(title="Fox Fact", color=self.COLOR)
            embed.set_author(name=self.AUTHOR, icon_url=self.AUTHOR_LINK)
            embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/877796755234783273/880011829194153984/im-355811.jfif")
            embed.add_field(name="Fact", value=f"{fact}", inline=False)
            embed.set_footer(text=f"Requested by {ctx.author.name}")
            await loading_message.delete()
            await ctx.send(embed=embed)
        
        except Exception as e:
            embed3=discord.Embed(title=":red_square: Error!", description="The command was unable to run successfully! ", color=self.COLOR)
            embed3.set_author(name=self.AUTHOR, icon_url=self.AUTHOR_LINK)
            embed3.set_thumbnail(url="https://cdn.discordapp.com/attachments/877796755234783273/879298565380386846/sign-red-error-icon-1.png")
            embed3.add_field(name="Error:", value=f"{e}", inline=False)
            embed3.set_footer(text=f"Requested by {ctx.author.name}")
            await loading_message.delete()
            await ctx.send(embed=embed3)


    @commands.command(aliases=["bird-facts", "birdfacts", "bird-fact"], 
    breif="Fact about birds", 
    description="Send a fact about birds. Works on both DM and on servers",
    help="Send a fact about birds. Works on both DM and on servers")
    async def birdfact(self, ctx):
        loading_message = await ctx.send(embed=self.please_wait_emb)

        try:
            r = requests.get('https://some-random-api.ml/facts/bird')
            c = r.json()
            fact = c["fact"]

            embed=discord.Embed(title="Bird Fact", color=self.COLOR)
            embed.set_author(name=self.AUTHOR, icon_url=self.AUTHOR_LINK)
            embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/877796755234783273/880012668084305930/DCTM_Penguin_UK_DK_AL526630_wkmzns.jpg")
            embed.add_field(name="Fact", value=f"{fact}", inline=False)
            embed.set_footer(text=f"Requested by {ctx.author.name}")
            await loading_message.delete()
            await ctx.send(embed=embed)
        
        except Exception as e:
            embed3=discord.Embed(title=":red_square: Error!", description="The command was unable to run successfully! ", color=self.COLOR)
            embed3.set_author(name=self.AUTHOR, icon_url=self.AUTHOR_LINK)
            embed3.set_thumbnail(url="https://cdn.discordapp.com/attachments/877796755234783273/879298565380386846/sign-red-error-icon-1.png")
            embed3.add_field(name="Error:", value=f"{e}", inline=False)
            embed3.set_footer(text=f"Requested by {ctx.author.name}")
            await loading_message.delete()
            await ctx.send(embed=embed3)


    @commands.command(aliases=["koala-facts", "koalafacts", "koala-fact"], 
    breif="Fact about koalas", 
    description="Send a fact about koalas. Works on both DM and on servers",
    help="Send a fact about koalas. Works on both DM and on servers")
    async def koalafact(self, ctx):
        loading_message = await ctx.send(embed=self.please_wait_emb)

        try:
            r = requests.get('https://some-random-api.ml/facts/koala')
            c = r.json()
            fact = c["fact"]

            embed=discord.Embed(title="Koala Fact", color=self.COLOR)
            embed.set_author(name=self.AUTHOR, icon_url=self.AUTHOR_LINK)
            embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/877796755234783273/880013091897770014/Koala.jpg")
            embed.add_field(name="Fact", value=f"{fact}", inline=False)
            embed.set_footer(text=f"Requested by {ctx.author.name}")
            await loading_message.delete()
            await ctx.send(embed=embed)
        
        except Exception as e:
            embed3=discord.Embed(title=":red_square: Error!", description="The command was unable to run successfully! ", color=self.COLOR)
            embed3.set_author(name=self.AUTHOR, icon_url=self.AUTHOR_LINK)
            embed3.set_thumbnail(url="https://cdn.discordapp.com/attachments/877796755234783273/879298565380386846/sign-red-error-icon-1.png")
            embed3.add_field(name="Error:", value=f"{e}", inline=False)
            embed3.set_footer(text=f"Requested by {ctx.author.name}")
            await loading_message.delete()
            await ctx.send(embed=embed3)


    @commands.command(aliases=["redpandaimage", "redpandaimg"], 
    breif="Image of a red panda", 
    description="Send an image of a red panda. Works on both DM and on servers",
    help="Send an image of a red panda. Works on both DM and on servers")
    async def redpanda(self, ctx):
        loading_message = await ctx.send(embed=self.please_wait_emb)

        try:
            r = requests.get('https://some-random-api.ml/img/red_panda')
            c = r.json()
            fact = c["link"]

            embed=discord.Embed(title="Red Panda Fact", color=self.COLOR)
            embed.set_author(name=self.AUTHOR, icon_url=self.AUTHOR_LINK)
            embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/877796755234783273/880013593465217034/16071828377_85109fdee4_o.0.0.jpg")
            embed.add_field(name="Fact", value=f"{fact}", inline=False)
            embed.set_footer(text=f"Requested by {ctx.author.name}")
            await loading_message.delete()
            await ctx.send(embed=embed)
        
        except Exception as e:
            embed3=discord.Embed(title=":red_square: Error!", description="The command was unable to run successfully! ", color=self.COLOR)
            embed3.set_author(name=self.AUTHOR, icon_url=self.AUTHOR_LINK)
            embed3.set_thumbnail(url="https://cdn.discordapp.com/attachments/877796755234783273/879298565380386846/sign-red-error-icon-1.png")
            embed3.add_field(name="Error:", value=f"{e}", inline=False)
            embed3.set_footer(text=f"Requested by {ctx.author.name}")
            await loading_message.delete()
            await ctx.send(embed=embed3)


    @commands.command(aliases=["birds", "bird-image", "bird-img"], 
    breif="Image of a bird", 
    description="Send an image of a bird. Works on both DM and on servers",
    help="Send an image of a bird. Works on both DM and on servers")
    async def bird(self, ctx):
        loading_message = await ctx.send(embed=self.please_wait_emb)

        try:
            r = requests.get('https://some-random-api.ml/img/birb')
            c = r.json()
            fact = c["link"]
            em = discord.Embed(title='a Bird', color=self.COLOR)
            em.set_author(name='a Random Bird', icon_url='https://ichef.bbci.co.uk/news/976/cpsprodpb/67CF/production/_108857562_mediaitem108857561.jpg')
            em.set_image(url=fact)
            em.set_footer(text=f"Requested by {ctx.author.name}")
            await loading_message.delete()
            await ctx.send(embed=em)

        except Exception as e:
            embed3=discord.Embed(title=":red_square: Error!", description="The command was unable to run successfully! ", color=self.COLOR)
            embed3.set_author(name=self.AUTHOR, icon_url=self.AUTHOR_LINK)
            embed3.set_thumbnail(url="https://cdn.discordapp.com/attachments/877796755234783273/879298565380386846/sign-red-error-icon-1.png")
            embed3.add_field(name="Error:", value=f"{e}", inline=False)
            embed3.set_footer(text=f"Requested by {ctx.author.name}")
            await loading_message.delete()
            await ctx.send(embed=embed3)


    @commands.command(aliases=["foxes", "fox-image", "fox-img"], 
    breif="Image of a fox", 
    description="Send an image of a fox. Works on both DM and on servers",
    help="Send an image of a fox. Works on both DM and on servers")
    async def fox(self, ctx):
        loading_message = await ctx.send(embed=self.please_wait_emb)

        try:
            r = requests.get('https://some-random-api.ml/img/fox')
            c = r.json()
            fact = c["link"]
            em = discord.Embed(title='a Fox', color=self.COLOR)
            em.set_author(name='a Fox', icon_url='https://images.unsplash.com/photo-1615602127413-459bdb48cf45?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=1000&q=80')
            em.set_image(url=fact)
            em.set_footer(text=f"Requested by {ctx.author.name}")
            await loading_message.delete()
            await ctx.send(embed=em)
        
        except Exception as e:
            embed3=discord.Embed(title=":red_square: Error!", description="The command was unable to run successfully! ", color=self.COLOR)
            embed3.set_author(name=self.AUTHOR, icon_url=self.AUTHOR_LINK)
            embed3.set_thumbnail(url="https://cdn.discordapp.com/attachments/877796755234783273/879298565380386846/sign-red-error-icon-1.png")
            embed3.add_field(name="Error:", value=f"{e}", inline=False)
            embed3.set_footer(text=f"Requested by {ctx.author.name}")
            await loading_message.delete()
            await ctx.send(embed=embed3)


    @commands.command(breif="Image of a raccoon", 
    description="Send an image of a raccoon. Works on both DM and on servers",
    help="Send an image of a raccoon. Works on both DM and on servers")
    async def raccoon(self, ctx):
        loading_message = await ctx.send(embed=self.please_wait_emb)

        try:
            r = requests.get("https://some-random-api.ml/animal/raccoon").json()

            embed=discord.Embed(title="a Raccoon", color=self.COLOR)
            embed.set_author(name="YourBot", icon_url="https://media.discordapp.net/attachments/877796755234783273/879295069834850324/Avatar.png?width=300&height=300")
            embed.set_image(url=str(r["image"]))
            embed.set_footer(text=f"Requested by {ctx.author.name}")
            await loading_message.delete()
            await ctx.send(embed=embed)

        except Exception as e:
            embed3=discord.Embed(title=":red_square: Error!", description="The command was unable to run successfully! ", color=self.COLOR)
            embed3.set_author(name=self.AUTHOR, icon_url=self.AUTHOR_LINK)
            embed3.set_thumbnail(url="https://cdn.discordapp.com/attachments/877796755234783273/879298565380386846/sign-red-error-icon-1.png")
            embed3.add_field(name="Error:", value=f"{e}", inline=False)
            embed3.set_footer(text=f"Requested by {ctx.author.name}")
            await loading_message.delete()
            await ctx.send(embed=embed3)


    @commands.command(breif="Fact about raccoons", 
    description="Send a fact about raccoons. Works on both DM and on servers",
    help="Send a fact about raccoons. Works on both DM and on servers")
    async def raccoonfact(self, ctx):
        loading_message = await ctx.send(embed=self.please_wait_emb)

        try:
            r = requests.get("https://some-random-api.ml/animal/raccoon").json()

            embed=discord.Embed(title="a Raccoon Fact", color=self.COLOR)
            embed.set_author(name="YourBot", icon_url="https://media.discordapp.net/attachments/877796755234783273/879295069834850324/Avatar.png?width=300&height=300")
            embed.set_thumbnail(url=str(r["image"]))
            embed.add_field(name="Fact", value=str(r["fact"]), inline=False)
            embed.set_footer(text=f"Requested by {ctx.author.name}")
            await loading_message.delete()
            await ctx.send(embed=embed)

        except Exception as e:
            embed3=discord.Embed(title=":red_square: Error!", description="The command was unable to run successfully! ", color=self.COLOR)
            embed3.set_author(name=self.AUTHOR, icon_url=self.AUTHOR_LINK)
            embed3.set_thumbnail(url="https://cdn.discordapp.com/attachments/877796755234783273/879298565380386846/sign-red-error-icon-1.png")
            embed3.add_field(name="Error:", value=f"{e}", inline=False)
            embed3.set_footer(text=f"Requested by {ctx.author.name}")
            await loading_message.delete()
            await ctx.send(embed=embed3)

    @commands.command(breif="Image of a kangaroo", 
    description="Send an image of a kangaroo. Works on both DM and on servers",
    help="Send an image of a kangaroo. Works on both DM and on servers")
    async def kangaroo(self, ctx):
        loading_message = await ctx.send(embed=self.please_wait_emb)

        try:
            r = requests.get("https://some-random-api.ml/animal/kangaroo").json()

            embed=discord.Embed(title="a Kangaroo", color=self.COLOR)
            embed.set_author(name="YourBot", icon_url="https://media.discordapp.net/attachments/877796755234783273/879295069834850324/Avatar.png?width=300&height=300")
            embed.set_image(url=str(r["image"]))
            embed.set_footer(text=f"Requested by {ctx.author.name}")
            await loading_message.delete()
            await ctx.send(embed=embed)

        except Exception as e:
            embed3=discord.Embed(title=":red_square: Error!", description="The command was unable to run successfully! ", color=self.COLOR)
            embed3.set_author(name=self.AUTHOR, icon_url=self.AUTHOR_LINK)
            embed3.set_thumbnail(url="https://cdn.discordapp.com/attachments/877796755234783273/879298565380386846/sign-red-error-icon-1.png")
            embed3.add_field(name="Error:", value=f"{e}", inline=False)
            embed3.set_footer(text=f"Requested by {ctx.author.name}")
            await loading_message.delete()
            await ctx.send(embed=embed3)


    @commands.command(breif="Fact about kangaroos", 
    description="Send a fact about kangaroos. Works on both DM and on servers",
    help="Send a fact about kangaroos. Works on both DM and on servers")
    async def kangaroofact(self, ctx):
        loading_message = await ctx.send(embed=self.please_wait_emb)

        try:
            r = requests.get("https://some-random-api.ml/animal/kangaroo").json()

            embed=discord.Embed(title="a Kangaroo Fact", color=self.COLOR)
            embed.set_author(name="YourBot", icon_url="https://media.discordapp.net/attachments/877796755234783273/879295069834850324/Avatar.png?width=300&height=300")
            embed.set_thumbnail(url=str(r["image"]))
            embed.add_field(name="Fact", value=str(r["fact"]), inline=False)
            embed.set_footer(text=f"Requested by {ctx.author.name}")
            await loading_message.delete()
            await ctx.send(embed=embed)

        except Exception as e:
            embed3=discord.Embed(title=":red_square: Error!", description="The command was unable to run successfully! ", color=self.COLOR)
            embed3.set_author(name=self.AUTHOR, icon_url=self.AUTHOR_LINK)
            embed3.set_thumbnail(url="https://cdn.discordapp.com/attachments/877796755234783273/879298565380386846/sign-red-error-icon-1.png")
            embed3.add_field(name="Error:", value=f"{e}", inline=False)
            embed3.set_footer(text=f"Requested by {ctx.author.name}")
            await loading_message.delete()
            await ctx.send(embed=embed3)
    
    @commands.command(breif="Fact about whales", 
    description="Send a fact about whales. Works on both DM and on servers", 
    help="Send a fact about whales. Works on both DM and on servers")
    async def whalefact(self, ctx):
        loading_message = await ctx.send(embed=self.please_wait_emb)

        try:
            r = requests.get("https://some-random-api.ml/facts/whale").json()

            embed=discord.Embed(title="a Whale Fact", color=self.COLOR)
            embed.set_author(name=self.AUTHOR, icon_url=self.AUTHOR_LINK)
            embed.add_field(name="Fact", value=f"{r['fact']}", inline=True)
            embed.set_thumbnail(url="https://media.discordapp.net/attachments/877796755234783273/880809109052588052/167291_web.jpg?width=759&height=504")
            embed.set_footer(text=f"Requested by {ctx.author.name}")
            await loading_message.delete()
            await ctx.send(embed=embed)

        except Exception as e:
            embed3=discord.Embed(title=":red_square: Error!", description="The command was unable to run successfully! ", color=self.COLOR)
            embed3.set_author(name=self.AUTHOR, icon_url=self.AUTHOR_LINK)
            embed3.set_thumbnail(url="https://media.discordapp.net/attachments/877796755234783273/880745781966037032/new-scrabble-words-2018-beatdown-5657-57124c9f228c0258d65053fe7d3891491x.jpg")
            embed3.add_field(name="Error:", value=f"{e}", inline=False)
            embed3.add_field(name="Possible Fix:", value=f"You must have only one '||' part for the whole message for the bot to divide the string", inline=False)
            embed3.set_footer(text=f"Requested by {ctx.author.name}")
            await loading_message.delete()
            await ctx.send(embed=embed3)






def setup(client: commands.Bot):
    client.add_cog(Animals(client))

