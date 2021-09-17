import discord, requests, aiohttp
from discord.ext import commands
from json import load as loadjson
from json import loads as loadjsonstring
from bs4 import BeautifulSoup
from random import choice as randomchoice

class Fun(commands.Cog):
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
    async def inspire(self, ctx):
        loading_message = await ctx.send(embed=self.please_wait_emb)

        try:
            r = requests.get("https://zenquotes.io/api/random")
            json_data = loadjsonstring(r.text)
            quote = json_data[0]['q'] + " - " + json_data[0]['a']
            embed=discord.Embed(title="Inspirational isn't it?", color=0xff0000)
            embed.set_author(name="YourBot", icon_url="https://cdn.discordapp.com/attachments/877796755234783273/879295069834850324/Avatar.png")
            embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/877796755234783273/879382016041291828/NicePng_light-streak-png_395357.png")
            embed.add_field(name="Inspirational Quote:", value=f"{quote}", inline=True)
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

    @commands.command()
    async def bored(self, ctx):
        loading_message = await ctx.send(embed=self.please_wait_emb)

        try:
            r = requests.get('http://www.boredapi.com/api/activity/')
            data = r.json()
            what_to_do_when_bored = f'[+] Activity: {data["activity"]} \n[+] Type: {data["type"]} \n[+] Participants: {data["participants"]} \n[+] Key: {data["key"]} \n[+] Accessibility: {data["accessibility"]} '
            embed=discord.Embed(title="Heres an Activity for you", description="If you are bored, consider doing this", color=0xff0000)
            embed.set_author(name="YourBot", icon_url="https://cdn.discordapp.com/attachments/877796755234783273/879295069834850324/Avatar.png")
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
            embed3=discord.Embed(title=":red_square: Error!", description="The command was unable to run successfully! ", color=0xff0000)
            embed3.set_author(name="YourBot", icon_url="https://cdn.discordapp.com/attachments/877796755234783273/879295069834850324/Avatar.png")
            embed3.set_thumbnail(url="https://cdn.discordapp.com/attachments/877796755234783273/879298565380386846/sign-red-error-icon-1.png")
            embed3.add_field(name="Error:", value=f"{e}", inline=False)
            embed3.set_footer(text=f"Requested by {ctx.author.name}")
            await loading_message.delete()
            await ctx.send(embed=embed3)

    @commands.command()
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

            embed=discord.Embed(title="a Dad Joke", color=0xff0000)
            embed.set_author(name="YourBot", icon_url="https://cdn.discordapp.com/attachments/877796755234783273/879295069834850324/Avatar.png")
            embed.set_thumbnail(url="https://user-images.githubusercontent.com/36286877/127767330-d3e68d90-67a0-4672-b3e1-6193b323bc21.png")
            embed.add_field(name="Joke", value=f"{r['joke']}", inline=False)
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
    async def joke(self, ctx):
        loading_message = await ctx.send(embed=self.please_wait_emb)

        r = requests.get("https://v2.jokeapi.dev/joke/Any")
        c = r.json()
        # print(c)

        try:
            jokeit = c["joke"]
        except:
            try:
                jokeit = c["setup"]
            except Exception as e:
                embed2=discord.Embed(title=":red_square: Error!", description="The command was unable to run successfully! ", color=0xff0000)
                embed2.set_author(name="YourBot", icon_url="https://cdn.discordapp.com/attachments/877796755234783273/879295069834850324/Avatar.png")
                embed2.set_thumbnail(url="https://cdn.discordapp.com/attachments/877796755234783273/879298565380386846/sign-red-error-icon-1.png")
                embed2.add_field(name="Error:", value=f"{e}", inline=False)
                embed2.set_footer(text=f"Requested by {ctx.author.name}")
                await loading_message.delete()
                await ctx.send(embed=embed2)
                return

        embed=discord.Embed(title=":grin: a Joke", color=0xff0000)
        embed.set_author(name="YourBot", icon_url="https://cdn.discordapp.com/attachments/877796755234783273/879295069834850324/Avatar.png")
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/877796755234783273/879303282139463680/480px-Happy_smiley_face.png")
        embed.add_field(name="Joke", value=f"{jokeit}", inline=False)
        embed.add_field(name="Information", value=f"Category: {c['category']} \nType: {c['type']} \nNSFW: {c['flags']['nsfw']} \nReligious: {c['flags']['religious']} \nPolitical: {c['flags']['political']} \nRacist: {c['flags']['racist']} \nSexist: {c['flags']['sexist']} \nExplicit: {c['flags']['explicit']} \nLanguage: {c['lang']}", inline=True)
        embed.set_footer(text=f"Requested by {ctx.author.name}")
        await loading_message.delete()
        await ctx.send(embed=embed)


    @commands.command(aliases=['wouldyourather', 'would-you-rather', 'wyrq'])
    async def wyr(self, ctx, *, questionhere):
        loading_message = await ctx.send(embed=self.please_wait_emb)

        try:
            r = requests.get('https://www.conversationstarters.com/wyrqlist.php').text

            soup = BeautifulSoup(r, 'html.parser')
            qa = soup.find(id='qa').text
            qor = soup.find(id='qor').text
            qb = soup.find(id='qb').text

            embed=discord.Embed(title="Would You Rather", color=0xff0000)
            embed.set_author(name="YourBot", icon_url="https://cdn.discordapp.com/attachments/877796755234783273/879295069834850324/Avatar.png")
            embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/877796755234783273/879583873527332904/Would-You-Rather_Questions-680x430.jpg")
            embed.add_field(name="Question", value=f"{questionhere}", inline=False)
            embed.add_field(name="Answer", value=f"{qa}\n{qor}\n{qb}", inline=False)
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
    async def advice(self, ctx):
        loading_message = await ctx.send(embed=self.please_wait_emb)

        try:
            r = requests.get("https://api.adviceslip.com/advice").json()
            c = r['slip']['advice']

            embed=discord.Embed(title="an Adive", color=0xff0000)
            embed.set_author(name="YourBot", icon_url="https://cdn.discordapp.com/attachments/877796755234783273/879295069834850324/Avatar.png")
            embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/877796755234783273/880034306720956456/download_1.jfif")
            embed.add_field(name="Advice", value=f"{c}", inline=False)
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

    @commands.command(aliases=["chuck-norris-joke", "chuck-joke"])
    async def chuckjoke(self, ctx):
        loading_message = await ctx.send(embed=self.please_wait_emb)

        try:
            url = f"https://api.chucknorris.io/jokes/random"
            r = requests.get(url).json()
            joke = r['value']
            created_at = r['created_at']
            urlfj = r['url']

            embed=discord.Embed(title="Chuck Joke", color=0xff0000)
            embed.set_author(name="YourBot", icon_url="https://cdn.discordapp.com/attachments/877796755234783273/879295069834850324/Avatar.png")
            embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/877796755234783273/880035248820342824/chuck-norris.png")
            embed.add_field(name="Joke", value=f"{joke}", inline=False)
            embed.add_field(name="Created At", value=f"{created_at}", inline=False)
            embed.add_field(name="URL", value=f"{urlfj}", inline=True)
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


    @commands.command(alieases=["guess-age"])
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

            embed=discord.Embed(title="Guess Age", color=0xff0000)
            embed.set_author(name="YourBot", icon_url="https://cdn.discordapp.com/attachments/877796755234783273/879295069834850324/Avatar.png")
            embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/877796755234783273/880027346478968872/image.jfif")
            embed.add_field(name="Name", value=f"{name}", inline=False)
            embed.add_field(name="Age", value=f"{age}", inline=False)
            embed.add_field(name="Count", value=f"{count}", inline=False)
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

    @commands.command(aliases=["propose"])
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
            embed3=discord.Embed(title=":red_square: Error!", description="The command was unable to run successfully! ", color=0xff0000)
            embed3.set_author(name="YourBot", icon_url="https://cdn.discordapp.com/attachments/877796755234783273/879295069834850324/Avatar.png")
            embed3.set_thumbnail(url="https://cdn.discordapp.com/attachments/877796755234783273/879298565380386846/sign-red-error-icon-1.png")
            embed3.add_field(name="Error:", value=f"{e}", inline=False)
            embed3.set_footer(text=f"Requested by {ctx.author.name}")
            await loading_message.delete()
            await ctx.send(embed=embed3)

    @commands.command(aliases=["jokenew"])
    async def joke2(self, ctx):
        loading_message = await ctx.send(embed=self.please_wait_emb)

        try:
            r = requests.get("https://some-random-api.ml/joke").json()

            embed=discord.Embed(title="a Joke", color=0xff0000)
            embed.set_author(name="YourBot", icon_url="https://cdn.discordapp.com/attachments/877796755234783273/879295069834850324/Avatar.png")
            embed.set_thumbnail(url="https://media.discordapp.net/attachments/877796755234783273/880742956552822794/mr-bean-avatar-character-cartoon-rowan-atkinson-png-image-33.png?width=454&height=584")
            embed.add_field(name="Joke", value=f"{r['joke']}", inline=False)
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













def setup(client: commands.Bot):
    client.add_cog(Fun(client))







