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
# import asyncio
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

client.remove_command('help')

token = os.environ['TOKEN']

# THE FUNCTIONS BELOW ARE TO HELP THE MAIN COMMANDS!

def give_server_invite_link():
    bot_inv_link = botconfigdata["invite-link"]
    link = bot_inv_link
    return link

def give_nice_codes():
  code = ''.join(random.choices(string.ascii_letters + string.digits, k=16))
  return f'https://discord.gift/{code}'

def give_rand_color():
  randcolor = discord.Color(random.randint(0x000000, 0xFFFFFF))
  return randcolor

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

def FAKE_PROFILE(howmuchinfo):
  '''
options available: high, name, dob, job, address, color, zipcode, lisence plate, iban, bban, cc, pno, bs, cp, cemail, ssn, ua, low
  '''
  if howmuchinfo == "high":
    fake = Faker()
    simple_dict = fake.profile()
    fake_info_simple = "Name: " + str(simple_dict['name']) + "\nJob: " + str(simple_dict['job']) + "\nBirthdate: " + str(simple_dict['birthdate']) + "\nCompany: " + str(simple_dict['company']) + "\SSN: " + str(simple_dict['ssn']) + "\nRecidence: " + simple_dict['residence'] + "\nCurrent Location:" + str(simple_dict['current_location']) + "\nBlood Group: " + str(simple_dict['blood_group']) + "\nUsername: " + str(simple_dict['username']) + "\nAddress: " + str(simple_dict['address']) + "\nMail: " + str(simple_dict['mail'])
    return fake_info_simple

  elif howmuchinfo == "name":
    faker = Faker()
    try:
      USname = faker.name()
      return "Name: " + str(USname)
    except:
      return "Unable to generate a random name"

  elif howmuchinfo == "dob":
    faker = Faker()
    try:
      USdob = faker.date_of_birth()
      return "DOB: " + str(USdob)
    except:
      return "Unable to generate a random name"
  
  elif howmuchinfo == "addr":
    faker = Faker()
    try:
      USaddress = faker.address()
      return "Address: \n" + str(USaddress)
    except:
      return "Unable to generate a random address"
  
  elif howmuchinfo == "job":
    faker = Faker()
    try:
      USjob = faker.job()
      return "Job: " + str(USjob)
    except:
      return "Unable to generate a random job"
  
  elif howmuchinfo == "color":
    faker = Faker()
    try:
      USfavColor = faker.color_name()
      return "Color: " + str(USfavColor)
    except:
      return "Unable to generate a random color"
  
  elif howmuchinfo == "zipcode":
    faker = Faker()
    try:
      USzip = faker.zipcode()
      return "Zip Code: " + str(USzip)
    except:
      return "Unable to generate a random zipcode"
  
  elif howmuchinfo == "city":
    faker = Faker()
    try:
      UScity = faker.city()
      return "City: " + str(UScity)
    except:
      return "Unable to generate a random zipcode"
  
  elif howmuchinfo == "license plate":
    faker = Faker()
    try:
      USnumberPlate = faker.license_plate()
      return "Number Plate: " + str(USnumberPlate)
    except:
      return "Unable to generate a random license plate"

  elif howmuchinfo == "bban":
    faker = Faker()
    try:
      USbasicBankAccountNumber = faker.bban()
      return "Basic Bank Account Number: " + str(USbasicBankAccountNumber)
    except:
      return "Unable to generate a random Basic Bank Account Number"
  
  elif howmuchinfo == "iban":
    faker = Faker()
    try:
      USinternationalBankAccountNumber = faker.iban()
      return "International Bank Account Number: " + str(USinternationalBankAccountNumber)
    except:
      return "Unable to generate a random International Bank Account Number"
  
  elif howmuchinfo == "bs":
    faker = Faker()
    try:
      USbs = faker.bs()
      return "BS: " + str(USbs)
    except:
      return "Unable to generate a random BS"
  
  elif howmuchinfo == "cc":
    faker = Faker()
    try:
      UScreditcard = faker.credit_card_full()
      return "Credit Card: \n" + str(UScreditcard)
    except:
      return "Unable to generate a random Credit Card"
  
  elif howmuchinfo == "cemail":
    faker = Faker()
    try:
      UScompanyemail = faker.company_email()
      return "Email: " + str(UScompanyemail)
    except:
      return "Unable to generate a random Email"
  
  elif howmuchinfo == "pno":
    faker = Faker()
    try:
      USphoneNumber = faker.phone_number()
      return "Phone Number: " + str(USphoneNumber)
    except:
      return "Unable to generate a random Phone Number"
  
  elif howmuchinfo == "cp":
    faker = Faker()
    try:
      UScatchPhrase = faker.catch_phrase()
      return "Catch Phrase: " + str(UScatchPhrase)
    except:
      return "Unable to generate a random catch phrase"
  
  elif howmuchinfo == "ssn":
    faker = Faker()
    try:
      USssa = faker.ssn()
      return "SSN: " + str(USssa)
    except:
      return "Unable to generate a random SSN"
  
  elif howmuchinfo == "ua":
    faker = Faker()
    try:
      USuseragent = faker.ssn()
      return "User Agent: " + str(USuseragent)
    except:
      return "Unable to generate a random User Agent"
  
  elif howmuchinfo == "low":
    fake_low = Faker()
    shitthing_simple = fake_low.simple_profile()

    fake_info_low_info = "Name: " + str(shitthing_simple['name']) + "\nSex: " + str(shitthing_simple['sex']) + "\nAddress: " + str(shitthing_simple['address']) + "\nMail: " + str(shitthing_simple['mail']) + "\nBirthday: " + str(shitthing_simple['birthdate'])

    return fake_info_low_info
  
  elif howmuchinfo == "help":
    fake_help = """high -> Generate a fake profile with high amount of  information
name -> create a fake name
dob -> create a fake Date of Birth
addr -> create a fake address
job -> create a fake job
color -> create a fake color
zipcode -> create a fake zipcode
city -> create a fake city
lp -> create a fake Lisence Number Plate
bban -> create a random Basic Bank Account Number
iban -> create a random International Bank Account Number
bs -> create a fake BS / Degree
cc -> create credit card details ( not valid )
pno -> create a fake phone number
cemail -> create a company email number
cp -> create a random catch phrase
ssn -> create a fake ssn number
    """
    return fake_help
  
  else:
    return "[-] Please enter a valid option, type '>fake help' for help"

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


# MOST COMMANDS USE THIS SIMPLE STRUCTURE
# ---------------------------------------
# @client.command() -- client is what we have used when defining the bot
# async def commandName(ctx): -- ctx is the context
#   Loading message is being sent ( using the main template in the above lines)
#   ------------------------
#   | The body of the code |
#   ------------------------
#   Deleting the loading message
#   Sending the result of the body code in here
# ---------------------------------------

# ctx is for 'context'
@client.command()
async def changeprefix(ctx):
  loading_message = await ctx.send(embed=please_wait_emb)
  await loading_message.delete()
  await ctx.send(f'This feature will be available in the future! Make sure to type the info command to see more information')


@client.command() 
async def ping(ctx):
    loading_message = await ctx.send(embed=please_wait_emb)
    try:
        embed=discord.Embed(title="Response Time", color=0xff0000)
        embed.set_author(name="YourBot", icon_url="https://cdn.discordapp.com/attachments/877796755234783273/879295069834850324/Avatar.png")
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/877796755234783273/879311068097290320/PngItem_1526969.png")
        embed.add_field(name=f"Ping :timer:", value=f"{round(client.latency * 1000)} ms", inline=False)
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

@commands.has_permissions(manage_messages=True)
@client.command()
async def clear(ctx, amount=5):
    amttdel = amount + 1
    await ctx.channel.purge(limit=amttdel)


@client.command(aliases=["8ball", "eightball"])
async def _8ball(ctx, *, question):
    loading_message = await ctx.send(embed=please_wait_emb)

    try:
      responses = ["It is certain.",
                  "Without a doubt",
                  "You may rely on it",
                  "Yes",
                  "Ask again later",
                  "No",
                  "Very doubtful",
                  'That is a resounding no',
                  'It is not looking likely',
                  'Too hard to tell',
                  'It is quite possible',
                  'That is a definite yes!',
                  'Maybe',
                  'There is a good chance']

      answer = random.choice(responses, color=0xff0000)
      embed = discord.Embed()
      embed.add_field(name="Question", value=question, inline=False)
      embed.add_field(name="Answer", value=answer, inline=False)
      embed.set_thumbnail(url="https://www.horoscope.com/images-US/games/game-magic-8-ball-no-text.png")
      embed.set_footer(text=f"Requested by {ctx.author.mention}")
      embed.set_author(name="YourBot", icon_url="https://cdn.discordapp.com/attachments/877796755234783273/879295069834850324/Avatar.png")
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


@commands.has_permissions(kick_members=True)
@client.command()
async def kick(ctx, member : discord.Member, *, reason=None): # call the member as in member object from discord module
    loading_message = await ctx.send(embed=please_wait_emb)
    try:
        # Kick the member from the server with a reason provided
        await member.kick(reason=reason)

        embed=discord.Embed(title=f":boom: Kicked {member.name}", color=0xff0000)
        embed.set_author(name="YourBot", icon_url="https://cdn.discordapp.com/attachments/877796755234783273/879295069834850324/Avatar.png")
        embed.set_thumbnail(url=f"https://cdn.discordapp.com/attachments/877796755234783273/879296561413259294/toppng.com-this-is-an-image-of-a-person-kicking-kick-1085x1335.png")
        embed.add_field(name="Reason", value=f"{reason}", inline=False)
        embed.add_field(name="By", value=f"{ctx.author.mention}", inline=False)
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


@commands.has_permissions(ban_members=True)
@client.command()
async def ban(ctx, user: discord.Member, *, reason="No reason provided"):
    loading_message = await ctx.send(embed=please_wait_emb)
    try:
        # Ban the user from the server with a reason
        await user.ban(reason=reason)

        embed=discord.Embed(title=f":boom: Banned {user.name}", color=0xff0000)
        embed.set_author(name="YourBot", icon_url="https://cdn.discordapp.com/attachments/877796755234783273/879295069834850324/Avatar.png")
        embed.set_thumbnail(url=f"https://cdn.discordapp.com/attachments/877796755234783273/879296561413259294/toppng.com-this-is-an-image-of-a-person-kicking-kick-1085x1335.png")
        embed.add_field(name="Reason", value=f"{reason}", inline=False)
        embed.add_field(name="By", value=f"{ctx.author.mention}", inline=False)
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


@commands.has_permissions(ban_members=True)
@client.command()
async def unban(ctx, *, member):
    loading_message = await ctx.send(embed=please_wait_emb)

    try:
      banned_users = await ctx.guild.bans() # a named tuple containing user object and the reason for ban
      member_name, member_discriminator = member.split("#")

      for ban_entry in banned_users:
          user = ban_entry.user

          # the unbanning happens here!
          if (user.name, user.discriminator) == (member_name, member_discriminator):
              await ctx.guild.unban(user)

              embed=discord.Embed(title=":hammer: Unbanned User", description=f"{user.mention}", color=0xff0000)
              embed.set_author(name="YourBot", icon_url="https://cdn.discordapp.com/attachments/877796755234783273/879295069834850324/Avatar.png")
              embed.set_footer(text=f"Requested by {ctx.author.name}")
              
              await loading_message.delete()
              await ctx.send(embed=embed)
              return
    except Exception as e:
      embed2=discord.Embed(title=":red_square: Error!", description="The command was unable to run successfully! ", color=0xff0000)
      embed2.set_author(name="YourBot", icon_url="https://cdn.discordapp.com/attachments/877796755234783273/879295069834850324/Avatar.png")
      embed2.set_thumbnail(url="https://cdn.discordapp.com/attachments/877796755234783273/879298565380386846/sign-red-error-icon-1.png")
      embed2.add_field(name="Error:", value=f"{e}", inline=False)
      embed2.set_footer(text=f"Requested by {ctx.author.name}")
      await loading_message.delete()
      await ctx.send(embed=embed2)


@client.command()
async def join(ctx):
    # Get the voice channel that the user is connected to and join to it
    channel = ctx.author.voice.channel
    await channel.connect()
    

@client.command()
async def leave(ctx):
    # Leave from any connected voice channel
    await ctx.voice_client.disconnect()


@client.command()
async def inv(ctx):
    await ctx.send("```Hey there! Make sure you have me in your server too! Bot Invite link:```" + give_server_invite_link())


@client.command()
async def inspire(ctx):
  loading_message = await ctx.send(embed=please_wait_emb)

  try:
    embed=discord.Embed(title="Inspirational isn't it?", color=0xff0000)
    embed.set_author(name="YourBot", icon_url="https://cdn.discordapp.com/attachments/877796755234783273/879295069834850324/Avatar.png")
    embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/877796755234783273/879382016041291828/NicePng_light-streak-png_395357.png")
    embed.add_field(name="Inspirational Quote:", value=f"{get_quote()}", inline=True)
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


@client.command()
async def fake(ctx, *, fake_mode="help"):
    loading_message = await ctx.send(embed=please_wait_emb)
    
    # All the information generated is in sync with each other
    if fake_mode == "high":
      try:
        fake = Faker()
        simple_dict = fake.profile()
        # fake_info_simple = "Name: " + str(simple_dict['name']) + "\nJob: " + str(simple_dict['job']) + "\nBirthdate: " + str(simple_dict['birthdate']) + "\nCompany: " + str(simple_dict['company']) + "\SSN: " + str(simple_dict['ssn']) + "\nRecidence: " + simple_dict['residence'] + "\nCurrent Location:" + str(simple_dict['current_location']) + "\nBlood Group: " + str(simple_dict['blood_group']) + "\nUsername: " + str(simple_dict['username']) + "\nAddress: " + str(simple_dict['address']) + "\nMail: " + str(simple_dict['mail'])
        emf = discord.Embed(title="Fake Information Generator", color=0xF00000)
        emf.set_footer(text=f"Requested by {ctx.author.name}")
        emf.set_author(name="YourBot", icon_url="https://cdn.discordapp.com/attachments/877796755234783273/879295069834850324/Avatar.png")
        emf.set_thumbnail(url="https://www.nicepng.com/png/detail/214-2146883_4-fake-stamp-vector-fake-news-logo-png.png")
        emf.add_field(name="Name", value=f"{str(simple_dict['name'])}")
        emf.add_field(name="Job", value=f"{str(simple_dict['job'])}")
        emf.add_field(name="Birthdate", value=f"{str(simple_dict['birthdate'])}")
        emf.add_field(name="Company", value=f"{str(simple_dict['company'])}")
        emf.add_field(name="SSN", value=f"{str(simple_dict['ssn'])}")
        emf.add_field(name="Recidence", value=f"{str(simple_dict['residence'])}")
        emf.add_field(name="Current Location", value=f"{str(simple_dict['current_location'])}")
        emf.add_field(name="Blood Group", value=f"{str(simple_dict['blood_group'])}")
        emf.add_field(name="Username", value=f"{str(simple_dict['username'])}")
        emf.add_field(name="Address", value=f"{str(simple_dict['address'])}")
        emf.add_field(name="Mail", value=f"{str(simple_dict['mail'])}")
        await loading_message.delete()
        await ctx.send(embed=emf)
      except Exception as e:
        embed2=discord.Embed(title=":red_square: Error!", description="The command was unable to run successfully! ", color=0xff0000)
        embed2.set_author(name="YourBot", icon_url="https://cdn.discordapp.com/attachments/877796755234783273/879295069834850324/Avatar.png")
        embed2.set_thumbnail(url="https://cdn.discordapp.com/attachments/877796755234783273/879298565380386846/sign-red-error-icon-1.png")
        embed2.add_field(name="Error:", value=f"{e}", inline=False)
        embed2.set_footer(text=f"Requested by {ctx.author.name}")
        await loading_message.delete()
        await ctx.send(embed=embed2)
    
    # Only a name
    elif fake_mode == "name":
      faker = Faker()
      try:
        USname = faker.name()
        emf2 = discord.Embed(title="Fake Information Generator", color=0xF00000)
        emf2.set_thumbnail(url="https://www.nicepng.com/png/detail/214-2146883_4-fake-stamp-vector-fake-news-logo-png.png")
        emf2.set_footer(text=f"Requested by {ctx.author.name}")
        emf2.set_author(name="YourBot", icon_url="https://cdn.discordapp.com/attachments/877796755234783273/879295069834850324/Avatar.png")
        emf2.add_field(name="Name", value=f"{str(USname)}")
        await loading_message.delete()
        await ctx.send(embed=emf2)
      except Exception as e:
        embed3=discord.Embed(title=":red_square: Error!", description="The command was unable to run successfully! ", color=0xff0000)
        embed3.set_author(name="YourBot", icon_url="https://cdn.discordapp.com/attachments/877796755234783273/879295069834850324/Avatar.png")
        embed3.set_thumbnail(url="https://cdn.discordapp.com/attachments/877796755234783273/879298565380386846/sign-red-error-icon-1.png")
        embed3.add_field(name="Error:", value=f"{e}", inline=False)
        embed3.set_footer(text=f"Requested by {ctx.author.name}")
        await loading_message.delete()
        await ctx.send(embed=embed3)
    
    # Only the Date of Birth
    elif fake_mode == "dob":
      faker = Faker()
      try:
        USdob = faker.date_of_birth()
        emf2 = discord.Embed(title="Fake Information Generator", color=0xF00000)
        emf2.set_thumbnail(url="https://www.nicepng.com/png/detail/214-2146883_4-fake-stamp-vector-fake-news-logo-png.png")
        emf2.set_footer(text=f"Requested by {ctx.author.name}")
        emf2.set_author(name="YourBot", icon_url="https://cdn.discordapp.com/attachments/877796755234783273/879295069834850324/Avatar.png")
        emf2.add_field(name="Date Of Birth", value=f"{str(USdob)}")
        await loading_message.delete()
        await ctx.send(embed=emf2)
      except Exception as e:
        embed3=discord.Embed(title=":red_square: Error!", description="The command was unable to run successfully! ", color=0xff0000)
        embed3.set_author(name="YourBot", icon_url="https://cdn.discordapp.com/attachments/877796755234783273/879295069834850324/Avatar.png")
        embed3.set_thumbnail(url="https://cdn.discordapp.com/attachments/877796755234783273/879298565380386846/sign-red-error-icon-1.png")
        embed3.add_field(name="Error:", value=f"{e}", inline=False)
        embed3.set_footer(text=f"Requested by {ctx.author.name}")
        await loading_message.delete()
        await ctx.send(embed=embed3)
    
    # Only the Address
    elif fake_mode == "addr":
      faker = Faker()
      try:
        USaddress = faker.address()
        emf2 = discord.Embed(title="Fake Information Generator", color=0xF00000)
        emf2.set_thumbnail(url="https://www.nicepng.com/png/detail/214-2146883_4-fake-stamp-vector-fake-news-logo-png.png")
        emf2.set_footer(text=f"Requested by {ctx.author.name}")
        emf2.set_author(name="YourBot", icon_url="https://cdn.discordapp.com/attachments/877796755234783273/879295069834850324/Avatar.png")
        emf2.add_field(name="Address", value=f"{str(USaddress)}")
        await loading_message.delete()
        await ctx.send(embed=emf2)
      except Exception as e:
        embed3=discord.Embed(title=":red_square: Error!", description="The command was unable to run successfully! ", color=0xff0000)
        embed3.set_author(name="YourBot", icon_url="https://cdn.discordapp.com/attachments/877796755234783273/879295069834850324/Avatar.png")
        embed3.set_thumbnail(url="https://cdn.discordapp.com/attachments/877796755234783273/879298565380386846/sign-red-error-icon-1.png")
        embed3.add_field(name="Error:", value=f"{e}", inline=False)
        embed3.set_footer(text=f"Requested by {ctx.author.name}")
        await loading_message.delete()
        await ctx.send(embed=embed3)
    
    # Only the JOB
    elif fake_mode == "job":
      faker = Faker()
      try:
        USjob = faker.job()
        emf2 = discord.Embed(title="Fake Information Generator", color=0xF00000)
        emf2.set_thumbnail(url="https://www.nicepng.com/png/detail/214-2146883_4-fake-stamp-vector-fake-news-logo-png.png")
        emf2.set_footer(text=f"Requested by {ctx.author.name}")
        emf2.set_author(name="YourBot", icon_url="https://cdn.discordapp.com/attachments/877796755234783273/879295069834850324/Avatar.png")
        emf2.add_field(name="Job", value=f"{str(USjob)}")
        await loading_message.delete()
        await ctx.send(embed=emf2)
      except Exception as e:
        embed3=discord.Embed(title=":red_square: Error!", description="The command was unable to run successfully! ", color=0xff0000)
        embed3.set_author(name="YourBot", icon_url="https://cdn.discordapp.com/attachments/877796755234783273/879295069834850324/Avatar.png")
        embed3.set_thumbnail(url="https://cdn.discordapp.com/attachments/877796755234783273/879298565380386846/sign-red-error-icon-1.png")
        embed3.add_field(name="Error:", value=f"{e}", inline=False)
        embed3.set_footer(text=f"Requested by {ctx.author.name}")
        await loading_message.delete()
        await ctx.send(embed=embed3)
    
    # Only the color
    elif fake_mode == "color":
      faker = Faker()
      try:
        USfavColor = faker.color_name()
        emf2 = discord.Embed(title="Fake Information Generator", color=0xF00000)
        emf2.set_thumbnail(url="https://www.nicepng.com/png/detail/214-2146883_4-fake-stamp-vector-fake-news-logo-png.png")
        emf2.set_footer(text=f"Requested by {ctx.author.name}")
        emf2.set_author(name="YourBot", icon_url="https://cdn.discordapp.com/attachments/877796755234783273/879295069834850324/Avatar.png")
        emf2.add_field(name="Color", value=f"{str(USfavColor)}")
        await loading_message.delete()
        await ctx.send(embed=emf2)
      except Exception as e:
        embed3=discord.Embed(title=":red_square: Error!", description="The command was unable to run successfully! ", color=0xff0000)
        embed3.set_author(name="YourBot", icon_url="https://cdn.discordapp.com/attachments/877796755234783273/879295069834850324/Avatar.png")
        embed3.set_thumbnail(url="https://cdn.discordapp.com/attachments/877796755234783273/879298565380386846/sign-red-error-icon-1.png")
        embed3.add_field(name="Error:", value=f"{e}", inline=False)
        embed3.set_footer(text=f"Requested by {ctx.author.name}")
        await loading_message.delete()
        await ctx.send(embed=embed3)
    
    # Only the ZipCode
    elif fake_mode == "zipcode":
      faker = Faker()
      try:
        USzip = faker.zipcode()
        emf2 = discord.Embed(title="Fake Information Generator", color=0xF00000)
        emf2.set_thumbnail(url="https://www.nicepng.com/png/detail/214-2146883_4-fake-stamp-vector-fake-news-logo-png.png")
        emf2.set_footer(text=f"Requested by {ctx.author.name}")
        emf2.set_author(name="YourBot", icon_url="https://cdn.discordapp.com/attachments/877796755234783273/879295069834850324/Avatar.png")
        emf2.add_field(name="Zip Code", value=f"{str(USzip)}")
        await loading_message.delete()
        await ctx.send(embed=emf2)
      except Exception as e:
        embed3=discord.Embed(title=":red_square: Error!", description="The command was unable to run successfully! ", color=0xff0000)
        embed3.set_author(name="YourBot", icon_url="https://cdn.discordapp.com/attachments/877796755234783273/879295069834850324/Avatar.png")
        embed3.set_thumbnail(url="https://cdn.discordapp.com/attachments/877796755234783273/879298565380386846/sign-red-error-icon-1.png")
        embed3.add_field(name="Error:", value=f"{e}", inline=False)
        embed3.set_footer(text=f"Requested by {ctx.author.name}")
        await loading_message.delete()
        await ctx.send(embed=embed3)
    
    # Only the city
    elif fake_mode == "city":
      faker = Faker()
      try:
        UScity = faker.city()
        emf2 = discord.Embed(title="Fake Information Generator", color=0xF00000)
        emf2.set_thumbnail(url="https://www.nicepng.com/png/detail/214-2146883_4-fake-stamp-vector-fake-news-logo-png.png")
        emf2.set_footer(text=f"Requested by {ctx.author.name}")
        emf2.set_author(name="YourBot", icon_url="https://cdn.discordapp.com/attachments/877796755234783273/879295069834850324/Avatar.png")
        emf2.add_field(name="City", value=f"{str(UScity)}")
        await loading_message.delete()
        await ctx.send(embed=emf2)
      except Exception as e:
        embed3=discord.Embed(title=":red_square: Error!", description="The command was unable to run successfully! ", color=0xff0000)
        embed3.set_author(name="YourBot", icon_url="https://cdn.discordapp.com/attachments/877796755234783273/879295069834850324/Avatar.png")
        embed3.set_thumbnail(url="https://cdn.discordapp.com/attachments/877796755234783273/879298565380386846/sign-red-error-icon-1.png")
        embed3.add_field(name="Error:", value=f"{e}", inline=False)
        embed3.set_footer(text=f"Requested by {ctx.author.name}")
        await loading_message.delete()
        await ctx.send(embed=embed3)
    
    # Only a lisence plate number
    elif fake_mode == "licenseplate":
      faker = Faker()
      try:
        USnumberPlate = faker.license_plate()
        emf2 = discord.Embed(title="Fake Information Generator", color=0xF00000)
        emf2.set_thumbnail(url="https://www.nicepng.com/png/detail/214-2146883_4-fake-stamp-vector-fake-news-logo-png.png")
        emf2.set_footer(text=f"Requested by {ctx.author.name}")
        emf2.set_author(name="YourBot", icon_url="https://cdn.discordapp.com/attachments/877796755234783273/879295069834850324/Avatar.png")
        emf2.add_field(name="License Plate", value=f"{str(USnumberPlate)}")
        await loading_message.delete()
        await ctx.send(embed=emf2)
      except Exception as e:
        embed3=discord.Embed(title=":red_square: Error!", description="The command was unable to run successfully! ", color=0xff0000)
        embed3.set_author(name="YourBot", icon_url="https://cdn.discordapp.com/attachments/877796755234783273/879295069834850324/Avatar.png")
        embed3.set_thumbnail(url="https://cdn.discordapp.com/attachments/877796755234783273/879298565380386846/sign-red-error-icon-1.png")
        embed3.add_field(name="Error:", value=f"{e}", inline=False)
        embed3.set_footer(text=f"Requested by {ctx.author.name}")
        await loading_message.delete()
        await ctx.send(embed=embed3)
    
    # Only a Basic Bank Account Number
    elif fake_mode == "bban":
      faker = Faker()
      try:
        USbasicBankAccountNumber = faker.bban()
        emf2 = discord.Embed(title="Fake Information Generator", color=0xF00000)
        emf2.set_thumbnail(url="https://www.nicepng.com/png/detail/214-2146883_4-fake-stamp-vector-fake-news-logo-png.png")
        emf2.set_footer(text=f"Requested by {ctx.author.name}")
        emf2.set_author(name="YourBot", icon_url="https://cdn.discordapp.com/attachments/877796755234783273/879295069834850324/Avatar.png")
        emf2.add_field(name="Basic Bank Account", value=f"{str(USbasicBankAccountNumber)}")
        await loading_message.delete()
        await ctx.send(embed=emf2)
      except Exception as e:
        embed3=discord.Embed(title=":red_square: Error!", description="The command was unable to run successfully! ", color=0xff0000)
        embed3.set_author(name="YourBot", icon_url="https://cdn.discordapp.com/attachments/877796755234783273/879295069834850324/Avatar.png")
        embed3.set_thumbnail(url="https://cdn.discordapp.com/attachments/877796755234783273/879298565380386846/sign-red-error-icon-1.png")
        embed3.add_field(name="Error:", value=f"{e}", inline=False)
        embed3.set_footer(text=f"Requested by {ctx.author.name}")
        await loading_message.delete()
        await ctx.send(embed=embed3)
    
    # Only a International Bank Account Number
    elif fake_mode == "iban":
      faker = Faker()
      try:
        USinternationalBankAccountNumber = faker.iban()
        emf2 = discord.Embed(title="Fake Information Generator", color=0xF00000)
        emf2.set_thumbnail(url="https://www.nicepng.com/png/detail/214-2146883_4-fake-stamp-vector-fake-news-logo-png.png")
        emf2.set_footer(text=f"Requested by {ctx.author.name}")
        emf2.set_author(name="YourBot", icon_url="https://cdn.discordapp.com/attachments/877796755234783273/879295069834850324/Avatar.png")
        emf2.add_field(name="International Bank Account", value=f"{str(USinternationalBankAccountNumber)}")
        await loading_message.delete()
        await ctx.send(embed=emf2)
      except Exception as e:
        embed3=discord.Embed(title=":red_square: Error!", description="The command was unable to run successfully! ", color=0xff0000)
        embed3.set_author(name="YourBot", icon_url="https://cdn.discordapp.com/attachments/877796755234783273/879295069834850324/Avatar.png")
        embed3.set_thumbnail(url="https://cdn.discordapp.com/attachments/877796755234783273/879298565380386846/sign-red-error-icon-1.png")
        embed3.add_field(name="Error:", value=f"{e}", inline=False)
        embed3.set_footer(text=f"Requested by {ctx.author.name}")
        await loading_message.delete()
        await ctx.send(embed=embed3)
    
    # Only a BSc
    elif fake_mode == "bs":
      faker = Faker()
      try:
        USbs = faker.bs()
        emf2 = discord.Embed(title="Fake Information Generator", color=0xF00000)
        emf2.set_thumbnail(url="https://www.nicepng.com/png/detail/214-2146883_4-fake-stamp-vector-fake-news-logo-png.png")
        emf2.set_footer(text=f"Requested by {ctx.author.name}")
        emf2.set_author(name="YourBot", icon_url="https://cdn.discordapp.com/attachments/877796755234783273/879295069834850324/Avatar.png")
        emf2.add_field(name="BS", value=f"{str(USbs)}")
        await loading_message.delete()
        await ctx.send(embed=emf2)
      except Exception as e:
        embed3=discord.Embed(title=":red_square: Error!", description="The command was unable to run successfully! ", color=0xff0000)
        embed3.set_author(name="YourBot", icon_url="https://cdn.discordapp.com/attachments/877796755234783273/879295069834850324/Avatar.png")
        embed3.set_thumbnail(url="https://cdn.discordapp.com/attachments/877796755234783273/879298565380386846/sign-red-error-icon-1.png")
        embed3.add_field(name="Error:", value=f"{e}", inline=False)
        embed3.set_footer(text=f"Requested by {ctx.author.name}")
        await loading_message.delete()
        await ctx.send(embed=embed3)
    
    # Only credit card information, provides everything
    elif fake_mode == "cc":
      faker = Faker()
      try:
        UScreditcard = faker.credit_card_full()
        emf2 = discord.Embed(title="Fake Information Generator", color=0xF00000)
        emf2.set_thumbnail(url="https://www.nicepng.com/png/detail/214-2146883_4-fake-stamp-vector-fake-news-logo-png.png")
        emf2.set_footer(text=f"Requested by {ctx.author.name}")
        emf2.set_author(name="YourBot", icon_url="https://cdn.discordapp.com/attachments/877796755234783273/879295069834850324/Avatar.png")
        emf2.add_field(name="Credit Card", value=f"{str(UScreditcard)}")
        await loading_message.delete()
        await ctx.send(embed=emf2)
      except Exception as e:
        embed3=discord.Embed(title=":red_square: Error!", description="The command was unable to run successfully! ", color=0xff0000)
        embed3.set_author(name="YourBot", icon_url="https://cdn.discordapp.com/attachments/877796755234783273/879295069834850324/Avatar.png")
        embed3.set_thumbnail(url="https://cdn.discordapp.com/attachments/877796755234783273/879298565380386846/sign-red-error-icon-1.png")
        embed3.add_field(name="Error:", value=f"{e}", inline=False)
        embed3.set_footer(text=f"Requested by {ctx.author.name}")
        await loading_message.delete()
        await ctx.send(embed=embed3)
    
    # only a Company Email
    elif fake_mode == "cemail":
      faker = Faker()
      try:
        UScompanyemail = faker.company_email()
        emf2 = discord.Embed(title="Fake Information Generator", color=0xF00000)
        emf2.set_thumbnail(url="https://www.nicepng.com/png/detail/214-2146883_4-fake-stamp-vector-fake-news-logo-png.png")
        emf2.set_footer(text=f"Requested by {ctx.author.name}")
        emf2.set_author(name="YourBot", icon_url="https://cdn.discordapp.com/attachments/877796755234783273/879295069834850324/Avatar.png")
        emf2.add_field(name="Email", value=f"{str(UScompanyemail)}")
        await loading_message.delete()
        await ctx.send(embed=emf2)
      except Exception as e:
        embed3=discord.Embed(title=":red_square: Error!", description="The command was unable to run successfully! ", color=0xff0000)
        embed3.set_author(name="YourBot", icon_url="https://cdn.discordapp.com/attachments/877796755234783273/879295069834850324/Avatar.png")
        embed3.set_thumbnail(url="https://cdn.discordapp.com/attachments/877796755234783273/879298565380386846/sign-red-error-icon-1.png")
        embed3.add_field(name="Error:", value=f"{e}", inline=False)
        embed3.set_footer(text=f"Requested by {ctx.author.name}")
        await loading_message.delete()
        await ctx.send(embed=embed3)
    
    # Only a Phone Number
    elif fake_mode == "pno":
      faker = Faker()
      try:
        USphoneNumber = faker.phone_number()
        emf2 = discord.Embed(title="Fake Information Generator", color=0xF00000)
        emf2.set_thumbnail(url="https://www.nicepng.com/png/detail/214-2146883_4-fake-stamp-vector-fake-news-logo-png.png")
        emf2.set_footer(text=f"Requested by {ctx.author.name}")
        emf2.set_author(name="YourBot", icon_url="https://cdn.discordapp.com/attachments/877796755234783273/879295069834850324/Avatar.png")
        emf2.add_field(name="Phone Number", value=f"{str(USphoneNumber)}")
        await loading_message.delete()
        await ctx.send(embed=emf2)
      except Exception as e:
        embed3=discord.Embed(title=":red_square: Error!", description="The command was unable to run successfully! ", color=0xff0000)
        embed3.set_author(name="YourBot", icon_url="https://cdn.discordapp.com/attachments/877796755234783273/879295069834850324/Avatar.png")
        embed3.set_thumbnail(url="https://cdn.discordapp.com/attachments/877796755234783273/879298565380386846/sign-red-error-icon-1.png")
        embed3.add_field(name="Error:", value=f"{e}", inline=False)
        embed3.set_footer(text=f"Requested by {ctx.author.name}")
        await loading_message.delete()
        await ctx.send(embed=embed3)
    
    # Only a Catch Phrase
    elif fake_mode == "cp":
      faker = Faker()
      try:
        UScatchPhrase = faker.catch_phrase()
        emf2 = discord.Embed(title="Fake Information Generator", color=0xF00000)
        emf2.set_thumbnail(url="https://www.nicepng.com/png/detail/214-2146883_4-fake-stamp-vector-fake-news-logo-png.png")
        emf2.set_footer(text=f"Requested by {ctx.author.name}")
        emf2.set_author(name="YourBot", icon_url="https://cdn.discordapp.com/attachments/877796755234783273/879295069834850324/Avatar.png")
        emf2.add_field(name="Catch Phrase", value=f"{str(UScatchPhrase)}")
        await loading_message.delete()
        await ctx.send(embed=emf2)
      except Exception as e:
        embed3=discord.Embed(title=":red_square: Error!", description="The command was unable to run successfully! ", color=0xff0000)
        embed3.set_author(name="YourBot", icon_url="https://cdn.discordapp.com/attachments/877796755234783273/879295069834850324/Avatar.png")
        embed3.set_thumbnail(url="https://cdn.discordapp.com/attachments/877796755234783273/879298565380386846/sign-red-error-icon-1.png")
        embed3.add_field(name="Error:", value=f"{e}", inline=False)
        embed3.set_footer(text=f"Requested by {ctx.author.name}")
        await loading_message.delete()
        await ctx.send(embed=embed3)
    
    # Only a SSN
    elif fake_mode == "ssn":
      faker = Faker()
      try:
        USssa = faker.ssn()
        emf2 = discord.Embed(title="Fake Information Generator", color=0xF00000)
        emf2.set_thumbnail(url="https://www.nicepng.com/png/detail/214-2146883_4-fake-stamp-vector-fake-news-logo-png.png")
        emf2.set_footer(text=f"Requested by {ctx.author.name}")
        emf2.set_author(name="YourBot", icon_url="https://cdn.discordapp.com/attachments/877796755234783273/879295069834850324/Avatar.png")
        emf2.add_field(name="SSN", value=f"{str(USssa)}")
        await loading_message.delete()
        await ctx.send(embed=emf2)
      except Exception as e:
        embed3=discord.Embed(title=":red_square: Error!", description="The command was unable to run successfully! ", color=0xff0000)
        embed3.set_author(name="YourBot", icon_url="https://cdn.discordapp.com/attachments/877796755234783273/879295069834850324/Avatar.png")
        embed3.set_thumbnail(url="https://cdn.discordapp.com/attachments/877796755234783273/879298565380386846/sign-red-error-icon-1.png")
        embed3.add_field(name="Error:", value=f"{e}", inline=False)
        embed3.set_footer(text=f"Requested by {ctx.author.name}")
        await loading_message.delete()
        await ctx.send(embed=embed3)
    
    # Generate the basic information
    elif fake_mode == "low":
      fake_low = Faker()
      try:
        shitthing_simple = fake_low.simple_profile()
        # fake_info_low_info = "Name: " + str(shitthing_simple['name']) + "\nSex: " + str(shitthing_simple['sex']) + "\nAddress: " + str(shitthing_simple['address']) + "\nMail: " + str(shitthing_simple['mail']) + "\nBirthday: " + str(shitthing_simple['birthdate'])
        emf2 = discord.Embed(title="Fake Information Generator", color=0xF00000)
        emf2.set_thumbnail(url="https://www.nicepng.com/png/detail/214-2146883_4-fake-stamp-vector-fake-news-logo-png.png")
        emf2.set_footer(text=f"Requested by {ctx.author.name}")
        emf2.set_author(name="YourBot", icon_url="https://cdn.discordapp.com/attachments/877796755234783273/879295069834850324/Avatar.png")
        emf2.add_field(name="Name", value=f"{str(shitthing_simple['name'])}")
        emf2.add_field(name="Sex", value=f"{str(shitthing_simple['sex'])}")
        emf2.add_field(name="Address", value=f"{str(shitthing_simple['address'])}")
        emf2.add_field(name="Mail", value=f"{str(shitthing_simple['mail'])}")
        emf2.add_field(name="Birthday", value=f"{str(shitthing_simple['birthdate'])}")
        await loading_message.delete()
        await ctx.send(embed=emf2)
      except Exception as e:
        embed3=discord.Embed(title=":red_square: Error!", description="The command was unable to run successfully! ", color=0xff0000)
        embed3.set_author(name="YourBot", icon_url="https://cdn.discordapp.com/attachments/877796755234783273/879295069834850324/Avatar.png")
        embed3.set_thumbnail(url="https://cdn.discordapp.com/attachments/877796755234783273/879298565380386846/sign-red-error-icon-1.png")
        embed3.add_field(name="Error:", value=f"{e}", inline=False)
        embed3.set_footer(text=f"Requested by {ctx.author.name}")
        await loading_message.delete()
        await ctx.send(embed=embed3)
    
    # Show help
    elif fake_mode == "help":
      bp = bot_prefix
      try:
        emf2 = discord.Embed(title="Fake Information Generator", color=0xF00000)
        emf2.set_thumbnail(url="https://www.nicepng.com/png/detail/214-2146883_4-fake-stamp-vector-fake-news-logo-png.png")
        emf2.set_footer(text=f"Requested by {ctx.author.name}")
        emf2.set_author(name="YourBot", icon_url="https://cdn.discordapp.com/attachments/877796755234783273/879295069834850324/Avatar.png")
        emf2.add_field(name=f"{bp}fake high", value=f"Generate a high amount of information")
        emf2.add_field(name=f"{bp}fake low", value=f"Generate a low amount of information")
        emf2.add_field(name=f"{bp}fake help", value=f"Show this / list all commands")
        emf2.add_field(name=f"{bp}fake name", value=f"Generate a fake name")
        emf2.add_field(name=f"{bp}fake dob", value=f"Generate a fake Date of Birth")
        emf2.add_field(name=f"{bp}fake addr", value=f"Generate a fake Address")
        emf2.add_field(name=f"{bp}fake job", value=f"Generate a fake Job")
        emf2.add_field(name=f"{bp}fake color", value=f"Generate a random color")
        emf2.add_field(name=f"{bp}fake zipcode", value=f"Generate a random zipcode")
        emf2.add_field(name=f"{bp}fake city", value=f"Generate a random City name")
        emf2.add_field(name=f"{bp}fake licenseplate", value=f"Generate a fake licenseplate number")
        emf2.add_field(name=f"{bp}fake bban", value=f"Generate a fake Basic Bank Account")
        emf2.add_field(name=f"{bp}fake bban", value=f"Generate a fake International Bank Account")
        emf2.add_field(name=f"{bp}fake bs", value=f"Generate a random BS degree")
        emf2.add_field(name=f"{bp}fake cc", value=f"Generate fake Credit Card Information")
        emf2.add_field(name=f"{bp}fake cemail", value=f"Generate a fake company email")
        emf2.add_field(name=f"{bp}fake pno", value=f"Generate a fake Phone Number")
        emf2.add_field(name=f"{bp}fake cp", value=f"Generate a fake Catch Phrase")
        emf2.add_field(name=f"{bp}fake ssn", value=f"Generate a fake SSN")
        await loading_message.delete()
        await ctx.send(embed=emf2)
      except Exception as e:
        embed3=discord.Embed(title=":red_square: Error!", description="The command was unable to run successfully! ", color=0xff0000)
        embed3.set_author(name="YourBot", icon_url="https://cdn.discordapp.com/attachments/877796755234783273/879295069834850324/Avatar.png")
        embed3.set_thumbnail(url="https://cdn.discordapp.com/attachments/877796755234783273/879298565380386846/sign-red-error-icon-1.png")
        embed3.add_field(name="Error:", value=f"{e}", inline=False)
        embed3.set_footer(text=f"Requested by {ctx.author.name}")
        await loading_message.delete()
        await ctx.send(embed=embed3)


@client.command(aliases=["ipinfo", "infoip", "ip-info", "info-ip"])
async def ip(ctx, *, ip_from_user):
    loading_message = await ctx.send(embed=please_wait_emb)

    try:
      r = requests.get(f"https://ipapi.co/{ip_from_user}/json").json()
      rc = requests.get(f"https://api.worldbank.org/v2/country/{r['country_code']}?format=json").json()

      embed=discord.Embed(title="IP Information", color=0xff0000)
      embed.set_thumbnail(url="https://user-images.githubusercontent.com/36286877/127773181-c98b63be-b18b-4d8b-a8b6-9426bd031b7c.png")
      embed.set_footer(text=f"Requested by {ctx.author.name}")
      embed.set_author(name="YourBot", icon_url="https://cdn.discordapp.com/attachments/877796755234783273/879295069834850324/Avatar.png")
      embed.add_field(name="IP Info", value="IP Address: " + str(r["ip"]) + "\nCity: " + str(r["city"]) + "\nRegion: " + str(r["region"]) + "\nCountry Name: " + str(r["country_name"]) + "\nLatitude: " + str(r["latitude"]) + "\nLongitude: " + str(r["longitude"]) + "\nTime Zone: " + str(r["timezone"]) + "\nUTC Offset: " + str(r["utc_offset"]) + "\nPostal Code: " + str(r["postal"]) + str("\nISP: " + r["org"]) + "\nASN: " + str(r["asn"]) + "\nCountry Code: " + str(r["country_code"]) + "\nCountry TLD: " + str(r["country_tld"]) + "\nPopulation: " + str(r["country_population"]) + "\nCurrency: " + str(r["currency"]) + "\n Curreny Name: " + str(r["currency_name"]) + "\nCountry Area: " + str(r["country_area"]) + "\nLanguages: " + str(r["languages"]) + "\nCalling Code: " + str(r["country_calling_code"]) + "\nGOOGLE MAPS Link: " + f"https://maps.google.com/?q={r['latitude']},{r['longitude']}", inline=False)
      embed.add_field(name="Country Info", value="ID: " + str(rc[1][0]["id"]) + "\niso2Code: " + str(rc[1][0]["iso2Code"]) + "\nName" + str(rc[1][0]["name"]) + "\n\nRegion: " + "\n   ID: " + str(rc[1][0]["region"]["id"]) + "\n   iso2Code: " + str(rc[1][0]["region"]["iso2code"]) + "\n   Value: " + str(rc[1][0]["region"]["value"]) + "\n\nAdmin Region: " + "\n   ID: " + str(rc[1][0]["adminregion"]["id"]) + "\n   iso2Code: " + str(rc[1][0]["adminregion"]["iso2code"]) + "\n   Value: " + str(rc[1][0]["adminregion"]["value"]) + "\n\nIncome Level: " + "\n   ID: " + str(rc[1][0]["incomeLevel"]["id"]) + "\n   iso2Code: " + str(rc[1][0]["incomeLevel"]["iso2code"]) + "\n   Value: " + str(rc[1][0]["incomeLevel"]["value"]) + "\n\nLending Type: " + "\n   ID: " + str(rc[1][0]["lendingType"]["id"]) + "\n   iso2Code: " + str(rc[1][0]["lendingType"]["iso2code"]) + "\n   Value: " + str(rc[1][0]["lendingType"]["value"]) + "\n\nCapital City: " + str(rc[1][0]["capitalCity"]) + "\nLongitude: " + str(rc[1][0]["longitude"]) + "\nLatitude: " + str(rc[1][0]["latitude"]), inline=False)
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

@client.command(alises=["country-info", "country", "infocountry", "country-information"])
async def countryinfo(ctx, *, countrycodeig):
  # MAKE SURE TO ENTER THE COUNTRY CODE AND NOT THE COUNTRY NAME
  # eg- sg ( for Singapore ), us for ( United States )
  loading_message = await ctx.send(embed=please_wait_emb)

  try:
    rc = requests.get(f"https://api.worldbank.org/v2/country/{countrycodeig}?format=json").json()

    embed=discord.Embed(title="Country Information", color=0xff0000)
    embed.set_thumbnail(url="https://user-images.githubusercontent.com/36286877/129850352-33345963-273b-42bf-b2bc-5523c8158229.png")
    embed.set_footer(text=f"Requested by {ctx.author.name}")
    embed.set_author(name="YourBot", icon_url="https://cdn.discordapp.com/attachments/877796755234783273/879295069834850324/Avatar.png")
    embed.add_field(name="Country Info", value="ID: " + str(rc[1][0]["id"]) + "\niso2Code: " + str(rc[1][0]["iso2Code"]) + "\nName" + str(rc[1][0]["name"]) + "\n\nRegion: " + "\n   ID: " + str(rc[1][0]["region"]["id"]) + "\n   iso2Code: " + str(rc[1][0]["region"]["iso2code"]) + "\n   Value: " + str(rc[1][0]["region"]["value"]) + "\n\nAdmin Region: " + "\n   ID: " + str(rc[1][0]["adminregion"]["id"]) + "\n   iso2Code: " + str(rc[1][0]["adminregion"]["iso2code"]) + "\n   Value: " + str(rc[1][0]["adminregion"]["value"]) + "\n\nIncome Level: " + "\n   ID: " + str(rc[1][0]["incomeLevel"]["id"]) + "\n   iso2Code: " + str(rc[1][0]["incomeLevel"]["iso2code"]) + "\n   Value: " + str(rc[1][0]["incomeLevel"]["value"]) + "\n\nLending Type: " + "\n   ID: " + str(rc[1][0]["lendingType"]["id"]) + "\n   iso2Code: " + str(rc[1][0]["lendingType"]["iso2code"]) + "\n   Value: " + str(rc[1][0]["lendingType"]["value"]) + "\n\nCapital City: " + str(rc[1][0]["capitalCity"]) + "\nLongitude: " + str(rc[1][0]["longitude"]) + "\nLatitude: " + str(rc[1][0]["latitude"]), inline=False)
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


@client.command(aliases=["mass-fake-profile", "massfakeprofile", "mass-fake-profiles", "massfakeprofiles"])
async def mfp(ctx, *, how_many):
    loading_message = await ctx.send(embed=please_wait_emb)

    try:
      fake_how_many = int(how_many)
      
      # This is the limit for this command to stop spamming!
      if fake_how_many <= 30:

        embed=discord.Embed(title="Mass Fake Profiles", color=0xff0000)
        embed.set_author(name="YourBot", icon_url="https://cdn.discordapp.com/attachments/877796755234783273/879295069834850324/Avatar.png")
        embed.set_thumbnail(url="https://www.nicepng.com/png/detail/214-2146883_4-fake-stamp-vector-fake-news-logo-png.png")
        embed.add_field(name=f"{ctx.author.name} requested {how_many} fake profiles!", value=f"Starting to send {how_many} fake profiles!", inline=True)
        # embed.set_footer(text=f"Requested by {ctx.author.name}")
        await loading_message.delete()
        await ctx.send(embed=embed)

        for i in range(fake_how_many):
            fake = Faker()
            simple_dict = fake.profile()
            emf = discord.Embed(title="Fake Information Generator", color=0xF00000)
            emf.set_thumbnail(url="https://www.nicepng.com/png/detail/214-2146883_4-fake-stamp-vector-fake-news-logo-png.png")
            emf.set_footer(text=f"Requested by {ctx.author.name}")
            emf.set_author(name="YourBot", icon_url="https://cdn.discordapp.com/attachments/877796755234783273/879295069834850324/Avatar.png")
            emf.add_field(name="Name", value=f"{str(simple_dict['name'])}")
            emf.add_field(name="Job", value=f"{str(simple_dict['job'])}")
            emf.add_field(name="Birthdate", value=f"{str(simple_dict['birthdate'])}")
            emf.add_field(name="Company", value=f"{str(simple_dict['company'])}")
            emf.add_field(name="SSN", value=f"{str(simple_dict['ssn'])}")
            emf.add_field(name="Recidence", value=f"{str(simple_dict['residence'])}")
            emf.add_field(name="Current Location", value=f"{str(simple_dict['current_location'])}")
            emf.add_field(name="Blood Group", value=f"{str(simple_dict['blood_group'])}")
            emf.add_field(name="Username", value=f"{str(simple_dict['username'])}")
            emf.add_field(name="Address", value=f"{str(simple_dict['address'])}")
            emf.add_field(name="Mail", value=f"{str(simple_dict['mail'])}")
            await ctx.send(embed=emf)

      else:
        embed=discord.Embed(title="Mass Fake Profiles", color=0xff0000)
        embed.set_author(name="YourBot", icon_url="https://cdn.discordapp.com/attachments/877796755234783273/879295069834850324/Avatar.png")
        embed.set_thumbnail(url="https://www.nicepng.com/png/detail/214-2146883_4-fake-stamp-vector-fake-news-logo-png.png")
        embed.add_field(name="Error", value="Please enter a value below 30; This is done to prevent spam!", inline=True)
        embed.set_footer(text=f"Requested by {ctx.author.name}")
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
async def pervert(ctx):
    # Just a text
    await ctx.send("```" + """Can I get a booty pic with your panties on? And one without them on? Can I also get 3 different pics of your boobs in any position. Also can I get a pic of your pussy from the front and one where it’s spread open. Can I get a picture of you fingering your self? Can I get a pic of you doing a kissing face but with your boobs in it? Can I get a picture of your pussy and ass from behind in one shot? Can I also get a pic of your full front body in just a bra and panties? And can I get a pic of your ass when your pants are all the way up? Also can I get a pic of your boobs when you’re in the shower? Also can I get another pussy pic while you’re in the shower? For the rest of the pics can you just send whatever other sexy things you want? For the videos can I get a video of you twerking in really short shorts? And one of you fingering yourself? One of you actually cumming? Also can I get a video of you playing with your tits while not wearing a shirt? u be squirtin? or u on the cream team? what color the inside? your booty real wet? do it clap? do it fart? do it grip the meat? it’s tight? how many fingers u use? what it taste like? can i smell it? is it warm? it’s real juicy? do it drip? you be moaning?""" + "```")


@client.command()
async def nitro(ctx, *, number_of_times):
    loading_message = await ctx.send(embed=please_wait_emb)

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
              await ctx.send(give_nice_codes())
              asyncio.sleep(0.4)

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

@commands.has_permissions(administrator=True)
@client.command()
async def spam(ctx, number_of_times_to_spam, *, message):
    loading_message = await ctx.send(embed=please_wait_emb)

    try:
      embed=discord.Embed(title="Spam Messages!", color=0xff0000)
      embed.set_footer(text=f"Requested by {ctx.author.name}")
      embed.set_author(name="YourBot", icon_url="https://cdn.discordapp.com/attachments/877796755234783273/879295069834850324/Avatar.png")
      embed.add_field(name="Requested by: ", value=f"{ctx.author}", inline=False)
      embed.add_field(name="Number of Messages: ", value=f"{number_of_times_to_spam}", inline=False)
      embed.add_field(name="Message: ", value=f"{message}", inline=False)
      await loading_message.delete()
      await ctx.send(embed=embed)

      # THE SPAM WILL START HERE
      # ONLY 2 MESSAGES WILL BE SENT FOR A SECOND
      for iteration, x in enumerate(range(int(number_of_times_to_spam))):
          await ctx.send(message)
          asyncio.sleep(0.5)

    except Exception as e:
      embed3=discord.Embed(title=":red_square: Error!", description="The command was unable to run successfully! ", color=0xff0000)
      embed3.set_author(name="YourBot", icon_url="https://cdn.discordapp.com/attachments/877796755234783273/879295069834850324/Avatar.png")
      embed3.set_thumbnail(url="https://cdn.discordapp.com/attachments/877796755234783273/879298565380386846/sign-red-error-icon-1.png")
      embed3.add_field(name="Error:", value=f"{e}", inline=False)
      embed3.set_footer(text=f"Requested by {ctx.author.name}")
      await loading_message.delete()
      await ctx.send(embed=embed3)


@client.command()
async def megaspamlol(ctx, *, number_of_times_spam_secret=10):
  loading_message = await ctx.send(embed=please_wait_emb)
  try:
    # ONLY I CAN USE THIS COMMAND, if someone else tries this, They will get a no permission message
    if ctx.author.id == bot_owner_id_zeacer:
      embed=discord.Embed(title="MEGA SPAM LOL", description="The very secret feature of this bot has been used!", color=0xff0000)
      await ctx.send(embed=embed)

      for iteration, x in enumerate(range(int(number_of_times_spam_secret))):
          await ctx.send("@everyone @here lol")
          time.sleep(0.5)

    else:
      embednw=discord.Embed(title="NO PERMISSIONS", color=0xff0000)
      embednw.set_footer(text=f"Requested by {ctx.author.name}")
      embednw.set_author(name="YourBot", icon_url="https://cdn.discordapp.com/attachments/877796755234783273/879295069834850324/Avatar.png")
      embednw.add_field(name="LOL NOPE!", value="You have no permission to use this command!", inline=True)
      await ctx.send(embed=embednw)

  except Exception as e:
    embed3=discord.Embed(title=":red_square: Error!", description="The command was unable to run successfully! ", color=0xff0000)
    embed3.set_author(name="YourBot", icon_url="https://cdn.discordapp.com/attachments/877796755234783273/879295069834850324/Avatar.png")
    embed3.set_thumbnail(url="https://cdn.discordapp.com/attachments/877796755234783273/879298565380386846/sign-red-error-icon-1.png")
    embed3.add_field(name="Error:", value=f"{e}", inline=False)
    embed3.set_footer(text=f"Requested by {ctx.author.name}")
    await loading_message.delete()
    await ctx.send(embed=embed3)


@client.command()
async def bored(ctx):
    loading_message = await ctx.send(embed=please_wait_emb)

    try:
      bored_activity_get = bored_activity()
      await loading_message.delete()
      await ctx.send("```" + bored_activity_get + "```")

    except Exception as e:
      embed3=discord.Embed(title=":red_square: Error!", description="The command was unable to run successfully! ", color=0xff0000)
      embed3.set_author(name="YourBot", icon_url="https://cdn.discordapp.com/attachments/877796755234783273/879295069834850324/Avatar.png")
      embed3.set_thumbnail(url="https://cdn.discordapp.com/attachments/877796755234783273/879298565380386846/sign-red-error-icon-1.png")
      embed3.add_field(name="Error:", value=f"{e}", inline=False)
      embed3.set_footer(text=f"Requested by {ctx.author.name}")
      await loading_message.delete()
      await ctx.send(embed=embed3)


@client.command()
async def color(ctx):
    loading_message = await ctx.send(embed=please_wait_emb)

    try:
      give_random_color_get = give_rand_color()
      await loading_message.delete()
      await ctx.send("```" + give_random_color_get + "```")

    except Exception as e:
      embed3=discord.Embed(title=":red_square: Error!", description="The command was unable to run successfully! ", color=0xff0000)
      embed3.set_author(name="YourBot", icon_url="https://cdn.discordapp.com/attachments/877796755234783273/879295069834850324/Avatar.png")
      embed3.set_thumbnail(url="https://cdn.discordapp.com/attachments/877796755234783273/879298565380386846/sign-red-error-icon-1.png")
      embed3.add_field(name="Error:", value=f"{e}", inline=False)
      embed3.set_footer(text=f"Requested by {ctx.author.name}")
      await loading_message.delete()
      await ctx.send(embed=embed3)


@client.command()
async def btc(ctx):
    loading_message = await ctx.send(embed=please_wait_emb)

    try:
      give_bitcoin_status_get = get_bitcoin_status()
      await loading_message.delete()
      await ctx.send("```" + give_bitcoin_status_get + "```")

    except Exception as e:
      embed3=discord.Embed(title=":red_square: Error!", description="The command was unable to run successfully! ", color=0xff0000)
      embed3.set_author(name="YourBot", icon_url="https://cdn.discordapp.com/attachments/877796755234783273/879295069834850324/Avatar.png")
      embed3.set_thumbnail(url="https://cdn.discordapp.com/attachments/877796755234783273/879298565380386846/sign-red-error-icon-1.png")
      embed3.add_field(name="Error:", value=f"{e}", inline=False)
      embed3.set_footer(text=f"Requested by {ctx.author.name}")
      await loading_message.delete()
      await ctx.send(embed=embed3)


@client.command()
async def covidlow(ctx):
  loading_message = await ctx.send(embed=please_wait_emb)

  try:
    # This is not very accurate
    r = requests.get('https://coronavirus-19-api.herokuapp.com/all') 
    data = r.json()
    confirmed_cases = data["cases"]
    deaths = data["deaths"]
    recovered = data["recovered"]
    
    em = discord.Embed(title="COVID-19 Stats Global - Low Info", color=0xff0000)
    em.set_footer(text=f"Requested by {ctx.author.name}")
    em.set_author(name="YourBot", icon_url="https://cdn.discordapp.com/attachments/877796755234783273/879295069834850324/Avatar.png")
    em.set_thumbnail(url="https://www.apsf.org/wp-content/uploads/newsletters/2020/3502/coronavirus-covid-19.png")
    em.add_field(name="Confirmed Cases", value=confirmed_cases)
    em.add_field(name="Deaths", value=deaths)
    em.add_field(name="Recovered", value=recovered) 
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


@client.command(aliases=["covidlk"])
async def covidsl(ctx):
  loading_message = await ctx.send(embed=please_wait_emb)

  try:
    # This uses the official API provided by the Sri Lankan Government to gather the needed data
    r = requests.get("https://www.hpb.health.gov.lk/api/get-current-statistical")
    c = r.json()
    data = c['data']

    update_date_time = data['update_date_time']
    local_new_cases = data['local_new_cases']
    local_total_cases = data['local_total_cases']
    local_total_number_of_individuals_in_hospitals = data['local_total_number_of_individuals_in_hospitals']
    local_deaths = data['local_deaths']
    local_new_deaths = data['local_new_deaths']
    local_recovered = data['local_recovered']
    local_active_cases = data['local_active_cases']
    
    em = discord.Embed(title="COVID-19 Statistics - Sri Lanka", color=0xff0000)
    em.set_footer(text=f"Requested by {ctx.author.name}")
    em.set_author(name="YourBot", icon_url="https://cdn.discordapp.com/attachments/877796755234783273/879295069834850324/Avatar.png")
    em.set_thumbnail(url="https://www.apsf.org/wp-content/uploads/newsletters/2020/3502/coronavirus-covid-19.png")
    em.add_field(name="Last Updated", value=update_date_time)
    em.add_field(name="Total Cases", value=local_total_cases)
    em.add_field(name="New Cases", value=local_new_cases)
    em.add_field(name="Total individuals in hospitals", value=local_total_number_of_individuals_in_hospitals)
    em.add_field(name="Total Deaths", value=local_deaths)
    em.add_field(name="New Deaths", value=local_new_deaths)
    em.add_field(name="Total Recovered", value=local_recovered)
    em.add_field(name="Active Cases", value=local_active_cases)
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


@client.command(aliases=["covidall"])
async def covid(ctx):
  loading_message = await ctx.send(embed=please_wait_emb)

  try:
  # This uses the official API provided by the Sri Lankan Government to gather the needed data
    r = requests.get("https://www.hpb.health.gov.lk/api/get-current-statistical")
    c = r.json()
    data = c['data']

    update_date_time = data['update_date_time']
    global_new_cases = data['global_new_cases']
    global_total_cases = data['global_total_cases']
    global_deaths = data['global_deaths']
    global_new_deaths = data['global_new_deaths']
    global_recovered = data['global_recovered']
    total_pcr_testing_count = data['total_pcr_testing_count']
    total_antigen_testing_count = data['total_antigen_testing_count']
    
    em = discord.Embed(title="COVID-19 Stats Global - All Info", color=0xff0000)
    em.set_footer(text=f"Requested by {ctx.author.name}")
    em.set_author(name="YourBot", icon_url="https://cdn.discordapp.com/attachments/877796755234783273/879295069834850324/Avatar.png")
    em.set_thumbnail(url="https://www.apsf.org/wp-content/uploads/newsletters/2020/3502/coronavirus-covid-19.png")
    em.add_field(name="Last Updated", value=update_date_time)
    em.add_field(name="New Cases", value=global_new_cases)
    em.add_field(name="Total Cases", value=global_total_cases)
    em.add_field(name="Total Deaths", value=global_deaths)
    em.add_field(name="New Deaths", value=global_new_deaths)
    em.add_field(name="Total Recovered", value=global_recovered)
    em.add_field(name="Total PCR Testing Count", value=total_pcr_testing_count)
    em.add_field(name="Total Antigen Testing Count", value=total_antigen_testing_count)
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


@client.command()
async def wiki(ctx, *, word_to_search):
    loading_message = await ctx.send(embed=please_wait_emb)
    try:
      embed=discord.Embed(title="Wikipedia Search", description="Search Wikipedia without visiting!", color=0xff0000)
      embed.set_footer(text=f"Requested by {ctx.author.name}")
      embed.set_author(name="YourBot", icon_url="https://cdn.discordapp.com/attachments/877796755234783273/879295069834850324/Avatar.png")
      embed.add_field(name="Content", value=f"``` {search_wikipedia(word_to_search)} ```", inline=True)
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
async def tinyurl(ctx, *, link):
    loading_message = await ctx.send(embed=please_wait_emb)

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


@client.command()
async def dadjoke(ctx):
  loading_message = await ctx.send(embed=please_wait_emb)

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


@client.command()
async def joke(ctx):
  loading_message = await ctx.send(embed=please_wait_emb)

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


@client.command(aliases=["server-icon"])
async def iconserver(ctx):
  loading_message = await ctx.send(embed=please_wait_emb)

  try:
    em = discord.Embed(title=ctx.guild.name)
    em.set_footer(text=f"Requested by {ctx.author.name}")
    em.set_author(name="YourBot", icon_url="https://cdn.discordapp.com/attachments/877796755234783273/879295069834850324/Avatar.png")
    em.set_image(url=ctx.guild.icon_url)
    em.add_field(name="Server Name:", value=f"{ctx.guild.name}", inline=False)
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


@client.command()
async def mac(ctx, mac):
  loading_message = await ctx.send(embed=please_wait_emb)

  try:
    r = requests.get('http://api.macvendors.com/' + mac)

    embed=discord.Embed(title="MAC Lookup", color=0xff0000)
    embed.set_author(name="YourBot", icon_url="https://cdn.discordapp.com/attachments/877796755234783273/879295069834850324/Avatar.png")
    embed.set_thumbnail(url="https://regmedia.co.uk/2016/09/22/wifi_icon_shutterstock.jpg?x=1200&y=794")
    embed.add_field(name="Result", value=f"{r.text}", inline=False)
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
async def bitcoin(ctx):
  loading_message = await ctx.send(embed=please_wait_emb)
  
  try:
    r = requests.get('https://min-api.cryptocompare.com/data/price?fsym=BTC&tsyms=USD,EUR')
    r = r.json()

    usd = r['USD']
    eur = r['EUR']

    embed=discord.Embed(title="Bitcoin", color=0xff0000)
    embed.set_author(name="YourBot", icon_url="https://cdn.discordapp.com/attachments/877796755234783273/879295069834850324/Avatar.png")
    embed.set_thumbnail(url="https://cdn.pixabay.com/photo/2013/12/08/12/12/bitcoin-225079_960_720.png")
    embed.add_field(name="USD", value=f"{usd}$", inline=False)
    embed.add_field(name="EUR", value=f"{eur}€", inline=False)
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
async def eth(ctx):
  loading_message = await ctx.send(embed=please_wait_emb)

  try:
    r = requests.get('https://min-api.cryptocompare.com/data/price?fsym=ETH&tsyms=USD,EUR')
    r = r.json()

    usd = r['USD']
    eur = r['EUR']

    embed=discord.Embed(title="Ethereum", color=0xff0000)
    embed.set_author(name="YourBot", icon_url="https://cdn.discordapp.com/attachments/877796755234783273/879295069834850324/Avatar.png")
    embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/271256875205525504/374282740218200064/2000px-Ethereum_logo.png")
    embed.add_field(name="USD", value=f"{usd}$", inline=False)
    embed.add_field(name="EUR", value=f"{eur}€", inline=False)
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


@client.command(aliases=['wouldyourather', 'would-you-rather', 'wyrq'])
async def wyr(ctx, *, questionhere):
  loading_message = await ctx.send(embed=please_wait_emb)

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


@client.command()
async def hastebin(ctx, *, message):
  loading_message = await ctx.send(embed=please_wait_emb)

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


@client.command()
async def asciiart(ctx, *, text):
  loading_message = await ctx.send(embed=please_wait_emb)

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

# Most of the NSFW image/GIF commands have the same structure
# ---------------------------------
# @client.command()
# async def nsfw_command_name(ctx):
#   Sending the loading message
# 
#   Sending a request to a public API
#   Converting the data from bytes to json
#   Creating a discord Embed
#   Adding the url extracted from the API result
# 
#   Deleting the loading message
#   Sending the embed
# ---------------------------------

@client.command()
async def anal(ctx):
  loading_message = await ctx.send(embed=please_wait_emb)

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


@client.command()
async def erofeet(ctx):
  loading_message = await ctx.send(embed=please_wait_emb)
  
  try:
    r = requests.get("https://nekos.life/api/v2/img/erofeet")
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


@client.command()
async def feet(ctx):
  loading_message = await ctx.send(embed=please_wait_emb)
  
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


@client.command()
async def hentai(ctx):
  loading_message = await ctx.send(embed=please_wait_emb)

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


@client.command()
async def boobs(ctx):
  loading_message = await ctx.send(embed=please_wait_emb)

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


@client.command()
async def tits(ctx):
  loading_message = await ctx.send(embed=please_wait_emb)

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


@client.command()
async def blowjob(ctx):
  loading_message = await ctx.send(embed=please_wait_emb)

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


@client.command()
async def lewd(ctx):
  loading_message = await ctx.send(embed=please_wait_emb)

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


@client.command()
async def lesbian(ctx):
  loading_message = await ctx.send(embed=please_wait_emb)

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

# THESE COMMANDS HAVE THE STRUCTURE AS THE NSFW COMMANDS DID

@client.command()
async def feed(ctx, user: discord.Member = None):
  loading_message = await ctx.send(embed=please_wait_emb)

  try:
    r = requests.get("https://nekos.life/api/v2/img/feed")
    res = r.json()

    if user == None:
      em = discord.Embed(description="User is not mentioned!", color=0xff0000)
      em.set_author(name="YourBot", icon_url="https://cdn.discordapp.com/attachments/877796755234783273/879295069834850324/Avatar.png")
      em.set_footer(text=f"Requested by {ctx.author.name}")
      em.set_image(url=res['url'])
      await loading_message.delete()
      await ctx.send(embed=em)
    
    else:
      em = discord.Embed(description=user.mention, color=0xff0000)
      em.set_author(name="YourBot", icon_url="https://cdn.discordapp.com/attachments/877796755234783273/879295069834850324/Avatar.png")
      em.set_footer(text=f"Requested by {ctx.author.name}")
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


@client.command()
async def tickle(ctx, user: discord.Member = None):
  loading_message = await ctx.send(embed=please_wait_emb)
  try:
    r = requests.get("https://nekos.life/api/v2/img/tickle")
    res = r.json()

    if user == None:
      em = discord.Embed(description="User is not mentioned!", color=0xff0000)
      em.set_author(name="YourBot", icon_url="https://cdn.discordapp.com/attachments/877796755234783273/879295069834850324/Avatar.png")
      em.set_footer(text=f"Requested by {ctx.author.name}")
      em.set_image(url=res['url'])
      await loading_message.delete()
      await ctx.send(embed=em)

    else:
      em = discord.Embed(description=user.mention, color=0xff0000)
      em.set_author(name="YourBot", icon_url="https://cdn.discordapp.com/attachments/877796755234783273/879295069834850324/Avatar.png")
      em.set_footer(text=f"Requested by {ctx.author.name}")
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
  

@client.command()
async def hit(ctx, user: discord.Member = None):
  loading_message = await ctx.send(embed=please_wait_emb)
  
  try:
    r = requests.get("https://nekos.life/api/v2/img/slap")
    res = r.json()

    if user == None:
      em = discord.Embed(description="User is not mentioned!", color=0xff0000)
      em.set_image(url=res['url'])
      em.set_author(name="YourBot", icon_url="https://cdn.discordapp.com/attachments/877796755234783273/879295069834850324/Avatar.png")
      em.set_footer(text=f"Requested by {ctx.author.name}")
      await loading_message.delete()
      await ctx.send(embed=em)
    else:
      em = discord.Embed(description=user.mention, color=0xff0000)
      em.set_author(name="YourBot", icon_url="https://cdn.discordapp.com/attachments/877796755234783273/879295069834850324/Avatar.png")
      em.set_footer(text=f"Requested by {ctx.author.name}")
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


@client.command()
async def hug(ctx, user: discord.Member):
  loading_message = await ctx.send(embed=please_wait_emb)

  try:
    r = requests.get("https://nekos.life/api/v2/img/hug")
    res = r.json()
    if user == None:
      em = discord.Embed(description="User is not mentioned!", color=0xff0000)
      em.set_author(name="YourBot", icon_url="https://cdn.discordapp.com/attachments/877796755234783273/879295069834850324/Avatar.png")
      em.set_footer(text=f"Requested by {ctx.author.name}")
      em.set_image(url=res['url'])
      await loading_message.delete()
      await ctx.send(embed=em)

    else:
      em = discord.Embed(description="user.mention", color=0xff0000)
      em.set_author(name="YourBot", icon_url="https://cdn.discordapp.com/attachments/877796755234783273/879295069834850324/Avatar.png")
      em.set_footer(text=f"Requested by {ctx.author.name}")
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


@client.command()
async def smug(ctx, user: discord.Member):
  loading_message = await ctx.send(embed=please_wait_emb)

  try:
    r = requests.get("https://nekos.life/api/v2/img/smug")
    res = r.json()

    if user == None:
      em = discord.Embed(description="User is not mentioned!", color=0xff0000)
      em.set_image(url=res['url'])
      em.set_author(name="YourBot", icon_url="https://cdn.discordapp.com/attachments/877796755234783273/879295069834850324/Avatar.png")
      em.set_footer(text=f"Requested by {ctx.author.name}")
      await loading_message.delete()
      await ctx.send(embed=em)

    else:
      em = discord.Embed(description=user.mention, color=0xff0000)
      em.set_image(url=res['url'])
      em.set_author(name="YourBot", icon_url="https://cdn.discordapp.com/attachments/877796755234783273/879295069834850324/Avatar.png")
      em.set_footer(text=f"Requested by {ctx.author.name}")
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


@client.command()
async def pat(ctx, user: discord.Member = None):
  loading_message = await ctx.send(embed=please_wait_emb)

  try:
    r = requests.get("https://nekos.life/api/v2/img/pat")
    res = r.json()

    if user == None:
      em = discord.Embed(description="User is not mentioned!", color=0xff0000)
      em.set_image(url=res['url'])
      em.set_author(name="YourBot", icon_url="https://cdn.discordapp.com/attachments/877796755234783273/879295069834850324/Avatar.png")
      em.set_footer(text=f"Requested by {ctx.author.name}")
      await loading_message.delete()
      await ctx.send(embed=em)

    else:
      em = discord.Embed(description=user.mention, color=0xff0000)
      em.set_image(url=res['url'])
      em.set_author(name="YourBot", icon_url="https://cdn.discordapp.com/attachments/877796755234783273/879295069834850324/Avatar.png")
      em.set_footer(text=f"Requested by {ctx.author.name}")
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


@client.command()
async def kiss(ctx, user: discord.Member = None):
  loading_message = await ctx.send(embed=please_wait_emb)

  try:
    r = requests.get("https://nekos.life/api/v2/img/kiss")
    res = r.json()

    if user == None:
      em = discord.Embed(description="User is not mentioned!", color=0xff0000)
      em.set_author(name="YourBot", icon_url="https://cdn.discordapp.com/attachments/877796755234783273/879295069834850324/Avatar.png")
      em.set_footer(text=f"Requested by {ctx.author.name}")
      em.set_image(url=res['url'])
      await loading_message.delete()
      await ctx.send(embed=em)
    
    else:
      em = discord.Embed(description=user.mention, color=0xff0000)
      em.set_author(name="YourBot", icon_url="https://cdn.discordapp.com/attachments/877796755234783273/879295069834850324/Avatar.png")
      em.set_footer(text=f"Requested by {ctx.author.name}")
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


# --------------

@client.command()
async def reverse(ctx, *, message):
  loading_message = await ctx.send(embed=please_wait_emb)
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



# THE BELOW COMMANDS HAVE A SIMILIAR STRUCTURE 
# ---------------------------------
# @client.command()
# async def command_name(ctx):
#   Deleting the message sent by the user
#   Defining the message to send
#   Sending the message
# ---------------------------------

@client.command()
async def shrug(ctx):
    await ctx.message.delete()
    shrug = r'¯\_(ツ)_/¯'
    await ctx.send(shrug)


@client.command()
async def lenny(ctx):
    await ctx.message.delete()
    lenny = '( ͡° ͜ʖ ͡°)'
    await ctx.send(lenny)


@client.command()
async def tableflip(ctx):
    tableflip = '(╯°□°）╯︵ ┻━┻'
    await ctx.send(tableflip)


@client.command()
async def unflip(ctx):
    await ctx.message.delete()
    unflip = '┬─┬ ノ( ゜-゜ノ)'
    await ctx.send(unflip)


@client.command()
async def bold(ctx, *, message):
    await ctx.message.delete()
    await ctx.send('**'+message+'**')


@client.command()
async def secret(ctx, *, message):
    await ctx.message.delete()
    await ctx.send('||'+message+'||')

# --------------

@client.command()
async def xmr(ctx):
  loading_message = await ctx.send(embed=please_wait_emb)

  try:
    r = requests.get("https://min-api.cryptocompare.com/data/price?fsym=XMR&tsyms=USD,EUR")
    NegroPuket = r.json()

    eur = NegroPuket['EUR']
    usd = NegroPuket['USD']

    embed=discord.Embed(title="XMR", color=0xff0000)
    embed.set_author(name="YourBot", icon_url="https://cdn.discordapp.com/attachments/877796755234783273/879295069834850324/Avatar.png")
    embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/877796755234783273/879739662837633074/monero-logo-png-transparent.png")
    embed.add_field(name="USD", value=f"{usd}", inline=False)
    embed.add_field(name="EUR", value=f"{eur}", inline=True)
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
async def doge(ctx):
  loading_message = await ctx.send(embed=please_wait_emb)

  try:
    r = requests.get("https://min-api.cryptocompare.com/data/price?fsym=DOGE&tsyms=USD,EUR")
    NegroPuketDOGE = r.json()

    eur = NegroPuketDOGE['EUR']
    usd = NegroPuketDOGE['USD']

    embed=discord.Embed(title="Doge Coin", color=0xff0000)
    embed.set_author(name="YourBot", icon_url="https://cdn.discordapp.com/attachments/877796755234783273/879295069834850324/Avatar.png")
    embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/877796755234783273/879741979183968286/Dogecoin_Logo.png")
    embed.add_field(name="USD", value=f"{usd}", inline=False)
    embed.add_field(name="EUR", value=f"{eur}", inline=True)
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
async def xrp(ctx):
  loading_message = await ctx.send(embed=please_wait_emb)

  try:
    r = requests.get("https://min-api.cryptocompare.com/data/price?fsym=XRP&tsyms=USD,EUR")
    kekistan = r.json()

    eur = kekistan['EUR']
    usd = kekistan['USD']

    embed=discord.Embed(title="Doge Coin", color=0xff0000)
    embed.set_author(name="YourBot", icon_url="https://cdn.discordapp.com/attachments/877796755234783273/879295069834850324/Avatar.png")
    embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/877796755234783273/879741815237017680/52.png")
    embed.add_field(name="USD", value=f"{usd}", inline=False)
    embed.add_field(name="EUR", value=f"{eur}", inline=True)
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

# THE BELOW COMMANDS HAVE A SIMILIAR STRUCTURE 
# ---------------------------------
# @client.command()
# async def command_name(ctx):
#   Deleting the message sent by the user
#   Defining the message to send
#   Sending the message
# ---------------------------------

@client.command()
async def goodnight(ctx):
  await ctx.message.delete()
  night = '✩⋆｡ ˚ᎶᎾᎾⅅ ℕᏐᎶℍᎢ⋆｡˚✩'
  await ctx.send(night)


@client.command()
async def smile(ctx):
  await ctx.message.delete()
  smile = '˙ ͜ʟ˙'
  await ctx.send(smile)


@client.command()
async def iloveu(ctx):
  await ctx.message.delete()
  love = '(๑′ᴗ‵๑)Ｉ Lᵒᵛᵉᵧₒᵤ♥'
  await ctx.send(love)


@client.command()
async def sword(ctx):
  await ctx.message.delete()
  sword = 'ס₪₪₪₪§|(Ξ≥≤≥≤≥≤ΞΞΞΞΞΞΞΞΞΞ>'
  await ctx.send(sword)


@client.command()
async def what(ctx):
  await ctx.message.delete()
  what = '( ʘ̆ ╭͜ʖ╮ ʘ̆ )'
  await ctx.send(what)


@client.command()
async def fuckyou(ctx):
  await ctx.message.delete()
  middlef = '╭∩╮(･◡･)╭∩╮'
  await ctx.send(middlef)


@client.command()
async def txt1(ctx):
  await ctx.message.delete()
  middlef = r"ヾ(•ω•`)o"
  await ctx.send(middlef)


@client.command()
async def txt2(ctx):
  await ctx.message.delete()
  middlef = r"\(￣︶￣*\))"
  await ctx.send(middlef)


@client.command()
async def txt3(ctx):
  await ctx.message.delete()
  middlef = r"(* ￣3)(ε￣ *)"
  await ctx.send(middlef)


@client.command()
async def txt4(ctx):
  await ctx.message.delete()
  middlef = r"－O－"
  await ctx.send(middlef)


@client.command()
async def txt5(ctx):
  await ctx.message.delete()
  middlef = r"(*￣3￣)╭)"
  await ctx.send(middlef)


@client.command()
async def txt6(ctx):
  await ctx.message.delete()
  middlef = r"( ´･･)ﾉ(._.`)"
  await ctx.send(middlef)


@client.command()
async def txt7(ctx):
  await ctx.message.delete()
  middlef = r"(｡･∀･)ﾉﾞ"
  await ctx.send(middlef)


@client.command()
async def txt8(ctx):
  await ctx.message.delete()
  middlef = r"o(*￣▽￣*)ブ"
  await ctx.send(middlef)


@client.command()
async def txt9(ctx):
  await ctx.message.delete()
  middlef = r"(_　_)。゜zｚＺ"
  await ctx.send(middlef)


@client.command()
async def txt10(ctx):
  await ctx.message.delete()
  middlef = r"(ToT)/~~~"
  await ctx.send(middlef)


@client.command()
async def txt11(ctx):
  await ctx.message.delete()
  middlef = r"(∪.∪ )...zzz"
  await ctx.send(middlef)


@client.command()
async def txt12(ctx):
  await ctx.message.delete()
  middlef = r"!(*￣(￣　*)"
  await ctx.send(middlef)


@client.command()
async def txt13(ctx):
  await ctx.message.delete()
  middlef = r"(￣o￣) . z Z)"
  await ctx.send(middlef)


@client.command()
async def txt14(ctx):
  await ctx.message.delete()
  middlef = r"(づ￣ 3￣)づ"
  await ctx.send(middlef)


@client.command()
async def txt15(ctx):
  await ctx.message.delete()
  middlef = r"（＾∀＾●）ﾉｼ"
  await ctx.send(middlef)


@client.command()
async def txt16(ctx):
  await ctx.message.delete()
  middlef = r"（づ￣3￣）づ╭❤～"
  await ctx.send(middlef)


@client.command()
async def txt17(ctx):
  await ctx.message.delete()
  middlef = r"\(@^0^@)/"
  await ctx.send(middlef)


@client.command()
async def txt18(ctx):
  await ctx.message.delete()
  middlef = r"ヾ(^▽^*)))"
  await ctx.send(middlef)


@client.command()
async def txt19(ctx):
  await ctx.message.delete()
  middlef = r"(～﹃～)~zZ"
  await ctx.send(middlef)


@client.command()
async def txt20(ctx):
  await ctx.message.delete()
  middlef = r"☆⌒(*＾-゜)v"
  await ctx.send(middlef)


@client.command()
async def txt21(ctx):
  await ctx.message.delete()
  middlef = r"(￣o￣) . z Z"
  await ctx.send(middlef)


@client.command()
async def txt22(ctx):
  await ctx.message.delete()
  middlef = r"(*￣;(￣ *)"
  await ctx.send(middlef)


@client.command()
async def txt23(ctx):
  await ctx.message.delete()
  middlef = r"||ヽ(*￣▽￣*)ノミ|Ю"
  await ctx.send(middlef)


@client.command()
async def txt24(ctx):
  await ctx.message.delete()
  middlef = r"☆⌒(*＾-゜)v"
  await ctx.send(middlef)


@client.command()
async def txt25(ctx):
  await ctx.message.delete()
  middlef = r"(＾Ｕ＾)ノ~ＹＯ)"
  await ctx.send(middlef)


@client.command()
async def txt26(ctx):
  await ctx.message.delete()
  middlef = r"o(*°▽°*)o"
  await ctx.send(middlef)


@client.command()
async def txt27(ctx):
  await ctx.message.delete()
  middlef = r"ヾ(￣▽￣) Bye~Bye~"
  await ctx.send(middlef)


@client.command()
async def txt28(ctx):
  await ctx.message.delete()
  middlef = r"( ﾟдﾟ)つ Bye)"
  await ctx.send(middlef)


@client.command()
async def txt29(ctx):
  await ctx.message.delete()
  middlef = r"(๑•̀ㅂ•́)و✧)"
  await ctx.send(middlef)


@client.command()
async def txt30(ctx):
  await ctx.message.delete()
  middlef = r"(ﾉ◕ヮ◕)ﾉ*:･ﾟ✧"
  await ctx.send(middlef)


@client.command()
async def txt31(ctx):
  await ctx.message.delete()
  middlef = r"(∩^o^)⊃━☆)"
  await ctx.send(middlef)

@client.command()
async def txt32(ctx):
  await ctx.message.delete()
  middlef = r"✪ ω ✪"
  await ctx.send(middlef)


@client.command()
async def txt33(ctx):
  await ctx.message.delete()
  middlef = r"d=====(￣▽￣*)b"
  await ctx.send(middlef)


@client.command()
async def txt34(ctx):
  await ctx.message.delete()
  middlef = r"＜（＾－＾）＞"
  await ctx.send(middlef)


@client.command()
async def txt35(ctx):
  await ctx.message.delete()
  middlef = r"o(*￣▽￣*)o"
  await ctx.send(middlef)


@client.command()
async def txt36(ctx):
  await ctx.message.delete()
  middlef = r"o(￣▽￣)ｄ"
  await ctx.send(middlef)


@client.command()
async def txt37(ctx):
  await ctx.message.delete()
  middlef = r"(╹ڡ╹ ))"
  await ctx.send(middlef)


@client.command()
async def txt38(ctx):
  await ctx.message.delete()
  middlef = r"(u‿ฺu✿ฺ))"
  await ctx.send(middlef)


@client.command()
async def txt39(ctx):
  await ctx.message.delete()
  middlef = r"♪(´▽｀)"
  await ctx.send(middlef)


@client.command()
async def txt40(ctx):
  await ctx.message.delete()
  middlef = r"(╯▽╰ ))"
  await ctx.send(middlef)


@client.command()
async def txt41(ctx):
  await ctx.message.delete()
  middlef = r"ヽ(✿ﾟ▽ﾟ)ノ"
  await ctx.send(middlef)


@client.command()
async def txt42(ctx):
  await ctx.message.delete()
  middlef = r"( •̀ .̫ •́ )✧"
  await ctx.send(middlef)


@client.command()
async def txt43(ctx):
  await ctx.message.delete()
  middlef = r"(^^ゞ"
  await ctx.send(middlef)


@client.command()
async def txt44(ctx):
  await ctx.message.delete()
  middlef = r"(＠＾０＾)"
  await ctx.send(middlef)


@client.command()
async def txt45(ctx):
  await ctx.message.delete()
  middlef = r"（。＾▽＾）"
  await ctx.send(middlef)


@client.command()
async def txt46(ctx):
  await ctx.message.delete()
  middlef = r"Ψ(￣∀￣)Ψ"
  await ctx.send(middlef)


@client.command()
async def txt47(ctx):
  await ctx.message.delete()
  middlef = r"*★,°*:.☆(￣▽￣)/$:*.°★* 。"
  await ctx.send(middlef)


@client.command()
async def txt48(ctx):
  await ctx.message.delete()
  middlef = r"o(≧∀≦)o"
  await ctx.send(middlef)


@client.command()
async def txt49(ctx):
  await ctx.message.delete()
  middlef = r"(。・∀・)ノ"
  await ctx.send(middlef)


@client.command()
async def txt50(ctx):
  await ctx.message.delete()
  middlef = r"~\(≧▽≦)/~"
  await ctx.send(middlef)


@client.command()
async def txt51(ctx):
  await ctx.message.delete()
  middlef = r"b(￣▽￣)d"
  await ctx.send(middlef)


@client.command()
async def txt52(ctx):
  await ctx.message.delete()
  middlef = r"o(^▽^)o"
  await ctx.send(middlef)


@client.command()
async def txt53(ctx):
  await ctx.message.delete()
  middlef = r"(☞ﾟヮﾟ)☞"
  await ctx.send(middlef)


@client.command()
async def txt54(ctx):
  await ctx.message.delete()
  middlef = r"☜(ﾟヮﾟ☜)"
  await ctx.send(middlef)


@client.command()
async def txt55(ctx):
  await ctx.message.delete()
  middlef = r"☜(⌒▽⌒)☞"
  await ctx.send(middlef)


@client.command()
async def txt56(ctx):
  await ctx.message.delete()
  middlef = r"(¬‿¬)"
  await ctx.send(middlef)


@client.command()
async def txt57(ctx):
  await ctx.message.delete()
  middlef = r"(•_•)"
  await ctx.send(middlef)


@client.command()
async def txt58(ctx):
  await ctx.message.delete()
  middlef = r"( •_•)>⌐■-■"
  await ctx.send(middlef)


@client.command()
async def txt59(ctx):
  await ctx.message.delete()
  middlef = r"(⌐■_■)"
  await ctx.send(middlef)


@client.command()
async def txt60(ctx):
  await ctx.message.delete()
  middlef = r"ヾ(⌐■_■)ノ♪"
  await ctx.send(middlef)


@client.command()
async def txt61(ctx):
  await ctx.message.delete()
  middlef = r"(▀̿Ĺ̯▀̿ ̿)"
  await ctx.send(middlef)


@client.command()
async def txt62(ctx):
  await ctx.message.delete()
  middlef = r"＼(ﾟｰﾟ＼)"
  await ctx.send(middlef)


@client.command()
async def txt63(ctx):
  await ctx.message.delete()
  middlef = r"( ﾉ ﾟｰﾟ)ﾉ"
  await ctx.send(middlef)


@client.command(aliases=['dong', 'penis', 'pp', 'psize', 'dicksize', 'penissize'])
async def dick(ctx, *, user: discord.User = None):
  loading_message = await ctx.send(embed=please_wait_emb)
  
  try:
    if user is None:
      user = ctx.author
      size = random.randint(2, 20) # this is the random dick size!
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
      size = random.randint(2, 20)
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


@client.command()
async def panda(ctx):
  loading_message = await ctx.send(embed=please_wait_emb)
  
  try:
    r = requests.get("https://some-random-api.ml/img/panda").json()

    embed = discord.Embed(color=0xff0000)
    embed.set_author(name="a Panda.", icon_url="https://cdn.freebiesupply.com/logos/large/2x/panda-7-logo-png-transparent.png") 
    embed.set_image(url=str(r["link"]))
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


@client.command(aliases=["lol"])
async def meme(ctx):
  loading_message = await ctx.send(embed=please_wait_emb)

  try:
    r = requests.get("https://some-random-api.ml/meme").json()

    embed = discord.Embed(color=0xff0000)
    embed.set_author(name="a Meme.", icon_url="https://freepngimg.com/thumb/internet_meme/3-2-troll-face-meme-png-thumb.png") 
    
    try:
      caption = str(r["caption"])
      embed.add_field(name="Just a random Meme", value=caption)
    except:
      pass
    
    embed.set_image(url=str(r["image"]))
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
async def dog(ctx):
  loading_message = await ctx.send(embed=please_wait_emb)
  try:
    r = requests.get("https://some-random-api.ml/img/dog").json()
    embed = discord.Embed(color=0xff0000)
    embed.set_author(name="a Dog." , icon_url="https://t4.ftcdn.net/jpg/03/66/78/13/360_F_366781345_oEr9wc8yWhYRPZe6CGyFWS6QolZIf2fJ.jpg") 
    embed.set_image(url=str(r["link"]))
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
async def cat(ctx):
  try:
    loading_message = await ctx.send(embed=please_wait_emb)
    r = requests.get("https://some-random-api.ml/img/cat").json()
    embed = discord.Embed(color=0xff0000)
    embed.set_author(name="a Cat.", icon_url="https://i.pinimg.com/736x/d6/0c/7e/d60c7e8983fdbd7c7a27fd42fb3d61ba.jpg") 
    embed.set_image(url=str(r["link"]))
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


@client.command(aliases=['pfp', 'avatar'])
async def av(ctx, *, user: discord.User = None):
  loading_message = await ctx.send(embed=please_wait_emb)

  try:
    format = "gif"
    user = user or ctx.author
    if user.is_avatar_animated() != True:
      format = "png"
    avatar = user.avatar_url_as(format=format if format != "gif" else None)
    async with aiohttp.ClientSession() as session:
      async with session.get(str(avatar)) as resp:
        image = await resp.read()
    with io.BytesIO(image) as file:
        await loading_message.delete()
        await ctx.send(file=discord.File(file, f"Avatar.{format}"))
  
  except Exception as e:
    embed3=discord.Embed(title=":red_square: Error!", description="The command was unable to run successfully! ", color=0xff0000)
    embed3.set_author(name="YourBot", icon_url="https://cdn.discordapp.com/attachments/877796755234783273/879295069834850324/Avatar.png")
    embed3.set_thumbnail(url="https://cdn.discordapp.com/attachments/877796755234783273/879298565380386846/sign-red-error-icon-1.png")
    embed3.add_field(name="Error:", value=f"{e}", inline=False)
    embed3.set_footer(text=f"Requested by {ctx.author.name}")
    await loading_message.delete()
    await ctx.send(embed=embed3)


@client.command(aliases=["av2"])
async def newav(ctx, user: discord.User = None):
  loading_message = await ctx.send(embed=please_wait_emb)

  link = f"{ctx.author.avatar_url}"
  await ctx.send(link)
  await ctx.send("STILL UNDER DEVELOPMENT!")
  await loading_message.delete()


@client.command(aliases=["guildinfo", "serverinfo", "si"])
async def infoserver(ctx):
  try:
    loading_message = await ctx.send(embed=please_wait_emb)
    date_format = "%a, %d %b %Y %I:%M %p"
    embed = discord.Embed(title=f"Server Info of {ctx.guild.name}:",
                              description=f"{ctx.guild.member_count} Members\n {len(ctx.guild.roles)} Roles\n {len(ctx.guild.text_channels)} Text-Channels\n {len(ctx.guild.voice_channels)} Voice-Channels\n {len(ctx.guild.categories)} Categories",
                              timestamp=datetime.datetime.utcnow(), color=0xff0000)
    embed.add_field(name="Server created at", value=f"{ctx.guild.created_at.strftime(date_format)}")
    embed.add_field(name="Server Owner", value=f"<@{ctx.guild.owner_id}>")
    embed.add_field(name="Server Region", value=f"{ctx.guild.region}")
    embed.add_field(name="Server ID", value=f"{ctx.guild.id}")
    embed.add_field(name="Bots", value=len(list(filter(lambda m: m.bot, ctx.guild.members))))
    embed.add_field(name="Banned members", value=len(await ctx.guild.bans()))
    embed.add_field(name="Invites", value=len(await ctx.guild.invites()))
    embed.set_footer(text=f"Requested by {ctx.author.name}")
    embed.set_thumbnail(url=f"{ctx.guild.icon_url}")
    embed.set_author(name="YourBot", icon_url="https://cdn.discordapp.com/attachments/877796755234783273/879295069834850324/Avatar.png")
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

  # emsi = discord.Embed(title=f'Info of **__{ctx.guild.name}__**')
  # emsi.set_thumbnail(url=f"{ctx.guild.icon_url}")
  # emsi.add_field(name=f"**Name: **", value=f'{ctx.guild.name}', inline=True)
  # emsi.add_field(name=f"ID:", value=f'{ctx.guild.id}', inline=True)
  # emsi.add_field(name=f"Owner:", value=f'<@{ctx.guild.owner_id}>', inline=True)
  # emsi.add_field(name=f"Owner ID:", value=f'{ctx.guild.owner_id}', inline=True)
  # emsi.add_field(name=f"Region:", value=f'{ctx.guild.region}', inline=True)
  # await ctx.send(embed=emsi)
 


@client.command(aliases=["servericon"])
async def guildicon(ctx):
  loading_message = await ctx.send(embed=please_wait_emb)

  try:
    embed = discord.Embed(color=0xff0000)
    embed.set_author(name=ctx.guild.name, icon_url=ctx.guild.icon_url)   
    embed.set_image(url=ctx.guild.icon_url)
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

@client.command(aliases=["account-creation-date", "account-date"])
async def accdate(ctx, *, user: discord.User = None):
  loading_message = await ctx.send(embed=please_wait_emb)

  try:
    if user is None:
      user = ctx.author      
    date_format = "%a, %d %b %Y %I:%M %p"
    em = discord.Embed(description=user.mention, color=0xff0000)
    em.set_author(name=str(user), icon_url=user.avatar_url)
    em.set_thumbnail(url=user.avatar_url)
    em.add_field(name="Registered", value=user.created_at.strftime(date_format))
    em.set_footer(text=f"Requested by {ctx.author.name}")
    await loading_message.delete()
    return await ctx.send(embed=em)
  
  except Exception as e:
    embed3=discord.Embed(title=":red_square: Error!", description="The command was unable to run successfully! ", color=0xff0000)
    embed3.set_author(name="YourBot", icon_url="https://cdn.discordapp.com/attachments/877796755234783273/879295069834850324/Avatar.png")
    embed3.set_thumbnail(url="https://cdn.discordapp.com/attachments/877796755234783273/879298565380386846/sign-red-error-icon-1.png")
    embed3.add_field(name="Error:", value=f"{e}", inline=False)
    embed3.set_footer(text=f"Requested by {ctx.author.name}")
    await loading_message.delete()
    await ctx.send(embed=embed3)


@client.command(aliases=["userinfo", "uinfo", "user-info"])
async def whoareyou(ctx, target: Optional[discord.Member]):
  loading_message = await ctx.send(embed=please_wait_emb)

  try:
    target = target or ctx.author

    embed = discord.Embed(title="User Information", color=target.color, timestamp=datetime.datetime.utcnow())

    fields = [("Name", str(target), True),
            ("ID", target.id, True),
            ("Bot?", target.bot, True),
            ("Top role", target.top_role.mention, True),
            ("Status", str(target.status).title(), True),
            ("Activity", f"{str(target.activity.type).split('.')[-1].title() if target.activity else 'N/A'} {target.activity.name if target.activity else ''}", True),
            ("Created at", target.created_at.strftime("%d/%m/%Y %H:%M:%S"), True),
            ("Joined at", target.joined_at.strftime("%d/%m/%Y %H:%M:%S"), True),
            ("Boosted", bool(target.premium_since), True)]
    
    for name, value, inline in fields:
      embed.add_field(name=name, value=value, inline=inline)
    
    embed.set_thumbnail(url=f"{target.avatar_url}")
    embed.set_author(name="YourBot", icon_url="https://cdn.discordapp.com/attachments/877796755234783273/879295069834850324/Avatar.png")
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


@client.command(aliases=["e_base64"])
async def e_b64(ctx, *, args):
  loading_message = await ctx.send(embed=please_wait_emb)

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

@client.command()
async def e_md5(ctx, *, args):
  loading_message = await ctx.send(embed=please_wait_emb)

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

@client.command()
async def e_sha1(ctx, *, args):
  loading_message = await ctx.send(embed=please_wait_emb)

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

@client.command()
async def e_sha224(ctx, *, args):
  loading_message = await ctx.send(embed=please_wait_emb)

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

@client.command()
async def e_sha512(ctx, *, args):
  loading_message = await ctx.send(embed=please_wait_emb)

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

@client.command(aliases=["leet"])
async def e_leet(ctx, *, args):
  loading_message = await ctx.send(embed=please_wait_emb)

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


@client.command(aliases=["addition"])
async def add(ctx, number_1, number_2):
  loading_message = await ctx.send(embed=please_wait_emb)
  try:
    ans = float(number_1) + float(number_2)

    embed=discord.Embed(title="Addition", color=0xff0000)
    embed.set_author(name="YourBot", icon_url="https://cdn.discordapp.com/attachments/877796755234783273/879295069834850324/Avatar.png")
    embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/877796755234783273/879962889509806080/addition-icon-3.jpg")
    embed.add_field(name="Query", value=f"{number_1} + {number_2}", inline=False)
    embed.add_field(name="Result", value=f"{ans}", inline=True)
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


@client.command(aliases=["substraction", "substract"])
async def subs(ctx, number_1, number_2):
  loading_message = await ctx.send(embed=please_wait_emb)

  try:
    ans = float(number_1) - float(number_2)

    embed=discord.Embed(title="Substraction", color=0xff0000)
    embed.set_author(name="YourBot", icon_url="https://cdn.discordapp.com/attachments/877796755234783273/879295069834850324/Avatar.png")
    embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/877796755234783273/879964954806083604/1043.png")
    embed.add_field(name="Query", value=f"{number_1} - {number_2}", inline=False)
    embed.add_field(name="Result", value=f"{ans}", inline=True)
    embed.set_footer(text=f"Requested by {ctx.author.name}")
    await ctx.send(embed=embed)
  
  except Exception as e:
    embed3=discord.Embed(title=":red_square: Error!", description="The command was unable to run successfully! ", color=0xff0000)
    embed3.set_author(name="YourBot", icon_url="https://cdn.discordapp.com/attachments/877796755234783273/879295069834850324/Avatar.png")
    embed3.set_thumbnail(url="https://cdn.discordapp.com/attachments/877796755234783273/879298565380386846/sign-red-error-icon-1.png")
    embed3.add_field(name="Error:", value=f"{e}", inline=False)
    embed3.set_footer(text=f"Requested by {ctx.author.name}")
    await loading_message.delete()
    await ctx.send(embed=embed3)


@client.command(aliases=["multiplication", "multiply"])
async def mul(ctx, number_1, number_2):
  loading_message = await ctx.send(embed=please_wait_emb)

  try:
    ans = float(number_1) * float(number_2)

    embed=discord.Embed(title="Multiplication", color=0xff0000)
    embed.set_author(name="YourBot", icon_url="https://cdn.discordapp.com/attachments/877796755234783273/879295069834850324/Avatar.png")
    embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/877796755234783273/879965848603869214/43165.png")
    embed.add_field(name="Query", value=f"{number_1} x {number_2}", inline=False)
    embed.add_field(name="Result", value=f"{ans}", inline=True)
    embed.set_footer(text="Requested by {ctx.author.name}")
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


@client.command(aliases=["division", "divide"])
async def div(ctx, number_1, number_2):
  loading_message = await ctx.send(embed=please_wait_emb)

  try:
    ans = float(number_1) / float(number_2)

    embed=discord.Embed(title="Division", color=0xff0000)
    embed.set_author(name="YourBot", icon_url="https://cdn.discordapp.com/attachments/877796755234783273/879295069834850324/Avatar.png")
    embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/877796755234783273/879966441502294026/674233_mathematics_512x512.png")
    embed.add_field(name="Query", value=f"{number_1} / {number_2}", inline=False)
    embed.add_field(name="Result", value=f"{ans}", inline=True)
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


@client.command(aliases=["echo"])
async def say(ctx, *, word_to_say):
  await ctx.message.delete()
  await ctx.send(str(word_to_say))


@client.command(aliases=["dog-facts", "dogfacts", "dog-fact"])
async def dogfact(ctx):
  loading_message = await ctx.send(embed=please_wait_emb)

  try:
    r = requests.get('https://some-random-api.ml/facts/dog')
    c = r.json()
    fact = c["fact"]

    embed=discord.Embed(title="Dog Fact", color=0xff0000)
    embed.set_author(name="YourBot", icon_url="https://cdn.discordapp.com/attachments/877796755234783273/879295069834850324/Avatar.png")
    embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/877796755234783273/880010039581102110/322868_1100-800x825.jpg")
    embed.add_field(name="Fact", value=f"{fact}", inline=False)
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


@client.command(aliases=["cat-facts", "catfacts", "cat-fact"])
async def catfact(ctx):
  loading_message = await ctx.send(embed=please_wait_emb)

  try:
    r = requests.get('https://some-random-api.ml/facts/cat')
    c = r.json()
    fact = c["fact"]

    embed=discord.Embed(title="Cat Fact", color=0xff0000)
    embed.set_author(name="YourBot", icon_url="https://cdn.discordapp.com/attachments/877796755234783273/879295069834850324/Avatar.png")
    embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/877796755234783273/880010397392969788/3683.jpg")
    embed.add_field(name="Fact", value=f"{fact}", inline=False)
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


@client.command(aliases=["elephant-facts", "elephantfacts", "elephant-fact"])
async def elephantfact(ctx):
  loading_message = await ctx.send(embed=please_wait_emb)

  try:
    r = requests.get('https://some-random-api.ml/facts/elephant')
    c = r.json()
    fact = c["fact"]

    embed=discord.Embed(title="Elephant Fact", color=0xff0000)
    embed.set_author(name="YourBot", icon_url="https://cdn.discordapp.com/attachments/877796755234783273/879295069834850324/Avatar.png")
    embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/877796755234783273/880010717913309204/WW187785.jpg")
    embed.add_field(name="Fact", value=f"{fact}", inline=False)
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


@client.command(aliases=["panda-facts", "pandafacts", "panda-fact"])
async def pandafact(ctx):
  loading_message = await ctx.send(embed=please_wait_emb)

  try:
    r = requests.get('https://some-random-api.ml/facts/panda')
    c = r.json()
    fact = c["fact"]

    embed=discord.Embed(title="Panda Fact", color=0xff0000)
    embed.set_author(name="YourBot", icon_url="https://cdn.discordapp.com/attachments/877796755234783273/879295069834850324/Avatar.png")
    embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/877796755234783273/880011140816576552/BabyGiantPanda.jpg")
    embed.add_field(name="Fact", value=f"{fact}", inline=False)
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


@client.command(aliases=["fox-facts", "foxfacts", "fox-fact"])
async def foxfact(ctx):
  loading_message = await ctx.send(embed=please_wait_emb)

  try:
    r = requests.get('https://some-random-api.ml/facts/fox')
    c = r.json()
    fact = c["fact"]

    embed=discord.Embed(title="Fox Fact", color=0xff0000)
    embed.set_author(name="YourBot", icon_url="https://cdn.discordapp.com/attachments/877796755234783273/879295069834850324/Avatar.png")
    embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/877796755234783273/880011829194153984/im-355811.jfif")
    embed.add_field(name="Fact", value=f"{fact}", inline=False)
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


@client.command(aliases=["bird-facts", "birdfacts", "bird-fact"])
async def birdfact(ctx):
  loading_message = await ctx.send(embed=please_wait_emb)

  try:
    r = requests.get('https://some-random-api.ml/facts/bird')
    c = r.json()
    fact = c["fact"]

    embed=discord.Embed(title="Bird Fact", color=0xff0000)
    embed.set_author(name="YourBot", icon_url="https://cdn.discordapp.com/attachments/877796755234783273/879295069834850324/Avatar.png")
    embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/877796755234783273/880012668084305930/DCTM_Penguin_UK_DK_AL526630_wkmzns.jpg")
    embed.add_field(name="Fact", value=f"{fact}", inline=False)
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


@client.command(aliases=["koala-facts", "koalafacts", "koala-fact"])
async def koalafact(ctx):
  loading_message = await ctx.send(embed=please_wait_emb)

  try:
    r = requests.get('https://some-random-api.ml/facts/koala')
    c = r.json()
    fact = c["fact"]

    embed=discord.Embed(title="Koala Fact", color=0xff0000)
    embed.set_author(name="YourBot", icon_url="https://cdn.discordapp.com/attachments/877796755234783273/879295069834850324/Avatar.png")
    embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/877796755234783273/880013091897770014/Koala.jpg")
    embed.add_field(name="Fact", value=f"{fact}", inline=False)
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


@client.command(aliases=["red-panda", "red-panda-image", "red-panda-img"])
async def redpanda(ctx):
  loading_message = await ctx.send(embed=please_wait_emb)

  try:
    r = requests.get('https://some-random-api.ml/img/red_panda')
    c = r.json()
    fact = c["link"]

    embed=discord.Embed(title="Red Panda Fact", color=0xff0000)
    embed.set_author(name="YourBot", icon_url="https://cdn.discordapp.com/attachments/877796755234783273/879295069834850324/Avatar.png")
    embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/877796755234783273/880013593465217034/16071828377_85109fdee4_o.0.0.jpg")
    embed.add_field(name="Fact", value=f"{fact}", inline=False)
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


@client.command(aliases=["birds", "bird-image", "bird-img"])
async def bird(ctx):
  loading_message = await ctx.send(embed=please_wait_emb)

  try:
    r = requests.get('https://some-random-api.ml/img/birb')
    c = r.json()
    fact = c["link"]
    em = discord.Embed(title='a Bird', color=0xff0000)
    em.set_author(name='a Random Bird', icon_url='https://ichef.bbci.co.uk/news/976/cpsprodpb/67CF/production/_108857562_mediaitem108857561.jpg')
    em.set_image(url=fact)
    em.set_footer(text=f"Requested by {ctx.author.name}")
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


@client.command(aliases=["foxes", "fox-image", "fox-img"])
async def fox(ctx):
  loading_message = await ctx.send(embed=please_wait_emb)

  try:
    r = requests.get('https://some-random-api.ml/img/fox')
    c = r.json()
    fact = c["link"]
    em = discord.Embed(title='a Fox', color=0xff0000)
    em.set_author(name='a Fox', icon_url='https://images.unsplash.com/photo-1615602127413-459bdb48cf45?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=1000&q=80')
    em.set_image(url=fact)
    em.set_footer(text=f"Requested by {ctx.author.name}")
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

@client.command(aliases=["a-wink", "winks"])
async def wink(ctx):
  loading_message = await ctx.send(embed=please_wait_emb)

  try:
    r = requests.get('https://some-random-api.ml/animu/wink')
    c = r.json()
    fact = c["link"]
    em = discord.Embed(title='a wink', color=0xff0000)
    em.set_author(name="YourBot", icon_url="https://cdn.discordapp.com/attachments/877796755234783273/879295069834850324/Avatar.png")
    em.set_image(url=fact)
    em.set_footer(text=f"Requested by {ctx.author.name}")
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


@client.command(aliases=["a-pikachu", "pikachuu"])
async def pikachu(ctx):
  loading_message = await ctx.send(embed=please_wait_emb)

  try:
    r = requests.get('https://some-random-api.ml/img/pikachu')
    c = r.json()
    fact = c["link"]
    em = discord.Embed(title='a Pickachu', color=0xff0000)
    em.set_author(name="YourBot", icon_url="https://cdn.discordapp.com/attachments/877796755234783273/879295069834850324/Avatar.png")
    em.set_image(url=fact)
    em.set_footer(text=f"Requested by {ctx.author.name}")
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


@client.command(aliases=["gay-colors", "gay-colours"])
async def gay(ctx, *, messagelink):
  loading_message = await ctx.send(embed=please_wait_emb)

  try:
    weblink = 'https://some-random-api.ml/canvas/gay?avatar=' + messagelink
    r = requests.get(weblink)
    em = discord.Embed(title='Gay Picture', color=0xff0000)
    em.set_author(name="YourBot", icon_url="https://cdn.discordapp.com/attachments/877796755234783273/879295069834850324/Avatar.png")
    em.set_image(url=weblink)
    em.set_footer(text=f"Requested by {ctx.author.name}")
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


@client.command(aliases=["glass-colors", "glass-colours", "glassy-colors", "glassy-colours"])
async def glass(ctx, *, messagelink):
  loading_message = await ctx.send(embed=please_wait_emb)

  try:
    weblink = 'https://some-random-api.ml/canvas/glass/?avatar=' + messagelink
    em = discord.Embed(title='Glassy Picture', color=0xff0000)
    em.set_author(name="YourBot", icon_url="https://cdn.discordapp.com/attachments/877796755234783273/879295069834850324/Avatar.png")
    em.set_image(url=weblink)
    em.set_footer(text=f"Requested by {ctx.author.name}")
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


@client.command(aliases=["wasted-colors", "wasted-colours", "wasted-image", "wasted-img"])
async def wasted(ctx, *, messagelink, color=0xff0000):
  loading_message = await ctx.send(embed=please_wait_emb)

  try:
    weblink = 'https://some-random-api.ml/canvas/glass/?avatar=' + messagelink
    em = discord.Embed(title='a Wasted Picture', color=0xff0000)
    em.set_author(name="YourBot", icon_url="https://cdn.discordapp.com/attachments/877796755234783273/879295069834850324/Avatar.png")
    em.set_image(url=weblink)
    em.set_footer(text=f"Requested by {ctx.author.name}")
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


@client.command()
async def triggered(ctx, *, messagelink):
  loading_message = await ctx.send(embed=please_wait_emb)

  try:
    weblink = 'https://some-random-api.ml/canvas/triggered?avatar=' + messagelink
    em = discord.Embed(title='a TRIGGERED Picture', color=0xff0000)
    em.set_author(name="YourBot", icon_url="https://cdn.discordapp.com/attachments/877796755234783273/879295069834850324/Avatar.png")
    em.set_image(url=weblink)
    em.set_footer(text=f"Requested by {ctx.author.name}")
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


@client.command(aliases=["bandw", "black-and-white"])
async def grayscale(ctx, *, messagelink):
  loading_message = await ctx.send(embed=please_wait_emb)

  try:
    weblink = 'https://some-random-api.ml/canvas/greyscale?avatar=' + messagelink
    em = discord.Embed(title='a Black and White Picture', color=0xff0000)
    em.set_author(name="YourBot", icon_url="https://cdn.discordapp.com/attachments/877796755234783273/879295069834850324/Avatar.png")
    em.set_image(url=weblink)
    em.set_footer(text=f"Requested by {ctx.author.name}")
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


@client.command(aliases=["invert-img", "invert-colors", "invert-image"])
async def invert(ctx, *, messagelink):
  loading_message = await ctx.send(embed=please_wait_emb)

  try:
    weblink = 'https://some-random-api.ml/canvas/invert?avatar=' + messagelink
    em = discord.Embed(title='a Inverted Picture', color=0xff0000)
    em.set_author(name="YourBot", icon_url="https://cdn.discordapp.com/attachments/877796755234783273/879295069834850324/Avatar.png")
    em.set_image(url=weblink)
    em.set_footer(text=f"Requested by {ctx.author.name}")
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


@client.command(aliases=["bright-img", "bright-colors", "bright-image", "bright"])
async def brightness(ctx, *, messagelink):
  loading_message = await ctx.send(embed=please_wait_emb)

  try:
    weblink = 'https://some-random-api.ml/canvas/brightness?avatar=' + messagelink
    em = discord.Embed(title='a Brightened Picture', color=0xff0000)
    em.set_author(name="YourBot", icon_url="https://cdn.discordapp.com/attachments/877796755234783273/879295069834850324/Avatar.png")
    em.set_image(url=weblink)
    em.set_footer(text=f"Requested by {ctx.author.name}")
    await loading_message.delete()
    await ctx.send(embed=em)
  
  except Exception as e:
    embed3=discord.Embed(title=":red_square: Error!", description="The command was unable to run successfully! ", color=0xff0000)
    embed3.set_author(name="YourBot", icon_url="https://cdn.discordapp.com/attachments/877796755234783273/879295069834850324/Avatar.png")
    embed3.set_thumbnail(url="https://cdn.discordapp.com/attachments/877796755234783273/879298565380386846/sign-red-error-icon-1.png")
    embed3.add_field(name="Error:", value=f"{e}", inline=False)
    embed3.set_footer(text=f"Requested by {ctx.author.name}")
    em.set_footer(text=f"Requested by {ctx.author.name}")
    await loading_message.delete()
    await ctx.send(embed=embed3)


@client.command(aliases=["threshold-img", "threshold-colors", "threshold-image", "thresh"])
async def threshold(ctx, *, messagelink):
  loading_message = await ctx.send(embed=please_wait_emb)

  try:
    weblink = 'https://some-random-api.ml/canvas/threshold?avatar=' + messagelink
    em = discord.Embed(title='a Threshold Picture', color=0xff0000)
    em.set_author(name="YourBot", icon_url="https://cdn.discordapp.com/attachments/877796755234783273/879295069834850324/Avatar.png")
    em.set_image(url=weblink)
    em.set_footer(text=f"Requested by {ctx.author.name}")
    await loading_message.delete()
    await ctx.send(embed=em)

  except Exception as e:
    embed3=discord.Embed(title=":red_square: Error!", description="The command was unable to run successfully! ", color=0xff0000)
    embed3.set_author(name="YourBot", icon_url="https://cdn.discordapp.com/attachments/877796755234783273/879295069834850324/Avatar.png")
    embed3.set_thumbnail(url="https://cdn.discordapp.com/attachments/877796755234783273/879298565380386846/sign-red-error-icon-1.png")
    embed3.add_field(name="Error:", value=f"{e}", inline=False)
    embed3.set_footer(text=f"Requested by {ctx.author.name}")
    em.set_footer(text=f"Requested by {ctx.author.name}")
    await loading_message.delete()
    await ctx.send(embed=embed3)


@client.command(aliases=["sepia-image", "sepia-color"])
async def sepia(ctx, *, messagelink):
  loading_message = await ctx.send(embed=please_wait_emb)

  try:
    weblink = 'https://some-random-api.ml/canvas/greyscale?avatar=' + messagelink
    em = discord.Embed(title='a Sepia Picture', color=0xff0000)
    em.set_author(name="YourBot", icon_url="https://cdn.discordapp.com/attachments/877796755234783273/879295069834850324/Avatar.png")
    em.set_image(url=weblink)
    em.set_footer(text=f"Requested by {ctx.author.name}")
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


@client.command(aliases=["red-image", "red-color"])
async def red(ctx, *, messagelink):
  loading_message = await ctx.send(embed=please_wait_emb)

  try:
    weblink = 'https://some-random-api.ml/canvas/red?avatar=' + messagelink
    em = discord.Embed(title='a Red Picture', color=0xff0000)
    em.set_author(name="YourBot", icon_url="https://cdn.discordapp.com/attachments/877796755234783273/879295069834850324/Avatar.png")
    em.set_image(url=weblink)
    em.set_footer(text=f"Requested by {ctx.author.name}")
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


@client.command(aliases=["green-image", "green-color"])
async def green(ctx, *, messagelink):
  loading_message = await ctx.send(embed=please_wait_emb)

  try:
    weblink = 'https://some-random-api.ml/canvas/green?avatar=' + messagelink
    em = discord.Embed(title='a Green Picture', color=0xff0000)
    em.set_author(name="YourBot", icon_url="https://cdn.discordapp.com/attachments/877796755234783273/879295069834850324/Avatar.png")
    em.set_image(url=weblink)
    em.set_footer(text=f"Requested by {ctx.author.name}")
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


@client.command(aliases=["blue-image", "blue-color"])
async def blue(ctx, *, messagelink):
  loading_message = await ctx.send(embed=please_wait_emb)

  try:
    weblink = 'https://some-random-api.ml/canvas/blue?avatar=' + messagelink
    em = discord.Embed(title='a Blue Picture', color=0xff0000)
    em.set_author(name="YourBot", icon_url="https://cdn.discordapp.com/attachments/877796755234783273/879295069834850324/Avatar.png")
    em.set_image(url=weblink)
    em.set_footer(text=f"Requested by {ctx.author.name}")
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


@client.command(aliases=["tint-image", "tint-color"])
async def tint(ctx, colorTotint, *, messagelink):
  loading_message = await ctx.send(embed=please_wait_emb)

  try:
    weblink = 'https://some-random-api.ml/canvas/color?avatar=' + messagelink + "&color=%" + colorTotint
    em = discord.Embed(title='a Tinted Picture', color=0xff0000)
    embed_text = "Picture tinted in " + colorTotint
    em.set_author(name="YourBot", icon_url="https://cdn.discordapp.com/attachments/877796755234783273/879295069834850324/Avatar.png")
    em.set_image(url=weblink)
    em.set_footer(text=f"Requested by {ctx.author.name}")
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


@client.command(aliases=["pixelate-image"])
async def pixelate(ctx, *, messagelink):
  loading_message = await ctx.send(embed=please_wait_emb)

  try:
    weblink = 'https://some-random-api.ml/canvas/pixelate' + messagelink
    em = discord.Embed(title='a Blue Picture', color=0xff0000)
    em.set_author(name="YourBot", icon_url="https://cdn.discordapp.com/attachments/877796755234783273/879295069834850324/Avatar.png")
    em.set_image(url=weblink)
    em.set_footer(text=f"Requested by {ctx.author.name}")
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


@client.command(aliases=["ytc", "youtubecomment", "youtube-comment", "yt-comment", "you-tube-comment"])
async def ytcomment(ctx, usernameofu="ZeaCeR5641", commentmsg="This_is_a_test", profilepictureLink="https://static.wikia.nocookie.net/ba0628fe-3bc1-42c3-9c0c-aa91ba24f03c/scale-to-width/370", mode="dark"):
  loading_message = await ctx.send(embed=please_wait_emb)

  try:
    weblink = "https://some-random-api.ml/canvas/youtube-comment?username=" + usernameofu.replace("_", "%20") + "&comment=" + commentmsg.replace("_", "%20") + "&avatar=" + profilepictureLink + "&dark=true"
    # em = discord.Embed(title='a picture of a YouTube Comment')
    # em.set_author(name='Fake YouTube Comment')
    # em.set_image(url=weblink)
    # await ctx.send(embed=em)
    await loading_message.delete()
    await ctx.send(weblink)
  
  except Exception as e:
    embed3=discord.Embed(title=":red_square: Error!", description="The command was unable to run successfully! ", color=0xff0000)
    embed3.set_author(name="YourBot", icon_url="https://cdn.discordapp.com/attachments/877796755234783273/879295069834850324/Avatar.png")
    embed3.set_thumbnail(url="https://cdn.discordapp.com/attachments/877796755234783273/879298565380386846/sign-red-error-icon-1.png")
    embed3.add_field(name="Error:", value=f"{e}", inline=False)
    embed3.set_footer(text=f"Requested by {ctx.author.name}")
    await loading_message.delete()
    await ctx.send(embed=embed3)


@client.command()
async def pokemon(ctx, pokemonName="pikachu", mode="new"):
  loading_message = await ctx.send(embed=please_wait_emb)

  try:
    weblink = "https://some-random-api.ml/pokedex?pokemon=" + pokemonName
    r = requests.get(weblink)
    c = r.json()
    name = c["name"]
    id = c["id"]
    typep = c["type"]
    species = c["species"]
    abilities = c["abilities"]
    height = c["height"]
    weight = c["weight"]
    base_experience = c["base_experience"]
    gender = c["gender"]
    egg_group = c["egg_groups"]
    stats = c["stats"]
    family = c["family"]
    sprites = c["sprites"]
    description = c["description"]
    generation = c["generation"]
    # under stats
    hp = stats["hp"]
    attack = stats["attack"]
    defense = stats["defense"]
    sp_atk = stats["sp_atk"]
    sp_def = stats["sp_def"]
    total = stats["total"]
    #under sprites
    normal_sprites = sprites["normal"]
    animated_sprites = sprites["animated"]
    # under family 
    evolutionstage = family["evolutionStage"]
    evolutionsLine = family["evolutionLine"]

    if mode == "new":
      embed=discord.Embed(title="Pokemon!", color=0xff0000)
      embed.set_thumbnail(url=str(normal_sprites))
      embed.add_field(name="General", value="**+ Name:** " + str(name) + "\n**+ ID:** " + str(id) + "\n**+ Type:** " + str(typep) + "\n**+ Species:** " + str(species) + "\n**+ Abilities:** " + str(abilities) + "\n**+Height:** " + str(height) + "\n**+ Weight:** " + str(weight) + "\n**+ Base Experience:** " + str(base_experience) + "\n**+ Gender:** " + str(gender) + "\n**Egg Group:** " + str(egg_group), inline=False)
      embed.add_field(name="Stats", value="**+ HP:** " + str(hp) + "\n**+ Attack:** " + str(attack) + "\n**+ Defense:** " + str(defense) + "\n**+ SP Attack:** " + str(sp_atk) + "\n**+ SP Defense:** " + str(sp_def) + "\n**+ Total:** " + str(total), inline=False)
      embed.add_field(name="Family", value="**+ Evolution:** " + str(evolutionstage) + "\n**+ Evolution Line:** " + str(evolutionsLine), inline=False)
      embed.add_field(name="Sprites", value="**+ Normal:** " + str(normal_sprites) + "\n**+ Animated:** " + str(animated_sprites), inline=False)
      embed.add_field(name="Other", value="**+ Description:** " + str(description) + "\n**+ Generation:** " + str(generation), inline=False)
      await loading_message.delete()
      await ctx.send(embed=embed)
    
    elif mode == "old":
      pokemon_thing_info = f'''[+] Name: {name}
[+] ID: {id}
[+] Type: {typep}
[+] Species: {species}
[+] Abilities:  {abilities}
[+] Height: {height}
[+] Weight: {weight}
[+] Base Experience: {base_experience}
[+] Gender: {gender}
[+] Egg Group: {egg_group}
[+] Stats:
  [+] HP: {hp}
  [+] Attack: {attack}
  [+] Defense: {defense}
  [+] SP Attack: {sp_atk}
  [+] SP Defense: {sp_def}
  [+] Total: {total}
[+] Family:
  [+] Evolution: {evolutionstage}
  [+] Evolution Line: {evolutionsLine}
[+] Sprites:
  [+] Normal: {normal_sprites}
  [+] Animated: {animated_sprites}
[+] Description: {description}
[+] Generation: {generation}'''
      await loading_message.delete()
      await ctx.send("```" + pokemon_thing_info + "```")
  
  except Exception as e:
    embed3=discord.Embed(title=":red_square: Error!", description="The command was unable to run successfully! ", color=0xff0000)
    embed3.set_author(name="YourBot", icon_url="https://cdn.discordapp.com/attachments/877796755234783273/879295069834850324/Avatar.png")
    embed3.set_thumbnail(url="https://cdn.discordapp.com/attachments/877796755234783273/879298565380386846/sign-red-error-icon-1.png")
    embed3.add_field(name="Error:", value=f"{e}", inline=False)
    embed3.set_footer(text=f"Requested by {ctx.author.name}")
    await loading_message.delete()
    await ctx.send(embed=embed3)


@client.command(aliases=["mincraft-info", "mincraft-user-info", "minecraftinfo"])
async def mcinfo(ctx, *, MinecraftUserName):
  loading_message = await ctx.send(embed=please_wait_emb)

  try:
    weblink = "https://some-random-api.ml/mc?username=" + MinecraftUserName
    r = requests.get(weblink)
    c = r.json()

    embed=discord.Embed(title="Minecraft Account Info", color=0xff0000)
    embed.set_author(name="YourBot", icon_url="https://cdn.discordapp.com/attachments/877796755234783273/879295069834850324/Avatar.png")
    embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/877796755234783273/880022933706260530/418cEZfh8-L.jpg")
    embed.add_field(name="Username", value=f"{c['username']}", inline=False)
    embed.add_field(name="UUID", value=f"{c['uuid']}", inline=False)
    try:
      embed.add_field(name=" Name History", value=f"{c['name_history']}", inline=False)
    except:
      pass
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


@client.command(aliases=["lyricsof"])
async def lyrics(ctx, *, search = None):
  loading_message = await ctx.send(embed=please_wait_emb)

  try:
    if not search:
          embed = discord.Embed(
              title = "No search argument!",
              description = "You havent entered anything, so i couldnt find lyrics!",
              color=0xff0000
          )
          embed.set_author(name="YourBot", icon_url="https://cdn.discordapp.com/attachments/877796755234783273/879295069834850324/Avatar.png")
          embed.set_footer(text=f"Requested by {ctx.author.name}")
          try:
            await loading_message.delete()
          except:
            pass
          return await ctx.send(embed = embed)
      
    song = urllib.parse.quote(search)
    
    async with aiohttp.ClientSession() as lyricsSession:
        async with lyricsSession.get(f'https://some-random-api.ml/lyrics?title={song}') as jsondata: 
            if not 300 > jsondata.status >= 200: 
              try:
                await loading_message.delete()
              except:
                pass
                return await ctx.send(f'Recieved poor status code of {jsondata.status}')
            lyricsData = await jsondata.json() 

    error = lyricsData.get('error')
    if error: 
        try:
          await loading_message.delete()
        except:
          pass
        return await ctx.send(f'Recieved unexpected error: {error}')

    songLyrics = lyricsData['lyrics'] 
    songArtist = lyricsData['author'] 
    songTitle = lyricsData['title'] 
    songThumbnail = lyricsData['thumbnail']['genius']
    
    for chunk in textwrap.wrap(songLyrics, 4096, replace_whitespace = False):
        embed = discord.Embed(
            title = f'{songTitle} - {songArtist}',
            description = chunk,
            color = 0xff0000
            # timestamp = datetime.datetime.utcnow()
        )
        embed.set_author(name="YourBot", icon_url="https://cdn.discordapp.com/attachments/877796755234783273/879295069834850324/Avatar.png")
        embed.set_thumbnail(url = songThumbnail)
        embed.set_footer(text=f"Requested by {ctx.author.name}")
        try:
          await loading_message.delete()
        except:
          pass
        await ctx.send(embed = embed)

  except Exception as e:
    embed3=discord.Embed(title=":red_square: Error!", description="The command was unable to run successfully! ", color=0xff0000)
    embed3.set_author(name="YourBot", icon_url="https://cdn.discordapp.com/attachments/877796755234783273/879295069834850324/Avatar.png")
    embed3.set_thumbnail(url="https://cdn.discordapp.com/attachments/877796755234783273/879298565380386846/sign-red-error-icon-1.png")
    embed3.add_field(name="Error:", value=f"{e}", inline=False)
    embed3.set_footer(text=f"Requested by {ctx.author.name}")
    await loading_message.delete()
    await ctx.send(embed=embed3)


@client.command(aliases=["to-binary", "e_binary"])
async def binary(ctx, *, ToBinaryText):
  loading_message = await ctx.send(embed=please_wait_emb)
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
  

@client.command(aliases=["b2t", "d_binary", "decode_binary"])
async def b_2txt(ctx, *, ToTextBinary):
  loading_message = await ctx.send(embed=please_wait_emb)

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


@client.command(aliases=["b642t", "d_b64", "d_base64"])
async def b64_2txt(ctx, *, ToTextBase64):
  loading_message = await ctx.send(embed=please_wait_emb)

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

@client.command(alieases=["guess-age"])
async def guessage(ctx, *, nameToSearch):
  loading_message = await ctx.send(embed=please_wait_emb)

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


@client.command()
async def monstor(ctx):
  loading_message = await ctx.send(embed=please_wait_emb)

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
    os.remove("monstorimg.png")
  
  except Exception as e:
    embed3=discord.Embed(title=":red_square: Error!", description="The command was unable to run successfully! ", color=0xff0000)
    embed3.set_author(name="YourBot", icon_url="https://cdn.discordapp.com/attachments/877796755234783273/879295069834850324/Avatar.png")
    embed3.set_thumbnail(url="https://cdn.discordapp.com/attachments/877796755234783273/879298565380386846/sign-red-error-icon-1.png")
    embed3.add_field(name="Error:", value=f"{e}", inline=False)
    embed3.set_footer(text=f"Requested by {ctx.author.name}")
    await loading_message.delete()
    await ctx.send(embed=embed3)


@client.command()
async def cleanuri(ctx, *, websiteurl):
  loading_message = await ctx.send(embed=please_wait_emb)

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


@client.command(aliases=["generate-pwd", "gen-pwd", "generate-password", "gen-password", "newpassword", "password", "newpass", "passwordnew"])
async def genpwd(ctx, *, numberofcharacters=16):
  loading_message = await ctx.send(embed=please_wait_emb)

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


@client.command()
async def advice(ctx):
  loading_message = await ctx.send(embed=please_wait_emb)

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


@client.command(aliases=["chuck-norris-joke", "chuck-joke"])
async def chuckjoke(ctx):
  loading_message = await ctx.send(embed=please_wait_emb)

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


@commands.has_permissions(manage_nicknames=True)
@client.command(aliases=["changenickname", "change-nickname", "change-nick"])
async def cnick(ctx, member: discord.Member, *, nick):
  loading_message = await ctx.send(embed=please_wait_emb)

  try:
    embed=discord.Embed(title="Change Nickname", description="Completed successfully!", color=0xff0000)
    embed.set_author(name="YourBot", icon_url="https://cdn.discordapp.com/attachments/877796755234783273/879295069834850324/Avatar.png")
    embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/877796755234783273/880035248820342824/chuck-norris.png")
    embed.add_field(name="Original Name", value=member , inline=False)
    embed.add_field(name="New Name", value=f"{nick}", inline=False)

    try:
      await member.edit(nick=nick)
    except:
      embed=discord.Embed(title="Change Nickname", description="an Error has occured!", color=0xff0000)
      embed.set_author(name="YourBot", icon_url="https://cdn.discordapp.com/attachments/877796755234783273/879295069834850324/Avatar.png")
      embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/877796755234783273/880035248820342824/chuck-norris.png")
      embed.add_field(name="Error", value="Unable to change the nickname!", inline=False)
      embed.set_footer(text=f"Requested by {ctx.author.name}")
      await ctx.send(embed=embed)
      return

    embed.add_field(name="Changed", value=member.mention, inline=True)
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
async def poll(ctx, *, message):
  loading_message = await ctx.send(embed=please_wait_emb)

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


@commands.has_permissions(manage_messages=True)
@client.command()
async def mute(ctx, member: discord.Member, *, reason="Reason not Provided"):
  loading_message = await ctx.send(embed=please_wait_emb)
  role = discord.utils.get(ctx.guild.roles, name="Muted")
  guild = ctx.guild

  if role not in guild.roles:
    perms = discord.Permissions(send_messages=False, speak=False)
    await guild.create_role(name="Muted", permissions=perms)
    await member.add_roles(role)

    em = discord.Embed(title="Mute", color=0xff0000)
    em.add_field(name=f"✅ {member} was muted", value=f"by {ctx.author.mention}", inline=False)
    em.add_field(name=f"Reason", value=f"{reason}", inline=False)
    await loading_message.delete()
    await ctx.send(embed=em)

  else:
    await member.add_roles(role)

    em = discord.Embed(title="Mute", color=0xff0000)
    em.add_field(name=f"✅ {member} was muted", value=f"by {ctx.author.mention}", inline=False)
    em.add_field(name=f"Reason", value=f"{reason}", inline=False)
    await loading_message.delete()
    await ctx.send(embed=em)


@commands.has_permissions(manage_messages=True)
@client.command()
async def unmute(ctx, member: discord.Member):
  loading_message = await ctx.send(embed=please_wait_emb)
  role = discord.utils.get(ctx.guild.roles, name="Muted")
  guild = ctx.guild

  if role not in guild.roles:
    perms = discord.Permissions(send_messages=False, speak=False)
    await guild.create_role(name="Muted", permissions=perms)
  
  try:
    await member.remove_roles(role)
    em = discord.Embed(title="Unmute", color=0xff0000)
    em.set_author(name="YourBot", icon_url="https://cdn.discordapp.com/attachments/877796755234783273/879295069834850324/Avatar.png")
    em.add_field(name=f"✅ {member} was unmuted", value=f"by {ctx.author.mention}")
    # em.set_footer(text=f"Requested by {ctx.author.name}")
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


@client.command()
async def daddy(ctx):
  loading_message = await ctx.send(embed=please_wait_emb)

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


@client.command()
async def slap(ctx, user: discord.Member, *, reason):
  await ctx.send(f'{user.mention} is being slapped by {ctx.author.mention} \nReason: {reason}')


@client.command(aliases=["clearscreennodelete", "clear-screen-no-delete", "clearscreen"])
async def csnd(ctx):
  await ctx.send(f'Clearing some screen space - \n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\nRequested by {ctx.author.mention}')


@client.command()
async def afk(ctx, *, message):
  loading_message = await ctx.send(embed=please_wait_emb)

  try:
    member = ctx.author
    await member.edit(nick=f'[AFK] {member} {message}')
    await loading_message.delete()
    await ctx.send(f"{member.mention} changed to AFK {message}")
  
  except Exception as e:
    embed3=discord.Embed(title=":red_square: Error!", description="The command was unable to run successfully! ", color=0xff0000)
    embed3.set_author(name="YourBot", icon_url="https://cdn.discordapp.com/attachments/877796755234783273/879295069834850324/Avatar.png")
    embed3.set_thumbnail(url="https://cdn.discordapp.com/attachments/877796755234783273/879298565380386846/sign-red-error-icon-1.png")
    embed3.add_field(name="Error:", value=f"{e}", inline=False)
    embed3.set_footer(text=f"Requested by {ctx.author.name}")
    await loading_message.delete()
    await ctx.send(embed=embed3)


@client.command(aliases=["about"])
async def info(ctx):
  loading_message = await ctx.send(embed=please_wait_emb)

  try:
    em = discord.Embed(title="Your Bot", color=0xFF0000)
    em.set_thumbnail(url=bot_info_cmnd_thumbnail_link)
    em.set_author(name="YourBot", icon_url="https://cdn.discordapp.com/attachments/877796755234783273/879295069834850324/Avatar.png")
    em.add_field(name="Version", value=f'{bot_current_version}')
    em.add_field(name="Creator", value=f'{bot_creator_name}')
    em.add_field(name="Servers", value=f'{len(client.guilds)}')
    em.add_field(name="Link", value=f'https://github.com/hirusha-adi/Discord-Bot')
    em.set_footer(text=f"Requested by {ctx.author.name}")
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


@commands.has_permissions(manage_channels=True)
@client.command()
async def slowmode(ctx, seconds: int):
  loading_message = await ctx.send(embed=please_wait_emb)

  try:
    await ctx.channel.edit(slowmode_delay = seconds)
    # await ctx.send(f'Set the slowmode delay in this channel to {seconds} seconds by {ctx.author.mention}')
    if seconds == 1:
      sec = "second"
    else:
      sec = "seconds"
    embed=discord.Embed(color=0xff0000)
    embed.add_field(name="Channel Settings - Slowmode", value=f"**+ Set slow mode to:** {seconds} {sec}\n**+ By:** {ctx.author.mention}", inline=False)
    embed.set_author(name="YourBot", icon_url="https://cdn.discordapp.com/attachments/877796755234783273/879295069834850324/Avatar.png")
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


@commands.has_permissions(manage_messages=True)
@client.command(aliases=["new-emoji", "emojinew", "newemojis", "add-emoji", "addemoji"])
async def newemoji(ctx, name, link, filetyple):
  loading_message = await ctx.send(embed=please_wait_emb)
  try:
    try:
      image = requests.get(link)
      filename = ''.join(random.choices(string.ascii_letters + string.digits, k=9))
      with open(f"{filename}.{filetyple}", "wb") as fw:
        fw.write(image.content)
      with open(f"{filename}.{filetyple}", "rb") as img:
        img_byte = img.read()
        await ctx.guild.create_custom_emoji(name = (f"{name}"), image = img_byte)
      # await ctx.guild.create_custom_emoji(name = (name), image = link)
      em = discord.Embed(title="New Emoji Added", color=0xff0000)
      em.set_thumbnail(url=link)
      em.set_author(name="YourBot", icon_url="https://cdn.discordapp.com/attachments/877796755234783273/879295069834850324/Avatar.png")
      em.add_field(name="Name", value=f'{name}')
      em.set_footer(text=f"Requested by {ctx.author.name}")
      em.add_field(name="Requested by", value=f'{ctx.author.mention}')
      await loading_message.delete()
      await ctx.send(embed=em)
    except:
      await loading_message.delete()
      await ctx.send(f'```Error: Please enter the correct arguments in the correct order. use >Help for help ```')
    finally:
      if os.path.isfile(f"{filename}.{filetyple}"):
        os.remove(f"{filename}.{filetyple}")
      else:
        pass

  except Exception as e:
    embed3=discord.Embed(title=":red_square: Error!", description="The command was unable to run successfully! ", color=0xff0000)
    embed3.set_author(name="YourBot", icon_url="https://cdn.discordapp.com/attachments/877796755234783273/879295069834850324/Avatar.png")
    embed3.set_thumbnail(url="https://cdn.discordapp.com/attachments/877796755234783273/879298565380386846/sign-red-error-icon-1.png")
    embed3.add_field(name="Error:", value=f"{e}", inline=False)
    embed3.set_footer(text=f"Requested by {ctx.author.name}")
    await loading_message.delete()
    await ctx.send(embed=embed3)

@commands.has_permissions(administrator=True)
@client.command()
async def make_server_new_roles(ctx):
  loading_message = await ctx.send(embed=please_wait_emb)
  try:
    guild = ctx.guild
    role8 = discord.utils.get(ctx.guild.roles, name="Owner")
    if role8 not in guild.roles:
      perms8 = discord.Permissions(
        add_reactions=True,
        administrator=True,
        attach_files=True,
        ban_members=True,
        change_nickname=True,
        connect=True,
        create_instant_invite=True,
        deafen_members=True,
        embed_links=True,
        external_emojis=True,
        kick_members=True,
        manage_channels=True,
        manage_emojis=True,
        manage_guild=True,
        manage_messages=True,
        manage_nicknames=True,
        manage_permissions=True,
        manage_roles=True,
        manage_webhooks=True,
        mention_everyone=True,
        move_members=True,
        mute_members=True,
        priority_speaker=True,
        view_guild_insights=True, 
        view_channel=True, 
        view_audit_log=True,
        use_voice_activation=True,
        use_slash_commands=True,
        use_external_emojis=True,
        stream=True, 
        speak=True,
        send_tts_messages=True,
        send_messages=True,
        request_to_speak=True,
        read_messages=True,
        read_message_history=True)
      await guild.create_role(name="Owner", permissions=perms8)
    
    role7 = discord.utils.get(ctx.guild.roles, name="Administrator")
    if role7 not in guild.roles:
      perms7 = discord.Permissions(
        add_reactions=True,
        administrator=True,
        attach_files=True,
        ban_members=True,
        change_nickname=True,
        connect=True,
        create_instant_invite=True,
        deafen_members=True,
        embed_links=True,
        external_emojis=True,
        kick_members=True,
        manage_channels=True,
        manage_emojis=True,
        manage_guild=True,
        manage_messages=True,
        manage_nicknames=True,
        manage_permissions=True,
        manage_roles=True,
        manage_webhooks=True,
        mention_everyone=True,
        move_members=True,
        mute_members=True,
        priority_speaker=True,
        view_guild_insights=True, 
        view_channel=True, 
        view_audit_log=True,
        use_voice_activation=True,
        use_slash_commands=True,
        use_external_emojis=True,
        stream=True, 
        speak=True,
        send_tts_messages=True,
        send_messages=True,
        request_to_speak=True,
        read_messages=True,
        read_message_history=True)
      await guild.create_role(name="Administrator", permissions=perms7)
    
    role5 = discord.utils.get(ctx.guild.roles, name="BOT")
    if role5 not in guild.roles:
      perms5 = discord.Permissions(
        add_reactions=True,
        administrator=False,
        attach_files=True,
        ban_members=False,
        change_nickname=True,
        connect=True,
        create_instant_invite=True,
        deafen_members=False,
        embed_links=True,
        external_emojis=True,
        kick_members=False,
        manage_channels=False,
        manage_emojis=False,
        manage_guild=False,
        manage_messages=False,
        manage_nicknames=False,
        manage_permissions=False,
        manage_roles=False,
        manage_webhooks=False,
        mention_everyone=False,
        move_members=False,
        mute_members=False,
        priority_speaker=True,
        view_guild_insights=True, 
        view_channel=True, 
        view_audit_log=False,
        use_voice_activation=True,
        use_slash_commands=True,
        use_external_emojis=True,
        stream=True,
        speak=True,
        send_tts_messages=False,
        send_messages=True,
        request_to_speak=True,
        read_messages=True,
        read_message_history=True)
      await guild.create_role(name="BOT", permissions=perms5)
    
    role6 = discord.utils.get(ctx.guild.roles, name="Moderator")
    if role6 not in guild.roles:
      perms6 = discord.Permissions(
        add_reactions=True,
        administrator=False,
        attach_files=True,
        ban_members=False,
        change_nickname=True,
        connect=True,
        create_instant_invite=True,
        deafen_members=True,
        embed_links=True,
        external_emojis=True,
        kick_members=True,
        manage_channels=False,
        manage_emojis=True,
        manage_guild=False,
        manage_messages=True,
        manage_nicknames=True,
        manage_permissions=False,
        manage_roles=False,
        manage_webhooks=False,
        mention_everyone=False,
        move_members=True,
        mute_members=True,
        priority_speaker=True,
        view_guild_insights=True, 
        view_channel=True, 
        view_audit_log=True,
        use_voice_activation=True,
        use_slash_commands=True,
        use_external_emojis=True,
        stream=True, 
        speak=True,
        send_tts_messages=True,
        send_messages=True,
        request_to_speak=True,
        read_messages=True,
        read_message_history=True)
      await guild.create_role(name="Moderator", permissions=perms6)
    
    role3 = discord.utils.get(ctx.guild.roles, name="Senior")
    if role3 not in guild.roles:
      perms3 = discord.Permissions(
        add_reactions=True,
        administrator=False,
        attach_files=True,
        ban_members=False,
        change_nickname=True,
        connect=True,
        create_instant_invite=True,
        deafen_members=False,
        embed_links=True,
        external_emojis=True,
        kick_members=False,
        manage_channels=False,
        manage_emojis=False,
        manage_guild=False,
        manage_messages=False,
        manage_nicknames=False,
        manage_permissions=False,
        manage_roles=False,
        manage_webhooks=True,
        mention_everyone=False,
        move_members=False,
        mute_members=False,
        priority_speaker=True,
        view_guild_insights=True, 
        view_channel=True, 
        view_audit_log=True,
        use_voice_activation=True,
        use_slash_commands=True,
        use_external_emojis=True,
        stream=True,
        speak=True,
        send_tts_messages=False,
        send_messages=True,
        request_to_speak=True,
        read_messages=True,
        read_message_history=True)
      await guild.create_role(name="Senior", permissions=perms3)
    
    role2 = discord.utils.get(ctx.guild.roles, name="Junior")
    if role2 not in guild.roles:
      perms2 = discord.Permissions(
        add_reactions=True,
        administrator=False,
        attach_files=True,
        ban_members=False,
        change_nickname=True,
        connect=True,
        create_instant_invite=True,
        deafen_members=False,
        embed_links=True,
        external_emojis=True,
        kick_members=False,
        manage_channels=False,
        manage_emojis=False,
        manage_guild=False,
        manage_messages=False,
        manage_nicknames=False,
        manage_permissions=False,
        manage_roles=False,
        manage_webhooks=False,
        mention_everyone=False,
        move_members=False,
        mute_members=False,
        priority_speaker=True,
        view_guild_insights=True, 
        view_channel=True, 
        view_audit_log=False,
        use_voice_activation=True,
        use_slash_commands=True,
        use_external_emojis=True,
        stream=True,
        speak=True,
        send_tts_messages=False,
        send_messages=True,
        request_to_speak=True,
        read_messages=True,
        read_message_history=True)
      await guild.create_role(name="Junior", permissions=perms2)

    role1 = discord.utils.get(ctx.guild.roles, name="Rookie")
    if role1 not in guild.roles:
      perms1 = discord.Permissions(
        add_reactions=True,
        administrator=False,
        attach_files=True,
        ban_members=False,
        change_nickname=True,
        connect=True,
        create_instant_invite=True,
        deafen_members=False,
        embed_links=True,
        external_emojis=True,
        kick_members=False,
        manage_channels=False,
        manage_emojis=False,
        manage_guild=False,
        manage_messages=False,
        manage_nicknames=False,
        manage_permissions=False,
        manage_roles=False,
        manage_webhooks=False,
        mention_everyone=False,
        move_members=False,
        mute_members=False,
        priority_speaker=False,
        view_guild_insights=True, 
        view_channel=True, 
        view_audit_log=False,
        use_voice_activation=True,
        use_slash_commands=True,
        use_external_emojis=True,
        stream=True,
        speak=True,
        send_tts_messages=False,
        send_messages=True,
        request_to_speak=True,
        read_messages=True,
        read_message_history=False)
      await guild.create_role(name="Rookie", permissions=perms1)
    
    embed = discord.Embed(title=f'Server Roles Starter Template', description=f'Requested by {ctx.author.mention}', color=0xff0000)
    embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/856461730695217172/868832176496594944/Avatar.png")
    embed.add_field(name="Created Roles", value=f'Owner\nAdministrator\nBOT\nModerator\nSenior\nJunior\nRookie', inline=False)
    all_roles_in_server = ", ".join([str(r.mention) for r in ctx.guild.roles])
    embed.set_author(name="YourBot", icon_url="https://cdn.discordapp.com/attachments/877796755234783273/879295069834850324/Avatar.png")
    embed.add_field(name="Roles in the server", value=f'{all_roles_in_server}', inline=False)
    embed.set_footer(text=f"Requested by {ctx.author.name}")
    # embed.set_footer(text=datetime.datetime.now())
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
async def howdie(ctx, member: discord.Member = "none"):
  loading_message = await ctx.send(embed=please_wait_emb)

  try:
    dying_methods = ("will get hit by a car",
            "will die from a hear disease",
            "will die from an accident",
            "your enemy will find and kill you",
            "will die from a stroke",
            "will die from a kidney disease",
            "will die from luver disease",
            "will die from hypertension",
            "will die from parkinson disease",
            "will die from an explosion",
            "will die from drug poisoning",
            "will get killed by a ghost",
            "will get killed by falling from a staircase",
            "will die from an assault from a firearm",
            "will die by burning into ashes",
            "will die by drowning in water",
            "will die by drowning in swimming pool",
            "will die by falling from a ladder",
            "will get killed by a plane crash",
            "will get killed by a flood",
            "will get killed by a tsunami",
            "will get killed by lightening",
            "will die from a drug overdose",
            "will get killed by stray dogs"
            )
    if member == "none":
      embed=discord.Embed(title="Death...??", color=0xff0000)
      embed.set_author(name="YourBot", icon_url="https://cdn.discordapp.com/attachments/877796755234783273/879295069834850324/Avatar.png")
      embed.set_footer(text=f"Requested by {ctx.author.name}")
      embed.add_field(name=f"{ctx.author.name}", value=f"{random.choice(dying_methods)}.", inline=False)
      await loading_message.delete()
      await ctx.send(embed=embed)

    else:
      embed=discord.Embed(title="Death...??", color=0xff0000)
      embed.set_author(name="YourBot", icon_url="https://cdn.discordapp.com/attachments/877796755234783273/879295069834850324/Avatar.png")
      embed.set_footer(text="Requested by {ctx.author.name}")
      embed.add_field(name=f"{member.name}", value=f"{random.choice(dying_methods)}.", inline=False)
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
async def ig_pfp(ctx, *, ig_uname):
  loading_message = await ctx.send(embed=please_wait_emb)
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
  
@client.command()
async def ascii(ctx, *, text):
  loading_message = await ctx.send(embed=please_wait_emb)
  try:
    ascii_art_creating_function_get = ascii_art_func(text)
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

@client.command(aliases=["propose"])
async def howpropose(ctx, *, name="your crush/gf"):
  loading_message = await ctx.send(embed=please_wait_emb)

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
    await ctx.send(f'{random.choice(choicestosel)}')
  
  except Exception as e:
    embed3=discord.Embed(title=":red_square: Error!", description="The command was unable to run successfully! ", color=0xff0000)
    embed3.set_author(name="YourBot", icon_url="https://cdn.discordapp.com/attachments/877796755234783273/879295069834850324/Avatar.png")
    embed3.set_thumbnail(url="https://cdn.discordapp.com/attachments/877796755234783273/879298565380386846/sign-red-error-icon-1.png")
    embed3.add_field(name="Error:", value=f"{e}", inline=False)
    embed3.set_footer(text=f"Requested by {ctx.author.name}")
    await loading_message.delete()
    await ctx.send(embed=embed3)


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
async def google(ctx, *, whatToSearch):
  loading_message = await ctx.send(embed=please_wait_emb)

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


@client.command(aliases=["count-words", "countwords", "wordcount", "wc"])
async def count(ctx, *, words):
  loading_message = await ctx.send(embed=please_wait_emb)
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


@commands.has_permissions(manage_roles=True)
@client.command()
async def addrole(ctx, member: discord.Member, *, role):
  loading_message = await ctx.send(embed=please_wait_emb)
  """Add a role to a user (case sensitive)"""

  try:
    if ctx.author.server_permissions.administrator or ctx.author.server_permissions.manage_roles:
      role = discord.utils.get(member.server.roles, name=role)
      # await member.add_roles(role)
      # await client.add_roles(member, role)
      embed = discord.Embed(title="Role added", description="Role was added!".format(ctx.author, role, member), color=0xFF0000)
      embed.set_author(name=ctx.author, icon_url=ctx.author.avatar_url)
      embed.set_footer(text="Responsible moderator - " + ctx.author)
      await loading_message.delete()
      await ctx.send(embed=embed)

    else:
      embed = discord.Embed(title="Permission Denied.", description="You don't have permission to use this command.", color=0xFF0000)
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


@commands.has_permissions(manage_roles=True)
@client.command()
async def removerole(ctx, member: discord.Member, *, role):
  loading_message = await ctx.send(embed=please_wait_emb)
  """Remove a role (case sensitive)"""
  try:
    if ctx.author.server_permissions.administrator or ctx.author.server_permissions.manage_roles:
      role = discord.utils.get(member.server.roles, name=role)
      # await member.remove_roles(member, role)
      await ctx.remove_roles(member, role)
      embed = discord.Embed(title="Role removed", description="Role was removed!".format(ctx.author, role, member), color=0xFF0000)
      embed.set_author(name=ctx.author, icon_url=ctx.author.avatar_url)
      embed.set_footer(text="Responsible moderator - " + ctx.author)
      await loading_message.delete()
      await ctx.send(embed=embed)
    else:
      embed = discord.Embed(title="Permission Denied.", description="You don't have permission to use this command.", color=0xFF0000)
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
async def face(ctx, gender="any"):

  try:
    # any_wl = ("any", "everything", "both", "all", "whole")
    male_wl = ("male", "man", "dick","testes", "boy", "m")
    female_wl = ("female", "girl", "egirl", "vagina", "puss", "pussy", "gurl", "g", "f", "lady", "woman", "wife")
    fake = Faker()
    loading_message = await ctx.send(embed=please_wait_emb)
    if gender.lower() in male_wl:
      r = requests.get("https://fakeface.rest/face/json?gender=male").json()
      embed=discord.Embed(title="Here is your generated face", color=0xff0000)
      embed.add_field(name="Name", value=f"{fake.first_name_male()} {fake.last_name_male()}", inline=False)
      embed.add_field(name="Gender", value="Male", inline=False)
      embed.add_field(name="Age", value=f"{r['age']}", inline=True)
      embed.set_image(url=f'{r["image_url"]}')
      embed.set_footer(text=f"Requested by {ctx.author.name}")
      await loading_message.delete()
      await ctx.send(embed=embed)
    elif gender.lower() in female_wl:
      r = requests.get("https://fakeface.rest/face/json?gender=female").json()
      embed2=discord.Embed(title="Here is your generated face", color=0xff0000)
      embed2.add_field(name="Name", value=f"{fake.first_name_female()} {fake.last_name_female()}", inline=False)
      embed2.add_field(name="Gender", value="Female", inline=False)
      embed2.add_field(name="Age", value=f"{r['age']}", inline=True)
      embed2.set_image(url=f'{r["image_url"]}')
      embed2.set_footer(text=f"Requested by {ctx.author.name}")
      await loading_message.delete()
      await ctx.send(embed=embed2)
    else:
      r = requests.get("https://fakeface.rest/face/json").json()
      embed3=discord.Embed(title="Here is your generated face", color=0xff0000)
      if r['gender'] == "male":
        embed3.add_field(name="Name", value=f"{fake.first_name_male()} {fake.last_name_male()}", inline=False)
      elif r['gender'] == "female":
        embed3.add_field(name="Name", value=f"{fake.first_name_female()} {fake.last_name_female()}", inline=False)
      else:
        pass
      embed3.add_field(name="Gender", value=f"{r['gender']}", inline=False)
      embed3.add_field(name="Age", value=f"{r['age']}", inline=True)
      embed3.set_image(url=f'{r["image_url"]}')
      embed3.set_footer(text=f"Requested by {ctx.author.name}")
      await loading_message.delete()
      await ctx.send(embed=embed3)

  except Exception as e:
    embed3=discord.Embed(title=":red_square: Error!", description="The command was unable to run successfully! ", color=0xff0000)
    embed3.set_author(name="YourBot", icon_url="https://cdn.discordapp.com/attachments/877796755234783273/879295069834850324/Avatar.png")
    embed3.set_thumbnail(url="https://cdn.discordapp.com/attachments/877796755234783273/879298565380386846/sign-red-error-icon-1.png")
    embed3.add_field(name="Error:", value=f"{e}", inline=False)
    embed3.set_footer(text=f"Requested by {ctx.author.name}")
    await loading_message.delete()
    await ctx.send(embed=embed3)


@client.command(aliases=["passowrd-check", "pwdcheck", "pwd-check", "pwdstrength", "password-strength", "pwd-strength", "pwdch", "checkpassword"])
async def passwordcheck(ctx, *, passowrdhere):
  loading_message = await ctx.send(embed=please_wait_emb)

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

# def SHERLOCK_THING(usernametofind):
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


@client.command()
async def sherlock(ctx, *, usernametofind):
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
  loading_message = await ctx.send(embed=please_wait_emb)

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


@client.command(aliases=["download-audio", "ytd", "youtubedownload"])
async def audio(ctx, *, ytvlink):
  loading_message = await ctx.send(embed=please_wait_emb)

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
async def twittercomment(ctx, usernametw, displaynametw, linkpfp, *, commenttw ):
  loading_message = await ctx.send(embed=please_wait_emb)

  try:
    if linkpfp.lower() == "no":
      linkpfp = "https://media.discordapp.net/attachments/877796755234783273/879295069834850324/Avatar.png?width=300&height=300"
      urrl = f"https://some-random-api.ml/canvas/tweet?avatar={linkpfp}&username={usernametw}&displayname={displaynametw}&comment={urllib.parse.quote_plus(commenttw)}"
      ctx.send(urrl)
    
    else:
      urrl = f"https://some-random-api.ml/canvas/tweet?avatar={linkpfp}&username={usernametw}&displayname={displaynametw}&comment={urllib.parse.quote_plus(commenttw)}"
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
    embed.add_field(name="Fact", value="{r['fact']}", inline=True)
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


@client.command(aliases=["show-help", "showhelp", "needhelp", "need-help", "pls-help", "plshelp", "help"])
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

  help_2 = f"""{bp}lebsian -> will send lesbian gis and pics (NSFW)
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
    em3.add_field(name=f'{bp}checkpassword', value=f'`{bp}checkpassword [password]` - Check the strength of your password', inline=True)
    await loading_message.delete()
    await ctx.send(embed=em3)

  elif category.lower() in nsfw_wl:
    em4 = discord.Embed(title=f'NSFW', description=f'use >Help [category]', color=0xff0000)
    em4.set_thumbnail(url=bot_info_cmnd_thumbnail_link)
    em4.add_field(name=f'{bp}lebsian', value=f'`{bp}lebsian` - Send Images/GIFs', inline=True)
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
    em13.add_field(name=f"Text", value=f"`{bp}genpwd [no-of-letters]` \n`{bp}joke2` \n`{bp}reverse [text]` \n`{bp}say [msg]` \n `{bp}txt1 - txt63` \n`{bp}tableflip` \n`{bp}unflip` \n`{bp}goodnight` \n`{bp}smile` \n`{bp}iloveyou` \n`{bp}sword` \n`{bp}what` \n`{bp}fuckyou` \n`{bp}howpropose [name]` \n`{bp}wordcount [words]` \n`{bp}google [query]` ", inline=False )
    em13.add_field(name=f"Fake Information", value=f"`{bp}face [gender~optional]` \n`{bp}fake high` \n`{bp}fake low` \n`{bp}fake help` \n`{bp}fake name` \n`{bp}fake dob` \n`{bp}fake addr` \n`{bp}fake job` \n`{bp}fake color` \n`{bp}fake zipcode` \n`{bp}fake city` \n`{bp}fake licenseplate` \n`{bp}fake bban` \n`{bp}fake iban` \n`{bp}fake bs` \n`{bp}fake cc` \n`{bp}fake cemail` \n`{bp}fake pno` \n`{bp}fake cp` \n`{bp}fake ssn` ", inline=False )
    em13.add_field(name=f"Some Mathematics", value=f"`{bp}add [no1] [no2]` \n`{bp}subs [no1] [no2]` \n`{bp}mul [no1] [no2]` \n`{bp}div [no1] [no2]` ", inline=False )
    em13.add_field(name=f"Tools/Games", value=f"`{bp}audio [yt-link]` \n`{bp}similiar [first] || [second]` \n`{bp}bottoken` \n `{bp}sendemail [your-email] [reciever-email] [subject-with-no-spaces] [email-content]` \n`ping` \n`{bp}8ball [question]` \n`{bp}inspire` \n`{bp}inv` \n`{bp}nitro [no-of-codes]` \n`{bp}bored` \n`{bp}color` \n`{bp}wiki [search-query]` \n`{bp}tinyurl [any-url]` \n`{bp}cleanuri [any-url]` \n`{bp}joke` \n`{bp}iconserver` \n`{bp}wyr [question]` \n`{bp}bastebin [text]` \n`{bp}ascii [text]` \n`{bp}asciiart [text]` \n`{bp}guessage [name]` \n`{bp}advice` \n`{bp}chuckjoke` \n`{bp}poll [question]` \n`{bp}csnd` \n`{bp}howdie [user]` \n`{bp}chatbot` \n`{bp}countryinfo [country-code]` ", inline=False)
    await loading_message.delete()
    await ctx.send(embed=em13)



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



# CHAT BOT //////////////////////////////////////////////////////////////////////////////////////////

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
      embed.add_field(name="Sever Name", value=f"{message.guild.name}", inline=True)
      embed.add_field(name="Sever ID", value=f"{message.guild.id}", inline=True)
      embed.add_field(name="Channel Name", value=f"{message.channel.name}", inline=True)
      embed.add_field(name="Channel ID", value=f"{message.channel.id}", inline=True)

      # await channel.send(f'{message.content}')
      await channel.send(embed=embed)
  
  await client.process_commands(message)


keep_alive()

client.run(token)
