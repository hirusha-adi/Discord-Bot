
# my files
from keep_alive import keep_alive
import installerm

import platform
import os
try:
  os.system("pip3 install prsaw")
  # installerm.pip_install("prsaw")
  print("TEST")
except Exception as e:
  print("error: ", e)

try:
  # installerm.INSTALL_ALL()
  print("TEST")
except Exception as e:
  print("error: ", e)

# all imports

from discord import permissions
from prsaw import RandomStuffV2
import discord
from discord.ext import commands
import random
import requests
import json
from faker import *
import string
import time
import wikipedia
import datetime
from bs4 import BeautifulSoup
from pyfiglet import Figlet


# Imports for music command!
if platform.system().lower().startswith('win'):
  os.system("pip install PyNaCl")
else:
  os.system("pip3 install PyNaCl")
try:
  import nacl
except ImportError:
  if platform.system().lower().startswith('win'):
    os.system("pip install PyNaCl")
  else:
    os.system("pip3 install PyNaCl")

# FOR THE LAVALINK MUSIC COMMAND!
try:
    if platform.system().lower().startswith('win'):
            # os.system("pip install discord.py")
            os.system("pip install dismusic==1.0.1")
            # os.system("pip install discord-custom-help")
    else:
            # os.system("pip3 install discord.py")
            os.system("pip3 install dismusic==1.0.1")
            # os.system("pip3 install discord-custom-help")
except Exception as e:
  print("Error:", e)


# these will be needed almost everywhere

botconfigdata = json.load(open("config.json", "r"))
bot_prefix = botconfigdata["msg-prefix"]
bot_info_cmnd_thumbnail_link = botconfigdata["info-command-thumbnail-link"]
bot_creator_name = botconfigdata["bot-creator-name"]
bot_current_version = botconfigdata["bot-version"]
bot_owner_id_zeacer = botconfigdata["ownerid"]
bot_logging_commands_status = botconfigdata["log-user-data"]
bot_logging_channel_id = botconfigdata["log-channel-id"]


bot_email_addr = os.environ['EMAILA']
bot_email_password = os.environ['EMAILP']

client = commands.Bot(command_prefix = bot_prefix)
# client.remove_command('help')

token = os.environ['TOKEN']


def give_nice_codes():
  code = ''.join(random.choices(string.ascii_letters + string.digits, k=16))
  return f'https://discord.gift/{code}'


def get_bitcoin_status():
  r = requests.get('https://api.coindesk.com/v1/bpi/currentprice/btc.json').json()
  value = r['bpi']['USD']['rate']
  return value

def info_about_good_bot():
  info_of_gb = """This is created by ZeaCeR#5641

This is my second discord bot :)
The first one: https://github.com/hirusha-adi/firrst-discord-bot ( discontinued )

Music Playing will be added soon!

Motivated by Snakey
"""
  return info_of_gb

def change_directory(directory):
  try:
    os.chdir(f"{directory}")
  except Exception as e:
    print("Error-1-0: Unable to change directory! - continuing...")
    try:
      os.system(f"cd ./{directory}")
    except Exception as e:
      print("Error-1-1: Unable to change directory! - continuing...")
      try:
        os.system(f"cd .\{directory}")
      except Exception as e:
        print("Error-1-2: Unable to change directory! - continuing...")
        try:
          os.system(f"cd {directory}")
        except Exception as e:
          print("Error-1-3: Unable to change directory! - continuing...")
          return

def ascii_art_func(text):
  art = Figlet(font="slant")
  return str(art.renderText(text))

def ikmainlkScrapper(weblink):
    r = requests.get(weblink)
    c = r.content
    soup = BeautifulSoup(c, "html.parser")

    item_list_names = soup.find_all("h2", {"class": "heading--2eONR heading-2--1OnX8 title--3yncE block--3v-Ow"})
    item_list_images = soup.find_all("img", {"class": "normal-ad--1TyjD"})
    item_list_price = soup.find_all("div", {"class": "price--3SnqI color--t0tGX"})
    item_list_description = soup.find_all("div", {"class": "description--2-ez3"})
    list_updated_time = soup.find_all("div", {"class": "updated-time--1DbCk"})
    list_links_to_itms = soup.find_all("a", {"class":"card-link--3ssYv gtm-ad-item"})

    for  i in range(len(item_list_names)):
        print(item_list_names[i].text)

        price_list_index = item_list_price[i]
        print(price_list_index.find("span").text)
    
        links_to_sites_index = list_links_to_itms[i]
        print("https://ikman.lk/" + links_to_sites_index.get('href'))

        try:
            image_links_in_index = item_list_images[i] # if i don't do this, an error will occcur as this is a whole list
            print(image_links_in_index.get('src')) # so we index it and call a value and we get the src in it!
        except:
            print("")

        description_list = item_list_description[i]
        print(description_list.text)

        try:
            updated_time_index = list_updated_time[i]
            print(updated_time_index.text)
        except:
            print("")

        print("\n")

def get_quote():
    r = requests.get("https://zenquotes.io/api/random")
    json_data = json.loads(r.text)
    quote = json_data[0]['q'] + " - " + json_data[0]['a']
    return(quote)

def search_wikipedia(wordToSearch):
  result = wikipedia.summary(wordToSearch, sentences = 2)
  return result

def bored_activity():
  r = requests.get('http://www.boredapi.com/api/activity/')
  data = r.json()
  what_to_do_when_bored = f'[+] Activity: {data["activity"]} \n[+] Type: {data["type"]} \n[+] Participants: {data["participants"]} \nKey: {data["key"]} \n[+] Accessibility: {data["accessibility"]} '
  return what_to_do_when_bored

def show_pervert_text():
  pervert_text = """Can I get a booty pic with your panties on? And one without them on? Can I also get 3 different pics of your boobs in any position. Also can I get a pic of your pussy from the front and one where it’s spread open. Can I get a picture of you fingering your self? Can I get a pic of you doing a kissing face but with your boobs in it? Can I get a picture of your pussy and ass from behind in one shot? Can I also get a pic of your full front body in just a bra and panties? And can I get a pic of your ass when your pants are all the way up? Also can I get a pic of your boobs when you’re in the shower? Also can I get another pussy pic while you’re in the shower? For the rest of the pics can you just send whatever other sexy things you want? For the videos can I get a video of you twerking in really short shorts? And one of you fingering yourself? One of you actually cumming? Also can I get a video of you playing with your tits while not wearing a shirt? u be squirtin? or u on the cream team? what color the inside? your booty real wet? do it clap? do it fart? do it grip the meat? it’s tight? how many fingers u use? what it taste like? can i smell it? is it warm? it’s real juicy? do it drip? you be moaning?"""
  return pervert_text

def CREATE_FAKE_PROFILES_MANY():
  fake = Faker()
  simple_dict = fake.profile()
  fake_info_simple = "Name: " + str(simple_dict['name']) + "\nJob: " + str(simple_dict['job']) + "\nBirthdate: " + str(simple_dict['birthdate']) + "\nCompany: " + str(simple_dict['company']) + "\SSN: " + str(simple_dict['ssn']) + "\nRecidence: " + simple_dict['residence'] + "\nCurrent Location:" + str(simple_dict['current_location']) + "\nBlood Group: " + str(simple_dict['blood_group']) + "\nUsername: " + str(simple_dict['username']) + "\nAddress: " + str(simple_dict['address']) + "\nMail: " + str(simple_dict['mail'])
  return fake_info_simple

def give_nice_codes():
  code = ''.join(random.choices(string.ascii_letters + string.digits, k=16))
  return f'https://discord.gift/{code}'


def ipinfoshit(ipfromuser):
    r = requests.get('http://ip-api.com/json/' + str(ipfromuser)) # include the ip
    data = r.json()
    ipinfo = f'\n[+] Status: {data["status"]} \n[+] Country: {data["country"]} \n[+] Country Code: {data["countryCode"]} \n[+] Region: {data["region"]} \n[+] Region Name: {data["regionName"]} \n[+] City: {data["city"]} \n[+] ZIP: {data["zip"]} \n[+] Latitude: {data["lat"]} \n[+] Longitude: {data["lon"]} \n[+] TimeZone: {data["timezone"]} \n[+] ISP: {data["isp"]} \n[+] Organization: {data["org"]} \n[+] ASN: {data["as"]} \n[+] Query: {data["query"]} \n'
    return ipinfo

# THE MAIN COMMANDS OF THE BOT START HERE!

start_time = None

@client.event
async def on_ready():
    print(f'Logged in as {client.user.name}')
    print(f'Discord.py API version: {discord.__version__}')
    print(f'Python version: {platform.python_version()}')

    global start_time
    start_time = time.time()

    await client.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name=f"{len(client.guilds)} servers!"))
    print('Bot is ready!')


# THIS IS THE PLASE WAIT TEMPLATE!
# Almost all the commands use this, you can change it here!
please_wait_emb = discord.Embed(title="Please Wait", description="``` Processing Your Request ```", color=0xff0000)
please_wait_emb.set_author(name="YourBot")
please_wait_emb.set_thumbnail(url="https://c.tenor.com/I6kN-6X7nhAAAAAj/loading-buffering.gif")
please_wait_emb.set_footer(text="Bot created by ZeaCeR#5641")
please_wait_wt_bfd = 2








# DUMB MISTAKE, WILL BE FIXED SOON IN FUTURE
# @client.command()
# async def ikmanlk(ctx, *, link):
#     try:
#       r = requests.get(link)
#       c = r.content
#       soup = BeautifulSoup(c, "html.parser")

#       item_list_names = soup.find_all("h2", {"class": "heading--2eONR heading-2--1OnX8 title--3yncE block--3v-Ow"})
#       item_list_images = soup.find_all("img", {"class": "normal-ad--1TyjD"})
#       item_list_price = soup.find_all("div", {"class": "price--3SnqI color--t0tGX"})
#       item_list_description = soup.find_all("div", {"class": "description--2-ez3"})
#       list_updated_time = soup.find_all("div", {"class": "updated-time--1DbCk"})
#       list_links_to_itms = soup.find_all("a", {"class":"card-link--3ssYv gtm-ad-item"})

#       embed = discord.Embed(title=f'ikman.lk Scraper')
#       embed.set_thumbnail(url="https://ikman.lk/facebook-opengraph.png")
      
#       for  i in range(len(item_list_names)):
#         # Name
#         embed.add_field(name="Name", value=f'{item_list_names[i].text}', inline=False)
#         # Price
#         price_list_index = item_list_price[i]
#         embed.add_field(name="Price", value=f'{price_list_index.find("span").text}', inline=False)
#         # Link
#         links_to_sites_index = list_links_to_itms[i]
#         embed.add_field(name="Link", value=f'"https://ikman.lk/" {links_to_sites_index.get("href")}', inline=False)
#         # Image Link
#         try:
#           image_links_in_index = item_list_images[i]
#           embed.add_field(name="Image Link", value=f'{image_links_in_index.get("src")}', inline=False)
#         except:
#           embed.add_field(name="Image Link", value=f'None', inline=False)
#         # Location / Description
#         try:
#           description_list = item_list_description[i]
#           embed.add_field(name="Location", value=f'{description_list.text}', inline=False)
#         except:
#           embed.add_field(name="Location", value=f'None', inline=False)
#         # Updated Time
#         try:
#           updated_time_index = list_updated_time[i]
#           embed.add_field(name="Updated Date", value=f'{updated_time_index.text}', inline=False)
#         except:
#           embed.add_field(name="Updated Date", value=f'None', inline=False)
      
#       embed.set_footer(text=datetime.datetime.now())
#     except Exception as e:
#       await ctx.send(f'Error: {e}')


@client.command()
async def uptime(ctx):
  loading_message = await ctx.send(embed=please_wait_emb)

  try:
    current_time = time.time()
    difference = int(round(current_time - start_time))
    text = str(datetime.timedelta(seconds=difference))
    embed=discord.Embed(color=0xff0000)
    embed.add_field(name="The bot was online for: ", value=f":alarm_clock: {text}", inline=False)
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


@client.command()
async def status(ctx):
  loading_message = await ctx.send(embed=please_wait_emb)

  try:
    current_time = time.time()
    difference = int(round(current_time - start_time))
    text = str(datetime.timedelta(seconds=difference))

    embed=discord.Embed(color=0xff0000)
    embed.add_field(name="Announcements", value=f"``` -YourBot {bot_current_version}- Hello! Its been nearly two months after the first release of this discord bot. Most of the commands are very stable now, but not all of them. Help me make this bot have 500+ commands. use {bot_prefix}help to check all the commands available! ```", inline=False)
    embed.add_field(name="Servers", value=f"{len(client.guilds)}", inline=True)
    embed.add_field(name="Uptime", value=f"{text}", inline=True)
    embed.add_field(name="Version", value=f"{bot_current_version}", inline=True)
    embed.add_field(name="Source Code", value="https://github.com/hirusha-adi/Discord-Bot", inline=True)
    embed.add_field(name="Creator", value=f"{bot_creator_name}", inline=True)
    embed.add_field(name="Errors", value="``` There is bug when the chatbot feature is being used simultaneously in many channels, This issue will be fixed soon!  ```", inline=False)
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


# @client.command(aliases=["sendmail"])
# async def sendemail(ctx, senderemail, recieveremail, emailsubject="Hey", *, emailcontent="Hello There!"):

#   verified_mails = ("gmail.com", "outlook.com", "yahoo.com")

#   embed=discord.Embed(title="Please Wait", description="``` This may take longer than usual! ```", color=0xff0000)
#   embed.set_thumbnail(url="https://c.tenor.com/I6kN-6X7nhAAAAAj/loading-buffering.gif") 
#   embed.set_author(name="YourBot", icon_url="https://cdn.discordapp.com/attachments/877796755234783273/879295069834850324/Avatar.png")
#   embed.set_footer(text="Bot created by ZeaCeR#5641")
#   loadingthing = await ctx.send(embed=embed)

#   try:
#     if senderemail.split('@')[-1].lower() in verified_mails:
#       try:
#         server = smtplib.SMTP('smtp.gmail.com', 587)
#         server.starttls()

#         try:
#           server.login(bot_email_addr, bot_email_password)

#         except Exception as e:
#           embede=discord.Embed(title="Something was wrong!", description="Your request did not complete due to an error!", color=0xff0000)
#           embede.set_author(name="YourBot", icon_url="https://cdn.discordapp.com/attachments/877796755234783273/879295069834850324/Avatar.png")
#           embede.set_thumbnail(url="https://cdn.discordapp.com/attachments/877796755234783273/879668020006502440/SeekPng.com_envelope-icon-png_1336118.png")
#           embede.add_field(name="Error", value=f"{e}", inline=False)
#           embede.set_footer(text=f"Requested by {ctx.author.name}")
#           try:
#             await loadingthing.delete()
#           except:
#             pass
#           await ctx.send(embed=embede)
#           return

#         email = EmailMessage()

#         whoasktosend = ctx.author.name
#         whoasktosendid = ctx.author.id
#         emailcontentfinal = f"""This message it being sent from the discord bot named YourBot and was requested by the user {whoasktosend} / {whoasktosendid} / {senderemail}. The message: {emailcontent}   | Thank You. Have a Nice day, Stay safe! - YourBot"""

#         email['From'] = bot_email_addr
#         email['To'] = recieveremail
#         email['Subject'] = emailsubject
#         email.set_content(emailcontentfinal)
#         server.send_message(email)
#         server.close()

#         try:
#           embed2=discord.Embed(title="Email Sent", description="Your requested email was sent suceessfully! ", color=0xff0000)
#           embed2.set_author(name="YourBot", icon_url="https://cdn.discordapp.com/attachments/877796755234783273/879295069834850324/Avatar.png")
#           embed2.set_thumbnail(url="https://cdn.discordapp.com/attachments/877796755234783273/879668020006502440/SeekPng.com_envelope-icon-png_1336118.png")
#           embed2.add_field(name="Your Email Address", value=f"{senderemail}", inline=False)
#           embed2.add_field(name="Receiver Email Address", value=f"{recieveremail}", inline=False)
#           embed2.add_field(name="Email Subject", value=f"{emailsubject}", inline=False)
#           embed2.add_field(name="Email Content", value=f"{emailcontentfinal}", inline=False)
#           embed2.set_footer(text=f"Requested by {ctx.author.name}")
#           try:
#             await loadingthing.delete()
#           except:
#             pass
#           await ctx.send(embed=embed2)

#         except:
#           try:
#             await loadingthing.delete()
#           except:
#             pass
#           await ctx.send("Email was sent successfully!")

#       except Exception as e:
#         embed3=discord.Embed(title=":red_square: Error!", description="The command was unable to run successfully! ", color=0xff0000)
#         embed3.set_author(name="YourBot", icon_url="https://cdn.discordapp.com/attachments/877796755234783273/879295069834850324/Avatar.png")
#         embed3.set_thumbnail(url="https://cdn.discordapp.com/attachments/877796755234783273/879298565380386846/sign-red-error-icon-1.png")
#         embed3.add_field(name="Error:", value=f"{e}", inline=False)
#         embed3.set_footer(text=f"Requested by {ctx.author.name}")
#         try:
#           await loadingthing.delete()
#         except:
#           pass
#         await ctx.send(embed=embed3)
    
#     else:
#       embed=discord.Embed(title="Something was wrong!", description="Your request did not complete due to an error!", color=0xff0000)
#       embed.set_author(name="YourBot", icon_url="https://cdn.discordapp.com/attachments/877796755234783273/879295069834850324/Avatar.png")
#       embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/877796755234783273/879668020006502440/SeekPng.com_envelope-icon-png_1336118.png")
#       embed.add_field(name="Error", value="Invalid Email Address", inline=False)
#       embed.add_field(name="How to fix", value=f"Enter a email address that ends with {verified_mails}", inline=True)
#       embed.set_footer(text=f"Requested by {ctx.author.name}")
#       try:
#         await loadingthing.delete()
#       except:
#         pass
#       await ctx.send(embed=embed)
#   except Exception as e:
#     embed3=discord.Embed(title=":red_square: Error!", description="The command was unable to run successfully! ", color=0xff0000)
#     embed3.set_author(name="YourBot", icon_url="https://cdn.discordapp.com/attachments/877796755234783273/879295069834850324/Avatar.png")
#     embed3.set_thumbnail(url="https://cdn.discordapp.com/attachments/877796755234783273/879298565380386846/sign-red-error-icon-1.png")
#     embed3.add_field(name="Error:", value=f"{e}", inline=False)
#     embed3.set_footer(text=f"Requested by {ctx.author.name}")
#     try:
#       await loadingthing.delete()
#     except:
#       pass
#     await ctx.send(embed=embed3)




# ERROR HANDLING //////////////////////////////////////////////////////////////////////////////////////////
# https://stackoverflow.com/questions/62234166/cant-get-discord-py-to-raise-an-error-if-user-doesnt-have-permissions-to-kick
@client.event
async def on_command_error(ctx, error):
  if isinstance(error, commands.MissingPermissions):
    embed=discord.Embed(title="ERROR", description="`You don't have the permissions required to use this command!`", color=0xff0000)
    embed.set_author(name="YourBot", icon_url="https://cdn.discordapp.com/attachments/877796755234783273/879295069834850324/Avatar.png")
    embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/877796755234783273/879298565380386846/sign-red-error-icon-1.png")
    await ctx.send(embed=embed)
    return

  if isinstance(error, commands.MissingRequiredArgument):
    embed=discord.Embed(title="Something is wrong!", description="An error has been occured!", color=0xff0000)
    embed.set_author(name="YourBot", icon_url="https://cdn.discordapp.com/attachments/877796755234783273/879295069834850324/Avatar.png")
    embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/877796755234783273/879298565380386846/sign-red-error-icon-1.png")
    embed.add_field(name="Error", value="You haven't passed the needed arguments for this command to run properly", inline=True)
    embed.add_field(name="Possible Fix", value=f"use `{bot_prefix}help all` to list out all the command and check the proper usage of the command you used", inline=True)
    await ctx.send(embed=embed)
    return
  
@client.command()
async def loadex(ctx, extension):
  if ctx.author.id == bot_owner_id_zeacer:
    client.load_extension(f'cogs.{extension}')
    embed=discord.Embed(title="SUCCESS", description=f"`ADDED cogs.{extension} from YourBot`", color=0xff0000)
    embed.set_author(name="YourBot", icon_url="https://cdn.discordapp.com/attachments/877796755234783273/879295069834850324/Avatar.png")
    embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/877796755234783273/879298565380386846/sign-red-error-icon-1.png")
    await ctx.send(embed=embed)
    return
  else:
    embed=discord.Embed(title="ERROR", description="`You don't have the permissions required to use this command!`", color=0xff0000)
    embed.set_author(name="YourBot", icon_url="https://cdn.discordapp.com/attachments/877796755234783273/879295069834850324/Avatar.png")
    embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/877796755234783273/879298565380386846/sign-red-error-icon-1.png")
    await ctx.send(embed=embed)
    return


@client.command()
async def unloadex(ctx, extension):
  if ctx.author.id == bot_owner_id_zeacer:
    try:
      client.unload_extension(f'cogs.{extension}')
      embed=discord.Embed(title="SUCCESS", description=f"`REMOVED cogs.{extension} from YourBot`", color=0xff0000)
      embed.set_author(name="YourBot", icon_url="https://cdn.discordapp.com/attachments/877796755234783273/879295069834850324/Avatar.png")
      embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/877796755234783273/879298565380386846/sign-red-error-icon-1.png")
      await ctx.send(embed=embed)
      return
    except:
      embed=discord.Embed(title="ERROR", description="`You don't have the permissions required to use this command!`", color=0xff0000)
      embed.set_author(name="YourBot", icon_url="https://cdn.discordapp.com/attachments/877796755234783273/879295069834850324/Avatar.png")
      embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/877796755234783273/879298565380386846/sign-red-error-icon-1.png")
      await ctx.send(embed=embed)
      return

# Loading all the cogs at startup
for filename in os.listdir('./cogs'):
  if filename.endswith('.py'):
    client.load_extension(f'cogs.{filename[:-3]}')


#  FOR MUSIC BOT //////////////////////////////////////////////////////////////////////////////////////////
# The lava.link could be a localhost:port, but i chooses these servers and i dont host it manually
client.lava_nodes = [
  {
    'host':"lava.link",
    'port':80,
    'rest_uri':f'http://lava.link:80',
    'identifier':'MAIN',
    'password':'anything',
    'region':'singapore'
  }
]

# Adding the cog
client.load_extension('dismusic')



#  FOR CHAT BOT //////////////////////////////////////////////////////////////////////////////////////////
rs = RandomStuffV2()

credits_wl = (
  "who made you",
  "developer",
  "who created you",
  "creator",
  "who is your owner",
  "your owner"
  "zeacer",
  "5641",
  "zeacer5641",
  "zeacer#5641",
  "your father",
  "your mother",
  "your creator",
  "develop",
  "who is your father",
  "who is your mother",
  "who is your zeacer",
  "who is your creator"
)

credits_reply_wl = (
  "I was created by ZeaCeR#5641",
  "ZeaCeR#5641 created me",
  "ZeaCeR#5641 is the creator of me",
  "ZeaCeR#5641 is person who created me"
)

channel_lis = (
  863706778743341076,
  874577378746175508,
  874963358254780447,
  874964067322822696
)

bp = bot_prefix


@client.event
async def on_message(message):
  
  if message.channel.id in channel_lis:
    if client.user == message.author:
      return

    if message.content.lower() in credits_wl:
      await message.reply(f"{random.choice(credits_reply_wl)}")
    elif message.content.startswith(f'{bp}help'):
      pass
    else:
      try:
          response = rs.get_ai_response(message.content)
          await message.reply(response['message'])
      except Exception as e:
        await message.reply(f'Error: {e}')
  
  if client.user == message.author:
    return
    
  if bot_logging_commands_status == "yes":
    if message.content.startswith('>'):
      channel = client.get_channel(bot_logging_channel_id)
      embed = discord.Embed(title=f"{message.author.name} has used a command!", colour=discord.Colour(0xff0000), timestamp=datetime.datetime.utcfromtimestamp(1629281713))
      embed.set_thumbnail(url=f"{message.author.avatar_url}")
      embed.set_author(name="YourBot", icon_url="https://cdn.discordapp.com/attachments/861861096512290836/877496519123677195/Avatar.png")
      embed.set_footer(text="Command Logger - YourBot", icon_url="https://cdn.discordapp.com/attachments/861861096512290836/877496519123677195/Avatar.png")
      embed.add_field(name="Command", value=f"{message.content}", inline=False)
      embed.add_field(name="User Name", value=f"{message.author.name}", inline=True)
      embed.add_field(name="User ID", value=f"{message.author.id}", inline=True)
      try:
        embed.add_field(name="Sever Name", value=f"{message.guild.name}", inline=True)
        embed.add_field(name="Sever ID", value=f"{message.guild.id}", inline=True)
        embed.add_field(name="Channel Name", value=f"{message.channel.name}", inline=True)
        embed.add_field(name="Channel ID", value=f"{message.channel.id}", inline=True)
      except AttributeError:
        embed.add_field(name="Location", value=f"Direct Message", inline=True)

      # await channel.send(f'{message.content}')
      await channel.send(embed=embed)
  
  await client.process_commands(message)


# Loading the music cog
# client.add_cog(Music(client))



keep_alive()
client.run(token)
