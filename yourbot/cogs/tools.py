import discord
import platform
import base64
import asyncio
import os
from discord.ext import commands
from random import choices as randomchoices
from string import ascii_letters, digits
from email.message import EmailMessage
import smtplib
import textwrap
import datetime
import yourbot.database.retrieve_embeds as getembed
import yourbot.database.retrieve_base as getbase
import yourbot.others.installerm as ybinstaller
try:
    from zxcvbn import zxcvbn
except:
    if platform.system().lower().startswith('win'):
        os.system("pip install zxcvbn")
    else:
        os.system("pip3 install zxcvbn")

try:
    import requests
except:
    ybinstaller.pip_install("requests")
    import requests

try:
    import hashlib
except:
    ybinstaller.pip_install("hashlib")
    import hashlib

try:
    import urllib
except:
    ybinstaller.pip_install("urllib")
    import urllib

try:
    from password_strength import PasswordStats
except:
    ybinstaller.pip_install("password_strength")
    from password_strength import PasswordStats

try:
    import Proxy_List_Scrapper
except:
    ybinstaller.pip_install("Proxy-List-Scrapper")
    import Proxy_List_Scrapper

try:
    from pytube import *
except:
    ybinstaller.pip_install("pytube")
    from pytube import *

try:
    import instaloader
except:
    ybinstaller.pip_install("instaloader")
    import instaloader

try:
    from pyfiglet import Figlet
except:
    ybinstaller.pip_install("pyfiglet")
    from pyfiglet import Figlet

try:
    from youtubesearchpython import VideosSearch
except:
    ybinstaller.pip_install("youtube-search-python")
    from youtubesearchpython import VideosSearch


class Tools(commands.Cog, description="a set of tools built to make many acitivies easier and simpler!"):
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

        self.bot_email_addr = os.environ['EMAILA']
        self.bot_email_password = os.environ['EMAILP']

        self.filepwdlist1 = open("yourbot/assets/pwds.txt", "r")
        self.lines = self.filepwdlist1.readlines()

    @commands.command(aliases=["pwdc", "passwordcheck"],
                      breif="Password Check",
                      description="Check if the given password is in a list of 11 million passwords",
                      help="Check if the given password is in a list of 11 million passwords")
    async def pwdcheck(self, ctx, *, password):
        """
        Idea by discord user NoPe / The founder of TeamSDS | https://teamsds.net/
        Password List: https://github.com/danielmiessler/SecLists/blob/master/Passwords/Common-Credentials/10-million-password-list-top-1000000.txt
        """
        loading_message = await ctx.send(embed=self.please_wait_emb)

        try:
            if password + "\n" in self.lines:
                embed = discord.Embed(
                    title="Password Checker!", color=getembed.Common.COLOR)
                embed.set_author(name=getembed.Common.AUTHOR,
                                 icon_url=getembed.Common.AUTHOR_LINK)
                embed.set_thumbnail(
                    url="https://media.discordapp.net/attachments/877796755234783273/881072664658214912/change-password.png?width=479&height=464")
                embed.add_field(name=f"Your Passoword",
                                value=f"{password}", inline=False)
                embed.add_field(
                    name=f"Safety", value=f"Not Safe. This password is in the list of most common 10 million passwords!", inline=False)
                embed.set_footer(text=f"Requested by {ctx.author.name}")
                await loading_message.delete()
                await ctx.send(embed=embed)

            else:
                embed = discord.Embed(
                    title="Password Checker!", color=getembed.Common.COLOR)
                embed.set_author(name=getembed.Common.AUTHOR,
                                 icon_url=getembed.Common.AUTHOR_LINK)
                embed.set_thumbnail(
                    url="https://media.discordapp.net/attachments/877796755234783273/881072664658214912/change-password.png?width=479&height=464")
                embed.add_field(name=f"Your Passoword",
                                value=f"{password}", inline=False)
                embed.add_field(
                    name=f"Safety", value=f"Safe. This password is not in the list of most common 10 million passwords!", inline=False)
                embed.set_footer(text=f"Requested by {ctx.author.name}")
                await loading_message.delete()
                await ctx.send(embed=embed)

        except Exception as e:
            embed2 = discord.Embed(title=getembed.ErrorEmbeds.TITLE,
                                   description=getembed.ErrorEmbeds.DESCRIPTION, color=getembed.ErrorEmbeds.COLOR)
            embed2.set_author(name=getembed.Common.AUTHOR,
                              icon_url=getembed.Common.AUTHOR_LINK)
            embed2.set_thumbnail(url=getembed.ErrorEmbeds.THUMBNAIL)
            embed2.add_field(name="Error:", value=f"{e}", inline=False)
            embed2.set_footer(text=f"Requested by {ctx.author.name}")
            await loading_message.delete()
            await ctx.send(embed=embed2)

    @commands.command(aliases=["passowrd-strength-check", "pwdstrengthcheck", "pwdsc"],
                      breif="Password Strength Check",
                      description="Check if the given password is strong enough. If the strength is above `0.5`, its safe and its the most minimum recommended.",
                      help="Check if the given password is strong enough. If the strength is above `0.5`, its safe and its the most minimum recommended.")
    async def passwordstrentghcheck(self, ctx, *, passowrdhere):
        loading_message = await ctx.send(embed=self.please_wait_emb)
        """
        I tried to create something like the discord bot named 'Pencord' by Markiemm had created
        Later, he gave me the code + stuff used to get it done
        But i sticked to my own
        """
        try:
            stats = PasswordStats(f'{passowrdhere}')
            embed = discord.Embed(
                title="Password Strength Checker", color=getembed.Common.COLOR)
            embed.add_field(name="Strenth:",
                            value=f"{stats.strength()}", inline=False)
            embed.set_footer(text=f"Requested by {ctx.author.name}")
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

    @commands.command(breif="Shorten any link - tinyurl",
                      description="Shorten any given URL easily with tinyurl for a quick memmorable link!",
                      help="Shorten any given URL easily with tinyurl for a quick memmorable link!")
    async def tinyurl(self, ctx, *, link):
        loading_message = await ctx.send(embed=self.please_wait_emb)

        try:
            # Using the public API of TinyURL
            r = requests.get(
                f'http://tinyurl.com/api-create.php?url={link}').text

            em = discord.Embed(color=getembed.Common.COLOR)
            em.set_footer(text=f"Requested by {ctx.author.name}")
            em.set_author(name=getembed.Common.AUTHOR,
                          icon_url=getembed.Common.AUTHOR_LINK)
            em.add_field(name="Shortened Link", value=r, inline=False)
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

    @commands.command(breif="Random Discord Nitro Codes",
                      description="All these codes are randomly generated and most of them will not work! if you are lucky, maybe you will get a chance!",
                      help="All these codes are randomly generated and most of them will not work! if you are lucky, maybe you will get a chance!")
    async def nitro(self, ctx, *, number_of_times):
        loading_message = await ctx.send(embed=self.please_wait_emb)

        try:
            # The limit is 20 to prevent spam
            if int(number_of_times) <= 20:
                embed = discord.Embed(
                    title="Nitro Code Generator", color=getembed.Common.COLOR)
                embed.set_author(name=getembed.Common.AUTHOR,
                                 icon_url=getembed.Common.AUTHOR_LINK)
                embed.set_thumbnail(
                    url="https://user-images.githubusercontent.com/36286877/127767330-d3e68d90-67a0-4672-b3e1-6193b323bc21.png")
                embed.add_field(name="You have Requested:",
                                value=f"{number_of_times} Nitro Codes", inline=False)
                embed.set_footer(text=f"Requested by {ctx.author.name}")
                await loading_message.delete()
                await ctx.send(embed=embed)

                for iteration, x in enumerate(range(int(number_of_times))):
                    code = ''.join(randomchoices(ascii_letters + digits, k=16))
                    await ctx.send(f'https://discord.gift/{code}')
                    await asyncio.sleep(0.6)

            else:
                embed = discord.Embed(
                    title="Nitro Code Generator", color=getembed.Common.COLOR)
                embed.set_author(name=getembed.Common.AUTHOR,
                                 icon_url=getembed.Common.AUTHOR_LINK)
                embed.set_thumbnail(
                    url="https://www.nicepng.com/png/detail/214-2146883_4-fake-stamp-vector-fake-news-logo-png.png")
                embed.add_field(
                    name="Error", value="Please enter a value below 20; This is done to prevent spam!", inline=True)
                embed.set_footer(text=f"Requested by {ctx.author.name}")
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

    @commands.command(breif="Password Checker",
                      description="This command will send you very useful information about your password",
                      help="This command will send you very useful information about your password")
    async def passwordc(self, ctx, *, password):
        loading_message = await ctx.send(embed=self.please_wait_emb)

        try:
            results = zxcvbn('hirusha')
            embed3 = discord.Embed(title=getembed.ErrorEmbeds.TITLE,
                                   description=getembed.ErrorEmbeds.DESCRIPTION, color=getembed.ErrorEmbeds.COLOR)
            embed3.set_author(name=getembed.Common.AUTHOR,
                              icon_url=getembed.Common.AUTHOR_LINK)
            embed3.set_thumbnail(url=getembed.ErrorEmbeds.THUMBNAIL)

            embed3.add_field(
                name="Password", value=f"{password}", inline=False)
            embed3.add_field(
                name="Guesses", value=f"Decimal: {results['guesses']}\nLog 10: {results['guesses_log10']}", inline=False)

            pat = ""
            for seq in results['sequence']:
                pat += f"\n-------\nPattern: {seq['pattern']}\ni: {seq['i']}\nj: {seq['j']}\nToken: {seq['token']}\nMatched Word: {seq['matched_word']}\nRank: {seq['rank']}\nDictionary Name: {seq['dictionary_name']}\nReversed: {seq['reversed']}\nl33t: {seq['l33t']}\nBase Guesses: {seq['base_guesses']}\nUppercase Variations: {seq['uppercase_variations']}\nl33t Variations: {seq['l33t_variations']}\nGuesses: {seq['guesses']}\nGuesses Log10: {seq['guesses_log10']}"

            embed3.add_field(name="Pattern: ", value=f"{pat}", inline=False)
            embed3.add_field(name="Calculate Time: ",
                             value=f"{results['calc_time']}", inline=False)
            embed3.add_field(name="Crack Time Seconds: ",
                             value=f"Online Throttling 100 Per Hour: {results['crack_times_seconds']['online_throttling_100_per_hour']}\nOnline no Throttling 10 Per Second: {results['crack_times_seconds']['online_no_throttling_10_per_second']}\nOffline Slow Hashing 1e4 Per Second: {results['crack_times_seconds']['offline_slow_hashing_1e4_per_second']}\nOffline Fast Hashing 1e10 Per Second: {results['crack_times_seconds']['offline_fast_hashing_1e10_per_second']}", inline=False)
            embed3.add_field(name="Crack Times Display: ",
                             value=f"Online Throttling 100 Per Hour: {results['crack_times_display']['online_throttling_100_per_hour']}\nOnline No Throttling 10 Per Second: {results['crack_times_display']['online_no_throttling_10_per_second']}\nOffline Slow Hashing 1e4 Per Second: {results['crack_times_display']['offline_slow_hashing_1e4_per_second']}\nOffline Fast Hashing 1e10 Per Second: {results['crack_times_display']['offline_fast_hashing_1e10_per_second']}", inline=False)
            embed3.add_field(
                name="Score: ", value=f"{results['score']}", inline=False)

            fdb = ""
            for feedbsug in results['feedback']['suggestions']:
                fdb += f"{feedbsug}\n"

            embed3.add_field(
                name="Feedback: ", value=f"{results['feedback']['warning']}\n{fdb}", inline=False)

            embed3.set_footer(text=f"Requested by {ctx.author.name}")
            await loading_message.delete()
            await ctx.send(embed=embed3)

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

    @commands.command(breif="Create a hastebin",
                      description="Create a hastebin without any limitation (except for the message length given by discord) without leaving discord! this command will send you the link of the hastebin.",
                      help="Create a hastebin without any limitation (except for the message length given by discord) without leaving discord! this command will send you the link of the hastebin.")
    async def hastebin(self, ctx, *, message):
        loading_message = await ctx.send(embed=self.please_wait_emb)

        try:
            r = requests.post(
                "https://hastebin.com/documents", data=message).json()

            try:
                embed = discord.Embed(
                    title="Hastebin", color=getembed.Common.COLOR)
                embed.set_author(name=getembed.Common.AUTHOR,
                                 icon_url=getembed.Common.AUTHOR_LINK)
                embed.set_thumbnail(
                    url="https://cdn.discordapp.com/attachments/877796755234783273/879586340520480768/large.png")
                embed.add_field(
                    name="Link", value=f"https://hastebin.com/{r['key']}", inline=False)
                embed.add_field(
                    name=f"Text by {ctx.author.name}", value=f"{message}", inline=False)
                embed.set_footer(text=f"Requested by {ctx.author.name}")
                await loading_message.delete()
                await ctx.send(embed=embed)

            except:
                embed = discord.Embed(
                    title="Hastebin", color=getembed.Common.COLOR)
                embed.set_author(name=getembed.Common.AUTHOR,
                                 icon_url=getembed.Common.AUTHOR_LINK)
                embed.set_thumbnail(
                    url="https://cdn.discordapp.com/attachments/877796755234783273/879586340520480768/large.png")
                embed.add_field(
                    name="Link", value=f"https://hastebin.com/{r['key']}", inline=False)
                embed.set_footer(text=f"Requested by {ctx.author.name}")
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

    @commands.command(breif="ASCII Art v1",
                      description="Create an ASCII banner / art easily. `text` is what you want the banner to be.",
                      help="Create an ASCII banner / art easily. `text` is what you want the banner to be.")
    async def asciiart(self, ctx, *, text):
        loading_message = await ctx.send(embed=self.please_wait_emb)

        try:
            r = requests.get(
                f'http://artii.herokuapp.com/make?text={urllib.parse.quote_plus(text)}').text

            # IF ITS MORE THAN 2000, it will send an error, the if statement is to stop it
            if len('```'+r+'```') > 2000:
                embed = discord.Embed(
                    title="ASCII ART", description="There was a problem!", color=getembed.Common.COLOR)
                embed.set_author(name=getembed.Common.AUTHOR,
                                 icon_url=getembed.Common.AUTHOR_LINK)
                embed.set_thumbnail(url=getembed.ErrorEmbeds.THUMBNAIL)
                embed.add_field(
                    name="Error:", value="The message has over 2000 characters", inline=False)
                embed.add_field(name="Possible fix:",
                                value="Enter something short", inline=True)
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
            embed3 = discord.Embed(title=getembed.ErrorEmbeds.TITLE,
                                   description=getembed.ErrorEmbeds.DESCRIPTION, color=getembed.ErrorEmbeds.COLOR)
            embed3.set_author(name=getembed.Common.AUTHOR,
                              icon_url=getembed.Common.AUTHOR_LINK)
            embed3.set_thumbnail(url=getembed.ErrorEmbeds.THUMBNAIL)
            embed3.add_field(name="Error:", value=f"{e}", inline=False)
            embed3.set_footer(text=f"Requested by {ctx.author.name}")
            await loading_message.delete()
            await ctx.send(embed=embed3)

    @commands.command(breif="Reverse Text",
                      description="Reverse any given word or a sentence easily with this command!",
                      help="Reverse any given word or a sentence easily with this command!")
    async def reverse(self, ctx, *, message):
        loading_message = await ctx.send(embed=self.please_wait_emb)
        try:
            message = message[::-1]

            embed = discord.Embed(title="Reverse Text!",
                                  color=getembed.Common.COLOR)
            embed.set_author(name=getembed.Common.AUTHOR,
                             icon_url=getembed.Common.AUTHOR_LINK)
            embed.set_thumbnail(
                url="https://cdn.discordapp.com/attachments/877796755234783273/879728497822687272/reverse.png")
            embed.add_field(name="Reversed", value="{message}", inline=False)
            embed.set_footer(text="Requested by {ctx.author.name}")
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

    @commands.command(aliases=["e_base64"],
                      breif="to Base64",
                      description="Encode any given text to Base64",
                      help="Encode any given text to Base64")
    async def e_b64(self, ctx, *, args):
        loading_message = await ctx.send(embed=self.please_wait_emb)

        try:
            msg = base64.b64encode('{}'.format(args).encode('ascii'))
            enc = str(msg)
            enc = enc[2:len(enc)-1]

            embed = discord.Embed(
                title="to Base64", color=getembed.Common.COLOR)
            embed.set_author(name=getembed.Common.AUTHOR,
                             icon_url=getembed.Common.AUTHOR_LINK)
            embed.set_thumbnail(
                url="https://cdn.discordapp.com/attachments/877796755234783273/879955815602200586/base64-logo-352x200.jpg")
            embed.add_field(name="Query", value=f"{args}", inline=False)
            embed.add_field(name="Result", value=f"{enc}", inline=True)
            embed.set_footer(text=f"Requested by {ctx.author.name}")
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

    @commands.command(
        breif="to MD5",
        description="any given text to Base64",
        help="any given text to Base64")
    async def e_md5(self, ctx, *, args):
        loading_message = await ctx.send(embed=self.please_wait_emb)

        try:
            msg = hashlib.md5(args.encode())
            slpake = msg.hexdigest()

            embed = discord.Embed(title="to MD5", color=getembed.Common.COLOR)
            embed.set_author(name=getembed.Common.AUTHOR,
                             icon_url=getembed.Common.AUTHOR_LINK)
            embed.set_thumbnail(
                url="https://cdn.discordapp.com/attachments/877796755234783273/879956672771137546/MD5.png")
            embed.add_field(name="Query", value=f"{args}", inline=False)
            embed.add_field(name="Result", value=f"{slpake}", inline=True)
            embed.set_footer(text=f"Requested by {ctx.author.name}")
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

    @commands.command(
        breif="to SHA1",
        description="any given text to SHA1",
        help="any given text to SHA1")
    async def e_sha1(self, ctx, *, args):
        loading_message = await ctx.send(embed=self.please_wait_emb)

        try:
            msg = hashlib.sha1(args.encode())
            slpuka = msg.hexdigest()

            embed = discord.Embed(title="to SHA1", color=getembed.Common.COLOR)
            embed.set_author(name=getembed.Common.AUTHOR,
                             icon_url=getembed.Common.AUTHOR_LINK)
            embed.set_thumbnail(
                url="https://cdn.discordapp.com/attachments/877796755234783273/879957622546108436/SHA1.png")
            embed.add_field(name="Query", value=f"{args}", inline=False)
            embed.add_field(name="Result", value=f"{slpuka}", inline=True)
            embed.set_footer(text=f"Requested by {ctx.author.name}")
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

    @commands.command(
        breif="to SHA224",
        description="any given text to SHA224",
        help="any given text to SHA224")
    async def e_sha224(self, ctx, *, args):
        loading_message = await ctx.send(embed=self.please_wait_emb)

        try:
            msg = hashlib.sha3_224(args.encode())
            crnja = msg.hexdigest()

            embed = discord.Embed(
                title="to SHA224", color=getembed.Common.COLOR)
            embed.set_author(name=getembed.Common.AUTHOR,
                             icon_url=getembed.Common.AUTHOR_LINK)
            embed.set_thumbnail(
                url="https://cdn.discordapp.com/attachments/877796755234783273/879958751640191046/download.png")
            embed.add_field(name="Query", value=f"{args}", inline=False)
            embed.add_field(name="Result", value=f"{crnja}", inline=True)
            embed.set_footer(text=f"Requested by {ctx.author.name}")
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

    @commands.command(
        breif="to SHA512",
        description="any given text to SHA512",
        help="any given text to SHA512")
    async def e_sha512(self, ctx, *, args):
        loading_message = await ctx.send(embed=self.please_wait_emb)

        try:
            msg = hashlib.sha3_512(args.encode())
            crnja = msg.hexdigest()

            embed = discord.Embed(
                title="to SHA512", color=getembed.Common.COLOR)
            embed.set_author(name=getembed.Common.AUTHOR,
                             icon_url=getembed.Common.AUTHOR_LINK)
            embed.set_thumbnail(
                url="https://cdn.discordapp.com/attachments/877796755234783273/879960296863698944/download_1.png")
            embed.add_field(name="Query", value=f"{args}", inline=False)
            embed.add_field(name="Result", value=f"{crnja}", inline=True)
            embed.set_footer(text=f"Requested by {ctx.author.name}")
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

    @commands.command(aliases=["leet", "l33t"],
                      breif="to L33T",
                      description="any given text to L33T",
                      help="any given text to L33T")
    async def e_leet(self, ctx, *, args):
        loading_message = await ctx.send(embed=self.please_wait_emb)

        try:
            encoded = args.replace('e', '3').replace('a', '4').replace('i', '!').replace('u', '|_|').replace('U', '|_|').replace('E', '3').replace('I', '!').replace('A', '4').replace('o', '0').replace(
                'O', '0').replace('t', '7').replace('T', '7').replace('l', '1').replace('L', '1').replace('k', '|<').replace('K', '|<').replace('CK', 'X').replace('ck', 'x').replace('Ck', 'X').replace('cK', 'x')

            embed = discord.Embed(title="to LEET", color=getembed.Common.COLOR)
            embed.set_author(name=getembed.Common.AUTHOR,
                             icon_url=getembed.Common.AUTHOR_LINK)
            embed.set_thumbnail(
                url="https://cdn.discordapp.com/attachments/877796755234783273/879961162895212574/download_2.png")
            embed.add_field(name="Query", value=f"{args}", inline=False)
            embed.add_field(name="Result", value=f"{encoded}", inline=True)
            embed.set_footer(text=f"Requested by {ctx.author.name}")
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

    @commands.command(aliases=["to-binary", "e_binary"],
                      breif="to Binary",
                      description="any given text to Binary",
                      help="any given text to Binary")
    async def binary(self, ctx, *, ToBinaryText):
        loading_message = await ctx.send(embed=self.please_wait_emb)
        try:
            r = requests.get(
                'https://some-random-api.ml/binary?text=' + ToBinaryText)
            c = r.json()
            fact = c["binary"]

            embed = discord.Embed(
                title="to Binary", color=getembed.Common.COLOR)
            embed.set_author(name=getembed.Common.AUTHOR,
                             icon_url=getembed.Common.AUTHOR_LINK)
            embed.set_thumbnail(
                url="https://cdn.discordapp.com/attachments/877796755234783273/880025172055314462/85-855085_binary-codes-on-data-sheet-with-magnifying-lens.png")
            embed.add_field(
                name="Query", value=f"{ToBinaryText}", inline=False)
            embed.add_field(name="Result", value=f"{fact}", inline=True)
            embed.set_footer(text=f"Requested by {ctx.author.name}")
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

    @commands.command(aliases=["e_cipher"],
                      breif="to Ceaser Cipher",
                      description="any given text to Ceaser Cipher",
                      help="any given text to Ceaser Cipher")
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

            embed = discord.Embed(title="to Ceaser Cipher",
                                  color=getembed.Common.COLOR)
            embed.set_author(name=getembed.Common.AUTHOR,
                             icon_url=getembed.Common.AUTHOR_LINK)
            embed.set_thumbnail(
                url="https://cdn.discordapp.com/attachments/877796755234783273/880025172055314462/85-855085_binary-codes-on-data-sheet-with-magnifying-lens.png")
            embed.add_field(
                name="Query", value=f"{ToCeaserCipher}", inline=False)
            embed.add_field(name="Result", value=f"{cipher}", inline=True)
            embed.set_footer(text=f"Requested by {ctx.author.name}")
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

    @commands.command(aliases=["d_cipher"],
                      breif="from Ceaser Cipher",
                      description="from Ceaser Cipher | DECODE",
                      help="from Ceaser Cipher | DEOCDE")
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

            embed = discord.Embed(title="from Ceaser Cipher",
                                  color=getembed.Common.COLOR)
            embed.set_author(name=getembed.Common.AUTHOR,
                             icon_url=getembed.Common.AUTHOR_LINK)
            embed.set_thumbnail(
                url="https://cdn.discordapp.com/attachments/877796755234783273/880025172055314462/85-855085_binary-codes-on-data-sheet-with-magnifying-lens.png")
            embed.add_field(
                name="Query", value=f"{ToCeaserCipher}", inline=False)
            embed.add_field(name="Result", value=f"{cipher}", inline=True)
            embed.set_footer(text=f"Requested by {ctx.author.name}")
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

    @commands.command(aliases=["b2t", "d_binary", "decode_binary"],
                      breif="from Binary",
                      description="from Binary",
                      help="from Binary")
    async def b_2txt(self, ctx, *, ToTextBinary):
        loading_message = await ctx.send(embed=self.please_wait_emb)

        try:
            r = requests.get(
                'https://some-random-api.ml/binary?decode=' + ToTextBinary)
            c = r.json()
            fact = c["text"]

            embed = discord.Embed(title="From Binary",
                                  color=getembed.Common.COLOR)
            embed.set_author(name=getembed.Common.AUTHOR,
                             icon_url=getembed.Common.AUTHOR_LINK)
            embed.set_thumbnail(
                url="https://cdn.discordapp.com/attachments/877796755234783273/880025172055314462/85-855085_binary-codes-on-data-sheet-with-magnifying-lens.png")
            embed.add_field(
                name="Query", value=f"{ToTextBinary}", inline=False)
            embed.add_field(name="Result", value=f"{fact}", inline=True)
            embed.set_footer(text=f"Requested by {ctx.author.name}")
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

    @commands.command(aliases=["b642t", "d_b64", "d_base64"],
                      breif="from Base64",
                      description="from Base64",
                      help="from Base64")
    async def b64_2txt(self, ctx, *, ToTextBase64):
        loading_message = await ctx.send(embed=self.please_wait_emb)

        try:
            r = requests.get(
                'https://some-random-api.ml/base64?decode=' + ToTextBase64)
            c = r.json()
            fact = c["text"]

            embed = discord.Embed(title="From Base64",
                                  color=getembed.Common.COLOR)
            embed.set_author(name=getembed.Common.AUTHOR,
                             icon_url=getembed.Common.AUTHOR_LINK)
            embed.set_thumbnail(
                url="https://cdn.discordapp.com/attachments/877796755234783273/879955815602200586/base64-logo-352x200.jpg")
            embed.add_field(
                name="Query", value=f"{ToTextBase64}", inline=False)
            embed.add_field(name="Result", value=f"{fact}", inline=True)
            embed.set_footer(text=f"Requested by {ctx.author.name}")
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

    @commands.command(breif="Shorten any link - cleanuri",
                      description="Shorten any given URL easily with cleanuri for a quick memmorable link!",
                      help="Shorten any given URL easily with cleanuri for a quick memmorable link!")
    async def cleanuri(self, ctx, *, websiteurl):
        loading_message = await ctx.send(embed=self.please_wait_emb)

        try:
            url = 'https://cleanuri.com/api/v1/shorten'
            myobj = {'url': f'{websiteurl}'}
            r = requests.post(url, data=myobj).json()
            shorten_url = r['result_url']

            embed = discord.Embed(title="URL Shortener",
                                  color=getembed.Common.COLOR)
            embed.set_author(name=getembed.Common.AUTHOR,
                             icon_url=getembed.Common.AUTHOR_LINK)
            embed.set_thumbnail(
                url="https://cdn.discordapp.com/attachments/877796755234783273/880028609924976690/828161_url_512x512.png")
            embed.add_field(name="Original Link",
                            value=f"{websiteurl}", inline=False)
            embed.add_field(name="Shortened Link",
                            value=f"{shorten_url}", inline=False)
            embed.set_footer(text=f"Requested by {ctx.author.name}")
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

    @commands.command(aliases=["generate-pwd", "gen-pwd", "generate-password", "gen-password", "newpassword", "password", "newpass", "passwordnew"],
                      breif="Generate a password",
                      description="Generate a secure password with a max length of 40 characters.",
                      help="Generate a secure password with a max length of 40 characters.")
    async def genpwd(self, ctx, *, numberofcharacters: int = 16):
        loading_message = await ctx.send(embed=self.please_wait_emb)

        try:
            pwd_lenlis = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20,
                          21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40)
            try:
                numberofcharsinint = int(numberofcharacters)

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
                return

            if numberofcharsinint in pwd_lenlis:
                url = f"https://passwordinator.herokuapp.com/generate?num=true&char=true&caps=true&len={numberofcharacters}"
                r = requests.get(url)
                c = r.json()

                embed = discord.Embed(
                    title="Password Generator", color=getembed.Common.COLOR)
                embed.set_author(name=getembed.Common.AUTHOR,
                                 icon_url=getembed.Common.AUTHOR_LINK)
                embed.set_thumbnail(
                    url="https://cdn.discordapp.com/attachments/877796755234783273/880031728369016832/704187.png")
                embed.add_field(name="Password Length",
                                value=f"{numberofcharacters}", inline=False)
                embed.add_field(name="Password",
                                value=f"{c['data']}", inline=False)
                embed.set_footer(text=f"Requested by {ctx.author.name}")
                await loading_message.delete()
                await ctx.send(embed=embed)

            else:
                embed = discord.Embed(
                    title="Password Generator", description="An Error has occured!", color=getembed.Common.COLOR)
                embed.set_author(name=getembed.Common.AUTHOR,
                                 icon_url=getembed.Common.AUTHOR_LINK)
                embed.set_thumbnail(
                    url="https://cdn.discordapp.com/attachments/877796755234783273/880031728369016832/704187.png")
                embed.add_field(
                    name="Error", value="The value of the number is high", inline=False)
                embed.add_field(name="Possible Fix",
                                value="Enter a value below 40", inline=False)
                embed.set_footer(text=f"Requested by {ctx.author.name}")
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

    @commands.command(aliases=["clearscreennodelete", "clear-screen-no-delete", "clearscreen"],
                      breif="Get some Screen Space",
                      description="Get some Screen Space",
                      help="Get some Screen Space")
    async def csnd(self, ctx):
        await ctx.send(f'Clearing some screen space - \n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\nRequested by {ctx.author.mention}')

    @commands.command(breif="profile picture of any instagram profile",
                      description="profile picture of any instagram profile. `ig_uname` should be the username of the user as in instagram!",
                      help="profile picture of any instagram profile. `ig_uname` should be the username of the user as in instagram!")
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
            embed = discord.Embed(title="Instagram Profile Picture",
                                  description=f"of {ig_uname}", color=getembed.Common.COLOR)
            embed.set_author(name=getembed.Common.AUTHOR,
                             icon_url=getembed.Common.AUTHOR_LINK)
            embed.add_field(
                name="Link", value=f"https://instagram.com/{ig_uname}", inline=False)
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

    @commands.command(breif="a simple poll",
                      description="Create a simple poll for people to vote on",
                      help="Create a simple poll for people to vote on")
    async def poll(self, ctx, *, message):
        loading_message = await ctx.send(embed=self.please_wait_emb)

        try:
            emb = discord.Embed(
                title=" POLL ", description=f'{message}', color=getembed.Common.COLOR)
            emb.set_author(name=getembed.Common.AUTHOR,
                           icon_url=getembed.Common.AUTHOR_LINK)
            emb.set_footer(text=f"Requested by {ctx.author.name}")
            await loading_message.delete()
            msg = await ctx.send(embed=emb)
            await msg.add_reaction('👍')
            await msg.add_reaction('👎')

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

    @commands.command(breif="Ascii art",
                      description="Create an ascii banner / ascii art without requesting to a public api like the other command which similiar to this",
                      help="Create an ascii banner / ascii art without requesting to a public api like the other command which similiar to this")
    async def ascii(self, ctx, *, text):
        loading_message = await ctx.send(embed=self.please_wait_emb)
        try:
            art = Figlet(font="slant")
            ascii_art_creating_function_get = art.renderText(text)
            await loading_message.delete()
            await ctx.send(f'``` {ascii_art_creating_function_get} ```')

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

    @commands.command(breif="Google seach link",
                      description="Recieve a direct google search link easily!",
                      help="Recieve a direct google search link easily!")
    async def google(self, ctx, *, whatToSearch):
        loading_message = await ctx.send(embed=self.please_wait_emb)

        try:
            embed = discord.Embed(
                title="Google Search", description="Link to query", color=getembed.Common.COLOR)
            embed.set_author(name=getembed.Common.AUTHOR,
                             icon_url=getembed.Common.AUTHOR_LINK)
            embed.set_thumbnail(
                url="https://cdn.discordapp.com/attachments/877796755234783273/880664487965900821/Google__G__Logo.svg.png")
            embed.add_field(
                name="Link", value=f"https://www.google.com/search?q={whatToSearch}", inline=True)
            embed.set_footer(text=f"Requested by {ctx.author.name}")
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

    @commands.command(aliases=["count-words", "countwords", "wordcount"],
                      breif="Word count",
                      description="Count the number of words in a given sentence. (each word is seperated by a SPACE)",
                      help="Count the number of words in a given sentence. (each word is seperated by a SPACE)")
    async def count(self, ctx, *, words):
        loading_message = await ctx.send(embed=self.please_wait_emb)
        try:
            spl = words.split(" ")
            no = len(spl)
            embed = discord.Embed(title="Word Counter",
                                  color=getembed.Common.COLOR)
            embed.add_field(name="Number of Words:", value=f"{no}")
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

    @commands.command(
        breif="Public Profiles",
        description="Sends a list of all possible social platforms in which an account exist with the given username ( `usernametofind` ). NOT ALL LINKS WORK!",
        help="Sends a list of all possible social platforms in which an account exist with the given username ( `usernametofind` ). NOT ALL LINKS WORK!")
    async def sherlock(self, ctx, *, usernametofind):
        # https://github.com/sherlock-project/sherlock

        # OLD, ORIGINAL CODE, WORKING AS INTENDED, VERY BUGGY, BOT WONT WORK WHILE THIS COMMAND IS RUNNING!
        # lading_sherlock_stay = discord.Embed(title="```  Processing - This may take longer than usual.  ```", color=getembed.Common.COLOR)
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
            embed1 = discord.Embed(
                title="Sherlock!", color=getembed.Common.COLOR)
            embed1.set_thumbnail(
                url="https://user-images.githubusercontent.com/27065646/53551960-ae4dff80-3b3a-11e9-9075-cef786c69364.png")
            embed1.add_field(name="All Possible Profiles!",
                             value=all_possible_accounts_1, inline=False)
            embed1.set_footer(
                text="All links won't work! We will add a check real soon!")

            embed2 = discord.Embed(title="Sherlock! - 2",
                                   color=getembed.Common.COLOR)
            embed2.set_thumbnail(
                url="https://user-images.githubusercontent.com/27065646/53551960-ae4dff80-3b3a-11e9-9075-cef786c69364.png")
            embed2.add_field(name="All Possible Profiles!",
                             value=all_possible_accounts_2, inline=False)
            embed2.set_footer(text="All links won't work! Part 2")

            embed3 = discord.Embed(title="Sherlock! - 3",
                                   color=getembed.Common.COLOR)
            embed3.set_thumbnail(
                url="https://user-images.githubusercontent.com/27065646/53551960-ae4dff80-3b3a-11e9-9075-cef786c69364.png")
            embed3.add_field(name="All Possible Profiles!",
                             value=all_possible_accounts_3, inline=False)
            embed3.set_footer(text="All links won't work! Part 3")

            embed4 = discord.Embed(title="Sherlock! - 4",
                                   color=getembed.Common.COLOR)
            embed4.set_thumbnail(
                url="https://user-images.githubusercontent.com/27065646/53551960-ae4dff80-3b3a-11e9-9075-cef786c69364.png")
            embed4.add_field(name="All Possible Profiles!",
                             value=all_possible_accounts_4, inline=False)
            embed4.set_footer(text="All links won't work! Part 4")

            embed5 = discord.Embed(title="Sherlock! - 5",
                                   color=getembed.Common.COLOR)
            embed5.set_thumbnail(
                url="https://user-images.githubusercontent.com/27065646/53551960-ae4dff80-3b3a-11e9-9075-cef786c69364.png")
            embed5.add_field(name="All Possible Profiles!",
                             value=all_possible_accounts_5, inline=False)
            embed5.set_footer(text="All links won't work! Part 5")

            embed6 = discord.Embed(title="Sherlock! - 6",
                                   color=getembed.Common.COLOR)
            embed6.set_thumbnail(
                url="https://user-images.githubusercontent.com/27065646/53551960-ae4dff80-3b3a-11e9-9075-cef786c69364.png")
            embed6.add_field(name="All Possible Profiles!",
                             value=all_possible_accounts_6, inline=False)
            embed6.set_footer(text="All links won't work! Part 6")

            embed7 = discord.Embed(title="Sherlock! - 7",
                                   color=getembed.Common.COLOR)
            embed7.set_thumbnail(
                url="https://user-images.githubusercontent.com/27065646/53551960-ae4dff80-3b3a-11e9-9075-cef786c69364.png")
            embed7.add_field(name="All Possible Profiles!",
                             value=all_possible_accounts_7, inline=False)
            embed7.set_footer(text="All links won't work! Part 7")

            embed8 = discord.Embed(title="Sherlock! - 8",
                                   color=getembed.Common.COLOR)
            embed8.set_thumbnail(
                url="https://user-images.githubusercontent.com/27065646/53551960-ae4dff80-3b3a-11e9-9075-cef786c69364.png")
            embed8.add_field(name="All Possible Profiles!",
                             value=all_possible_accounts_8, inline=False)
            embed8.set_footer(text="All links won't work! Part 8")

            embed9 = discord.Embed(title="Sherlock! - 9",
                                   color=getembed.Common.COLOR)
            embed9.set_thumbnail(
                url="https://user-images.githubusercontent.com/27065646/53551960-ae4dff80-3b3a-11e9-9075-cef786c69364.png")
            embed9.add_field(name="All Possible Profiles!",
                             value=all_possible_accounts_9, inline=False)
            embed9.set_footer(text="All links won't work! Part 9")

            embed10 = discord.Embed(
                title="Sherlock! - 10", color=getembed.Common.COLOR)
            embed10.set_thumbnail(
                url="https://user-images.githubusercontent.com/27065646/53551960-ae4dff80-3b3a-11e9-9075-cef786c69364.png")
            embed10.add_field(name="All Possible Profiles!",
                              value=all_possible_accounts_10, inline=False)
            embed10.set_footer(text="All links won't work! Part 10")

            embed11 = discord.Embed(
                title="Sherlock! - 11", color=getembed.Common.COLOR)
            embed11.set_thumbnail(
                url="https://user-images.githubusercontent.com/27065646/53551960-ae4dff80-3b3a-11e9-9075-cef786c69364.png")
            embed11.add_field(name="All Possible Profiles!",
                              value=all_possible_accounts_11, inline=False)
            embed11.set_footer(text="All links won't work! Part 11")

            embed12 = discord.Embed(
                title="Sherlock! - 12", color=getembed.Common.COLOR)
            embed12.set_thumbnail(
                url="https://user-images.githubusercontent.com/27065646/53551960-ae4dff80-3b3a-11e9-9075-cef786c69364.png")
            embed12.add_field(name="All Possible Profiles!",
                              value=all_possible_accounts_12, inline=False)
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
            embed3 = discord.Embed(title=getembed.ErrorEmbeds.TITLE,
                                   description=getembed.ErrorEmbeds.DESCRIPTION, color=getembed.ErrorEmbeds.COLOR)
            embed3.set_author(name=getembed.Common.AUTHOR,
                              icon_url=getembed.Common.AUTHOR_LINK)
            embed3.set_thumbnail(url=getembed.ErrorEmbeds.THUMBNAIL)
            embed3.add_field(name="Error:", value=f"{e}", inline=False)
            embed3.set_footer(text=f"Requested by {ctx.author.name}")
            await loading_message.delete()
            await ctx.send(embed=embed3)

    @commands.command(aliases=["download-audio", "ytd", "youtubedownload"],
                      breif="Public Profiles",
                      description="Sends a list of all possible social platforms in which an account exist with the given username ( `usernametofind` ). NOT ALL LINKS WORK!",
                      help="Sends a list of all possible social platforms in which an account exist with the given username ( `usernametofind` ). NOT ALL LINKS WORK!")
    async def audio(self, ctx, *, ytvlink):
        DOWNLOAD_QUALITY = "320kbps"
        loading_message = await ctx.send(embed=self.please_wait_emb)
        try:
            if ytvlink.lower().startswith('http') or ytvlink.lower().startswith('https'):
                ytvlink_link = True
                ytvlink = ytvlink

            else:
                ytvlink_link = False
                videosSearch = VideosSearch(f'{ytvlink}', limit=1)
                mainresult = videosSearch.result()["result"]
                video_index = mainresult[0]
                ytvlink = video_index["link"]

            try:
                # Inititalizing the video
                try:
                    yt = YouTube(ytvlink)
                except Exception as e:
                    embed = discord.Embed(
                        title="An error has occured!", color=getembed.Common.COLOR)
                    embed.add_field(
                        name="Error:", value=f"Unable to access the video!", inline=False)
                    embed.set_author(name=getembed.Common.AUTHOR,
                                     icon_url=getembed.Common.AUTHOR_LINK)
                    embed.set_footer(text=f"Requested by {ctx.author.name}")
                    await loading_message.delete()
                    await ctx.send(embed=embed)
                    return

                # Downloading the video
                try:
                    video = yt.streams.filter(only_audio=True).filter(
                        abr=f"{DOWNLOAD_QUALITY}").filter(file_extension="webm").first().download()
                except:
                    try:
                        video = yt.streams.filter(only_audio=True).filter(
                            file_extension="webm").first().download()
                    except Exception as e:
                        embed = discord.Embed(
                            title="An error has occured!", color=getembed.Common.COLOR)
                        embed.add_field(
                            name="Error:", value=f"{e}", inline=False)
                        embed.set_author(
                            name=getembed.Common.AUTHOR, icon_url=getembed.Common.AUTHOR_LINK)
                        embed.set_footer(
                            text=f"Requested by {ctx.author.name}")
                        await loading_message.delete()
                        await ctx.send(embed=embed)
                        return

                # Renaming the video
                try:
                    os.system("mv *.webm audio0001.webm")
                except:
                    try:
                        os.rename("*.webm", "audio0001.webm")
                    except:
                        embed = discord.Embed(
                            title="An error has occured!", color=getembed.Common.COLOR)
                        embed.add_field(
                            name="Error:", value="Unable to rename file", inline=False)
                        embed.set_author(
                            name=getembed.Common.AUTHOR, icon_url=getembed.Common.AUTHOR_LINK)
                        embed.set_footer(
                            text=f"Requested by {ctx.author.name}")
                        try:
                            await loading_message.delete()
                        except:
                            pass
                        await ctx.send(embed=embed)
                        return

                # Converting to mp3
                try:
                    # os.system("ffmpeg -i audio0001.webm audio0001.mp3")
                    # filename_lastpart = "audio0001.mp3"

                    filename_lastpart = "audio0001.webm"
                except:
                    filename_lastpart = "audio0001.webm"

                # Sending the video
                try:
                    with open(f"{filename_lastpart}", "rb") as f:
                        audiof = discord.File(f)
                        try:
                            await loading_message.delete()
                        except:
                            pass
                        await ctx.send(file=audiof)

                except Exception as e:
                    embed = discord.Embed(
                        title="An error has occured!", color=getembed.Common.COLOR)
                    embed.add_field(name="Error:", value=f"{e}", inline=False)
                    embed.set_author(name=getembed.Common.AUTHOR,
                                     icon_url=getembed.Common.AUTHOR_LINK)
                    embed.set_footer(text=f"Requested by {ctx.author.name}")
                    try:
                        await loading_message.delete()
                    except:
                        pass
                    await ctx.send(embed=embed)

            except Exception as e:
                embed = discord.Embed(
                    title="An error has occured!", color=getembed.Common.COLOR)
                embed.add_field(name="Error:", value=f"{e}", inline=False)
                embed.set_author(name=getembed.Common.AUTHOR,
                                 icon_url=getembed.Common.AUTHOR_LINK)
                embed.set_footer(text=f"Requested by {ctx.author.name}")
                try:
                    await loading_message.delete()
                except:
                    pass
                await ctx.send(embed=embed)

        except Exception as e:
            embed = discord.Embed(
                title="An error has occured!", color=getembed.Common.COLOR)
            embed.add_field(name="Error:", value=f"{e}", inline=False)
            embed.set_author(name=getembed.Common.AUTHOR,
                             icon_url=getembed.Common.AUTHOR_LINK)
            embed.set_footer(text=f"Requested by {ctx.author.name}")
            try:
                await loading_message.delete()
            except:
                pass
            await ctx.send(embed=embed)

        finally:
            try:
                os.system("rm audio0001.webm")
            except:
                try:
                    os.system("rm -rf audio0001.webm")
                except Exception as e:
                    embed = discord.Embed(
                        title="An error has occured!", color=getembed.Common.COLOR)
                    embed.add_field(name="Error:", value=f"{e}", inline=False)
                    embed.set_author(name=getembed.Common.AUTHOR,
                                     icon_url=getembed.Common.AUTHOR_LINK)
                    embed.set_footer(text=f"Requested by {ctx.author.name}")
                    try:
                        await loading_message.delete()
                    except:
                        pass
                    await ctx.send(embed=embed)

            # try:
            #     os.system("rm audio0001.mp3")
            # except:
            #     try:
            #         os.system("rm -rf audio0001.mp3")
            #     except Exception as e:
            #         embed=discord.Embed(title="An error has occured!", color=getembed.Common.COLOR)
            #         embed.add_field(name="Error:", value=f"{e}", inline=False)
            #         embed.set_author(name=getembed.Common.AUTHOR, icon_url=getembed.Common.AUTHOR_LINK)
            #         embed.set_footer(text=f"Requested by {ctx.author.name}")
            #         try:
            #             await loading_message.delete()
            #         except:
            #             pass
            #         await ctx.send(embed=embed)

    # THE SAME CODE BUT WITH youtube_dl
    # @commands.command(aliases=["download-audio", "ytd", "youtubedownload"])
    # async def audio(self, ctx, *, ytvlink):
    #     loading_message = await ctx.send(embed=self.please_wait_emb)

    #     try:
    #         if ytvlink.lower().startswith('https://'):
    #             try:
    #                 try:
    #                     options = {
    #                     # 'format': "134",
    #                     'format': 'bestaudio/best',  # choice of quality
    #                     'extractaudio': True,        # only keep the audio
    #                     'audioformat': "mp3",        # convert to mp3
    #                     'outtmpl': '%(id)s',         # name the file the ID of the video
    #                     'noplaylist': True,          # only download single song, not playlist
    #                     'listformats': True,         # print a list of the formats to stdout and exit
    #                     }
    #                     ydl_opts = {'format':'139'} # this is for .m4a - lowest audio quality i guess

    #                     file_extentsion_dlded = "m4a"

    #                     with youtube_dl.YoutubeDL(ydl_opts) as ydl:
    #                         ydl.download([f'{ytvlink}'])

    #                     try:
    #                         os.system(f"mv *.{file_extentsion_dlded} audio1.{file_extentsion_dlded}")
    #                     except:
    #                         try:
    #                             os.system(f"Ren *.{file_extentsion_dlded} audio1.{file_extentsion_dlded}")
    #                         except:
    #                             pass

    #                     try:
    #                         with open(f"audio1.{file_extentsion_dlded}", "rb") as f:
    #                             audiof = discord.File(f)
    #                             await loading_message.delete()
    #                             await ctx.send(file=audiof)
    #                     except Exception as e:
    #                         embed=discord.Embed(title="An error has occured!", color=getembed.Common.COLOR)
    #                         embed.add_field(name="Error:", value=f"{e}", inline=False)
    #                         embed.set_author(name=getembed.Common.AUTHOR, icon_url=getembed.Common.AUTHOR_LINK)
    #                         embed.set_footer(text=f"Requested by {ctx.author.name}")
    #                         await loading_message.delete()
    #                         await ctx.send(embed=embed)

    #                     finally:
    #                         try:
    #                             os.system(f"rm audio1.{file_extentsion_dlded}")
    #                         except Exception as e:
    #                             embed=discord.Embed(title="An error has occured!", color=getembed.Common.COLOR)
    #                             embed.add_field(name="Error:", value=f"{e}", inline=False)
    #                             embed.set_author(name=getembed.Common.AUTHOR, icon_url=getembed.Common.AUTHOR_LINK)
    #                             embed.set_footer(text=f"Requested by {ctx.author.name}")
    #                             try:
    #                                 await loading_message.delete()
    #                             except:
    #                                 pass
    #                             await ctx.send(embed=embed)

    #                 except Exception as e:
    #                     embed=discord.Embed(title="An error has occured!", color=getembed.Common.COLOR)
    #                     embed.add_field(name="Error:", value=f"{e}", inline=False)
    #                     embed.set_author(name=getembed.Common.AUTHOR, icon_url=getembed.Common.AUTHOR_LINK)
    #                     embed.set_footer(text=f"Requested by {ctx.author.name}")
    #                     await loading_message.delete()
    #                     await ctx.send(embed=embed)

    #             except Exception as e:
    #                 embed=discord.Embed(title="An error has occured!", color=getembed.Common.COLOR)
    #                 embed.add_field(name="Error:", value=f"{e}", inline=False)
    #                 embed.set_author(name=getembed.Common.AUTHOR, icon_url=getembed.Common.AUTHOR_LINK)
    #                 embed.set_footer(text=f"Requested by {ctx.author.name}")
    #                 try:
    #                     await loading_message.delete()
    #                 except:
    #                     pass
    #                 await ctx.send(embed=embed)

    #             finally:
    #                 try:
    #                     os.system(f"rm audio1.{file_extentsion_dlded}")
    #                 except Exception as e:
    #                     embed=discord.Embed(title="An error has occured!", color=getembed.Common.COLOR)
    #                     embed.add_field(name="Error:", value=f"{e}", inline=False)
    #                     embed.set_author(name=getembed.Common.AUTHOR, icon_url=getembed.Common.AUTHOR_LINK)
    #                     embed.set_footer(text=f"Requested by {ctx.author.name}")
    #                     try:
    #                         await loading_message.delete()
    #                     except:
    #                         pass
    #                     await ctx.send(embed=embed)

    #         else:
    #             embed=discord.Embed(title="An error has occured!", color=getembed.Common.COLOR)
    #             embed.set_author(name=getembed.Common.AUTHOR, icon_url=getembed.Common.AUTHOR_LINK)
    #             embed.set_footer(text=f"Requested by {ctx.author.name}")
    #             embed.add_field(name="Error:", value=f"Please enter a vliad youtube url!", inline=False)
    #             await ctx.send(embed=embed)

    #     except Exception as e:
    #         embed3=discord.Embed(title=getembed.ErrorEmbeds.TITLE, description=getembed.ErrorEmbeds.DESCRIPTION, color=getembed.ErrorEmbeds.COLOR)
    #         embed3.set_author(name=getembed.Common.AUTHOR, icon_url=getembed.Common.AUTHOR_LINK)
    #         embed3.set_thumbnail(url=getembed.ErrorEmbeds.THUMBNAIL)
    #         embed3.add_field(name="Error:", value=f"{e}", inline=False)
    #         embed3.set_footer(text=f"Requested by {ctx.author.name}")
    #         await loading_message.delete()
    #         await ctx.send(embed=embed3)

    @commands.command(aliases=["sendmail"],
                      breif="Send emails to anyone",
                      description="Sends emails to anyone easily with YourBot Emails Service!",
                      help="Sends emails to anyone easily with YourBot Emails Service!")
    async def sendemail(self, ctx, senderemail, recieveremail, emailsubject="Hey", *, emailcontent="Hello There!"):
        verified_mails = ("gmail.com", "outlook.com", "yahoo.com")
        embed = discord.Embed(
            title="Please Wait", description="``` This may take longer than usual! ```", color=getembed.Common.COLOR)
        embed.set_thumbnail(
            url="https://c.tenor.com/I6kN-6X7nhAAAAAj/loading-buffering.gif")
        embed.set_author(name=getembed.Common.AUTHOR,
                         icon_url=getembed.Common.AUTHOR_LINK)
        embed.set_footer(text="Bot created by ZeaCeR#5641")
        loadingthing = await ctx.send(embed=embed)
        print(
            f"recieved args {emailsubject} | {emailcontent} | {recieveremail} | {senderemail}")

        try:
            if senderemail.split('@')[-1].lower() in verified_mails:
                # print("email is valid")
                try:
                    server = smtplib.SMTP('smtp.gmail.com', 587)
                    server.starttls()
                    # print("created server")

                    try:
                        server.login(self.bot_email_addr,
                                     self.bot_email_password)
                        # print("logged in")

                    except Exception as e:
                        embede = discord.Embed(
                            title="Something was wrong!", description="Your request did not complete due to an error!", color=getembed.Common.COLOR)
                        embede.set_author(
                            name=getembed.Common.AUTHOR, icon_url=getembed.Common.AUTHOR_LINK)
                        embede.set_thumbnail(
                            url="https://cdn.discordapp.com/attachments/877796755234783273/879668020006502440/SeekPng.com_envelope-icon-png_1336118.png")
                        embede.add_field(
                            name="Error", value=f"{e}", inline=False)
                        embede.set_footer(
                            text=f"Requested by {ctx.author.name}")
                        try:
                            await loadingthing.delete()
                        except:
                            pass
                        await ctx.send(embed=embede)
                        # print("unable to login")
                        return

                    email = EmailMessage()
                    # print("writing email")
                    whoasktosend = ctx.author.name
                    whoasktosendid = ctx.author.id
                    emailcontentfinal = f"""This message it being sent from the discord bot named YourBot and was requested by the user {whoasktosend} / {whoasktosendid} / {senderemail}. The message: {emailcontent}   | Thank You. Have a Nice day, Stay safe! - YourBot"""

                    email['From'] = self.bot_email_addr
                    email['To'] = recieveremail
                    email['Subject'] = emailsubject
                    email.set_content(emailcontentfinal)
                    server.send_message(email)
                    # print("email sent")
                    server.close()
                    # print("closed server")

                    try:
                        embed2 = discord.Embed(
                            title="Email Sent", description="Your requested email was sent suceessfully! ", color=getembed.Common.COLOR)
                        embed2.set_author(
                            name=getembed.Common.AUTHOR, icon_url=getembed.Common.AUTHOR_LINK)
                        embed2.set_thumbnail(
                            url="https://cdn.discordapp.com/attachments/877796755234783273/879668020006502440/SeekPng.com_envelope-icon-png_1336118.png")
                        embed2.add_field(
                            name="Your Email Address", value=f"{senderemail}", inline=False)
                        embed2.add_field(
                            name="Receiver Email Address", value=f"{recieveremail}", inline=False)
                        embed2.add_field(name="Email Subject",
                                         value=f"{emailsubject}", inline=False)
                        embed2.add_field(
                            name="Email Content", value=f"{emailcontentfinal}", inline=False)
                        embed2.set_footer(
                            text=f"Requested by {ctx.author.name}")
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
                        # print("sent embed")
                        await ctx.send("Email was sent successfully!")

                except Exception as e:
                    embed3 = discord.Embed(
                        title=getembed.ErrorEmbeds.TITLE, description=getembed.ErrorEmbeds.DESCRIPTION, color=getembed.ErrorEmbeds.COLOR)
                    embed3.set_author(name=getembed.Common.AUTHOR,
                                      icon_url=getembed.Common.AUTHOR_LINK)
                    embed3.set_thumbnail(url=getembed.ErrorEmbeds.THUMBNAIL)
                    embed3.add_field(name="Error:", value=f"{e}", inline=False)
                    embed3.set_footer(text=f"Requested by {ctx.author.name}")
                    try:
                        await loadingthing.delete()
                    except:
                        pass
                    await ctx.send(embed=embed3)
                    print(e)

            else:
                embed = discord.Embed(
                    title="Something was wrong!", description="Your request did not complete due to an error!", color=getembed.Common.COLOR)
                embed.set_author(name=getembed.Common.AUTHOR,
                                 icon_url=getembed.Common.AUTHOR_LINK)
                embed.set_thumbnail(
                    url="https://cdn.discordapp.com/attachments/877796755234783273/879668020006502440/SeekPng.com_envelope-icon-png_1336118.png")
                embed.add_field(
                    name="Error", value="Invalid Email Address", inline=False)
                embed.add_field(
                    name="How to fix", value=f"Enter a email address that ends with {verified_mails}", inline=True)
                embed.set_footer(text=f"Requested by {ctx.author.name}")
                try:
                    await loadingthing.delete()
                except:
                    pass
                await ctx.send(embed=embed)
                print("email is not valid")

        except Exception as e:
            embed3 = discord.Embed(title=getembed.ErrorEmbeds.TITLE,
                                   description=getembed.ErrorEmbeds.DESCRIPTION, color=getembed.ErrorEmbeds.COLOR)
            embed3.set_author(name=getembed.Common.AUTHOR,
                              icon_url=getembed.Common.AUTHOR_LINK)
            embed3.set_thumbnail(url=getembed.ErrorEmbeds.THUMBNAIL)
            embed3.add_field(name="Error:", value=f"{e}", inline=False)
            embed3.set_footer(text=f"Requested by {ctx.author.name}")
            try:
                await loadingthing.delete()
            except:
                pass
            await ctx.send(embed=embed3)
            print(e)

    @commands.command(aliases=["similarity", "closematch", "closematches"],
                      breif="Text similarity finder",
                      description="Find the similarity of 2 given texts which sould be seperated by `||`",
                      help="Find the similarity of 2 given texts which sould be seperated by `||`")
    async def similiar(self, ctx, *, message):
        """
        The two messages ( strings ) will be divided by the 
        """
        loading_message = await ctx.send(embed=self.please_wait_emb)

        try:
            message1, message2 = message.split('||')
            r = requests.get(
                f"https://some-random-api.ml/stringsimilarity?string1={message1}&string2={message2}").json()

            embed = discord.Embed(
                title="Find Similarity", description="between two strings", color=getembed.Common.COLOR)
            embed.set_author(name=getembed.Common.AUTHOR,
                             icon_url=getembed.Common.AUTHOR_LINK)
            embed.set_thumbnail(
                url="https://media.discordapp.net/attachments/877796755234783273/880742956552822794/mr-bean-avatar-character-cartoon-rowan-atkinson-png-image-33.png?width=454&height=584")
            embed.add_field(name="First", value=f"{message1}", inline=False)
            embed.add_field(name="Second", value=f"{message2}", inline=False)
            embed.add_field(name="Similarity",
                            value=f"{r['similarity']}", inline=False)
            embed.set_footer(text=f"Requested by {ctx.author.name}")
            await ctx.send(embed=embed)

        except Exception as e:
            embed3 = discord.Embed(title=getembed.ErrorEmbeds.TITLE,
                                   description=getembed.ErrorEmbeds.DESCRIPTION, color=getembed.ErrorEmbeds.COLOR)
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
        breif="Youtube video search",
        description="Enter what to search as `query` and the bot will send you the top result you will get if you search from youtube manually! (personalization excluded)",
        help="Enter what to search as `query` and the bot will send you the top result you will get if you search from youtube manually! (personalization excluded)")
    async def youtube(self, ctx, *, query):
        loading_message = await ctx.send(embed=self.please_wait_emb)
        try:
            videosSearch = VideosSearch(f'{query}', limit=1)
            mainresult = videosSearch.result()["result"]
            video_index = mainresult[0]
            video_link = video_index["link"]
            await loading_message.delete()
            await ctx.send(video_link)
        except Exception as e:
            embed3 = discord.Embed(title=getembed.ErrorEmbeds.TITLE,
                                   description=getembed.ErrorEmbeds.DESCRIPTION, color=getembed.ErrorEmbeds.COLOR)
            embed3.set_author(name=getembed.Common.AUTHOR,
                              icon_url=getembed.Common.AUTHOR_LINK)
            embed3.set_thumbnail(
                url="https://media.discordapp.net/attachments/877796755234783273/880745781966037032/new-scrabble-words-2018-beatdown-5657-57124c9f228c0258d65053fe7d3891491x.jpg")
            embed3.add_field(name="Error:", value=f"{e}", inline=False)
            embed3.add_field(name="Possible Fix:",
                             value=f"Search something valid", inline=False)
            embed3.set_footer(text=f"Requested by {ctx.author.name}")
            await loading_message.delete()
            await ctx.send(embed=embed3)

    @commands.command(aliases=["proxy"],
                      breif="Scrap for proxies",
                      description="scrap for high quality proxies and send it. \nSources:\nhttps://www.sslproxies.org/\nhttps://www.google-proxy.net/\nhttps://free-proxy-list.net/anonymous-proxy.html\nhttps://free-proxy-list.net/uk-proxy.html\nhttps://www.us-proxy.org/\nhttps://free-proxy-list.net/\nhttp://spys.me/proxy.txt\nhttps://api.proxyscrape.com/?request=getproxies&proxytype=all&country=all&ssl=all&anonymity=all\nhttps://www.proxynova.com/proxy-server-list/\nhttps://www.proxy-list.download/HTTP\nhttps://www.proxy-list.download/HTTPS\nhttps://www.proxy-list.download/SOCKS4\nhttps://www.proxy-list.download/SOCKS5",
                      help="scrap for high quality proxies and send it. \nSources:\nhttps://www.sslproxies.org/\nhttps://www.google-proxy.net/\nhttps://free-proxy-list.net/anonymous-proxy.html\nhttps://free-proxy-list.net/uk-proxy.html\nhttps://www.us-proxy.org/\nhttps://free-proxy-list.net/\nhttp://spys.me/proxy.txt\nhttps://api.proxyscrape.com/?request=getproxies&proxytype=all&country=all&ssl=all&anonymity=all\nhttps://www.proxynova.com/proxy-server-list/\nhttps://www.proxy-list.download/HTTP\nhttps://www.proxy-list.download/HTTPS\nhttps://www.proxy-list.download/SOCKS4\nhttps://www.proxy-list.download/SOCKS5")
    async def proxies(self, ctx):
        loading_message = await ctx.send(embed=self.please_wait_emb)
        try:
            ALL = 'ALL'
            scrapper = Proxy_List_Scrapper.Scrapper(
                category=ALL, print_err_trace=False)
            data = scrapper.getProxies()
            all_proxies = ""
            for item in data.proxies:
                all_proxies += '\n{}:{}'.format(item.ip, item.port)

            # this might need to be true... bruh
            for chunk in textwrap.wrap(all_proxies, 4096, replace_whitespace=False):
                embed = discord.Embed(
                    title="Proxy Scraper",
                    description=chunk,
                    color=getembed.Common.COLOR,
                    timestamp=datetime.datetime.utcnow()
                )
                embed.set_author(name=getembed.Common.AUTHOR,
                                 icon_url=getembed.Common.AUTHOR_LINK)
                await ctx.author.send(embed=embed)

            try:
                await loading_message.delete()
            except:
                pass
            await ctx.send(f"**{ctx.author.name}**, All the proxies have been sent to you via Direct Message")

        except Exception as e:
            embed3 = discord.Embed(title=getembed.ErrorEmbeds.TITLE,
                                   description=getembed.ErrorEmbeds.DESCRIPTION, color=getembed.ErrorEmbeds.COLOR)
            embed3.set_author(name=getembed.Common.AUTHOR,
                              icon_url=getembed.Common.AUTHOR_LINK)
            embed3.set_thumbnail(
                url="https://media.discordapp.net/attachments/877796755234783273/880745781966037032/new-scrabble-words-2018-beatdown-5657-57124c9f228c0258d65053fe7d3891491x.jpg")
            embed3.add_field(name="Error:", value=f"{e}", inline=False)
            embed3.add_field(name="Possible Fix:",
                             value=f"Search something valid", inline=False)
            embed3.set_footer(text=f"Requested by {ctx.author.name}")
            await loading_message.delete()
            await ctx.send(embed=embed3)

    @commands.command(aliases=["proxiessource", "proxieslink", "proxysource"],
                      breif="Best proxy sites",
                      description="Best websites to get free high quality proxies",
                      help="Best websites to get free high quality proxies")
    async def proxylink(self, ctx):
        loading_message = await ctx.send(embed=self.please_wait_emb)
        try:
            embed = discord.Embed(
                title="HQ Proxies - Sources", color=getembed.Common.COLOR)
            embed.set_author(name=getembed.Common.AUTHOR,
                             icon_url=getembed.Common.AUTHOR_LINK)
            embed.add_field(name="Links:", value="https://www.sslproxies.org/\nhttps://www.google-proxy.net/\nhttps://free-proxy-list.net/anonymous-proxy.html\nhttps://free-proxy-list.net/uk-proxy.html\nhttps://www.us-proxy.org/\nhttps://free-proxy-list.net/\nhttp://spys.me/proxy.txt\nhttps://api.proxyscrape.com/?request=getproxies&proxytype=all&country=all&ssl=all&anonymity=all\nhttps://www.proxynova.com/proxy-server-list/\nhttps://www.proxy-list.download/HTTP\nhttps://www.proxy-list.download/HTTPS\nhttps://www.proxy-list.download/SOCKS4\nhttps://www.proxy-list.download/SOCKS5\nhttps://free-proxy-list.net/\nhttps://api.proxyscrape.com/v2/?request=getproxies&protocol=socks4&timeout=10000&country=all\nhttps://api.proxyscrape.com/v2/?request=getproxies&protocol=http&timeout=10000&country=all&ssl=all&anonymity=all\nhttps://api.proxyscrape.com/v2/?request=getproxies&protocol=socks5&timeout=10000&country=all", inline=False)
            embed.set_footer(text=f"Requested by {ctx.author.name}")
            await loading_message.delete()
            await ctx.send(embed=embed)

        except Exception as e:
            embed3 = discord.Embed(title=getembed.ErrorEmbeds.TITLE,
                                   description=getembed.ErrorEmbeds.DESCRIPTION, color=getembed.ErrorEmbeds.COLOR)
            embed3.set_author(name=getembed.Common.AUTHOR,
                              icon_url=getembed.Common.AUTHOR_LINK)
            embed3.set_thumbnail(
                url="https://media.discordapp.net/attachments/877796755234783273/880745781966037032/new-scrabble-words-2018-beatdown-5657-57124c9f228c0258d65053fe7d3891491x.jpg")
            embed3.add_field(name="Error:", value=f"{e}", inline=False)
            embed3.add_field(name="Possible Fix:",
                             value=f"Search something valid", inline=False)
            embed3.set_footer(text=f"Requested by {ctx.author.name}")
            await loading_message.delete()
            await ctx.send(embed=embed3)

    @commands.has_permissions(manage_messages=True)
    @commands.command(aliases=["dump_msgs", "dump_msges", "dump_messages"],
                      breif="Save Channel Messages",
                      description="Save the mentioned number of messages send in the channel, save it to a text file and send it",
                      help="Save the mentioned number of messages send in the channel, save it to a text file and send it")
    async def dump_msg(self, ctx, number_of_messages=50):
        loading_message = await ctx.send(embed=self.please_wait_emb)

        try:

            try:
                if number_of_messages >= 1000:
                    embed3 = discord.Embed(title=getembed.ErrorEmbeds.TITLE,
                                           description=getembed.ErrorEmbeds.DESCRIPTION, color=getembed.ErrorEmbeds.COLOR)
                    embed3.set_author(name=getembed.Common.AUTHOR,
                                      icon_url=getembed.Common.AUTHOR_LINK)
                    embed3.set_thumbnail(url=getembed.ErrorEmbeds.THUMBNAIL)
                    embed3.add_field(
                        name="Error:", value=f"Please enter a value below 1000", inline=False)
                    embed3.set_footer(text=f"Requested by {ctx.author.name}")
                    await loading_message.delete()
                    await ctx.send(embed=embed3)
                    return
            except:
                embed3 = discord.Embed(title=getembed.ErrorEmbeds.TITLE,
                                       description=getembed.ErrorEmbeds.DESCRIPTION, color=getembed.ErrorEmbeds.COLOR)
                embed3.set_author(name=getembed.Common.AUTHOR,
                                  icon_url=getembed.Common.AUTHOR_LINK)
                embed3.set_thumbnail(url=getembed.ErrorEmbeds.THUMBNAIL)
                embed3.add_field(
                    name="Error:", value=f"Please enter a valid value for `number_of_messages`. Please refer the help command for more information.", inline=False)
                embed3.set_footer(text=f"Requested by {ctx.author.name}")
                await loading_message.delete()
                await ctx.send(embed=embed3)
                return

            try:
                filename = f"{ctx.channel.name}.txt"
                with open(filename, "w+") as file:
                    async for msg in ctx.channel.history(limit=number_of_messages):
                        file.write(
                            f"{msg.created_at} - {msg.author.display_name}: {msg.clean_content}\n")
            except:
                filename = f"MessageDump.txt"
                with open(filename, "w+") as file:
                    async for msg in ctx.channel.history(limit=number_of_messages):
                        file.write(
                            f"{msg.created_at} - {msg.author.display_name}: {msg.clean_content}\n")

            em = discord.Embed(title=getembed.Common.AUTHOR,
                               color=getembed.Common.COLOR)
            em.set_thumbnail(
                url="https://cdn.discordapp.com/attachments/877796755234783273/879295069834850324/Avatar.png")
            em.set_author(name=getembed.Common.AUTHOR,
                          icon_url=getembed.Common.AUTHOR_LINK)
            em.add_field(name="Number of messages in the log",
                         value=f'{number_of_messages}')
            em.add_field(name="Filename",
                         value=f'{filename}')
            em.set_footer(text=f"Requested by {ctx.author.name}")
            try:
                await loading_message.delete()
            except:
                pass
            await ctx.send(embed=em)

            with open(filename, "rb") as filec:
                await ctx.send("Your file is:", file=discord.File(filec, f"{filename}"))

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
    client.add_cog(Tools(client))
