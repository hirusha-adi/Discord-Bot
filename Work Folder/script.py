from __future__ import unicode_literals
import asyncio
import smtplib
from email.message import EmailMessage

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
from password_strength import PasswordStats
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
import aiohttp
from bs4 import BeautifulSoup
import urllib
import io
import base64
import hashlib
from typing import Optional, Text
# from datetime import datetime
import instaloader
from pyfiglet import Figlet
import youtube_dl
import textwrap
import subprocess
import threading
from multiprocessing import Process


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
            # os.system("pip3 install discord.py")
            os.system("pip3 install dismusic==1.0.1")
            # os.system("pip3 install discord-custom-help")
    else:
            os.system("pip install discord.py")
            # os.system("pip install dismusic==1.0.1")
            # os.system("pip install discord-custom-help")
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
async def chatbot(ctx, command="main"):
  loading_message = await ctx.send(embed=please_wait_emb)

  try:
    old_wl = ("1", "1.0", "one", "first", "olddays")
    bp = bot_prefix
    if command in old_wl:
      emh1 = discord.Embed(title=f'Chat Bot', description=f'Lonely Bot v2.0', color=0xFF0000)
      emh1.set_thumbnail(url=r"https://cdn.discordapp.com/attachments/863706778743341076/874579616210239488/Avatar.png")
      emh1.add_field(name=f'NOTICE', value=f'This project is now seperate from this!', inline=True)
      emh1.add_field(name=f'Invite Link', value=f'https://discord.com/api/oauth2/authorize?client_id=863712001724776488&permissions=139653925952&scope=bot', inline=True)
      emh1.set_author(name="YourBot", icon_url="https://cdn.discordapp.com/attachments/877796755234783273/879295069834850324/Avatar.png")
      emh1.set_footer(text=f"Requested by {ctx.author.name}")
      await loading_message.delete()
      await ctx.send(embed=emh1)

    elif command == "main":
      emh2 = discord.Embed(title=f'Chat Bot', description=f'Setup', color=0xFF0000)
      emh2.set_thumbnail(url=r"https://cdn.discordapp.com/attachments/863706778743341076/874579616210239488/Avatar.png")
      emh2.add_field(name=f'How to start?', value=f'DM the Channel ID to `ZeaCeR#5641`', inline=True)
      emh2.add_field(name=f'Help', value=f'use `{bp}chatbot help` to Help', inline=True)
      emh2.set_author(name="YourBot", icon_url="https://cdn.discordapp.com/attachments/877796755234783273/879295069834850324/Avatar.png")
      emh2.set_footer(text=f"Requested by {ctx.author.name}")
      await loading_message.delete()
      await ctx.send(embed=emh2)

    elif command == "history":
      emh3 = discord.Embed(title=f'Chat Bot', description=f'Chatbot History', color=0xFF0000)
      emh3.set_thumbnail(url=r"https://cdn.discordapp.com/attachments/863706778743341076/874579616210239488/Avatar.png")
      emh3.add_field(name=f'History', value=f'First Started as `Lonely Bot#7613`', inline=True)
      emh3.set_author(name="YourBot", icon_url="https://cdn.discordapp.com/attachments/877796755234783273/879295069834850324/Avatar.png")
      emh3.set_footer(text=f"Requested by {ctx.author.name}")
      await loading_message.delete()
      await ctx.send(embed=emh3)
    
    elif command == "list":
      emh4 = discord.Embed(title=f'Chat Bot - Channel List', description=f'all activated channels', color=0xFF0000)
      emh4.set_thumbnail(url=r"https://cdn.discordapp.com/attachments/863706778743341076/874579616210239488/Avatar.png")
      emh4.add_field(name=f'List', value='863706778743341076 \n874577378746175508\n', inline=True)
      emh4.set_author(name="YourBot", icon_url="https://cdn.discordapp.com/attachments/877796755234783273/879295069834850324/Avatar.png")
      emh4.set_footer(text=f"Requested by {ctx.author.name}")
      await loading_message.delete()
      await ctx.send(embed=emh4)

    elif command == "help":
      emh2 = discord.Embed(title=f'Chat Bot - Help', description=f'Setup', color=0xFF0000)
      emh2.set_thumbnail(url=r"https://cdn.discordapp.com/attachments/863706778743341076/874579616210239488/Avatar.png")
      emh2.add_field(name=f'History', value=f'`{bp}chatbot history` to see the beginning of the chatbot project', inline=True)
      emh2.add_field(name=f'List Active Channels', value=f'`{bp}chatbot list` to see the list of active channels of chatbot', inline=True)
      emh2.set_author(name="YourBot", icon_url="https://cdn.discordapp.com/attachments/877796755234783273/879295069834850324/Avatar.png")
      emh2.set_footer(text=f"Requested by {ctx.author.name}")
      emh2.add_field(name=f'Old Days', value=f'`{bp}chatbot olddays`', inline=True)
      await loading_message.delete()
      await ctx.send(embed=emh2)
    
    else:
      emh2 = discord.Embed(title=f'Chat Bot - Help', description=f'Setup', color=0xFF0000)
      emh2.set_thumbnail(url=r"https://cdn.discordapp.com/attachments/863706778743341076/874579616210239488/Avatar.png")
      emh2.add_field(name=f'History', value=f'`{bp}chatbot history` to see the beginning of the chatbot project', inline=True)
      emh2.add_field(name=f'List Active Channels', value=f'`{bp}chatbot list` to see the list of active channels of chatbot', inline=True)
      emh2.set_author(name="YourBot", icon_url="https://cdn.discordapp.com/attachments/877796755234783273/879295069834850324/Avatar.png")
      emh2.set_footer(text=f"Requested by {ctx.author.name}")
      emh2.add_field(name=f'Old Days', value=f'`{bp}chatbot olddays`', inline=True)
      await loading_message.delete()
      await ctx.send(embed=emh2)
  
  except Exception as e:
    embed3=discord.Embed(title=":red_square: Error!", description="The command was unable to run successfully! ", color=0xff0000)
    embed3.set_author(name="YourBot", icon_url="https://cdn.discordapp.com/attachments/877796755234783273/879295069834850324/Avatar.png")
    embed3.set_thumbnail(url="https://cdn.discordapp.com/attachments/877796755234783273/879298565380386846/sign-red-error-icon-1.png")
    embed3.add_field(name="Error:", value=f"{e}", inline=False)
    embed3.set_footer(text=f"Requested by {ctx.author.name}")
    await loading_message.delete()
    await ctx.send(embed=embed3)



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


@client.command(aliases=["sendmail"])
async def sendemail(ctx, senderemail, recieveremail, emailsubject="Hey", *, emailcontent="Hello There!"):

  verified_mails = ("gmail.com", "outlook.com", "yahoo.com")

  embed=discord.Embed(title="Please Wait", description="``` This may take longer than usual! ```", color=0xff0000)
  embed.set_thumbnail(url="https://c.tenor.com/I6kN-6X7nhAAAAAj/loading-buffering.gif") 
  embed.set_author(name="YourBot", icon_url="https://cdn.discordapp.com/attachments/877796755234783273/879295069834850324/Avatar.png")
  embed.set_footer(text="Bot created by ZeaCeR#5641")
  loadingthing = await ctx.send(embed=embed)

  try:
    if senderemail.split('@')[-1].lower() in verified_mails:
      try:
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()

        try:
          server.login(bot_email_addr, bot_email_password)

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
          return

        email = EmailMessage()

        whoasktosend = ctx.author.name
        whoasktosendid = ctx.author.id
        emailcontentfinal = f"""This message it being sent from the discord bot named YourBot and was requested by the user {whoasktosend} / {whoasktosendid} / {senderemail}. The message: {emailcontent}   | Thank You. Have a Nice day, Stay safe! - YourBot"""

        email['From'] = bot_email_addr
        email['To'] = recieveremail
        email['Subject'] = emailsubject
        email.set_content(emailcontentfinal)
        server.send_message(email)
        server.close()

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

        except:
          try:
            await loadingthing.delete()
          except:
            pass
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


@client.command()
async def slots(ctx):
  loading_message = await ctx.send(embed=please_wait_emb)

  try:
    responses = ["🍋" , "🍊", "🍉", ":seven:", ]
    embed=discord.Embed(title="🎰 Slot Machine 🎰", description=random.choice(responses) + random.choice(responses) + random.choice(responses), color=0xFF0000)
    embed.set_author(name="YourBot", icon_url="https://cdn.discordapp.com/attachments/877796755234783273/879295069834850324/Avatar.png")
    embed.set_footer(text="You need triple 7's to win.")
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
async def raccoon(ctx):
  loading_message = await ctx.send(embed=please_wait_emb)

  try:
    r = requests.get("https://some-random-api.ml/animal/raccoon").json()

    embed=discord.Embed(title="a Raccoon", color=0xff0000)
    embed.set_author(name="YourBot", icon_url="https://media.discordapp.net/attachments/877796755234783273/879295069834850324/Avatar.png?width=300&height=300")
    embed.set_image(url=str(r["image"]))
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
async def raccoonfact(ctx):
  loading_message = await ctx.send(embed=please_wait_emb)

  try:
    r = requests.get("https://some-random-api.ml/animal/raccoon").json()

    embed=discord.Embed(title="a Raccoon Fact", color=0xff0000)
    embed.set_author(name="YourBot", icon_url="https://media.discordapp.net/attachments/877796755234783273/879295069834850324/Avatar.png?width=300&height=300")
    embed.set_thumbnail(url=str(r["image"]))
    embed.add_field(name="Fact", value=str(r["fact"]), inline=False)
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
async def kangaroo(ctx):
  loading_message = await ctx.send(embed=please_wait_emb)

  try:
    r = requests.get("https://some-random-api.ml/animal/kangaroo").json()

    embed=discord.Embed(title="a Kangaroo", color=0xff0000)
    embed.set_author(name="YourBot", icon_url="https://media.discordapp.net/attachments/877796755234783273/879295069834850324/Avatar.png?width=300&height=300")
    embed.set_image(url=str(r["image"]))
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
async def kangaroofact(ctx):
  loading_message = await ctx.send(embed=please_wait_emb)

  try:
    r = requests.get("https://some-random-api.ml/animal/kangaroo").json()

    embed=discord.Embed(title="a Kangaroo Fact", color=0xff0000)
    embed.set_author(name="YourBot", icon_url="https://media.discordapp.net/attachments/877796755234783273/879295069834850324/Avatar.png?width=300&height=300")
    embed.set_thumbnail(url=str(r["image"]))
    embed.add_field(name="Fact", value=str(r["fact"]), inline=False)
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


@client.command(aliases=["jokenew"])
async def joke2(ctx):

  loading_message = await ctx.send(embed=please_wait_emb)
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


@client.command(aliases=["similarity", "closematch", "closematches"])
async def similiar(ctx, *, message):
  """
  The two messages ( strings ) will be divided by the 
  """
  loading_message = await ctx.send(embed=please_wait_emb)

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


@client.command(aliases=["twc"])
async def twittercomment(ctx, usernametw="User1", displaynametw="user", linkpfp="https://media.discordapp.net/attachments/877796755234783273/879295069834850324/Avatar.png?width=300&height=300", *, commenttw="The comment comes here" ):
  loading_message = await ctx.send(embed=please_wait_emb)

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
    embed3=discord.Embed(title=":red_square: Error!", description="The command was unable to run successfully! ", color=0xff0000)
    embed3.set_author(name="YourBot", icon_url="https://cdn.discordapp.com/attachments/877796755234783273/879295069834850324/Avatar.png")
    embed3.set_thumbnail(url="https://media.discordapp.net/attachments/877796755234783273/880745781966037032/new-scrabble-words-2018-beatdown-5657-57124c9f228c0258d65053fe7d3891491x.jpg")
    embed3.add_field(name="Error:", value=f"{e}", inline=False)
    embed3.add_field(name="Possible Fix:", value=f"You must have only one '||' part for the whole message for the bot to divide the string", inline=False)
    embed3.set_footer(text=f"Requested by {ctx.author.name}")
    await loading_message.delete()
    await ctx.send(embed=embed3)


@client.command()
async def whalefact(ctx):
  loading_message = await ctx.send(embed=please_wait_emb)

  try:
    r = requests.get("https://some-random-api.ml/facts/whale").json()

    embed=discord.Embed(title="a Whale Fact", color=0xff0000)
    embed.set_author(name="YourBot", icon_url="https://cdn.discordapp.com/attachments/877796755234783273/879295069834850324/Avatar.png")
    embed.add_field(name="Fact", value=f"{r['fact']}", inline=True)
    embed.set_thumbnail(url="https://media.discordapp.net/attachments/877796755234783273/880809109052588052/167291_web.jpg?width=759&height=504")
    embed.set_footer(text=f"Requested by {ctx.author.name}")
    await loading_message.delete()
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


@client.command()
async def bottoken(ctx):
  loading_message = await ctx.send(embed=please_wait_emb)

  try:
    r = requests.get("https://some-random-api.ml/bottoken").json()

    embed=discord.Embed(title="Discord Bot Token Generator", description="`{r['token']}`", color=0xff0000)
    embed.set_author(name="YourBot", icon_url="https://cdn.discordapp.com/attachments/877796755234783273/879295069834850324/Avatar.png")
    embed.set_thumbnail(url="https://user-images.githubusercontent.com/36286877/127767330-d3e68d90-67a0-4672-b3e1-6193b323bc21.png")
    embed.set_footer(text="Requested by {ctx.author.name}")
    await loading_message.delete()
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



@client.command(aliases=["show-help", "showhelp", "needhelp", "need-help", "pls-help", "plshelp", "helpo"])
async def Help(ctx, category="none"):
  loading_message = await ctx.send(embed=please_wait_emb)
  bp = bot_prefix
  help_1 = f"""{bp}ping -> Will show the ping of the bot"
{bp}clear 5 -> will clear the last 5 messages
{bp}8ball -> will tell something about anything ({bp}8ball can i pass my exams?)
{bp}kick @user -> will kick the user
{bp}ban @user -> will ban the user
{bp}unban user#1981 -> will unban the user (if banned)
{bp}inspire -> give an inspiring quote
{bp}inv -> send invite link of the bot
{bp}fake help -> show the fake info generating command list
{bp}ip 192.168.0.1 -> will show information about any public IP address
{bp}mfp 3 -> will create 3 fake profiles
{bp}pervert -> show some perverty text
{bp}nitro 5 -> will send 5 random nitro codes
{bp}spam 10 lol -> will spam "lol" for 10 times
{bp}bored -> will give a task for you to do with additional info
{bp}color -> generate a random color
{bp}btc -> get the current bitcoin prices
{bp}wiki Sri Lanka -> will send the first two sentences about "Sri Lanka" from wikipedia
{bp}tinyurl https://youtube.com -> will shorten the given link and send it ( with tinyurl )
{bp}joke -> get a random joke
{bp}iconserver -> will send the server icon to the chat
{bp}mac ff-ff-ff-ff-ff-ff -> will show information about the given mac address
{bp}bitcoin -> will show more information about bitcoin rates
{bp}eth -> show etherium values
{bp}wyr -> a fun thing ( would you rather )
{bp}hastebin Hello ssup -> will add the text to a hastebin and send the link
{bp}ascii test -> will convert any text given to an ASCII art (in this case, its "test")
{bp}asciiart test -> will send a ascii art ( same as {bp}ascii but different style)
"""

  help_2 = f"""{bp}lesbian -> will send lesbian gis and pics (NSFW)
{bp}anal -> will send anal (NSFW)
{bp}erofeet -> will send erofeet (NSFW)
{bp}feet -> will send feet pics and gifs (NSFW)
{bp}hentai -> will send hentai (NSFW)
{bp}boobs -> will send boobs (NSFW)
{bp}tits -> send tits / boobs (NSFW)
{bp}blowjob -> will send blowjb pics and gifs (NSFW)
{bp}lewd -> will send lewds (NSFW)
{bp}cleanuri https://google.com -> will send the shortened link made with cleanuri
{bp}genpwd 16 -> will generate you a very random secure password
{bp}pwdc [passwordhere] -> will check your password in a 10 million password database - Thanks to NoPe
{bp}pwdsc [passwordhere] -> will check the strength of your password
{bp}advice -> will give you a random advice!
{bp}chuckjoke -> will tell a Chuck Norris Joke
{bp}poll are you ok? -> will create poll with the given text so the users can vote
{bp}csnd -> will send a message with some white spacing at middle to clear the screen of unwated stuff without deleting
{bp}covid -> will send global covid information
{bp}covidlow -> will send main global covid information
{bp}covidlk -> will send Sri Lankan Covid information 
{bp}afk title -> UNDER DEVELOPMENT! NOT RECOMMENDED TO USE!
{bp}slowmode 5 -> with change the channel slowdown to 5 seconds
{bp}newemoji emoji_name https://emoji-link.emoji.png png -> the last parameter is for the file extension
{bp}make_server_new_roles -> will create the main roles needed for a new discord server ( no colored roles ) - kind of a template to get started
{bp}howpropose name -> will tell you how to propose to "name"
{bp}countryinfo lk -> will tell you information about Sri Lanka (sg for Singapore, etc...)
{bp}uptime -> will show the bots uptime
"""

  help_nsfw = f"""{bp}feed @user -> will send it in an embed by tagging the user
{bp}tickle @user -> will send it in an embed by tagging the user
{bp}hit @user -> will send an imaege in an embed by tagging the user
{bp}hug @user -> will send it in an embed by tagging the user
{bp}smug @user -> will send it in an embed by tagging the user
{bp}pat @user -> will send it in an embed by tagging the user
{bp}kiss @user -> will send it in an embed by tagging the user
{bp}reverse hello -> will send reverse the message (in this case, output is "olleh")
{bp}tableflip -> will delete your message and send '(╯°□°）╯︵ ┻━┻'
{bp}unflip -> will delete your message and send '┬─┬ ノ( ゜-゜ノ)'
{bp}goodnight -> will delete your message and send '✩⋆｡ ˚ᎶᎾᎾⅅ ℕᏐᎶℍᎢ⋆｡˚✩'
{bp}smile -> will delete your message and send '˙ ͜ʟ˙'
{bp}iloveu -> will delete your message and send '(๑′ᴗ‵๑)Ｉ Lᵒᵛᵉᵧₒᵤ♥'
{bp}sword -> will delete your message and send 'ס₪₪₪₪§|(Ξ≥≤≥≤≥≤ΞΞΞΞΞΞΞΞΞΞ>'
{bp}what -> will delete your message and send '( ʘ̆ ╭͜ʖ╮ ʘ̆ )'
{bp}fuckyou -> will delete your message and send '╭∩╮(･◡･)╭∩╮'
{bp}dick -> will send a random dick size
{bp}ig_pfp ig_user_name -> Get the profile picture of any existing instagram profile
{bp}guessage Name -> will gues the age of the name, show the number of people with the same name
{bp}face -> generate a random face!
{bp}sherlock key -> will send all social profiles of "key" username. still in BETA, not all links work!
{bp}checkpassword Password^&GoesHere#! -> will tell how strong your passowrd is!
"""

  help_3 = f"""{bp}panda -> will send a random panda image
{bp}meme -> will send a random meme
{bp}dog -> will send a random dog image
{bp}cat -> will send a random cat image
{bp}dogfact -> will send a random fact about dogs
{bp}catfact -> will send a random fact about cats
{bp}elephantfact -> will send a random fact elephants
{bp}pandafact -> will send a random fact about pandas
{bp}foxfact -> will send a random fact about foxes
{bp}birdfact -> will send a random fact about birds
{bp}koalafact -> will send a random fact about koala bears
{bp}redpanda -> will send a random redpanda image
{bp}fox -> will send a random fox image
{bp}wink -> will send a random anime image
{bp}pikachu -> will send a random pikachu image
{bp}mute @user -> will mute the user, anyone with perms will have to unmute manually!
{bp}slap @user reason -> will slap the user with a resaon
{bp}daddy -> get some hot pictures!
{bp}cnick @user lol -> will change the username of @user to "lol"
{bp}txt1 - txt63 -> make the bot say some Kaomoji
{bp}sendmail [your-email] [reciever-email] [subject-with-no-spaces] [email-content]` - Send an email, we ask for your email for the reciever to be clear who this is!
"""

  help_4 = f"""{bp}gay https://i.imgur.com/nToSGkI.png -> will add a gay rgb theme to the image in the link ( links should be direct )
{bp}glass https://i.imgur.com/nToSGkI.png -> will a glassy theme onto the image in the link ( the link should be direct )
{bp}wasted https://i.imgur.com/nToSGkI.png -> will add the GTA wasted effect the the image in the link ( the link should be direct )
{bp}triggered https://i.imgur.com/nToSGkI.png -> will add the triggered effect to the image in the link ( the link should be direct )
{bp}grayscale https://i.imgur.com/nToSGkI.png -> will make the image black and white in the link ( the link should be direct )
{bp}invert https://i.imgur.com/nToSGkI.png -> will make the colors inverted to the image in the link ( the link should be direct )
{bp}brightness https://i.imgur.com/nToSGkI.png -> will make the image bright in the link ( the link should be direct )
{bp}threshold https://i.imgur.com/nToSGkI.png -> will increase the throshold of the image (black and white) to the image in the link ( the link should be direct )
{bp}sepia https://i.imgur.com/nToSGkI.png -> will add the sepia effect to the image in the link ( the link should be direct )
{bp}red https://i.imgur.com/nToSGkI.png -> will add a red tint to the image in the link ( the link should be direct )
{bp}green https://i.imgur.com/nToSGkI.png -> will add a green tint to the image in the link ( the link should be direct )
{bp}blue https://i.imgur.com/nToSGkI.png -> will add a blue tint to the image in the link ( the link should be direct )
{bp}tint dc80cb https://i.imgur.com/nToSGkI.png -> will add a (hex) dc80cb colored tint to the image in the link ( the link should be direct )
{bp}pixelate https://i.imgur.com/nToSGkI.png -> will piexelate the image in the link ( the link should be direct )
{bp}ytcomment User_Name Comment_goes_here https://profile.pciture/jpg/png/jpeg -> keep one space within the words, the profile picture link is optional, use "_" instead of " "(spaces)"""

  help_5 = f"""{bp}pokemon pikachu -> will send information about pikachu
{bp}minecraftinfo beast -> wil send public information about the minecraft profile named "beast"
{bp}lyricsof who let the dogs out  -> will send the song name, author, lyrics, genius link ( if there is one )
{bp}av @user -> will send the avatar of @user
{bp}serverinfo -> will send server information (in the server where the bot is in)
{bp}guildicon -> will send the server icon
{bp}accdate @user -> will send the accoutn creation date of @user ({bp}userinfo shows all of them )
{bp}userinfo @user -> will send all public account information
{bp}e_b64 hello -> will encode the given text to Base64
{bp}e_md5 hello -> will encode the given text to MD5
{bp}e_sha1 hello -> will encode the given text to SHA1
{bp}e_sha224 hello -> will encode the given text to SHA224
{bp}e_sha512 hello -> will encode the given text to SHA512
{bp}leet hello -> will encode the given text to leet format
{bp}e_binary hello -> will encode the text to binary
{bp}d_binary 01001 -> will decode the binary to text
{bp}d_b64 aGlydXNoYQ== -> will decode this to text
{bp}add 4 5 -> will add 4 to 5 and send the answer as 9
{bp}subs 5 4 -> will substract 5 from 4 and send the answer as 1
{bp}mul 2 3 -> will multiply 2 and 3 and send the answer as 6
{bp}div 4 2 -> will divite 4 from 2 and send the answer as 4
{bp}monstor -> will send a random pic of a pixel monstor
{bp}howdie @user -> will predict how the user will die
{bp}chatbot -> will send you the steps of configuring it!
{bp}google [what_to_search] -> you can get a direct google link in search of this!
{bp}wordcount passage in here -> will send you the number of words, in this case, its three
"""

  old_wl = ("old", "og")
  mod_wl = ("mod", "moderation", "admin", "administration")
  info_wl = ("info", "find", "information")
  nsfw_wl = ("nsfw", "porn", "pornstuff", "sex", "fap", "finger")
  others_wl = ("others", "fun", "funny", "other")
  images_wl = ("images", "img", "imgs", "image", "imagestuff")
  text_wl = ("text", "txt", "txtstuff", "textstuff")
  enc_wl = ("enc", "econding", "encode", "decode", "dec", "decoding")
  math_wl = ("maths", "math", "mathematics")
  imgfx_wl = ("imageeffects", "imgfx", "imagefx", "imageeffect", "imgfxstuff", "effects", "imgfxs", "imgfun")
  animals_wl = ("animal", "animals", "pet", "pets")
  all_small_list = ("all", "everything")
  music_cmnds_list = ("music", "songs", "song", "sing")

  if category.lower() in old_wl:
    await loading_message.delete()
    await ctx.send("```" + help_1 + "```")
    await ctx.send("```" + help_2 + "```")
    await ctx.send("```" + help_nsfw + "```")
    await ctx.send("```" + help_3 + "```")
    await ctx.send("```" + help_4 + "```")
    await ctx.send("```" + help_5 + "```")

  elif category == "none":
    em1 = discord.Embed(title=f'Help', description=f'use {bp}Help [category]', color=0xff0000)
    em1.set_thumbnail(url=bot_info_cmnd_thumbnail_link)
    em1.add_field(name=f'Moderation', value=f'`{bp}Help mod`')
    em1.add_field(name=f'Information', value=f'`{bp}Help info`')
    em1.add_field(name=f'NSFW', value=f'`{bp}Help nsfw`')
    em1.add_field(name=f'Images', value=f'`{bp}Help img`')
    em1.add_field(name=f'Text', value=f'`{bp}Help txt`')
    em1.add_field(name=f'Encoding and Decoding', value=f'`{bp}Help enc`')
    em1.add_field(name=f'Mathematics', value=f'`{bp}Help math`')
    em1.add_field(name=f'Image Effects and Fun stuff', value=f'`{bp}Help imgfx`')
    em1.add_field(name=f'Animals', value=f'`{bp}Help animals`')
    em1.add_field(name=f'Others', value=f'`{bp}Help others`')
    em1.add_field(name=f'ABOUT', value=f'`{bp}info` To see bot information!')
    em1.add_field(name=f'NOTE', value=f'This bot is free and open source - use `{bp}info`')
    await loading_message.delete()
    await ctx.send(embed=em1)

  elif category.lower() in mod_wl:
    em2 = discord.Embed(title=f'Moderation', description=f'use >Help [category]', color=0xff0000)
    em2.set_thumbnail(url=bot_info_cmnd_thumbnail_link)
    em2.add_field(name=f'{bp}kick', value=f'`{bp}kick [user]` - Kick a user from the server', inline=True)
    em2.add_field(name=f'{bp}ban', value=f'`{bp}ban [user]` - Ban a user from the server', inline=True)
    em2.add_field(name=f'{bp}unban', value=f'`{bp}unban [user#1981]` - Kick a user from the server', inline=True)
    em2.add_field(name=f'{bp}spam', value=f'`{bp}spam [how_many] [message]` - Spam Messages', inline=True)
    em2.add_field(name=f'{bp}clear', value=f'`{bp}clear [number_of_msges]`- Delete messages from a channel', inline=True)
    em2.add_field(name=f'{bp}make_server_new_roles', value=f'`{bp}make_server_new_roles` - Creates the primary roles needed for a new server!', inline=True)
    em2.add_field(name=f'{bp}newemoji', value=f'`{bp}newemoji [emoji_name] [link] [file_extension]`- Add a new emoji to the server', inline=True)
    em2.add_field(name=f'{bp}slowmode', value=f'`{bp}slowmode [no_of_seconds]`- Add a new emoji to the server', inline=True)
    em2.add_field(name=f'{bp}cnick', value=f'`{bp}slowmode [@user] [new_nickname]`- Change the nickname of a user', inline=True)
    em2.add_field(name=f'{bp}slap', value=f'`{bp}slap [@user] [reason]`- Warn a user', inline=True)
    em2.add_field(name=f'{bp}mute', value=f'`{bp}mute [@user]`- Mute a member', inline=True)
    await loading_message.delete()
    await ctx.send(embed=em2)
    
  elif category.lower() in info_wl:
    em3 = discord.Embed(title=f'Information', description=f'use >Help [category]', color=0xff0000)
    em3.set_thumbnail(url=bot_info_cmnd_thumbnail_link)
    em3.add_field(name=f'{bp}fake', value=f'`{bp}fake [argument]` - Generate Fake Information', inline=True)
    em3.add_field(name=f'{bp}mfp', value=f'`{bp}mfp [no_of_time]` - Will generate the given number of fake user profiles ( Mass Fake Profile )', inline=True)
    em3.add_field(name=f'{bp}ip', value=f'`{bp}ip [ip_address]` - Get Information of any IPv4 address', inline=True)
    em3.add_field(name=f'{bp}mac', value=f'`{bp}mac [mac_address]` - Get Information of any IPv4 address', inline=True)
    em3.add_field(name=f'{bp}bitcoin', value=f'`{bp}bitcoin` - Current Bitcoin Prices', inline=True)
    em3.add_field(name=f'{bp}eth', value=f'`{bp}eth` - Current Etherium Prices', inline=True)
    em3.add_field(name=f'{bp}eth', value=f'`{bp}eth` - Current Etherium Prices', inline=True)
    em3.add_field(name=f'{bp}covid', value=f'`{bp}covid` - All Global Covid Info', inline=True)
    em3.add_field(name=f'{bp}covidlow', value=f'`{bp}covidlow` - Main Global Covid Info', inline=True)
    em3.add_field(name=f'{bp}covidlk', value=f'`{bp}covidlk` - Sri Lankan Covid Info', inline=True)
    em3.add_field(name=f'{bp}minecraftinfo', value=f'`{bp}minecraftinfo [mc_username]` - Information about any minecraft profile/account', inline=True)
    em3.add_field(name=f'{bp}pokemon', value=f'`{bp}pokemon [type]` - Information about any pokemon', inline=True)
    em3.add_field(name=f'{bp}lyricsof', value=f'`{bp}lyricsof [songs_name]` - Lyrics of any song', inline=True)
    em3.add_field(name=f'{bp}av', value=f'`{bp}av [@user_or_id]` - Get the profile picture of any user', inline=True)
    em3.add_field(name=f'{bp}serverinfo', value=f'`{bp}serverinfo` - Current server Information', inline=True)
    em3.add_field(name=f'{bp}guildicon', value=f'`{bp}guildicon` - Current server icon', inline=True)
    em3.add_field(name=f'{bp}accdate', value=f'`{bp}accdate [@user]` - See the account creation date', inline=True)
    em3.add_field(name=f'{bp}userinfo', value=f'`{bp}userinfo [@user]` - See the public account information', inline=True)
    em3.add_field(name=f'{bp}ig_pfp', value=f'`{bp}ig_pfp [@ig_username]` - Get the Instagram profile picture of anyone!', inline=True)
    em3.add_field(name=f'{bp}sherlock', value=f'`{bp}sherlock [any_username]` - Search for social media profiles of the username', inline=True)
    em3.add_field(name=f'{bp}pwdc', value=f'`{bp}pwdc [password]` - Check your password in a 10 million password database | Thanks to NoPe', inline=True)
    em3.add_field(name=f'{bp}pwdsc', value=f'`{bp}pwdsc [password]` - Check the strength of your password', inline=True)
    await loading_message.delete()
    await ctx.send(embed=em3)

  elif category.lower() in nsfw_wl:
    em4 = discord.Embed(title=f'NSFW', description=f'use >Help [category]', color=0xff0000)
    em4.set_thumbnail(url=bot_info_cmnd_thumbnail_link)
    em4.add_field(name=f'{bp}lesbian', value=f'`{bp}lebsian` - Send Images/GIFs', inline=True)
    em4.add_field(name=f'{bp}anal', value=f'`{bp}anal` - Send Images/GIFs', inline=True)
    em4.add_field(name=f'{bp}feet', value=f'`{bp}feet` - Send Images/GIFs', inline=True)
    em4.add_field(name=f'{bp}hentai', value=f'`{bp}hentai` - Send Images/GIFs', inline=True)
    em4.add_field(name=f'{bp}boobs', value=f'`{bp}boobs` - Send Images/GIFs', inline=True)
    em4.add_field(name=f'{bp}tits', value=f'`{bp}tits` - Send Images/GIFs', inline=True)
    em4.add_field(name=f'{bp}blowjob', value=f'`{bp}blowjob` - Send Images/GIFs', inline=True)
    em4.add_field(name=f'{bp}lewd', value=f'`{bp}lewd` - Send Images/GIFs', inline=True)
    em4.add_field(name=f'{bp}pervert', value=f'`{bp}pervert` - Send a fun text', inline=True)
    em4.add_field(name=f'{bp}dick', value=f'`{bp}dick` - Guess your dick size', inline=True)
    em4.add_field(name=f'{bp}daddy', value=f'`{bp}daddy` - Get something hot', inline=True)
    await loading_message.delete()
    await ctx.send(embed=em4)
  
  elif category.lower() in others_wl:
    em5 = discord.Embed(title=f'Others', description=f'use >Help [category]', color=0xff0000)
    em5.set_thumbnail(url=bot_info_cmnd_thumbnail_link)
    em5.add_field(name=f'{bp}ping', value=f'`{bp}ping` - Show the ping/response time of the bot', inline=True)
    em5.add_field(name=f'{bp}8ball', value=f'`{bp}8ball [any_question]` - The simple 8ball game', inline=True)
    em5.add_field(name=f'{bp}inspire', value=f'`{bp}inspire` - Give you an inspiring quote', inline=True)
    em5.add_field(name=f'{bp}inv', value=f'`{bp}inv` - get the Bot Invite Link', inline=True)
    em5.add_field(name=f'{bp}nitro', value=f'`{bp}nitro [no_of_nitro_codes]` - Generate random Nitro Codes', inline=True)
    em5.add_field(name=f'{bp}bored', value=f'`{bp}bored` - Will give you a task to do', inline=True)
    em5.add_field(name=f'{bp}color', value=f'`{bp}color` - Generate a Random Color', inline=True)
    em5.add_field(name=f'{bp}wiki', value=f'`{bp}wiki [any_thing]` - First 2 sentences about the given thing in WikiPedia', inline=True)
    em5.add_field(name=f'{bp}tinyurl', value=f'`{bp}tinyurl [any_url]` - Generate Shortened Link', inline=True)
    em5.add_field(name=f'{bp}cleanuri', value=f'`{bp}cleanuri [any_url]` - Generate Shortened Link', inline=True)
    em5.add_field(name=f'{bp}joke', value=f'`{bp}joke` - Want a good joke to laugh??', inline=True)
    em5.add_field(name=f'{bp}iconserver', value=f'`{bp}iconserver` - Send the server icon', inline=True)
    em5.add_field(name=f'{bp}wyr', value=f'`{bp}wyr` - the Simple Would you rather game', inline=True)
    em5.add_field(name=f'{bp}hastbin', value=f'`{bp}hastbin [any_text]` - Create a hastebin with the text you enter', inline=True)
    em5.add_field(name=f'{bp}ascii', value=f'`{bp}ascii [any_text]` - Create a ASCII Art', inline=True)
    em5.add_field(name=f'{bp}asciiart', value=f'`{bp}asciiart [any_text]` - Create a ASCII Art ( different style )', inline=True)
    em5.add_field(name=f'{bp}guessage', value=f'`{bp}guessage [name]` - Guess the age from the name given', inline=True)

    # em7 = discord.Embed(title=f'Others Part 2', description=f'use >Help [category]')
    # em7.set_thumbnail(url=bot_info_cmnd_thumbnail_link)
    em5.add_field(name=f'{bp}advice', value=f'`{bp}feed` - Get a random advice', inline=True)
    em5.add_field(name=f'{bp}chuckjoke', value=f'`{bp}chuckjoke` - Get a random Chuck Joke', inline=True)
    em5.add_field(name=f'{bp}poll', value=f'`{bp}poll [question]` - Create a poll', inline=True)
    em5.add_field(name=f'{bp}csnd', value=f'`{bp}csnd` - Clear the screen without deleting any message', inline=True)
    em5.add_field(name=f'{bp}howdie', value=f'`{bp}howdie [@user]` - Will predict how someone will die', inline=True)
    em5.add_field(name=f'{bp}chatbot', value=f'`{bp}chatbot` - Will give you the steps to configure the chatbot to your server', inline=True)
    em5.add_field(name=f'{bp}countryinfo', value=f'`{bp}countryinfo [country_code]` - Will send information about the given country, ex=lk, sg, eu', inline=True)
    em5.add_field(name=f'{bp}audio', value=f'`{bp}audio [yt-link]` - Send the m4a (like mp3) of the file!', inline=True)
    em5.add_field(name=f'{bp}sendmail', value=f'`{bp}sendmail [your-email] [reciever-email] [subject-with-no-spaces] [email-content]` - Send an email, we ask for your email for the reciever to be clear who this is!', inline=True)

    await loading_message.delete()
    await ctx.send(embed=em5)
    # await ctx.send(embed=em7)

  elif category.lower() in images_wl:
    em6 = discord.Embed(title=f'Images', description=f'use >Help [category]', color=0xff0000)
    em6.set_thumbnail(url=bot_info_cmnd_thumbnail_link)
    em6.add_field(name=f'{bp}meme', value=f'`{bp}meme` - a Good Funni Meme', inline=True)
    em6.add_field(name=f'{bp}feed', value=f'`{bp}feed [@user]` - Send an Image/GIF', inline=True)
    em6.add_field(name=f'{bp}tickle', value=f'`{bp}tickle [@user]` - Send an Image/GIF', inline=True)
    em6.add_field(name=f'{bp}hit', value=f'`{bp}hit [@user]` - Send an Image/GIF', inline=True)
    em6.add_field(name=f'{bp}hug', value=f'`{bp}hug [@user]` - Send an Image/GIF', inline=True)
    em6.add_field(name=f'{bp}smug', value=f'`{bp}smug [@user]` - Send an Image/GIF', inline=True)
    em6.add_field(name=f'{bp}pat', value=f'`{bp}pat [@user]` - Send an Image/GIF', inline=True)
    em6.add_field(name=f'{bp}kiss', value=f'`{bp}kiss [@user]` - Send an Image/GIF', inline=True)
    em6.add_field(name=f'{bp}monstor', value=f'`{bp}monstor` - Send an Image/GIF', inline=True)
    em6.add_field(name=f'{bp}wink', value=f'`{bp}wink` - Send an Image/GIF', inline=True)
    em6.add_field(name=f'{bp}face', value=f'`{bp}face [gender-optional]` - Send an Image of a Face with Age, Name, Gender!', inline=True)
    await loading_message.delete()
    await ctx.send(embed=em6)

  elif category.lower() in text_wl:
    em8 = discord.Embed(title=f'Text', description=f'use >Help [category]', color=0xff0000)
    em8.set_thumbnail(url=bot_info_cmnd_thumbnail_link)
    em8.add_field(name=f'{bp}genpwd', value=f'`{bp}genpwd [no_of_letters]` - Generate a very secure password', inline=True)
    em8.add_field(name=f'{bp}reverse', value=f'`{bp}reverse [any_text]` - Reverse text', inline=True)
    em8.add_field(name=f'{bp}say', value=f'`{bp}say [any_message]` - Delete your message and the bot will send it like he says it', inline=True)
    em8.add_field(name=f'{bp}tableflip', value=f'`{bp}tableflip` - Bot will send `(╯°□°）╯︵ ┻━┻` after deleting your message', inline=True)
    em8.add_field(name=f'{bp}unflip', value=f'`{bp}unflip` - Bot will send `┬─┬ ノ( ゜-゜ノ)` after deleting your message', inline=True)
    em8.add_field(name=f'{bp}goodnight', value=f'`{bp}goodnight` - Bot will send `✩⋆｡ ˚ᎶᎾᎾⅅ ℕᏐᎶℍᎢ⋆｡˚✩` after deleting your message', inline=True)
    em8.add_field(name=f'{bp}smile', value=f'`{bp}smile` - Bot will send `˙ ͜ʟ˙` after deleting your message', inline=True)
    em8.add_field(name=f'{bp}iloveu', value=f'`{bp}iloveu` - Bot will send `(๑′ᴗ‵๑)Ｉ Lᵒᵛᵉᵧₒᵤ♥` after deleting your message', inline=True)
    em8.add_field(name=f'{bp}sword', value=f'`{bp}sword` - Bot will send `ס₪₪₪₪§|(Ξ≥≤≥≤≥≤ΞΞΞΞΞΞΞΞΞΞ>` after deleting your message', inline=True)
    em8.add_field(name=f'{bp}what', value=f'`{bp}what` - Bot will send ( ʘ̆ ╭͜ʖ╮ ʘ̆ )` after deleting your message', inline=True)
    em8.add_field(name=f'{bp}fuckyou', value=f'`{bp}fuckyou` - Bot will send `╭∩╮(･◡･)╭∩╮` after deleting your message', inline=True)
    em8.add_field(name=f'{bp}howpropose', value=f'`{bp}howpropose [name]` - Will tell you how to propose to [name]', inline=True)
    em8.add_field(name=f'{bp}wordcount', value=f'`{bp}wordcount [words in here]` - Will count the number of words, seperated by spaces!', inline=True)
    em8.add_field(name=f'{bp}google', value=f'`{bp}google [query]` - Will send a direct link to Google Search query', inline=True)
    em8.add_field(name=f'{bp}txt1 - txt63', value=f'`{bp}txt1 - txt63` - Make the bot say some Kaomoji', inline=True)
    em8.add_field(name=f'{bp}bottoken', value=f'`{bp}bottoken` - Generate a dummy discord bot token', inline=True)
    em8.add_field(name=f'{bp}joke2', value=f'`{bp}joke2` - a Good Funni Joke', inline=True)
    await loading_message.delete()
    await ctx.send(embed=em8)
  
  elif category.lower() in enc_wl:
    em9 = discord.Embed(title=f'Encoding and Decoding', description=f'use >Help [category]', color=0xff0000)
    em9.set_thumbnail(url=bot_info_cmnd_thumbnail_link)
    em9.add_field(name=f'{bp}e_b64', value=f'`{bp}e_b64 [any_text]` - Convert to Base64', inline=True)
    em9.add_field(name=f'{bp}e_md5', value=f'`{bp}e_md5 [any_text]` - Convert to MD5', inline=True)
    em9.add_field(name=f'{bp}e_sha1', value=f'`{bp}e_sha1 [any_text]` - Convert to SHA1', inline=True)
    em9.add_field(name=f'{bp}e_sha224', value=f'`{bp}e_sha224 [any_text]` - Convert to SHA224', inline=True)
    em9.add_field(name=f'{bp}e_sha512', value=f'`{bp}e_sha512 [any_text]` - Convert to SHA512', inline=True)
    em9.add_field(name=f'{bp}leet', value=f'`{bp}leet [any_text]` - Convert to L33T', inline=True)
    em9.add_field(name=f'{bp}e_binary', value=f'`{bp}e_binary [any_text]` - Convert to Binary', inline=True)
    em9.add_field(name=f'{bp}d_binary', value=f'`{bp}d_binary [binary]` - Convert From binary to text', inline=True)
    em9.add_field(name=f'{bp}d_b64', value=f'`{bp}d_b64 [b64]` - Convert From Base64 to text', inline=True)
    await loading_message.delete()
    await ctx.send(embed=em9)

  elif category.lower() in math_wl:
    em10 = discord.Embed(title=f'Maths', description=f'use >Help [category]', color=0xff0000)
    em10.set_thumbnail(url=bot_info_cmnd_thumbnail_link)
    em10.add_field(name=f'{bp}add', value=f'`{bp}add [no_1] [no_2]` - Add two number', inline=True)
    em10.add_field(name=f'{bp}subs', value=f'`{bp}subs [no_1] [no_2]` - Substract two number', inline=True)
    em10.add_field(name=f'{bp}mul', value=f'`{bp}mul [no_1] [no_2]` - Multiply two number', inline=True)
    em10.add_field(name=f'{bp}div', value=f'`{bp}div [no_1] [no_2]` - Divide two number', inline=True)
    await loading_message.delete()
    await ctx.send(embed=em10)

  elif category.lower() in imgfx_wl:
    em11 = discord.Embed(title=f'Image Effects', description=f'use >Help [category]', color=0xff0000)
    em11.set_thumbnail(url=bot_info_cmnd_thumbnail_link)
    em11.add_field(name=f'{bp}gay', value=f'`{bp}gay [image_link]` - Apply the effect', inline=True)
    em11.add_field(name=f'{bp}glass', value=f'`{bp}glass [image_link]` - Apply the effect', inline=True)
    em11.add_field(name=f'{bp}wasted', value=f'`{bp}wasted [image_link]` - Apply the effect', inline=True)
    em11.add_field(name=f'{bp}triggered', value=f'`{bp}triggered [image_link]` - Apply the effect', inline=True)
    em11.add_field(name=f'{bp}grayscale', value=f'`{bp}grayscale [image_link]` - Apply the effect', inline=True)
    em11.add_field(name=f'{bp}invert', value=f'`{bp}invert [image_link]` - Apply the effect', inline=True)
    em11.add_field(name=f'{bp}brightness', value=f'`{bp}brightness [image_link]` - Apply the effect', inline=True)
    em11.add_field(name=f'{bp}threshold', value=f'`{bp}threshold [image_link]` - Apply the effect', inline=True)
    em11.add_field(name=f'{bp}sepia', value=f'`{bp}sepia [image_link]` - Apply the effect', inline=True)
    em11.add_field(name=f'{bp}red', value=f'`{bp}red [image_link]` - Apply the tint', inline=True)
    em11.add_field(name=f'{bp}green', value=f'`{bp}green [image_link]` - Apply the tint', inline=True)
    em11.add_field(name=f'{bp}blue', value=f'`{bp}blue [image_link]` - Apply the tint', inline=True)
    em11.add_field(name=f'{bp}tint', value=f'`{bp}blue [hex_color_no#] [image_link]` - Apply the tint with any color. Dont mention "#" when giving the hash', inline=True)
    em11.add_field(name=f'{bp}pixelate', value=f'`{bp}pixelate [image_link]` - Pixelate', inline=True)
    em11.add_field(name=f'{bp}ytcomment', value=f'`{bp}ytcomment [acc_name] [comment] [profile_picture_link]` - Create a fake image of a youtube comment, pfp link is not required', inline=True)
    em11.add_field(name=f'{bp}twittercomment', value=f'`{bp}twittercomment [username] [display_name] [profile_picture_link] [comment]` - Create a fake image of a youtube comment, pfp link is not required', inline=True)
    await loading_message.delete()
    await ctx.send(embed=em11)
  
  elif category.lower() in animals_wl:
    em12 = discord.Embed(title=f'Animals', description=f'use >Help [category]', color=0xff0000)
    em12.set_thumbnail(url=bot_info_cmnd_thumbnail_link)
    em12.add_field(name=f'{bp}dog', value=f'`{bp}dog` - Get a Image', inline=True)
    em12.add_field(name=f'{bp}panda', value=f'`{bp}panda` - Get a Image', inline=True)
    em12.add_field(name=f'{bp}cat', value=f'`{bp}cat` - Get a Image', inline=True)
    em12.add_field(name=f'{bp}fox', value=f'`{bp}fox` - Get a Image', inline=True)
    em12.add_field(name=f'{bp}dogfact', value=f'`{bp}dogfact` - Get a Fact', inline=True)
    em12.add_field(name=f'{bp}catfact', value=f'`{bp}catfact` - Get a Fact', inline=True)
    em12.add_field(name=f'{bp}elephantfact', value=f'`{bp}elephantfact` - Get a Fact', inline=True)
    em12.add_field(name=f'{bp}pandafact', value=f'`{bp}pandafact` - Get a Fact', inline=True)
    em12.add_field(name=f'{bp}foxfact', value=f'`{bp}foxfact` - Get a Fact', inline=True)
    em12.add_field(name=f'{bp}birdfact', value=f'`{bp}birdfact` - Get a Fact', inline=True)
    em12.add_field(name=f'{bp}koalafact', value=f'`{bp}koalafact` - Get a Fact', inline=True)
    em12.add_field(name=f'{bp}redpanda', value=f'`{bp}redpanda` - Get a Image', inline=True)
    em12.add_field(name=f'{bp}raccoon', value=f'`{bp}raccoon` - Get a Image', inline=True)
    em12.add_field(name=f'{bp}raccoonfact', value=f'`{bp}raccoonfact` - Get a Fact', inline=True)
    em12.add_field(name=f'{bp}kangaroo', value=f'`{bp}kangaroo` - Get a Image', inline=True)
    em12.add_field(name=f'{bp}kangaroofact', value=f'`{bp}kangaroofact` - Get a Fact', inline=True)
    em12.add_field(name=f'{bp}whalefact', value=f'`{bp}whalefact` - Get a Fact', inline=True)
    await loading_message.delete()
    await ctx.send(embed=em12)
  
  elif category.lower() in all_small_list:
    em13 = discord.Embed(title=f'Animals', description=f'use >Help [category]', color=0xff0000)
    em13.set_thumbnail(url=bot_info_cmnd_thumbnail_link)
    em13.add_field(name=f"Moderation", value=f"`{bp}kick [user]` \n`{bp}ban [@user]` \n`{bp}unban [user#id]` \n`{bp}spam [how-many] [message]` \n`{bp}clear [no-to-del]` \n`{bp}make_server_new_roles` \n`{bp}newemoji [name] [link] [file-ext]` \n`{bp}slowmode [amt-in-secs]` \n`{bp}cnick [user] [new-nickname]` \n`{bp}slap [user] [reason]` \n`{bp}mute [user]`", inline=False)
    em13.add_field(name=f"Information", value=f"`{bp}fake [arg]` \n`{bp}mfp [number]` \n`{bp}ip [ip-addr]` \n`{bp}mac [mac-addr]` \n`{bp}bitcoin` \n`{bp}eth` \n`{bp}covid` \n`{bp}covidlow` \n`{bp}covidlk` \n`{bp}minecraftinfo [mc-uname]` \n`{bp}pokemon [type]` \n`{bp}lyricsof [song-name]` \n`{bp}av [user]` \n`{bp}serverinfo` \n`{bp}guildicon` \n`{bp}accdate [user]` \n`{bp}userinfo [user]` \n`{bp}ig_pfp [ig-profile-name]` \n`{bp}sherlock [user]` \n`{bp}checkpassword` ", inline=False)
    em13.add_field(name=f"NSFW", value=f"`{bp}lesbian` \n`{bp}anal` \n`{bp}feet` \n`{bp}hentai` \n`{bp}boobs` \n`{bp}tits` \n`{bp}blowjob` \n`{bp}lewd` \n`{bp}pervert` \n`{bp}dick` \n`{bp}daddy` ", inline=False)
    em13.add_field(name=f"Images", value=f"`{bp}feed [user]` \n`{bp}meme` \n`{bp}tickle [user]` \n`{bp}hit [user]` \n`{bp}hug [user]` \n`{bp}smug [user]` \n`{bp}pat [user]` \n`{bp}kiss [user]` \n`{bp}monstor` \n`{bp}wink` \n`{bp}face` ", inline=False)
    em13.add_field(name=f"Image Effects", value=f"`{bp}glass [img-link]` \n`{bp}gay [img-link]` \n`{bp}wasted [img-link]` \n`{bp}triggered [img-link]` \n`{bp}grayscale [img-link]` \n`{bp}invert [img-link]` \n`{bp}brightness [img-link]` \n`{bp}threshold [img-link]` \n`{bp}sepia [img-link]` \n`{bp}red [img-link]` \n`{bp}green [img-link]` \n`{bp}blue [img-link]` \n`{bp}tint [hex-with-no-#]` \n`{bp}pixelate [img-link]` \n`{bp}ytcomment [acc-name] [comment] [pfp-link~optional]` \n`{bp}twittercomment [username] [display_name] [profile_picture_link] [comment]` ", inline=False)
    em13.add_field(name=f"Animals", value=f"`{bp}whalefact` \n`{bp}kangaroofact` \n`kangaroo` \n`raccoonfact` \n`raccoon` \n`{bp}dog` \n`{bp}panda` \n`{bp}cat` \n`{bp}fox` \n`{bp}dogfact` \n`{bp}catfact` \n`{bp}elephantfact` \n`{bp}pandafact` \n`{bp}foxfact` \n`{bp}birdfact` \n`{bp}koalafact` \n`{bp}redpanda`  ", inline=False )
    em13.add_field(name=f"Encoding/Decoding", value=f"`{bp}e_b64` \n`{bp}e_md5 [text]` \n`{bp}e_sha1 [text]` \n`{bp}e_sha224 [text]` \n`{bp}e_sha512 [text]` \n`{bp}leet [text]` \n`{bp}e_binary [text]` \n`{bp}d_binary [binary]` \n`{bp}d_b64 [b64]` ", inline=False )
    em13.add_field(name=f"Text", value=f"`{bp}joke2` \n`{bp}reverse [text]` \n`{bp}say [msg]` \n `{bp}txt1 - txt63` \n`{bp}tableflip` \n`{bp}unflip` \n`{bp}goodnight` \n`{bp}smile` \n`{bp}iloveyou` \n`{bp}sword` \n`{bp}what` \n`{bp}fuckyou` \n`{bp}howpropose [name]` \n`{bp}wordcount [words]` \n`{bp}google [query]` ", inline=False )
    em13.add_field(name=f"Fake Information", value=f"`{bp}face [gender~optional]` \n`{bp}fake high` \n`{bp}fake low` \n`{bp}fake help` \n`{bp}fake name` \n`{bp}fake dob` \n`{bp}fake addr` \n`{bp}fake job` \n`{bp}fake color` \n`{bp}fake zipcode` \n`{bp}fake city` \n`{bp}fake licenseplate` \n`{bp}fake bban` \n`{bp}fake iban` \n`{bp}fake bs` \n`{bp}fake cc` \n`{bp}fake cemail` \n`{bp}fake pno` \n`{bp}fake cp` \n`{bp}fake ssn` ", inline=False )
    em13.add_field(name=f"Some Mathematics", value=f"`{bp}add [no1] [no2]` \n`{bp}subs [no1] [no2]` \n`{bp}mul [no1] [no2]` \n`{bp}div [no1] [no2]` ", inline=False )
    em13.add_field(name="Music", value=f"`{bp}play [song-name]` \n`{bp}join` \n`{bp}leave` \n`{bp}skip` \n`{bp}summon [vc-name]` \n`{bp}now` \n`{bp}queue` \n`{bp}shuffle` \n`{bp}remove [index-from-queue]` \n`{bp}loop` ", inline=False)
    em13.add_field(name=f"Tools/Games", value=f"`{bp}genpwd [no-of-letters]` \n`{bp}pwdcheck [password_here]` - Thank you NoPe \n`{bp}pwdstrengthcheck [password_here]` \n`{bp}audio [yt-link]` \n`{bp}similiar [first] || [second]` \n`{bp}bottoken` \n `{bp}sendemail [your-email] [reciever-email] [subject-with-no-spaces] [email-content]` \n`ping` \n`{bp}8ball [question]` \n`{bp}inspire` \n`{bp}inv` \n`{bp}nitro [no-of-codes]` \n`{bp}bored` \n`{bp}color` \n`{bp}wiki [search-query]` \n`{bp}tinyurl [any-url]` \n`{bp}cleanuri [any-url]` \n`{bp}joke` \n`{bp}iconserver` \n`{bp}wyr [question]` \n`{bp}bastebin [text]` \n`{bp}ascii [text]` \n`{bp}asciiart [text]` \n`{bp}guessage [name]` \n`{bp}advice` \n`{bp}chuckjoke` \n`{bp}poll [question]` \n`{bp}csnd` \n`{bp}howdie [user]` \n`{bp}chatbot` \n`{bp}countryinfo [country-code]` ", inline=False)
    await loading_message.delete()
    await ctx.send(embed=em13)
  
  elif category.lower() in music_cmnds_list:
    em14 = discord.Embed(title=f'Music (BETA)', description=f'use >Help [category]', color=0xff0000)
    em14.set_thumbnail(url=bot_info_cmnd_thumbnail_link)
    em14.add_field(name=f'{bp}play', value=f'`{bp}play [song-name]` - Join to Voice Channel and play the song', inline=True)
    em14.add_field(name=f'{bp}join', value=f'`{bp}join` - Join Voice Channel', inline=True)
    em14.add_field(name=f'{bp}leave', value=f'`{bp}leave` - Leave Voice Channel', inline=True)
    # em14.add_field(name=f'{bp}pause', value=f'`{bp}pause` - Pause the paused music', inline=True)
    # em14.add_field(name=f'{bp}resume', value=f'`{bp}resume` - Resume the paused music', inline=True)
    # em14.add_field(name=f'{bp}stop', value=f'`{bp}stop` - Stop Playing', inline=True)
    em14.add_field(name=f'{bp}skip', value=f'`{bp}skip` - Skip the current playing song and go to the next', inline=True)
    em14.add_field(name=f'{bp}summon', value=f'`{bp}summon [vc-name]` - Make the bot join to a VC (Case Sensitive)', inline=True)
    em14.add_field(name=f'{bp}now', value=f'`{bp}now` - Displays the current playing song', inline=True)
    em14.add_field(name=f'{bp}queue', value=f'`{bp}queue` - Send the music queue waiting to be played!', inline=True)
    em14.add_field(name=f'{bp}shuffle', value=f'`{bp}shuffle` - Shuffle the queue', inline=True)
    em14.add_field(name=f'{bp}remove', value=f'`{bp}remove [index-from-queue]` - Remove a song from the queue', inline=True)
    em14.add_field(name=f'{bp}loop', value=f'`{bp}loop` - Loop the same song, use again to unloop', inline=True)
    await loading_message.delete()
    await ctx.send(embed=em14)


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
