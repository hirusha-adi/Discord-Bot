import discord, requests, aiohttp
from discord.ext import commands
from json import load as loadjson
from json import loads as loadjsonstring
from bs4 import BeautifulSoup
from random import choice as randomchoice
import database.retrieve_embeds as getembed


class Fun(commands.Cog, description="Laughter is the best medicine!"):
    def __init__(self, client: commands.Bot):
        self.client = client

        # Loading config.json and its important content for this file
        self.botconfigdata = loadjson(open("config.json", "r"))
        self.bot_prefix = self.botconfigdata["msg-prefix"]
        self.bot_inv_link = self.botconfigdata["invite-link"]

       # This is the please-wait/Loading embed
        self.please_wait_emb = discord.Embed(title=getembed.PleaseWait.TITLE, description=f"``` {getembed.PleaseWait.DESCRIPTION} ```", color=getembed.PleaseWait.COLOR)
        self.please_wait_emb.set_author(name=getembed.PleaseWait.AUTHOR_NAME, icon_url=getembed.PleaseWait.AUTHOR_LINK)
        self.please_wait_emb.set_thumbnail(url=getembed.PleaseWait.THUMBNAIL)
        self.please_wait_emb.set_footer(text=getembed.PleaseWait.FOOTER)
    

    @commands.command(breif="Inspiration quotes",
    description="Get an inspiration quote with the author's name",
    help="Get an inspiration quote with the author's name")
    async def inspire(self, ctx):
        loading_message = await ctx.send(embed=self.please_wait_emb)

        try:
            r = requests.get("https://zenquotes.io/api/random")
            json_data = loadjsonstring(r.text)
            quote = json_data[0]['q'] + " - " + json_data[0]['a']
            embed=discord.Embed(title="Inspirational isn't it?", color=getembed.Common.COLOR)
            embed.set_author(name=getembed.Common.AUTHOR, icon_url=getembed.Common.AUTHOR_LINK)
            embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/877796755234783273/879382016041291828/NicePng_light-streak-png_395357.png")
            embed.add_field(name="Inspirational Quote:", value=f"{quote}", inline=True)
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


    @commands.command(breif="get an Activity to do",
    description="Get an activity/task to do when you are bored",
    help="Get an activity/task to do when you are bored")
    async def bored(self, ctx):
        loading_message = await ctx.send(embed=self.please_wait_emb)

        try:
            r = requests.get('http://www.boredapi.com/api/activity/')
            data = r.json()
            what_to_do_when_bored = f'[+] Activity: {data["activity"]} \n[+] Type: {data["type"]} \n[+] Participants: {data["participants"]} \n[+] Key: {data["key"]} \n[+] Accessibility: {data["accessibility"]} '
            embed=discord.Embed(title="Heres an Activity for you", description="If you are bored, consider doing this", color=getembed.Common.COLOR)
            embed.set_author(name=getembed.Common.AUTHOR, icon_url=getembed.Common.AUTHOR_LINK)
            embed.add_field(name="Activity", value=f"{data['activity']}", inline=False)
            embed.add_field(name="Type", value=f"{data['type']}", inline=False)
            embed.add_field(name="Participants", value=f"{data['participants']}", inline=False)
            embed.add_field(name="Key", value=f"{data['key']}", inline=False)
            embed.add_field(name="Accessibility", value=f"{data['accessibility']}", inline=False)
            embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/877796755234783273/884694742716268554/unnamed.png")
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

    @commands.command(breif="a Dad Joke",
    description="All you need is a dad joke right now!",
    help="All you need is a dad joke right now!")
    async def dadjoke(self, ctx):
        loading_message = await ctx.send(embed=self.please_wait_emb)

        try:
            headers = {
            "Accept": "application/json"
            }
            # Get data from the API with the above mentioned headers
            async with aiohttp.ClientSession()as session:
                async with session.get("https://icanhazdadjoke.com", headers=headers) as req:
                    r = await req.json()

            embed=discord.Embed(title="a Dad Joke", color=getembed.Common.COLOR)
            embed.set_author(name=getembed.Common.AUTHOR, icon_url=getembed.Common.AUTHOR_LINK)
            embed.set_thumbnail(url="https://user-images.githubusercontent.com/36286877/127767330-d3e68d90-67a0-4672-b3e1-6193b323bc21.png")
            embed.add_field(name="Joke", value=f"{r['joke']}", inline=False)
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
    


    @commands.command(breif="a Joke",
    description="All you need is a joke right now!",
    help="All you need is a dad right now!")
    async def joke(self, ctx):
        loading_message = await ctx.send(embed=self.please_wait_emb)

        try:
            r = requests.get("https://v2.jokeapi.dev/joke/Any")
            c = r.json()
            # print(c)

            try:
                jokeit = c["joke"]
            except:
                try:
                    jokeit = c["setup"]
                except Exception as e:
                    embed2=discord.Embed(title=":red_square: Error!", description="The command was unable to run successfully! ", color=getembed.Common.COLOR)
                    embed2.set_author(name=getembed.Common.AUTHOR, icon_url=getembed.Common.AUTHOR_LINK)
                    embed2.set_thumbnail(url="https://cdn.discordapp.com/attachments/877796755234783273/879298565380386846/sign-red-error-icon-1.png")
                    embed2.add_field(name="Error:", value=f"{e}", inline=False)
                    embed2.set_footer(text=f"Requested by {ctx.author.name}")
                    await loading_message.delete()
                    await ctx.send(embed=embed2)
                    return

            embed=discord.Embed(title=":grin: a Joke", color=getembed.Common.COLOR)
            embed.set_author(name=getembed.Common.AUTHOR, icon_url=getembed.Common.AUTHOR_LINK)
            embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/877796755234783273/879303282139463680/480px-Happy_smiley_face.png")
            embed.add_field(name="Joke", value=f"{jokeit}", inline=False)
            embed.add_field(name="Information", value=f"Category: {c['category']} \nType: {c['type']} \nNSFW: {c['flags']['nsfw']} \nReligious: {c['flags']['religious']} \nPolitical: {c['flags']['political']} \nRacist: {c['flags']['racist']} \nSexist: {c['flags']['sexist']} \nExplicit: {c['flags']['explicit']} \nLanguage: {c['lang']}", inline=True)
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


    @commands.command(aliases=['wouldyourather', 'would-you-rather', 'wyrq'],
    breif="would you rather?",
    description="just a simple 'would you rather?' question",
    help="just a simple 'would you rather?' question")
    async def wyr(self, ctx, *, questionhere):
        loading_message = await ctx.send(embed=self.please_wait_emb)

        try:
            r = requests.get('https://www.conversationstarters.com/wyrqlist.php').text

            soup = BeautifulSoup(r, 'html.parser')
            qa = soup.find(id='qa').text
            qor = soup.find(id='qor').text
            qb = soup.find(id='qb').text

            embed=discord.Embed(title="Would You Rather", color=getembed.Common.COLOR)
            embed.set_author(name=getembed.Common.AUTHOR, icon_url=getembed.Common.AUTHOR_LINK)
            embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/877796755234783273/879583873527332904/Would-You-Rather_Questions-680x430.jpg")
            embed.add_field(name="Question", value=f"{questionhere}", inline=False)
            embed.add_field(name="Answer", value=f"{qa}\n{qor}\n{qb}", inline=False)
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

    
    @commands.command(breif="an Advice",
    description="Good advices make our like better!",
    help="Good advices make our like better!")
    async def advice(self, ctx):
        loading_message = await ctx.send(embed=self.please_wait_emb)

        try:
            r = requests.get("https://api.adviceslip.com/advice").json()
            c = r['slip']['advice']

            embed=discord.Embed(title="an Adive", color=getembed.Common.COLOR)
            embed.set_author(name=getembed.Common.AUTHOR, icon_url=getembed.Common.AUTHOR_LINK)
            embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/877796755234783273/880034306720956456/download_1.jfif")
            embed.add_field(name="Advice", value=f"{c}", inline=False)
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


    @commands.command(aliases=["chuck-norris-joke", "chuck-joke"],
    breif="a Chuck Norris Joke",
    description="send a Chuck Norris Joke to you",
    help="send a Chuck Norris Joke to you")
    async def chuckjoke(self, ctx):
        loading_message = await ctx.send(embed=self.please_wait_emb)

        try:
            url = f"https://api.chucknorris.io/jokes/random"
            r = requests.get(url).json()
            joke = r['value']
            created_at = r['created_at']
            urlfj = r['url']

            embed=discord.Embed(title="Chuck Joke", color=getembed.Common.COLOR)
            embed.set_author(name=getembed.Common.AUTHOR, icon_url=getembed.Common.AUTHOR_LINK)
            embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/877796755234783273/880035248820342824/chuck-norris.png")
            embed.add_field(name="Joke", value=f"{joke}", inline=False)
            embed.add_field(name="Created At", value=f"{created_at}", inline=False)
            embed.add_field(name="URL", value=f"{urlfj}", inline=True)
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


    @commands.command(alieases=["guess-age"],
    breif="Guess your age",
    description="Enter the name and this will guess your age + send the number of people with the name",
    help="Enter the name and this will guess your age + send the number of people with the name")
    async def guessage(self, ctx, *, nameToSearch):
        loading_message = await ctx.send(embed=self.please_wait_emb)

        try:
            r = requests.get("https://api.agify.io/?name=" + nameToSearch)
            c = r.json()
            try:
                name = c["name"]
            except:
                name = "Unable to get the Name"
            try:
                age = c["age"]
            except:
                age = "Unable to get the Age"
            try:
                count = c["count"]
            except:
                count = "Unable to get the Count"

            embed=discord.Embed(title="Guess Age", color=getembed.Common.COLOR)
            embed.set_author(name=getembed.Common.AUTHOR, icon_url=getembed.Common.AUTHOR_LINK)
            embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/877796755234783273/880027346478968872/image.jfif")
            embed.add_field(name="Name", value=f"{name}", inline=False)
            embed.add_field(name="Age", value=f"{age}", inline=False)
            embed.add_field(name="Count", value=f"{count}", inline=False)
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

    @commands.command(aliases=["propose"],
    breif="best method to propose",
    description="This will give you the best method on how to propose your crush/gf",
    help="This will give you the best method on how to propose your crush/gf")
    async def howpropose(self, ctx, *, name="your crush/gf"):
        loading_message = await ctx.send(embed=self.please_wait_emb)

        try:
            choicestosel = (
            f'You may directly propose {name} as she will accept you',
            f'You will need to have a lot of foreplay before sex {name} to make her like you',
            f'Buy {name} a pizza and kiss her',
            f'Buy a vibrator for {name}',
            f'say {name} a thot',
            f'touch {name}s vagina',
            f'ask "PLEASE SEND BOOB AND PUSSY PICS" from {name}'
            )
            await loading_message.delete()
            await ctx.send(f'{randomchoice(choicestosel)}')
        
        except Exception as e:
            embed3=discord.Embed(title=getembed.ErrorEmbeds.TITLE, description=getembed.ErrorEmbeds.DESCRIPTION, color=getembed.ErrorEmbeds.COLOR)
            embed3.set_author(name=getembed.Common.AUTHOR, icon_url=getembed.Common.AUTHOR_LINK)
            embed3.set_thumbnail(url=getembed.ErrorEmbeds.THUMBNAIL)
            embed3.add_field(name="Error:", value=f"{e}", inline=False)
            embed3.set_footer(text=f"Requested by {ctx.author.name}")
            await loading_message.delete()
            await ctx.send(embed=embed3)

    @commands.command(aliases=["jokenew"],
    breif="a new Joke",
    description="Laughing is a real good medicine",
    help="Laughing is a real good medicine")
    async def joke2(self, ctx):
        loading_message = await ctx.send(embed=self.please_wait_emb)

        try:
            r = requests.get("https://some-random-api.ml/joke").json()

            embed=discord.Embed(title="a Joke", color=getembed.Common.COLOR)
            embed.set_author(name=getembed.Common.AUTHOR, icon_url=getembed.Common.AUTHOR_LINK)
            embed.set_thumbnail(url="https://media.discordapp.net/attachments/877796755234783273/880742956552822794/mr-bean-avatar-character-cartoon-rowan-atkinson-png-image-33.png?width=454&height=584")
            embed.add_field(name="Joke", value=f"{r['joke']}", inline=False)
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


    @commands.command(aliases=["bettasinghe", "weththasinghe", "wettasinghe"],
    breif="iPhone 5s Flex",
    description="rare footage of a big headed oblivion flexing an iphone 5s",
    help="rare footage of a big headed oblivion flexing an iphone 5s")
    async def minusha(self, ctx):
        loading_message = await ctx.send(embed=self.please_wait_emb)

        try:
            await loading_message.delete()
            await ctx.send("https://cdn.discordapp.com/attachments/877796755234783273/888643848845283328/minusha_flexing_iphone_5s.mp4")
            
        
        except Exception as e:
            embed3=discord.Embed(title=getembed.ErrorEmbeds.TITLE, description=getembed.ErrorEmbeds.DESCRIPTION, color=getembed.ErrorEmbeds.COLOR)
            embed3.set_author(name=getembed.Common.AUTHOR, icon_url=getembed.Common.AUTHOR_LINK)
            embed3.set_thumbnail(url=getembed.ErrorEmbeds.THUMBNAIL)
            embed3.add_field(name="Error:", value=f"{e}", inline=False)
            embed3.set_footer(text=f"Requested by {ctx.author.name}")
            await loading_message.delete()
            await ctx.send(embed=embed3)





def setup(client: commands.Bot):
    client.add_cog(Fun(client))







