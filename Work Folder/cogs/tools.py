import discord, requests, hashlib, urllib, base64, asyncio, os, youtube_dl
from discord.ext import commands
from json import load as loadjson
from random import choices as randomchoices
from string import ascii_letters, digits
from password_strength import PasswordStats
from email.message import EmailMessage
import smtplib



from platform import system as pltfsys
try:
    import instaloader
except:
    if pltfsys().lower().startswith('win'):
        os.system("pip install instaloader")
    else:
        os.system("pip3 install instaloader")
    import instaloader

try:
    from pyfiglet import Figlet
except:
    if pltfsys().lower().startswith('win'):
        os.system("pip install pyfiglet")
    else:
        os.system("pip3 install pyfiglet")
    from pyfiglet import Figlet

try:
    from youtubesearchpython import VideosSearch
except:
    if pltfsys().lower().startswith('win'):
        os.system("pip install youtube-search-python")
    else:
        os.system("pip3 install youtube-search-python")
    from youtubesearchpython import VideosSearch


class ToolCommands(commands.Cog):
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

        self.bot_email_addr = os.environ['EMAILA']
        self.bot_email_password = os.environ['EMAILP']
        
        self.filepwdlist1 = open("pwds2.txt", "r")
        self.lines = self.filepwdlist1.readlines()


    @commands.command(aliases=["pwdc", "passwordcheck"])
    async def pwdcheck(self, ctx, *, password):
        """
        Idea by discord user NoPe / The founder of TeamSDS | https://teamsds.net/
        Password List: https://github.com/danielmiessler/SecLists/blob/master/Passwords/Common-Credentials/10-million-password-list-top-1000000.txt
        """
        loading_message = await ctx.send(embed=self.please_wait_emb)

        try:
            if password + "\n" in self.lines:
                embed=discord.Embed(title="Password Checker!", color=0xff0000)
                embed.set_author(name="NearBot", icon_url="https://cdn.discordapp.com/attachments/877796755234783273/879295069834850324/Avatar.png")
                embed.set_thumbnail(url="https://media.discordapp.net/attachments/877796755234783273/881072664658214912/change-password.png?width=479&height=464")
                embed.add_field(name=f"Your Passoword", value=f"{password}", inline=False)
                embed.add_field(name=f"Safety", value=f"Not Safe. This password is in the list of most common 10 million passwords!", inline=False)
                embed.set_footer(text=f"Requested by {ctx.author.name}")
                await loading_message.delete()
                await ctx.send(embed=embed)

            else:
                embed=discord.Embed(title="Password Checker!", color=0xff0000)
                embed.set_author(name="NearBot", icon_url="https://cdn.discordapp.com/attachments/877796755234783273/879295069834850324/Avatar.png")
                embed.set_thumbnail(url="https://media.discordapp.net/attachments/877796755234783273/881072664658214912/change-password.png?width=479&height=464")
                embed.add_field(name=f"Your Passoword", value=f"{password}", inline=False)
                embed.add_field(name=f"Safety", value=f"Safe. This password is not in the list of most common 10 million passwords!", inline=False)
                embed.set_footer(text=f"Requested by {ctx.author.name}")
                await loading_message.delete()
                await ctx.send(embed=embed)

        except Exception as e:
            embed2=discord.Embed(title=":red_square: Error!", description="The command was unable to run successfully! ", color=0xff0000)
            embed2.set_author(name="NearBot", icon_url="https://cdn.discordapp.com/attachments/877796755234783273/879295069834850324/Avatar.png")
            embed2.set_thumbnail(url="https://cdn.discordapp.com/attachments/877796755234783273/879298565380386846/sign-red-error-icon-1.png")
            embed2.add_field(name="Error:", value=f"{e}", inline=False)
            embed2.set_footer(text=f"Requested by {ctx.author.name}")
            await loading_message.delete()
            await ctx.send(embed=embed2)
    
    @commands.command(aliases=["passowrd-strength-check", "pwdstrengthcheck", "pwdsc"])
    async def passwordstrentghcheck(self, ctx, *, passowrdhere):
        loading_message = await ctx.send(embed=self.please_wait_emb)
        """
        I tried to create something like the discord bot named 'Pencord' by Markiemm had created
        Later, he gave me the code + stuff used to get it done
        But i sticked to my own
        """
        try:
            stats = PasswordStats(f'{passowrdhere}')
            embed=discord.Embed(title="Password Strength Checker", color=0xff0000)
            embed.add_field(name="Strenth:", value=f"{stats.strength()}", inline=False)
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
    async def tinyurl(self, ctx, *, link):
        loading_message = await ctx.send(embed=self.please_wait_emb)

        try:
            # Using the public API of TinyURL
            r = requests.get(f'http://tinyurl.com/api-create.php?url={link}').text

            em = discord.Embed(color=0xff0000)
            em.set_footer(text=f"Requested by {ctx.author.name}")
            em.set_author(name="YourBot", icon_url="https://cdn.discordapp.com/attachments/877796755234783273/879295069834850324/Avatar.png")
            em.add_field(name="Shortened Link", value=r, inline=False)
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
    async def nitro(self, ctx, *, number_of_times):
        loading_message = await ctx.send(embed=self.please_wait_emb)

        try:
        # The limit is 20 to prevent spam
            if int(number_of_times) <= 20:
                embed=discord.Embed(title="Nitro Code Generator", color=0xff0000)
                embed.set_author(name="YourBot", icon_url="https://cdn.discordapp.com/attachments/877796755234783273/879295069834850324/Avatar.png")
                embed.set_thumbnail(url="https://user-images.githubusercontent.com/36286877/127767330-d3e68d90-67a0-4672-b3e1-6193b323bc21.png")
                embed.add_field(name="You have Requested:", value=f"{number_of_times} Nitro Codes", inline=False)
                embed.set_footer(text=f"Requested by {ctx.author.name}")
                await loading_message.delete()
                await ctx.send(embed=embed)
                
                for iteration, x in enumerate(range(int(number_of_times))):
                    code = ''.join(randomchoices(ascii_letters + digits, k=16))
                    await ctx.send(f'https://discord.gift/{code}')
                    await asyncio.sleep(0.6)

            else:
                embed=discord.Embed(title="Nitro Code Generator", color=0xff0000)
                embed.set_author(name="YourBot", icon_url="https://cdn.discordapp.com/attachments/877796755234783273/879295069834850324/Avatar.png")
                embed.set_thumbnail(url="https://www.nicepng.com/png/detail/214-2146883_4-fake-stamp-vector-fake-news-logo-png.png")
                embed.add_field(name="Error", value="Please enter a value below 20; This is done to prevent spam!", inline=True)
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
    async def hastebin(self, ctx, *, message):
        loading_message = await ctx.send(embed=self.please_wait_emb)

        try:
            r = requests.post("https://hastebin.com/documents", data=message).json()

            try:
                embed=discord.Embed(title="Hastebin", color=0xff0000)
                embed.set_author(name="YourBot", icon_url="https://cdn.discordapp.com/attachments/877796755234783273/879295069834850324/Avatar.png")
                embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/877796755234783273/879586340520480768/large.png")
                embed.add_field(name="Link", value=f"https://hastebin.com/{r['key']}", inline=False)
                embed.add_field(name=f"Text by {ctx.author.name}", value=f"{message}", inline=False)
                embed.set_footer(text=f"Requested by {ctx.author.name}")
                await loading_message.delete()
                await ctx.send(embed=embed)
            
            except:
                embed=discord.Embed(title="Hastebin", color=0xff0000)
                embed.set_author(name="YourBot", icon_url="https://cdn.discordapp.com/attachments/877796755234783273/879295069834850324/Avatar.png")
                embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/877796755234783273/879586340520480768/large.png")
                embed.add_field(name="Link", value=f"https://hastebin.com/{r['key']}", inline=False)
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
    async def asciiart(self, ctx, *, text):
        loading_message = await ctx.send(embed=self.please_wait_emb)

        try:
            r = requests.get(f'http://artii.herokuapp.com/make?text={urllib.parse.quote_plus(text)}').text
            
            # IF ITS MORE THAN 2000, it will send an error, the if statement is to stop it
            if len('```'+r+'```') > 2000:
                embed=discord.Embed(title="ASCII ART", description="There was a problem!", color=0xff0000)
                embed.set_author(name="YourBot", icon_url="https://cdn.discordapp.com/attachments/877796755234783273/879295069834850324/Avatar.png")
                embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/877796755234783273/879298565380386846/sign-red-error-icon-1.png")
                embed.add_field(name="Error:", value="The message has over 2000 characters", inline=False)
                embed.add_field(name="Possible fix:", value="Enter something short", inline=True)
                embed.set_footer(text=f"Requested by {ctx.author.name}")
                await loading_message.delete()
                await ctx.send(embed=embed)
                return
            try:
                await loading_message.delete()
            except:
                pass
            await ctx.send(f"```{r}```")

        except Exception as e:
            embed3=discord.Embed(title=":red_square: Error!", description="The command was unable to run successfully! ", color=0xff0000)
            embed3.set_author(name="YourBot", icon_url="https://cdn.discordapp.com/attachments/877796755234783273/879295069834850324/Avatar.png")
            embed3.set_thumbnail(url="https://cdn.discordapp.com/attachments/877796755234783273/879298565380386846/sign-red-error-icon-1.png")
            embed3.add_field(name="Error:", value=f"{e}", inline=False)
            embed3.set_footer(text=f"Requested by {ctx.author.name}")
            await loading_message.delete()
            await ctx.send(embed=embed3)


    @commands.command()
    async def reverse(self, ctx, *, message):
        loading_message = await ctx.send(embed=self.please_wait_emb)
        try:
            message = message[::-1]

            embed=discord.Embed(title="Reverse Text!", color=0xff0000)
            embed.set_author(name="YourBot", icon_url="https://cdn.discordapp.com/attachments/877796755234783273/879295069834850324/Avatar.png")
            embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/877796755234783273/879728497822687272/reverse.png")
            embed.add_field(name="Reversed", value="{message}", inline=False)
            embed.set_footer(text="Requested by {ctx.author.name}")
            await ctx.send(embed=embed)

        except Exception as e:
            embed3=discord.Embed(title=":red_square: Error!", description="The command was unable to run successfully! ", color=0xff0000)
            embed3.set_author(name="YourBot", icon_url="https://cdn.discordapp.com/attachments/877796755234783273/879295069834850324/Avatar.png")
            embed3.set_thumbnail(url="https://cdn.discordapp.com/attachments/877796755234783273/879298565380386846/sign-red-error-icon-1.png")
            embed3.add_field(name="Error:", value=f"{e}", inline=False)
            embed3.set_footer(text=f"Requested by {ctx.author.name}")
            await loading_message.delete()
            await ctx.send(embed=embed3)

    @commands.command(aliases=["e_base64"])
    async def e_b64(self, ctx, *, args):
        loading_message = await ctx.send(embed=self.please_wait_emb)

        try:
            msg = base64.b64encode('{}'.format(args).encode('ascii'))
            enc = str(msg)
            enc = enc[2:len(enc)-1]

            embed=discord.Embed(title="to Base64", color=0xff0000)
            embed.set_author(name="YourBot", icon_url="https://cdn.discordapp.com/attachments/877796755234783273/879295069834850324/Avatar.png")
            embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/877796755234783273/879955815602200586/base64-logo-352x200.jpg")
            embed.add_field(name="Query", value=f"{args}", inline=False)
            embed.add_field(name="Result", value=f"{enc}", inline=True)
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
    async def e_md5(self, ctx, *, args):
        loading_message = await ctx.send(embed=self.please_wait_emb)

        try:
            msg = hashlib.md5(args.encode())
            slpake =  msg.hexdigest()

            embed=discord.Embed(title="to MD5", color=0xff0000)
            embed.set_author(name="YourBot", icon_url="https://cdn.discordapp.com/attachments/877796755234783273/879295069834850324/Avatar.png")
            embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/877796755234783273/879956672771137546/MD5.png")
            embed.add_field(name="Query", value=f"{args}", inline=False)
            embed.add_field(name="Result", value=f"{slpake}", inline=True)
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
    async def e_sha1(self, ctx, *, args):
        loading_message = await ctx.send(embed=self.please_wait_emb)

        try:
            msg = hashlib.sha1(args.encode())
            slpuka =  msg.hexdigest()

            embed=discord.Embed(title="to SHA1", color=0xff0000)
            embed.set_author(name="YourBot", icon_url="https://cdn.discordapp.com/attachments/877796755234783273/879295069834850324/Avatar.png")
            embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/877796755234783273/879957622546108436/SHA1.png")
            embed.add_field(name="Query", value=f"{args}", inline=False)
            embed.add_field(name="Result", value=f"{slpuka}", inline=True)
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
    async def e_sha224(self, ctx, *, args):
        loading_message = await ctx.send(embed=self.please_wait_emb)

        try:
            msg = hashlib.sha3_224(args.encode())
            crnja =  msg.hexdigest()

            embed=discord.Embed(title="to SHA224", color=0xff0000)
            embed.set_author(name="YourBot", icon_url="https://cdn.discordapp.com/attachments/877796755234783273/879295069834850324/Avatar.png")
            embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/877796755234783273/879958751640191046/download.png")
            embed.add_field(name="Query", value=f"{args}", inline=False)
            embed.add_field(name="Result", value=f"{crnja}", inline=True)
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
    async def e_sha512(self, ctx, *, args):
        loading_message = await ctx.send(embed=self.please_wait_emb)

        try:
            msg = hashlib.sha3_512(args.encode())
            crnja =  msg.hexdigest()

            embed=discord.Embed(title="to SHA512", color=0xff0000)
            embed.set_author(name="YourBot", icon_url="https://cdn.discordapp.com/attachments/877796755234783273/879295069834850324/Avatar.png")
            embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/877796755234783273/879960296863698944/download_1.png")
            embed.add_field(name="Query", value=f"{args}", inline=False)
            embed.add_field(name="Result", value=f"{crnja}", inline=True)
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

    @commands.command(aliases=["leet"])
    async def e_leet(self, ctx, *, args):
        loading_message = await ctx.send(embed=self.please_wait_emb)

        try:
            encoded = args.replace('e', '3').replace('a', '4').replace('i', '!').replace('u', '|_|').replace('U', '|_|').replace('E', '3').replace('I', '!').replace('A', '4').replace('o','0').replace('O','0').replace('t','7').replace('T','7').replace('l','1').replace('L','1').replace('k','|<').replace('K','|<').replace('CK','X').replace('ck','x').replace('Ck','X').replace('cK','x')

            embed=discord.Embed(title="to LEET", color=0xff0000)
            embed.set_author(name="YourBot", icon_url="https://cdn.discordapp.com/attachments/877796755234783273/879295069834850324/Avatar.png")
            embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/877796755234783273/879961162895212574/download_2.png")
            embed.add_field(name="Query", value=f"{args}", inline=False)
            embed.add_field(name="Result", value=f"{encoded}", inline=True)
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

    @commands.command(aliases=["to-binary", "e_binary"])
    async def binary(self, ctx, *, ToBinaryText):
        loading_message = await ctx.send(embed=self.please_wait_emb)
        try:
            r = requests.get('https://some-random-api.ml/binary?text=' + ToBinaryText)
            c = r.json()
            fact = c["binary"]

            embed=discord.Embed(title="to Binary", color=0xff0000)
            embed.set_author(name="YourBot", icon_url="https://cdn.discordapp.com/attachments/877796755234783273/879295069834850324/Avatar.png")
            embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/877796755234783273/880025172055314462/85-855085_binary-codes-on-data-sheet-with-magnifying-lens.png")
            embed.add_field(name="Query", value=f"{ToBinaryText}", inline=False)
            embed.add_field(name="Result", value=f"{fact}", inline=True)
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
    
    @commands.command(aliases=["e_cipher"])
    async def e_ceaser(self, ctx, *, ToCeaserCipher):
        loading_message = await ctx.send(embed=self.please_wait_emb)
        try:
            
            cipher = ''
            for char in ToCeaserCipher:
                if not char.isalpha():
                    continue
                char = char.upper()
                code = ord(char) + 1
                if code > ord('Z'):
                    code = ord('A')
                cipher += chr(code)

            embed=discord.Embed(title="to Ceaser Cipher", color=0xff0000)
            embed.set_author(name="YourBot", icon_url="https://cdn.discordapp.com/attachments/877796755234783273/879295069834850324/Avatar.png")
            embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/877796755234783273/880025172055314462/85-855085_binary-codes-on-data-sheet-with-magnifying-lens.png")
            embed.add_field(name="Query", value=f"{ToCeaserCipher}", inline=False)
            embed.add_field(name="Result", value=f"{cipher}", inline=True)
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
    
    @commands.command(aliases=["d_cipher"])
    async def d_ceaser(self, ctx, *, ToCeaserCipher):
        loading_message = await ctx.send(embed=self.please_wait_emb)
        try:
            
            cipher = ''
            for char in ToCeaserCipher:
                if not char.isalpha():
                    continue
                char = char.upper()
                code = ord(char) - 1
                if code < ord('A'):
                    code = ord('Z')
                cipher += chr(code)

            embed=discord.Embed(title="from Ceaser Cipher", color=0xff0000)
            embed.set_author(name="YourBot", icon_url="https://cdn.discordapp.com/attachments/877796755234783273/879295069834850324/Avatar.png")
            embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/877796755234783273/880025172055314462/85-855085_binary-codes-on-data-sheet-with-magnifying-lens.png")
            embed.add_field(name="Query", value=f"{ToCeaserCipher}", inline=False)
            embed.add_field(name="Result", value=f"{cipher}", inline=True)
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



    @commands.command(aliases=["b2t", "d_binary", "decode_binary"])
    async def b_2txt(self, ctx, *, ToTextBinary):
        loading_message = await ctx.send(embed=self.please_wait_emb)

        try:
            r = requests.get('https://some-random-api.ml/binary?decode=' + ToTextBinary)
            c = r.json()
            fact = c["text"]

            embed=discord.Embed(title="From Binary", color=0xff0000)
            embed.set_author(name="YourBot", icon_url="https://cdn.discordapp.com/attachments/877796755234783273/879295069834850324/Avatar.png")
            embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/877796755234783273/880025172055314462/85-855085_binary-codes-on-data-sheet-with-magnifying-lens.png")
            embed.add_field(name="Query", value=f"{ToTextBinary}", inline=False)
            embed.add_field(name="Result", value=f"{fact}", inline=True)
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


    @commands.command(aliases=["b642t", "d_b64", "d_base64"])
    async def b64_2txt(self, ctx, *, ToTextBase64):
        loading_message = await ctx.send(embed=self.please_wait_emb)

        try:
            r = requests.get('https://some-random-api.ml/base64?decode=' + ToTextBase64)
            c = r.json()
            fact = c["text"]

            embed=discord.Embed(title="From Base64", color=0xff0000)
            embed.set_author(name="YourBot", icon_url="https://cdn.discordapp.com/attachments/877796755234783273/879295069834850324/Avatar.png")
            embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/877796755234783273/879955815602200586/base64-logo-352x200.jpg")
            embed.add_field(name="Query", value=f"{ToTextBase64}", inline=False)
            embed.add_field(name="Result", value=f"{fact}", inline=True)
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
    async def cleanuri(self, ctx, *, websiteurl):
        loading_message = await ctx.send(embed=self.please_wait_emb)

        try:
            url = 'https://cleanuri.com/api/v1/shorten'
            myobj = {'url': f'{websiteurl}'}  
            r = requests.post(url, data = myobj).json()
            shorten_url = r['result_url']
            
            embed=discord.Embed(title="URL Shortener", color=0xff0000)
            embed.set_author(name="YourBot", icon_url="https://cdn.discordapp.com/attachments/877796755234783273/879295069834850324/Avatar.png")
            embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/877796755234783273/880028609924976690/828161_url_512x512.png")
            embed.add_field(name="Original Link", value=f"{websiteurl}", inline=False)
            embed.add_field(name="Shortened Link", value=f"{shorten_url}", inline=False)
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


    
    @commands.command(aliases=["generate-pwd", "gen-pwd", "generate-password", "gen-password", "newpassword", "password", "newpass", "passwordnew"])
    async def genpwd(self, ctx, *, numberofcharacters=16):
        loading_message = await ctx.send(embed=self.please_wait_emb)

        try:
            pwd_lenlis = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40)
            try:
                numberofcharsinint = int(numberofcharacters)

            except Exception as e:
                embed3=discord.Embed(title=":red_square: Error!", description="The command was unable to run successfully! ", color=0xff0000)
                embed3.set_author(name="YourBot", icon_url="https://cdn.discordapp.com/attachments/877796755234783273/879295069834850324/Avatar.png")
                embed3.set_thumbnail(url="https://cdn.discordapp.com/attachments/877796755234783273/879298565380386846/sign-red-error-icon-1.png")
                embed3.add_field(name="Error:", value=f"{e}", inline=False)
                embed3.set_footer(text=f"Requested by {ctx.author.name}")
                await loading_message.delete()
                await ctx.send(embed=embed3)
                return
            
            if numberofcharsinint in pwd_lenlis:
                url = f"https://passwordinator.herokuapp.com/generate?num=true&char=true&caps=true&len={numberofcharacters}"
                r = requests.get(url)
                c = r.json()

                embed=discord.Embed(title="Password Generator", color=0xff0000)
                embed.set_author(name="YourBot", icon_url="https://cdn.discordapp.com/attachments/877796755234783273/879295069834850324/Avatar.png")
                embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/877796755234783273/880031728369016832/704187.png")
                embed.add_field(name="Password Length", value=f"{numberofcharacters}", inline=False)
                embed.add_field(name="Password", value=f"{c['data']}", inline=False)
                embed.set_footer(text=f"Requested by {ctx.author.name}")
                await loading_message.delete()
                await ctx.send(embed=embed)

            else:
                embed=discord.Embed(title="Password Generator", description="An Error has occured!", color=0xff0000)
                embed.set_author(name="YourBot", icon_url="https://cdn.discordapp.com/attachments/877796755234783273/879295069834850324/Avatar.png")
                embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/877796755234783273/880031728369016832/704187.png")
                embed.add_field(name="Error", value="The value of the number is high", inline=False)
                embed.add_field(name="Possible Fix", value="Enter a value below 40", inline=False)
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

    @commands.command(aliases=["clearscreennodelete", "clear-screen-no-delete", "clearscreen"])
    async def csnd(self, ctx):
        await ctx.send(f'Clearing some screen space - \n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\nRequested by {ctx.author.mention}')

    
    @commands.command()
    async def ig_pfp(self, ctx, *, ig_uname):
        loading_message = await ctx.send(embed=self.please_wait_emb)
        try:
            igpfp = instaloader.Instaloader()
            igpfp.download_profile(ig_uname, profile_pic_only=True)
            os.chdir(f'{ig_uname}')
            try:
                os.system("mv *.jpg ..")
            except:
                os.system("move *.jpg ..")
            os.chdir("..")
            try:
                os.system("mv *.jpg igtemp.jpg")
            except:
                os.system("ren *.jpg igtemp.jpg")
            try:
                os.system(f'rm -r {ig_uname}')
            except:
                os.system(f'DEL {ig_uname} /F/Q/S')

            # OLD CODE
            # await ctx.send(file=discord.File(f'igtemp.jpg'))
            # await ctx.send(f"Profile link: https://instagram.com/{ig_uname}")

            # NEW CODE
            file = discord.File(f'igtemp.jpg', filename="image.jpg")
            embed=discord.Embed(title="Instagram Profile Picture", description=f"of {ig_uname}", color=0xff0000)
            embed.set_author(name="YourBot", icon_url="https://cdn.discordapp.com/attachments/877796755234783273/879295069834850324/Avatar.png")
            embed.add_field(name="Link", value=f"https://instagram.com/{ig_uname}", inline=False)
            embed.set_image(url="attachment://image.jpg")
            embed.set_footer(text=f"Requested by {ctx.author.name}")
            await loading_message.delete()
            await ctx.send(file=file, embed=embed)

            try:
                os.system(f"rm igtemp.jpg")
            except:
                os.remove(f'{ig_uname}')
        except Exception as e:
            await ctx.send(f"Error: {e}")
    
    
    @commands.command()
    async def poll(self, ctx, *, message):
        loading_message = await ctx.send(embed=self.please_wait_emb)

        try:
            emb = discord.Embed(title=" POLL ", description=f'{message}', color=0xff0000)
            emb.set_author(name="YourBot", icon_url="https://cdn.discordapp.com/attachments/877796755234783273/879295069834850324/Avatar.png")
            emb.set_footer(text=f"Requested by {ctx.author.name}")
            await loading_message.delete()
            msg = await ctx.send(embed=emb)
            await msg.add_reaction('👍')
            await msg.add_reaction('👎')

        except Exception as e:
            embed3=discord.Embed(title=":red_square: Error!", description="The command was unable to run successfully! ", color=0xff0000)
            embed3.set_author(name="YourBot", icon_url="https://cdn.discordapp.com/attachments/877796755234783273/879295069834850324/Avatar.png")
            embed3.set_thumbnail(url="https://cdn.discordapp.com/attachments/877796755234783273/879298565380386846/sign-red-error-icon-1.png")
            embed3.add_field(name="Error:", value=f"{e}", inline=False)
            embed3.set_footer(text=f"Requested by {ctx.author.name}")
            await loading_message.delete()
            await ctx.send(embed=embed3)


    @commands.command()
    async def ascii(self, ctx, *, text):
        loading_message = await ctx.send(embed=self.please_wait_emb)
        try:
            art = Figlet(font="slant")
            ascii_art_creating_function_get = art.renderText(text)
            await loading_message.delete()
            await ctx.send(f'``` {ascii_art_creating_function_get} ```')
        
        except Exception as e:
            embed3=discord.Embed(title=":red_square: Error!", description="The command was unable to run successfully! ", color=0xff0000)
            embed3.set_author(name="YourBot", icon_url="https://cdn.discordapp.com/attachments/877796755234783273/879295069834850324/Avatar.png")
            embed3.set_thumbnail(url="https://cdn.discordapp.com/attachments/877796755234783273/879298565380386846/sign-red-error-icon-1.png")
            embed3.add_field(name="Error:", value=f"{e}", inline=False)
            embed3.set_footer(text=f"Requested by {ctx.author.name}")
            await loading_message.delete()
            await ctx.send(embed=embed3)

    @commands.command()
    async def google(self, ctx, *, whatToSearch):
        loading_message = await ctx.send(embed=self.please_wait_emb)

        try:
            embed=discord.Embed(title="Google Search", description="Link to query", color=0xFF0000)
            embed.set_author(name="YourBot", icon_url="https://cdn.discordapp.com/attachments/877796755234783273/879295069834850324/Avatar.png")
            embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/877796755234783273/880664487965900821/Google__G__Logo.svg.png")
            embed.add_field(name="Link", value=f"https://www.google.com/search?q={whatToSearch}", inline=True)
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

    
    @commands.command(aliases=["count-words", "countwords", "wordcount"])
    async def count(self, ctx, *, words):
        loading_message = await ctx.send(embed=self.please_wait_emb)
        try:
            spl = words.split(" ")
            no = len(spl)
            embed = discord.Embed(title="Word Counter", color=0xFF0000)
            embed.add_field(name="Number of Words:", value=f"{no}")
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

    
    # async def SHERLOCK_THING(usernametofind):
    #   change_directory("dsherlock")
    #   try:
    #     print("RUNNING THE COMMAND!")
    #     data = subprocess.check_output(['python3', 'sherlock', f'{usernametofind}']).decode('utf-8', errors="backslashreplace")
    #     print("RAN THE COMMAND!")
    #     change_directory("..")
    #     with open(f"{usernametofind}.txt", "w+") as slf:
    #       slf.write(data)
    #     print("FILE CREATED SUCCESSFULLY!")
    #     with open(f"{usernametofind}.txt", "r+") as slfs:
    #       filedataig = slfs.read()
    #     return data
    #   except Exception as e:
    #     print(e)
    #     return


    # @client.command()
    # async def shln(ctx, *, usernametofind):

    #   # x = threading.Thread(target=SHERLOCK_THING, args=(usernametofind,))
    #   SHERLOCK_THING(usernametofind)
    #   # x.start()
    #   p1 = Process(target=SHERLOCK_THING, args=(usernametofind,))
    #   p1.start()
    #   p1.join()

    #   try:
    #     with open(f"{usernametofind}.txt", "r+") as slfs:
    #       await ctx.send(file=discord.File(slfs, f"{usernametofind}.txt"))
        
    #     os.system(f"rm {usernametofind}.txt")

    #   except Exception as e:
    #     print(e)
    #     return


    @commands.command()
    async def sherlock(self, ctx, *, usernametofind):
    # https://github.com/sherlock-project/sherlock

    # OLD, ORIGINAL CODE, WORKING AS INTENDED, VERY BUGGY, BOT WONT WORK WHILE THIS COMMAND IS RUNNING!
    # lading_sherlock_stay = discord.Embed(title="```  Processing - This may take longer than usual.  ```", color=0xff0000)
    # lading_sherlock_stay.set_author(name="YourBot")
    # lading_sherlock_stay.set_thumbnail(url="https://c.tenor.com/I6kN-6X7nhAAAAAj/loading-buffering.gif")
    # lading_sherlock_stay.set_footer(text="Bot created by ZeaCeR#5641")
    # loading_message = await ctx.send(embed=lading_sherlock_stay)
    # change_directory("dsherlock")
    # try:
    #   print("RUNNING THE COMMAND!")
    #   try:
    #     data = subprocess.check_output(['python3', 'sherlock', f'{usernametofind}'], timeout=10).decode('utf-8', errors="backslashreplace")
    #   except:
    #     pass
    #   print("RAN THE COMMAND!")
    #   change_directory("..")
        
    #   with open(f"{usernametofind}.txt", "w+") as slf:
    #     slf.write(data)
        
    #   print("FILE CREATED SUCCESSFULLY!")
    #   with open(f"{usernametofind}.txt", "r+") as slfs:
    #     await loading_message.delete()
    #     await ctx.send(file=discord.File(slfs, f"{usernametofind}.txt"))
        
    #   os.system(f"rm {usernametofind}.txt")
    # except Exception as e:
    #   print(e)
    #   return

    # NEW CODE, FAST, NOT WORKING AS INTENDED, RETURNS ALL UNWATED STUFF
        loading_message = await ctx.send(embed=self.please_wait_emb)

        try:
            all_possible_accounts_1 = f"""+ 7Cups: https://www.7cups.com/@{usernametofind}
        + 9GAG: https://www.9gag.com/u/{usernametofind}
        + About.me: https://about.me/{usernametofind}
        + Archive.org: https://archive.org/details/@{usernametofind}
        + AskFM: https://ask.fm/{usernametofind}
        + Audiojungle: https://audiojungle.net/user/{usernametofind}
        + BLIP.fm: https://blip.fm/{usernametofind}
        + Bandcamp: https://www.bandcamp.com/{usernametofind}
        + Behance: https://www.behance.net/{usernametofind}
        + BinarySearch: https://binarysearch.io/@/{usernametofind}
        + BitBucket: https://bitbucket.org/{usernametofind}/
        + BitCoinForum: https://bitcoinforum.com/profile/{usernametofind}
        + Blogger: https://{usernametofind}.blogspot.com
        + Bookcrossing: https://www.bookcrossing.com/mybookshelf/{usernametofind}/
        + BuzzFeed: https://buzzfeed.com/{usernametofind}
        + CNET: https://www.cnet.com/profiles/{usernametofind}/
        + Carbonmade: https://{usernametofind}.carbonmade.com"""

            all_possible_accounts_2 = f"""
        + Career.habr: https://career.habr.com/{usernametofind}
        + Championat: https://www.championat.com/user/{usernametofind}
        + CloudflareCommunity: https://community.cloudflare.com/u/{usernametofind}
        + Codecademy: https://www.codecademy.com/profiles/{usernametofind}
        + Codewars: https://www.codewars.com/users/{usernametofind}
        + DailyMotion: https://www.dailymotion.com/{usernametofind}
        + Designspiration: https://www.designspiration.net/{usernametofind}/
        + DeviantART: https://{usernametofind}.deviantart.com
        + Discogs: https://www.discogs.com/user/{usernametofind}
        + Discuss.Elastic.co: https://discuss.elastic.co/u/{usernametofind}
        + Disqus: https://disqus.com/{usernametofind}"""

            all_possible_accounts_3 = f"""+ Dribbble: https://dribbble.com/{usernametofind}
        + Duolingo: https://www.duolingo.com/profile/{usernametofind}
        + Ello: https://ello.co/{usernametofind}
        + Euw: https://euw.op.gg/summoner/userName={usernametofind}
        + EyeEm: https://www.eyeem.com/u/{usernametofind}
        + F3.cool: https://f3.cool/{usernametofind}/
        + Facebook: https://www.facebook.com/{usernametofind}
        + Flickr: https://www.flickr.com/people/{usernametofind}
        + Flipboard: https://flipboard.com/@{usernametofind}
        + FortniteTracker: https://fortnitetracker.com/profile/all/{usernametofind}
        + Freelance.habr: https://freelance.habr.com/freelancers/{usernametofind}
        + Freelancer: https://www.freelancer.com/u/{usernametofind}
        + Freesound: https://freesound.org/people/{usernametofind}/
        + Giphy: https://giphy.com/{usernametofind}"""

            all_possible_accounts_4 = f"""
        + GitHub: https://www.github.com/{usernametofind}
        + GitHub Support Community: https://github.community/u/{usernametofind}/summary
        + GitLab: https://gitlab.com/{usernametofind}
        + Gitee: https://gitee.com/{usernametofind}
        + Gumroad: https://www.gumroad.com/{usernametofind}
        + GuruShots: https://gurushots.com/{usernametofind}/photos
        + Hackaday: https://hackaday.io/{usernametofind}
        + HackerNews: https://news.ycombinator.com/user?id={usernametofind}
        + HackerOne: https://hackerone.com/{usernametofind}
        + HackerRank: https://hackerrank.com/{usernametofind}
        + House-Mixes.com: https://www.house-mixes.com/profile/{usernametofind}
        + IFTTT: https://www.ifttt.com/p/{usernametofind}"""

            all_possible_accounts_5 = f"""+ Itch.io: https://{usernametofind}.itch.io/
        + Keybase: https://{usernametofind}base.io/{usernametofind}
        + Kik: https://kik.me/{usernametofind}
        + Launchpad: https://launchpad.net/~{usernametofind}
        + LeetCode: https://leetcode.com/{usernametofind}
        + Letterboxd: https://letterboxd.com/{usernametofind}
        + Lichess: https://lichess.org/@/{usernametofind}
        + LiveJournal: https://{usernametofind}.livejournal.com
        + Lolchess: https://lolchess.gg/profile/na/{usernametofind}
        + Medium: https://medium.com/@{usernametofind}
        + Memrise: https://www.memrise.com/user/{usernametofind}/
        + MixCloud: https://www.mixcloud.com/{usernametofind}/
        + Munzee: https://www.munzee.com/m/{usernametofind}
        + MyAnimeList: https://myanimelist.net/profile/{usernametofind}
        + MyMiniFactory: https://www.myminifactory.com/users/{usernametofind}"""

            all_possible_accounts_6 = f"""+ Myspace: https://myspace.com/{usernametofind}
        + NICommunityForum: https://www.native-instruments.com/forum/members?username={usernametofind}
        + Naver: https://blog.naver.com/{usernametofind}
        + Newgrounds: https://{usernametofind}.newgrounds.com
        + Otzovik: https://otzovik.com/profile/{usernametofind}
        + PCGamer: https://forums.pcgamer.com/members/?username={usernametofind}
        + Pastebin: https://pastebin.com/u/{usernametofind}
        + Patreon: https://www.patreon.com/{usernametofind}
        + Periscope: https://www.periscope.tv/{usernametofind}/
        + Pinkbike: https://www.pinkbike.com/u/{usernametofind}/
        + Pinterest: https://www.pinterest.com/{usernametofind}/
        + Pokemon Showdown: https://pokemonshowdown.com/users/{usernametofind}
        + Polarsteps: https://polarsteps.com/{usernametofind}
        + ProductHunt: https://www.producthunt.com/@{usernametofind}"""

            all_possible_accounts_7 = f"""+ PromoDJ: http://promodj.com/{usernametofind}
        + PyPi: https://pypi.org/user/{usernametofind}
        + Quizlet: https://quizlet.com/{usernametofind}
        + Quora: https://www.quora.com/profile/{usernametofind}
        + Raidforums: https://raidforums.com/User-{usernametofind}
        + Rajce.net: https://{usernametofind}.rajce.idnes.cz/
        + Rate Your Music: https://rateyourmusic.com/~{usernametofind}
        + Reddit: https://www.reddit.com/user/{usernametofind}
        + ReverbNation: https://www.reverbnation.com/{usernametofind}
        + Roblox: https://www.roblox.com/user.aspx?username={usernametofind}
        + RubyGems: https://rubygems.org/profiles/{usernametofind}
        + Sbazar.cz: https://www.sbazar.cz/{usernametofind}
        + Scratch: https://scratch.mit.edu/users/{usernametofind}
        + Scribd: https://www.scribd.com/{usernametofind}
        + Slack: https://{usernametofind}.slack.com"""

            all_possible_accounts_8 = f"""
        + Slashdot: https://slashdot.org/~{usernametofind}
        + SlideShare: https://slideshare.net/{usernametofind}
        + Smule: https://www.smule.com/{usernametofind}
        + SoundCloud: https://soundcloud.com/{usernametofind}
        + SourceForge: https://sourceforge.net/u/{usernametofind}
        + SparkPeople: https://www.sparkpeople.com/mypage.asp?id={usernametofind}
        + Speedrun.com: https://speedrun.com/user/{usernametofind}
        + SportsRU: https://www.sports.ru/profile/{usernametofind}/
        + Spotify: https://open.spotify.com/user/{usernametofind}
        + Star Citizen: https://robertsspaceindustries.com/citizens/{usernametofind}
        + Steam: https://steamcommunity.com/id/{usernametofind}
        + SteamGroup: https://steamcommunity.com/groups/{usernametofind}
        + Strava: https://www.strava.com/athletes/{usernametofind}
        + TETR.IO: https://ch.tetr.io/u/{usernametofind}
        + Tellonym.me: https://tellonym.me/{usernametofind}
        + Tinder: https://www.gotinder.com/@{usernametofind}"""

            all_possible_accounts_9 = f"""+ TrackmaniaLadder: http://en.tm-ladder.com/{usernametofind}_rech.php
        + TradingView: https://www.tradingview.com/u/{usernametofind}/
        + Trakt: https://www.trakt.tv/users/{usernametofind}
        + TrashboxRU: https://trashbox.ru/users/{usernametofind}
        + Trello: https://trello.com/{usernametofind}
        + TryHackMe: https://tryhackme.com/p/{usernametofind}
        + Ultimate-Guitar: https://ultimate-guitar.com/u/{usernametofind}
        + Unsplash: https://unsplash.com/@{usernametofind}
        + VK: https://vk.com/{usernametofind}
        + VSCO: https://vsco.co/{usernametofind}
        + Vero: https://vero.co/{usernametofind}
        + Vimeo: https://vimeo.com/{usernametofind}
        + Virgool: https://virgool.io/@{usernametofind}
        + VirusTotal: https://www.virustotal.com/ui/users/{usernametofind}/trusted_users
        + Warrior Forum: https://www.warriorforum.com/members/{usernametofind}.html"""

            all_possible_accounts_10 = f"""
        + We Heart It: https://weheartit.com/{usernametofind}
        + Whonix Forum: https://forums.whonix.org/u/{usernametofind}
        + Wikidot: http://www.wikidot.com/user:info/{usernametofind}
        + Windy: https://community.windy.com/user/{usernametofind}
        + WordPressOrg: https://profiles.wordpress.org/{usernametofind}/
        + YouNow: https://www.younow.com/{usernametofind}/
        + akniga: https://akniga.org/profile/{usernametofind}
        + authorSTREAM: http://www.authorstream.com/{usernametofind}/
        + couchsurfing: https://www.couchsurfing.com/people/{usernametofind}
        + d3RU: https://d3.ru/user/{usernametofind}/posts
        + dailykos: https://www.dailykos.com/user/{usernametofind}
        + drive2: https://www.drive2.ru/users/{usernametofind}
        + fl: https://www.fl.ru/users/{usernametofind}
        + geocaching: https://www.geocaching.com/p/default.aspx?u={usernametofind}
        + habr: https://habr.com/ru/users/{usernametofind}"""

            all_possible_accounts_11 = f"""+ igromania: http://forum.igromania.ru/member.php?username={usernametofind}
        + interpals: https://www.interpals.net/{usernametofind}
        + irecommend: https://irecommend.ru/users/{usernametofind}
        + jbzd.com.pl: https://jbzd.com.pl/uzytkownik/{usernametofind}
        + jeuxvideo: http://www.jeuxvideo.com/profil/{usernametofind}?mode=infos
        + last.fm: https://last.fm/user/{usernametofind}
        + livelib: https://www.livelib.ru/reader/{usernametofind}
        + mastodon.social: https://mastodon.social/@{usernametofind}
        + metacritic: https://www.metacritic.com/user/{usernametofind}
        + moikrug: https://moikrug.ru/{usernametofind}
        + nairaland.com: https://www.nairaland.com/{usernametofind}"""

            all_possible_accounts_12 = f"""
        + nnRU: https://{usernametofind}.www.nn.ru/
        + note: https://note.com/{usernametofind}
        + npm: https://www.npmjs.com/~{usernametofind}
        + opennet: https://www.opennet.ru/~{usernametofind}
        + osu!: https://osu.ppy.sh/users/{usernametofind}
        + phpRU: https://php.ru/forum/members/?username={usernametofind}
        + pr0gramm: https://pr0gramm.com/user/{usernametofind}
        + radio_echo_msk: https://echo.msk.ru/users/{usernametofind}
        + spletnik: https://spletnik.ru/user/{usernametofind}
        + toster: https://www.toster.ru/user/{usernametofind}/answers
        + Instagram: https://www.instagram.com/{usernametofind}
        + Tiktok: https://www.tiktok.com/@{usernametofind}
        """
            embed1=discord.Embed(title="Sherlock!", color=0xff0000)
            embed1.set_thumbnail(url="https://user-images.githubusercontent.com/27065646/53551960-ae4dff80-3b3a-11e9-9075-cef786c69364.png")
            embed1.add_field(name="All Possible Profiles!", value=all_possible_accounts_1, inline=False)
            embed1.set_footer(text="All links won't work! We will add a check real soon!")

            embed2=discord.Embed(title="Sherlock! - 2", color=0xff0000)
            embed2.set_thumbnail(url="https://user-images.githubusercontent.com/27065646/53551960-ae4dff80-3b3a-11e9-9075-cef786c69364.png")
            embed2.add_field(name="All Possible Profiles!", value=all_possible_accounts_2, inline=False)
            embed2.set_footer(text="All links won't work! Part 2")

            embed3=discord.Embed(title="Sherlock! - 3", color=0xff0000)
            embed3.set_thumbnail(url="https://user-images.githubusercontent.com/27065646/53551960-ae4dff80-3b3a-11e9-9075-cef786c69364.png")
            embed3.add_field(name="All Possible Profiles!", value=all_possible_accounts_3, inline=False)
            embed3.set_footer(text="All links won't work! Part 3")

            embed4=discord.Embed(title="Sherlock! - 4", color=0xff0000)
            embed4.set_thumbnail(url="https://user-images.githubusercontent.com/27065646/53551960-ae4dff80-3b3a-11e9-9075-cef786c69364.png")
            embed4.add_field(name="All Possible Profiles!", value=all_possible_accounts_4, inline=False)
            embed4.set_footer(text="All links won't work! Part 4")

            embed5=discord.Embed(title="Sherlock! - 5", color=0xff0000)
            embed5.set_thumbnail(url="https://user-images.githubusercontent.com/27065646/53551960-ae4dff80-3b3a-11e9-9075-cef786c69364.png")
            embed5.add_field(name="All Possible Profiles!", value=all_possible_accounts_5, inline=False)
            embed5.set_footer(text="All links won't work! Part 5")

            embed6=discord.Embed(title="Sherlock! - 6", color=0xff0000)
            embed6.set_thumbnail(url="https://user-images.githubusercontent.com/27065646/53551960-ae4dff80-3b3a-11e9-9075-cef786c69364.png")
            embed6.add_field(name="All Possible Profiles!", value=all_possible_accounts_6, inline=False)
            embed6.set_footer(text="All links won't work! Part 6")

            embed7=discord.Embed(title="Sherlock! - 7", color=0xff0000)
            embed7.set_thumbnail(url="https://user-images.githubusercontent.com/27065646/53551960-ae4dff80-3b3a-11e9-9075-cef786c69364.png")
            embed7.add_field(name="All Possible Profiles!", value=all_possible_accounts_7, inline=False)
            embed7.set_footer(text="All links won't work! Part 7")

            embed8=discord.Embed(title="Sherlock! - 8", color=0xff0000)
            embed8.set_thumbnail(url="https://user-images.githubusercontent.com/27065646/53551960-ae4dff80-3b3a-11e9-9075-cef786c69364.png")
            embed8.add_field(name="All Possible Profiles!", value=all_possible_accounts_8, inline=False)
            embed8.set_footer(text="All links won't work! Part 8")

            embed9=discord.Embed(title="Sherlock! - 9", color=0xff0000)
            embed9.set_thumbnail(url="https://user-images.githubusercontent.com/27065646/53551960-ae4dff80-3b3a-11e9-9075-cef786c69364.png")
            embed9.add_field(name="All Possible Profiles!", value=all_possible_accounts_9, inline=False)
            embed9.set_footer(text="All links won't work! Part 9")

            embed10=discord.Embed(title="Sherlock! - 10", color=0xff0000)
            embed10.set_thumbnail(url="https://user-images.githubusercontent.com/27065646/53551960-ae4dff80-3b3a-11e9-9075-cef786c69364.png")
            embed10.add_field(name="All Possible Profiles!", value=all_possible_accounts_10, inline=False)
            embed10.set_footer(text="All links won't work! Part 10")

            embed11=discord.Embed(title="Sherlock! - 11", color=0xff0000)
            embed11.set_thumbnail(url="https://user-images.githubusercontent.com/27065646/53551960-ae4dff80-3b3a-11e9-9075-cef786c69364.png")
            embed11.add_field(name="All Possible Profiles!", value=all_possible_accounts_11, inline=False)
            embed11.set_footer(text="All links won't work! Part 11")

            embed12=discord.Embed(title="Sherlock! - 12", color=0xff0000)
            embed12.set_thumbnail(url="https://user-images.githubusercontent.com/27065646/53551960-ae4dff80-3b3a-11e9-9075-cef786c69364.png")
            embed12.add_field(name="All Possible Profiles!", value=all_possible_accounts_12, inline=False)
            embed12.set_footer(text="All links won't work! Part 12")

            await loading_message.delete()
            await ctx.send(embed=embed1)
            await ctx.send(embed=embed2)
            await ctx.send(embed=embed3)
            await ctx.send(embed=embed4)
            await ctx.send(embed=embed5)
            await ctx.send(embed=embed6)
            await ctx.send(embed=embed7)
            await ctx.send(embed=embed8)
            await ctx.send(embed=embed9)
            await ctx.send(embed=embed10)
            await ctx.send(embed=embed11)
            await ctx.send(embed=embed12)
        
        except Exception as e:
            embed3=discord.Embed(title=":red_square: Error!", description="The command was unable to run successfully! ", color=0xff0000)
            embed3.set_author(name="YourBot", icon_url="https://cdn.discordapp.com/attachments/877796755234783273/879295069834850324/Avatar.png")
            embed3.set_thumbnail(url="https://cdn.discordapp.com/attachments/877796755234783273/879298565380386846/sign-red-error-icon-1.png")
            embed3.add_field(name="Error:", value=f"{e}", inline=False)
            embed3.set_footer(text=f"Requested by {ctx.author.name}")
            await loading_message.delete()
            await ctx.send(embed=embed3)


    @commands.command(aliases=["download-audio", "ytd", "youtubedownload"])
    async def audio(self, ctx, *, ytvlink):
        loading_message = await ctx.send(embed=self.please_wait_emb)

        try:
            if ytvlink.lower().startswith('https://'):
                try:
                    try:
                        options = {
                        # 'format': "134",
                        'format': 'bestaudio/best',  # choice of quality
                        'extractaudio': True,        # only keep the audio
                        'audioformat': "mp3",        # convert to mp3
                        'outtmpl': '%(id)s',         # name the file the ID of the video
                        'noplaylist': True,          # only download single song, not playlist
                        'listformats': True,         # print a list of the formats to stdout and exit
                        }
                        ydl_opts = {'format':'139'} # this is for .m4a - lowest audio quality i guess

                        file_extentsion_dlded = "m4a"

                        with youtube_dl.YoutubeDL(ydl_opts) as ydl:
                            ydl.download([f'{ytvlink}'])

                        try:
                            os.system(f"mv *.{file_extentsion_dlded} audio1.{file_extentsion_dlded}")
                        except:
                            try:
                                os.system(f"Ren *.{file_extentsion_dlded} audio1.{file_extentsion_dlded}")
                            except:
                                pass
                    
                        try:
                            with open(f"audio1.{file_extentsion_dlded}", "rb") as f:
                                audiof = discord.File(f)
                                await loading_message.delete()
                                await ctx.send(file=audiof)
                        except Exception as e:
                            embed=discord.Embed(title="An error has occured!", color=0xff0000)
                            embed.add_field(name="Error:", value=f"{e}", inline=False)
                            embed.set_author(name="YourBot", icon_url="https://cdn.discordapp.com/attachments/877796755234783273/879295069834850324/Avatar.png")
                            embed.set_footer(text=f"Requested by {ctx.author.name}")
                            await loading_message.delete()
                            await ctx.send(embed=embed)
                        
                        finally:
                            try:
                                os.system(f"rm audio1.{file_extentsion_dlded}")
                            except Exception as e:
                                embed=discord.Embed(title="An error has occured!", color=0xff0000)
                                embed.add_field(name="Error:", value=f"{e}", inline=False)
                                embed.set_author(name="YourBot", icon_url="https://cdn.discordapp.com/attachments/877796755234783273/879295069834850324/Avatar.png")
                                embed.set_footer(text=f"Requested by {ctx.author.name}")
                                try:
                                    await loading_message.delete()
                                except:
                                    pass
                                await ctx.send(embed=embed)
                            
                    except Exception as e:
                        embed=discord.Embed(title="An error has occured!", color=0xff0000)
                        embed.add_field(name="Error:", value=f"{e}", inline=False)
                        embed.set_author(name="YourBot", icon_url="https://cdn.discordapp.com/attachments/877796755234783273/879295069834850324/Avatar.png")
                        embed.set_footer(text=f"Requested by {ctx.author.name}")
                        await loading_message.delete()
                        await ctx.send(embed=embed)

                except Exception as e:
                    embed=discord.Embed(title="An error has occured!", color=0xff0000)
                    embed.add_field(name="Error:", value=f"{e}", inline=False)
                    embed.set_author(name="YourBot", icon_url="https://cdn.discordapp.com/attachments/877796755234783273/879295069834850324/Avatar.png")
                    embed.set_footer(text=f"Requested by {ctx.author.name}")
                    try:
                        await loading_message.delete()
                    except:
                        pass
                    await ctx.send(embed=embed)

                finally:
                    try:
                        os.system(f"rm audio1.{file_extentsion_dlded}")
                    except Exception as e:
                        embed=discord.Embed(title="An error has occured!", color=0xff0000)
                        embed.add_field(name="Error:", value=f"{e}", inline=False)
                        embed.set_author(name="YourBot", icon_url="https://cdn.discordapp.com/attachments/877796755234783273/879295069834850324/Avatar.png")
                        embed.set_footer(text=f"Requested by {ctx.author.name}")
                        try:
                            await loading_message.delete()
                        except:
                            pass
                        await ctx.send(embed=embed)

            else:
                embed=discord.Embed(title="An error has occured!", color=0xff0000)
                embed.set_author(name="YourBot", icon_url="https://cdn.discordapp.com/attachments/877796755234783273/879295069834850324/Avatar.png")
                embed.set_footer(text=f"Requested by {ctx.author.name}")
                embed.add_field(name="Error:", value=f"Please enter a vliad youtube url!", inline=False)
                await ctx.send(embed=embed)

        except Exception as e:
            embed3=discord.Embed(title=":red_square: Error!", description="The command was unable to run successfully! ", color=0xff0000)
            embed3.set_author(name="YourBot", icon_url="https://cdn.discordapp.com/attachments/877796755234783273/879295069834850324/Avatar.png")
            embed3.set_thumbnail(url="https://cdn.discordapp.com/attachments/877796755234783273/879298565380386846/sign-red-error-icon-1.png")
            embed3.add_field(name="Error:", value=f"{e}", inline=False)
            embed3.set_footer(text=f"Requested by {ctx.author.name}")
            await loading_message.delete()
            await ctx.send(embed=embed3)

    @commands.command(aliases=["sendmail"])
    async def sendemail(self, ctx, senderemail, recieveremail, emailsubject="Hey", *, emailcontent="Hello There!"):
        verified_mails = ("gmail.com", "outlook.com", "yahoo.com")
        embed=discord.Embed(title="Please Wait", description="``` This may take longer than usual! ```", color=0xff0000)
        embed.set_thumbnail(url="https://c.tenor.com/I6kN-6X7nhAAAAAj/loading-buffering.gif") 
        embed.set_author(name="YourBot", icon_url="https://cdn.discordapp.com/attachments/877796755234783273/879295069834850324/Avatar.png")
        embed.set_footer(text="Bot created by ZeaCeR#5641")
        loadingthing = await ctx.send(embed=embed)
        print(f"recieved args {emailsubject} | {emailcontent} | {recieveremail} | {senderemail}")        

        try:
            if senderemail.split('@')[-1].lower() in verified_mails:
                print("email is valid")
                try:
                    server = smtplib.SMTP('smtp.gmail.com', 587)
                    server.starttls()
                    print("created server")

                    try:
                        server.login(self.bot_email_addr, self.bot_email_password)
                        print("logged in")

                    except Exception as e:
                        embede=discord.Embed(title="Something was wrong!", description="Your request did not complete due to an error!", color=0xff0000)
                        embede.set_author(name="YourBot", icon_url="https://cdn.discordapp.com/attachments/877796755234783273/879295069834850324/Avatar.png")
                        embede.set_thumbnail(url="https://cdn.discordapp.com/attachments/877796755234783273/879668020006502440/SeekPng.com_envelope-icon-png_1336118.png")
                        embede.add_field(name="Error", value=f"{e}", inline=False)
                        embede.set_footer(text=f"Requested by {ctx.author.name}")
                        try:
                            await loadingthing.delete()
                        except:
                            pass
                        await ctx.send(embed=embede)
                        print("unable to login")
                        return

                    email = EmailMessage()
                    print("writing email")
                    whoasktosend = ctx.author.name
                    whoasktosendid = ctx.author.id
                    emailcontentfinal = f"""This message it being sent from the discord bot named YourBot and was requested by the user {whoasktosend} / {whoasktosendid} / {senderemail}. The message: {emailcontent}   | Thank You. Have a Nice day, Stay safe! - YourBot"""

                    email['From'] = self.bot_email_addr
                    email['To'] = recieveremail
                    email['Subject'] = emailsubject
                    email.set_content(emailcontentfinal)
                    server.send_message(email)
                    print("email sent")
                    server.close()
                    print("closed server")

                    try:
                        embed2=discord.Embed(title="Email Sent", description="Your requested email was sent suceessfully! ", color=0xff0000)
                        embed2.set_author(name="YourBot", icon_url="https://cdn.discordapp.com/attachments/877796755234783273/879295069834850324/Avatar.png")
                        embed2.set_thumbnail(url="https://cdn.discordapp.com/attachments/877796755234783273/879668020006502440/SeekPng.com_envelope-icon-png_1336118.png")
                        embed2.add_field(name="Your Email Address", value=f"{senderemail}", inline=False)
                        embed2.add_field(name="Receiver Email Address", value=f"{recieveremail}", inline=False)
                        embed2.add_field(name="Email Subject", value=f"{emailsubject}", inline=False)
                        embed2.add_field(name="Email Content", value=f"{emailcontentfinal}", inline=False)
                        embed2.set_footer(text=f"Requested by {ctx.author.name}")
                        try:
                            await loadingthing.delete()
                        except:
                            pass
                        await ctx.send(embed=embed2)
                        print("sent embed")

                    except:
                        try:
                            await loadingthing.delete()
                        except:
                            pass
                        print("sent embed")
                        await ctx.send("Email was sent successfully!")

                except Exception as e:
                    embed3=discord.Embed(title=":red_square: Error!", description="The command was unable to run successfully! ", color=0xff0000)
                    embed3.set_author(name="YourBot", icon_url="https://cdn.discordapp.com/attachments/877796755234783273/879295069834850324/Avatar.png")
                    embed3.set_thumbnail(url="https://cdn.discordapp.com/attachments/877796755234783273/879298565380386846/sign-red-error-icon-1.png")
                    embed3.add_field(name="Error:", value=f"{e}", inline=False)
                    embed3.set_footer(text=f"Requested by {ctx.author.name}")
                    try:
                        await loadingthing.delete()
                    except:
                        pass
                    await ctx.send(embed=embed3)
                    print(e)

            else:
                embed=discord.Embed(title="Something was wrong!", description="Your request did not complete due to an error!", color=0xff0000)
                embed.set_author(name="YourBot", icon_url="https://cdn.discordapp.com/attachments/877796755234783273/879295069834850324/Avatar.png")
                embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/877796755234783273/879668020006502440/SeekPng.com_envelope-icon-png_1336118.png")
                embed.add_field(name="Error", value="Invalid Email Address", inline=False)
                embed.add_field(name="How to fix", value=f"Enter a email address that ends with {verified_mails}", inline=True)
                embed.set_footer(text=f"Requested by {ctx.author.name}")
                try:
                    await loadingthing.delete()
                except:
                    pass
                await ctx.send(embed=embed)
                print("email is not valid")
        
        except Exception as e:
            embed3=discord.Embed(title=":red_square: Error!", description="The command was unable to run successfully! ", color=0xff0000)
            embed3.set_author(name="YourBot", icon_url="https://cdn.discordapp.com/attachments/877796755234783273/879295069834850324/Avatar.png")
            embed3.set_thumbnail(url="https://cdn.discordapp.com/attachments/877796755234783273/879298565380386846/sign-red-error-icon-1.png")
            embed3.add_field(name="Error:", value=f"{e}", inline=False)
            embed3.set_footer(text=f"Requested by {ctx.author.name}")
            try:
                await loadingthing.delete()
            except:
                pass
            await ctx.send(embed=embed3)
            print(e)


    @commands.command(aliases=["similarity", "closematch", "closematches"])
    async def similiar(self, ctx, *, message):
        """
        The two messages ( strings ) will be divided by the 
        """
        loading_message = await ctx.send(embed=self.please_wait_emb)

        try:
            message1, message2 = message.split('||')
            r = requests.get(f"https://some-random-api.ml/stringsimilarity?string1={message1}&string2={message2}").json()

            embed=discord.Embed(title="Find Similarity", description="between two strings", color=0xff0000)
            embed.set_author(name="YourBot", icon_url="https://cdn.discordapp.com/attachments/877796755234783273/879295069834850324/Avatar.png")
            embed.set_thumbnail(url="https://media.discordapp.net/attachments/877796755234783273/880742956552822794/mr-bean-avatar-character-cartoon-rowan-atkinson-png-image-33.png?width=454&height=584")
            embed.add_field(name="First", value=f"{message1}", inline=False)
            embed.add_field(name="Second", value=f"{message2}", inline=False)
            embed.add_field(name="Similarity", value=f"{r['similarity']}", inline=False)
            embed.set_footer(text=f"Requested by {ctx.author.name}")
            await ctx.send(embed=embed)
        
        except Exception as e:
            embed3=discord.Embed(title=":red_square: Error!", description="The command was unable to run successfully! ", color=0xff0000)
            embed3.set_author(name="YourBot", icon_url="https://cdn.discordapp.com/attachments/877796755234783273/879295069834850324/Avatar.png")
            embed3.set_thumbnail(url="https://media.discordapp.net/attachments/877796755234783273/880745781966037032/new-scrabble-words-2018-beatdown-5657-57124c9f228c0258d65053fe7d3891491x.jpg")
            embed3.add_field(name="Error:", value=f"{e}", inline=False)
            embed3.add_field(name="Possible Fix:", value=f"You must have only one '||' part for the whole message for the bot to divide the string", inline=False)
            embed3.set_footer(text=f"Requested by {ctx.author.name}")
            await loading_message.delete()
            await ctx.send(embed=embed3)
    
    @commands.command()
    async def youtube(self, ctx, *, query):
        loading_message = await ctx.send(embed=self.please_wait_emb)
        try:
            videosSearch = VideosSearch(f'{query}', limit = 1)
            mainresult = videosSearch.result()["result"]
            video_index = mainresult[0]
            video_link = video_index["link"]
            await loading_message.delete()
            await ctx.send(video_link)
        except Exception as e:
            embed3=discord.Embed(title=":red_square: Error!", description="The command was unable to run successfully! ", color=0xff0000)
            embed3.set_author(name="YourBot", icon_url="https://cdn.discordapp.com/attachments/877796755234783273/879295069834850324/Avatar.png")
            embed3.set_thumbnail(url="https://media.discordapp.net/attachments/877796755234783273/880745781966037032/new-scrabble-words-2018-beatdown-5657-57124c9f228c0258d65053fe7d3891491x.jpg")
            embed3.add_field(name="Error:", value=f"{e}", inline=False)
            embed3.add_field(name="Possible Fix:", value=f"Search something valid", inline=False)
            embed3.set_footer(text=f"Requested by {ctx.author.name}")
            await loading_message.delete()
            await ctx.send(embed=embed3)











def setup(client: commands.Bot):
    client.add_cog(ToolCommands(client))
