from discord import permissions
from keep_alive import keep_alive

import os

try:
  os.system("pip3 install prsaw")
  print("TEST")
except Exception as e:
  print("error: ", e)

from prsaw import RandomStuffV2

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
import platform

botconfigdata = json.load(open("config.json", "r"))
bot_prefix = botconfigdata["msg-prefix"]
bot_info_cmnd_thumbnail_link = botconfigdata["info-command-thumbnail-link"]
bot_creator_name = botconfigdata["bot-creator-name"]
bot_current_version = botconfigdata["bot-version"]
bot_owner_id_zeacer = botconfigdata["ownerid"]

client = commands.Bot(command_prefix = bot_prefix)

client.remove_command('help')

token = os.environ['TOKEN']

# loading_message = await ctx.send(embed=please_wait_emb)
# await loading_message.delete()

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

@client.event
async def on_ready():
    print('Bot is ready!')
    print(f'Logged in as {client.user.name}')
    print(f'Discord.py API version: {discord.__version__}')
    print(f'Python version: {platform.python_version()}')
    await client.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name=f"{len(client.guilds)} servers!"))

please_wait_emb = discord.Embed(title="```  Processing your request  ```", color=0xff0000)
please_wait_emb.set_author(name="YourBot")
please_wait_emb.set_thumbnail(url="https://c.tenor.com/I6kN-6X7nhAAAAAj/loading-buffering.gif")
please_wait_emb.set_footer(text="Bot created by ZeaCeR#5641")
please_wait_wt_bfd = 2

@client.command()
async def changeprefix(ctx):
  loading_message = await ctx.send(embed=please_wait_emb)
  await loading_message.delete()
  await ctx.send(f'This feature will be available in the future! Make sure to type the info command to see more information')

# ctx is for 'context'
@client.command() 
async def ping(ctx):
    loading_message = await ctx.send(embed=please_wait_emb)
    try:
        await loading_message.delete()
        await ctx.send(f'```[+] Ping: {round(client.latency * 1000)}ms```')
    except Exception as e:
        await loading_message.delete()
        await ctx.send("```" + e + "```")

@client.command()
async def clear(ctx, amount=5):
    await ctx.channel.purge(limit=amount)

@client.command(aliases=["8ball", "eightball"])
async def _8ball(ctx, *, question):
    loading_message = await ctx.send(embed=please_wait_emb)
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
    # await ctx.send(f'```Question: {question}\nAnswer: {random.choice(responses)}```')
    answer = random.choice(responses)
    embed = discord.Embed()
    embed.add_field(name="Question", value=question, inline=False)
    embed.add_field(name="Answer", value=answer, inline=False)
    embed.set_thumbnail(url="https://www.horoscope.com/images-US/games/game-magic-8-ball-no-text.png")
    embed.set_footer(text=datetime.datetime.now())
    await loading_message.delete()
    await ctx.send(embed=embed)


@commands.has_permissions(kick_members=True)
@client.command()
async def kick(ctx, member : discord.Member, *, reason=None): # call the member as in member object from discord module
    loading_message = await ctx.send(embed=please_wait_emb)
    try:
        await member.kick(reason=reason)
        ban = discord.Embed(title=f":boom: Kicked {member.name}!", description=f"Reason: {reason}\nBy: {ctx.author.mention}")
        await ctx.channel.send(embed=ban)
        await loading_message.delete()
        await member.send(embed=ban)
    except Exception as e:
        await loading_message.delete()
        await ctx.send("```" + str(e) + "```")

@commands.has_permissions(ban_members=True)
@client.command()
async def ban(ctx, user: discord.Member, *, reason="No reason provided"):
    loading_message = await ctx.send(embed=please_wait_emb)
    try:
        await user.ban(reason=reason)
        ban = discord.Embed(title=f":boom: Banned {user.name}!", description=f"Reason: {reason}\nBy: {ctx.author.mention}")
        await ctx.channel.send(embed=ban)
        await loading_message.delete()
        await user.send(embed=ban)
    except Exception as e:
        await loading_message.delete()
        await ctx.send("```" + str(e) + "```")

@client.command()
async def unban(ctx, *, member):
    loading_message = await ctx.send(embed=please_wait_emb)
    banned_users = await ctx.guild.bans() # a named tuple containing user object and the reason for ban
    member_name, member_discriminator = member.split("#")

    for ban_entry in banned_users:
        user = ban_entry.user

        if (user.name, user.discriminator) == (member_name, member_discriminator):
            await ctx.guild.unban(user)
            await loading_message.delete()
            await ctx.send(f'```Unbanned {user.mention}```')
            return

@client.command()
async def join(ctx):
    channel = ctx.author.voice.channel
    await channel.connect()
    
@client.command()
async def leave(ctx):
    await ctx.voice_client.disconnect()

@client.command()
async def inv(ctx):
    await ctx.send("```Hey there! Make sure you have me in your server too! Bot Invite link:```" + give_server_invite_link())

@client.command()
async def inspire(ctx):
  loading_message = await ctx.send(embed=please_wait_emb)
  embed = discord.Embed(title="Inspiration", color=0xff0000)
  embed.add_field(name=" ", value=f"{get_quote()}", inline=True)
  await loading_message.delete()
  await ctx.send(embed=embed)

@client.command()
async def fake(ctx, *, fake_mode="help"):
    # await ctx.send("```" + FAKE_PROFILE(fake_mode) + "```")

    # this is the loading message and this will be deleted when the originallly requested message has been ready to send
    loading_message = await ctx.send(embed=please_wait_emb)

    
    if fake_mode == "high":
      fake = Faker()
      simple_dict = fake.profile()
      # fake_info_simple = "Name: " + str(simple_dict['name']) + "\nJob: " + str(simple_dict['job']) + "\nBirthdate: " + str(simple_dict['birthdate']) + "\nCompany: " + str(simple_dict['company']) + "\SSN: " + str(simple_dict['ssn']) + "\nRecidence: " + simple_dict['residence'] + "\nCurrent Location:" + str(simple_dict['current_location']) + "\nBlood Group: " + str(simple_dict['blood_group']) + "\nUsername: " + str(simple_dict['username']) + "\nAddress: " + str(simple_dict['address']) + "\nMail: " + str(simple_dict['mail'])
      
      emf = discord.Embed(title="Fake Information Generator", color=0xF00000)
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
      # await ctx.channel.purge(limit=please_wait_wt_bfd) # DOESNT WORK
    
      await loading_message.delete()
      await ctx.send(embed=emf)
    
    elif fake_mode == "name":
      faker = Faker()
      try:
        USname = faker.name()
        emf2 = discord.Embed(title="Fake Information Generator", color=0xF00000)
        emf2.set_thumbnail(url="https://www.nicepng.com/png/detail/214-2146883_4-fake-stamp-vector-fake-news-logo-png.png")
        # emf2.set_thumbnail(url="https://www.apsf.org/wp-content/uploads/newsletters/2020/3502/coronavirus-covid-19.png")
        emf2.add_field(name="Name", value=f"{str(USname)}")
        await loading_message.delete()
        await ctx.send(embed=emf2)
      except Exception as e:
        await loading_message.delete()
        await ctx.send(f"Error: {e}")
    
    elif fake_mode == "dob":
      faker = Faker()
      try:
        USdob = faker.date_of_birth()
        emf2 = discord.Embed(title="Fake Information Generator", color=0xF00000)
        emf2.set_thumbnail(url="https://www.nicepng.com/png/detail/214-2146883_4-fake-stamp-vector-fake-news-logo-png.png")
        # emf2.set_thumbnail(url="https://www.apsf.org/wp-content/uploads/newsletters/2020/3502/coronavirus-covid-19.png")
        emf2.add_field(name="Date Of Birth", value=f"{str(USdob)}")
        await loading_message.delete()
        await ctx.send(embed=emf2)
      except Exception as e:
        await loading_message.delete()
        await ctx.send(f"Error: {e}")
    
    elif fake_mode == "addr":
      faker = Faker()
      try:
        USaddress = faker.address()
        emf2 = discord.Embed(title="Fake Information Generator", color=0xF00000)
        emf2.set_thumbnail(url="https://www.nicepng.com/png/detail/214-2146883_4-fake-stamp-vector-fake-news-logo-png.png")
        # emf2.set_thumbnail(url="https://www.apsf.org/wp-content/uploads/newsletters/2020/3502/coronavirus-covid-19.png")
        emf2.add_field(name="Address", value=f"{str(USaddress)}")
        await loading_message.delete()
        await ctx.send(embed=emf2)
      except Exception as e:
        await loading_message.delete()
        await ctx.send(f"Error: {e}")
    
    elif fake_mode == "job":
      faker = Faker()
      try:
        USjob = faker.job()
        emf2 = discord.Embed(title="Fake Information Generator", color=0xF00000)
        emf2.set_thumbnail(url="https://www.nicepng.com/png/detail/214-2146883_4-fake-stamp-vector-fake-news-logo-png.png")
        # emf2.set_thumbnail(url="https://www.apsf.org/wp-content/uploads/newsletters/2020/3502/coronavirus-covid-19.png")
        emf2.add_field(name="Job", value=f"{str(USjob)}")
        await loading_message.delete()
        await ctx.send(embed=emf2)
      except Exception as e:
        await loading_message.delete()
        await ctx.send(f"Error: {e}")
    
    elif fake_mode == "color":
      faker = Faker()
      try:
        USfavColor = faker.color_name()
        emf2 = discord.Embed(title="Fake Information Generator", color=0xF00000)
        emf2.set_thumbnail(url="https://www.nicepng.com/png/detail/214-2146883_4-fake-stamp-vector-fake-news-logo-png.png")
        # emf2.set_thumbnail(url="https://www.apsf.org/wp-content/uploads/newsletters/2020/3502/coronavirus-covid-19.png")
        emf2.add_field(name="Color", value=f"{str(USfavColor)}")
        await loading_message.delete()
        await ctx.send(embed=emf2)
      except Exception as e:
        await loading_message.delete()
        await ctx.send(f"Error: {e}")
    
    elif fake_mode == "zipcode":
      faker = Faker()
      try:
        USzip = faker.zipcode()
        emf2 = discord.Embed(title="Fake Information Generator", color=0xF00000)
        emf2.set_thumbnail(url="https://www.nicepng.com/png/detail/214-2146883_4-fake-stamp-vector-fake-news-logo-png.png")
        # emf2.set_thumbnail(url="https://www.apsf.org/wp-content/uploads/newsletters/2020/3502/coronavirus-covid-19.png")
        emf2.add_field(name="Zip Code", value=f"{str(USzip)}")
        await loading_message.delete()
        await ctx.send(embed=emf2)
      except Exception as e:
        await loading_message.delete()
        await ctx.send(f"Error: {e}")
    
    elif fake_mode == "city":
      faker = Faker()
      try:
        UScity = faker.city()
        emf2 = discord.Embed(title="Fake Information Generator", color=0xF00000)
        emf2.set_thumbnail(url="https://www.nicepng.com/png/detail/214-2146883_4-fake-stamp-vector-fake-news-logo-png.png")
        # emf2.set_thumbnail(url="https://www.apsf.org/wp-content/uploads/newsletters/2020/3502/coronavirus-covid-19.png")
        emf2.add_field(name="City", value=f"{str(UScity)}")
        await loading_message.delete()
        await ctx.send(embed=emf2)
      except Exception as e:
        await loading_message.delete()
        await ctx.send(f"Error: {e}")
    
    elif fake_mode == "licenseplate":
      faker = Faker()
      try:
        USnumberPlate = faker.license_plate()
        emf2 = discord.Embed(title="Fake Information Generator", color=0xF00000)
        emf2.set_thumbnail(url="https://www.nicepng.com/png/detail/214-2146883_4-fake-stamp-vector-fake-news-logo-png.png")
        # emf2.set_thumbnail(url="https://www.apsf.org/wp-content/uploads/newsletters/2020/3502/coronavirus-covid-19.png")
        emf2.add_field(name="License Plate", value=f"{str(USnumberPlate)}")
        await loading_message.delete()
        await ctx.send(embed=emf2)
      except Exception as e:
        await loading_message.delete()
        await ctx.send(f"Error: {e}")
    
    elif fake_mode == "bban":
      faker = Faker()
      try:
        USbasicBankAccountNumber = faker.bban()
        emf2 = discord.Embed(title="Fake Information Generator", color=0xF00000)
        emf2.set_thumbnail(url="https://www.nicepng.com/png/detail/214-2146883_4-fake-stamp-vector-fake-news-logo-png.png")
        # emf2.set_thumbnail(url="https://www.apsf.org/wp-content/uploads/newsletters/2020/3502/coronavirus-covid-19.png")
        emf2.add_field(name="Basic Bank Account", value=f"{str(USbasicBankAccountNumber)}")
        await loading_message.delete()
        await ctx.send(embed=emf2)
      except Exception as e:
        await loading_message.delete()
        await ctx.send(f"Error: {e}")
    
    elif fake_mode == "iban":
      faker = Faker()
      try:
        USinternationalBankAccountNumber = faker.iban()
        emf2 = discord.Embed(title="Fake Information Generator", color=0xF00000)
        emf2.set_thumbnail(url="https://www.nicepng.com/png/detail/214-2146883_4-fake-stamp-vector-fake-news-logo-png.png")
        # emf2.set_thumbnail(url="https://www.apsf.org/wp-content/uploads/newsletters/2020/3502/coronavirus-covid-19.png")
        emf2.add_field(name="International Bank Account", value=f"{str(USinternationalBankAccountNumber)}")
        await loading_message.delete()
        await ctx.send(embed=emf2)
      except Exception as e:
        await loading_message.delete()
        await ctx.send(f"Error: {e}")
    
    elif fake_mode == "bs":
      faker = Faker()
      try:
        USbs = faker.bs()
        emf2 = discord.Embed(title="Fake Information Generator", color=0xF00000)
        emf2.set_thumbnail(url="https://www.nicepng.com/png/detail/214-2146883_4-fake-stamp-vector-fake-news-logo-png.png")
        # emf2.set_thumbnail(url="https://www.apsf.org/wp-content/uploads/newsletters/2020/3502/coronavirus-covid-19.png")
        emf2.add_field(name="BS", value=f"{str(USbs)}")
        await loading_message.delete()
        await ctx.send(embed=emf2)
      except Exception as e:
        await loading_message.delete()
        await ctx.send(f"Error: {e}")
    
    elif fake_mode == "cc":
      faker = Faker()
      try:
        UScreditcard = faker.credit_card_full()
        emf2 = discord.Embed(title="Fake Information Generator", color=0xF00000)
        emf2.set_thumbnail(url="https://www.nicepng.com/png/detail/214-2146883_4-fake-stamp-vector-fake-news-logo-png.png")
        # emf2.set_thumbnail(url="https://www.apsf.org/wp-content/uploads/newsletters/2020/3502/coronavirus-covid-19.png")
        emf2.add_field(name="Credit Card", value=f"{str(UScreditcard)}")
        await loading_message.delete()
        await ctx.send(embed=emf2)
      except Exception as e:
        await loading_message.delete()
        await ctx.send(f"Error: {e}")
    
    elif fake_mode == "cemail":
      faker = Faker()
      try:
        UScompanyemail = faker.company_email()
        emf2 = discord.Embed(title="Fake Information Generator", color=0xF00000)
        emf2.set_thumbnail(url="https://www.nicepng.com/png/detail/214-2146883_4-fake-stamp-vector-fake-news-logo-png.png")
        # emf2.set_thumbnail(url="https://www.apsf.org/wp-content/uploads/newsletters/2020/3502/coronavirus-covid-19.png")
        emf2.add_field(name="Email", value=f"{str(UScompanyemail)}")
        await loading_message.delete()
        await ctx.send(embed=emf2)
      except Exception as e:
        await loading_message.delete()
        await ctx.send(f"Error: {e}")
    
    elif fake_mode == "pno":
      faker = Faker()
      try:
        USphoneNumber = faker.phone_number()
        emf2 = discord.Embed(title="Fake Information Generator", color=0xF00000)
        emf2.set_thumbnail(url="https://www.nicepng.com/png/detail/214-2146883_4-fake-stamp-vector-fake-news-logo-png.png")
        # emf2.set_thumbnail(url="https://www.apsf.org/wp-content/uploads/newsletters/2020/3502/coronavirus-covid-19.png")
        emf2.add_field(name="Phone Number", value=f"{str(USphoneNumber)}")
        await loading_message.delete()
        await ctx.send(embed=emf2)
      except Exception as e:
        await loading_message.delete()
        await ctx.send(f"Error: {e}")
    
    elif fake_mode == "cp":
      faker = Faker()
      try:
        UScatchPhrase = faker.catch_phrase()
        emf2 = discord.Embed(title="Fake Information Generator", color=0xF00000)
        emf2.set_thumbnail(url="https://www.nicepng.com/png/detail/214-2146883_4-fake-stamp-vector-fake-news-logo-png.png")
        # emf2.set_thumbnail(url="https://www.apsf.org/wp-content/uploads/newsletters/2020/3502/coronavirus-covid-19.png")
        emf2.add_field(name="Catch Phrase", value=f"{str(UScatchPhrase)}")
        await loading_message.delete()
        await ctx.send(embed=emf2)
      except Exception as e:
        await loading_message.delete()
        await ctx.send(f"Error: {e}")
    
    elif fake_mode == "ssn":
      faker = Faker()
      try:
        USssa = faker.ssn()
        emf2 = discord.Embed(title="Fake Information Generator", color=0xF00000)
        emf2.set_thumbnail(url="https://www.nicepng.com/png/detail/214-2146883_4-fake-stamp-vector-fake-news-logo-png.png")
        # emf2.set_thumbnail(url="https://www.apsf.org/wp-content/uploads/newsletters/2020/3502/coronavirus-covid-19.png")
        emf2.add_field(name="SSN", value=f"{str(USssa)}")
        await loading_message.delete()
        await ctx.send(embed=emf2)
      except Exception as e:
        await loading_message.delete()
        await ctx.send(f"Error: {e}")
    
    elif fake_mode == "low":
      fake_low = Faker()
      try:
        shitthing_simple = fake_low.simple_profile()
        # fake_info_low_info = "Name: " + str(shitthing_simple['name']) + "\nSex: " + str(shitthing_simple['sex']) + "\nAddress: " + str(shitthing_simple['address']) + "\nMail: " + str(shitthing_simple['mail']) + "\nBirthday: " + str(shitthing_simple['birthdate'])
        emf2 = discord.Embed(title="Fake Information Generator", color=0xF00000)
        emf2.set_thumbnail(url="https://www.nicepng.com/png/detail/214-2146883_4-fake-stamp-vector-fake-news-logo-png.png")
        # emf2.set_thumbnail(url="https://www.apsf.org/wp-content/uploads/newsletters/2020/3502/coronavirus-covid-19.png")
        emf2.add_field(name="Name", value=f"{str(shitthing_simple['name'])}")
        emf2.add_field(name="Sex", value=f"{str(shitthing_simple['sex'])}")
        emf2.add_field(name="Address", value=f"{str(shitthing_simple['address'])}")
        emf2.add_field(name="Mail", value=f"{str(shitthing_simple['mail'])}")
        emf2.add_field(name="Birthday", value=f"{str(shitthing_simple['birthdate'])}")
        await loading_message.delete()
        await ctx.send(embed=emf2)
      except Exception as e:
        await loading_message.delete()
        await ctx.send(f"Error: {e}")
    
    elif fake_mode == "help":
      bp = bot_prefix
      emf2 = discord.Embed(title="Fake Information Generator", color=0xF00000)
      emf2.set_thumbnail(url="https://www.nicepng.com/png/detail/214-2146883_4-fake-stamp-vector-fake-news-logo-png.png")
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



@client.command()
async def ip(ctx, *, ip_from_user):
    loading_message = await ctx.send(embed=please_wait_emb)

    # old shit
    # ip_information_data_text = ipinfoshit(ip_from_user)
    # await loading_message.delete()
    # await ctx.send("```" + ip_information_data_text + "```")

    # new shit
    r = requests.get(f"https://ipapi.co/{ip_from_user}/json").json()
    rc = requests.get(f"https://api.worldbank.org/v2/country/{r['country_code']}?format=json").json()

    embed=discord.Embed(title="IP Information", color=0xff0000)
    embed.set_thumbnail(url="https://user-images.githubusercontent.com/36286877/127773181-c98b63be-b18b-4d8b-a8b6-9426bd031b7c.png")
    embed.add_field(name="IP Info", value="IP Address: " + str(r["ip"]) + "\nCity: " + str(r["city"]) + "\nRegion: " + str(r["region"]) + "\nCountry Name: " + str(r["country_name"]) + "\nLatitude: " + str(r["latitude"]) + "\nLongitude: " + str(r["longitude"]) + "\nTime Zone: " + str(r["timezone"]) + "\nUTC Offset: " + str(r["utc_offset"]) + "\nPostal Code: " + str(r["postal"]) + str("\nISP: " + r["org"]) + "\nASN: " + str(r["asn"]) + "\nCountry Code: " + str(r["country_code"]) + "\nCountry TLD: " + str(r["country_tld"]) + "\nPopulation: " + str(r["country_population"]) + "\nCurrency: " + str(r["currency"]) + "\n Curreny Name: " + str(r["currency_name"]) + "\nCountry Area: " + str(r["country_area"]) + "\nLanguages: " + str(r["languages"]) + "\nCalling Code: " + str(r["country_calling_code"]) + "\nGOOGLE MAPS Link: " + f"https://maps.google.com/?q={r['latitude']},{r['longitude']}", inline=False)
    embed.add_field(name="Country Info", value="ID: " + str(rc[1][0]["id"]) + "\niso2Code: " + str(rc[1][0]["iso2Code"]) + "\nName" + str(rc[1][0]["name"]) + "\n\nRegion: " + "\n   ID: " + str(rc[1][0]["region"]["id"]) + "\n   iso2Code: " + str(rc[1][0]["region"]["iso2code"]) + "\n   Value: " + str(rc[1][0]["region"]["value"]) + "\n\nAdmin Region: " + "\n   ID: " + str(rc[1][0]["adminregion"]["id"]) + "\n   iso2Code: " + str(rc[1][0]["adminregion"]["iso2code"]) + "\n   Value: " + str(rc[1][0]["adminregion"]["value"]) + "\n\nIncome Level: " + "\n   ID: " + str(rc[1][0]["incomeLevel"]["id"]) + "\n   iso2Code: " + str(rc[1][0]["incomeLevel"]["iso2code"]) + "\n   Value: " + str(rc[1][0]["incomeLevel"]["value"]) + "\n\nLending Type: " + "\n   ID: " + str(rc[1][0]["lendingType"]["id"]) + "\n   iso2Code: " + str(rc[1][0]["lendingType"]["iso2code"]) + "\n   Value: " + str(rc[1][0]["lendingType"]["value"]) + "\n\nCapital City: " + str(rc[1][0]["capitalCity"]) + "\nLongitude: " + str(rc[1][0]["longitude"]) + "\nLatitude: " + str(rc[1][0]["latitude"]), inline=False)
    await loading_message.delete()
    await ctx.send(embed=embed)

@client.command(alises=["country-info", "country", "infocountry", "country-information"])
async def countryinfo(ctx, *, countrycodeig):
  loading_message = await ctx.send(embed=please_wait_emb)
  rc = requests.get(f"https://api.worldbank.org/v2/country/{countrycodeig}?format=json").json()
  embed=discord.Embed(title="Country Information", color=0xff0000)
  embed.set_thumbnail(url="https://user-images.githubusercontent.com/36286877/129850352-33345963-273b-42bf-b2bc-5523c8158229.png")
  embed.add_field(name="Country Info", value="ID: " + str(rc[1][0]["id"]) + "\niso2Code: " + str(rc[1][0]["iso2Code"]) + "\nName" + str(rc[1][0]["name"]) + "\n\nRegion: " + "\n   ID: " + str(rc[1][0]["region"]["id"]) + "\n   iso2Code: " + str(rc[1][0]["region"]["iso2code"]) + "\n   Value: " + str(rc[1][0]["region"]["value"]) + "\n\nAdmin Region: " + "\n   ID: " + str(rc[1][0]["adminregion"]["id"]) + "\n   iso2Code: " + str(rc[1][0]["adminregion"]["iso2code"]) + "\n   Value: " + str(rc[1][0]["adminregion"]["value"]) + "\n\nIncome Level: " + "\n   ID: " + str(rc[1][0]["incomeLevel"]["id"]) + "\n   iso2Code: " + str(rc[1][0]["incomeLevel"]["iso2code"]) + "\n   Value: " + str(rc[1][0]["incomeLevel"]["value"]) + "\n\nLending Type: " + "\n   ID: " + str(rc[1][0]["lendingType"]["id"]) + "\n   iso2Code: " + str(rc[1][0]["lendingType"]["iso2code"]) + "\n   Value: " + str(rc[1][0]["lendingType"]["value"]) + "\n\nCapital City: " + str(rc[1][0]["capitalCity"]) + "\nLongitude: " + str(rc[1][0]["longitude"]) + "\nLatitude: " + str(rc[1][0]["latitude"]), inline=False)
  await loading_message.delete()
  await ctx.send(embed=embed)

@client.command()
async def mfp(ctx, *, how_many):
    fake_how_many = int(how_many)
    if fake_how_many <= 40:
      await ctx.send("```Sending " + str(how_many) + " Fake Profiles```")
      for i in range(fake_how_many):
          # await ctx.send("```" + CREATE_FAKE_PROFILES_MANY() + "```")
          fake = Faker()
          simple_dict = fake.profile()
          emf = discord.Embed(title="Fake Information Generator", color=0xF00000)
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
          await ctx.send(embed=emf)
    else:
      await ctx.send("```Please use a number below 40```")

@client.command()
async def pervert(ctx):
    await ctx.send("```" + """Can I get a booty pic with your panties on? And one without them on? Can I also get 3 different pics of your boobs in any position. Also can I get a pic of your pussy from the front and one where it’s spread open. Can I get a picture of you fingering your self? Can I get a pic of you doing a kissing face but with your boobs in it? Can I get a picture of your pussy and ass from behind in one shot? Can I also get a pic of your full front body in just a bra and panties? And can I get a pic of your ass when your pants are all the way up? Also can I get a pic of your boobs when you’re in the shower? Also can I get another pussy pic while you’re in the shower? For the rest of the pics can you just send whatever other sexy things you want? For the videos can I get a video of you twerking in really short shorts? And one of you fingering yourself? One of you actually cumming? Also can I get a video of you playing with your tits while not wearing a shirt? u be squirtin? or u on the cream team? what color the inside? your booty real wet? do it clap? do it fart? do it grip the meat? it’s tight? how many fingers u use? what it taste like? can i smell it? is it warm? it’s real juicy? do it drip? you be moaning?""" + "```")

@client.command()
async def nitro(ctx, *, number_of_times):
    loading_message = await ctx.send(embed=please_wait_emb)
    if int(number_of_times) <= 20:
        await ctx.send("```Sending " + str(number_of_times) + " Random Nitro Codes!```")
        await loading_message.delete()
        for iteration, x in enumerate(range(int(number_of_times))):
            await ctx.send(give_nice_codes())
            time.sleep(0.5)
    else:
        await loading_message.delete()
        ctx.send("```Please enter a value less than 20```")

@client.command()
async def spam(ctx, number_of_times_to_spam, *, message):
    loading_message = await ctx.send(embed=please_wait_emb)
    # await ctx.send("```Spaming " + str(number_of_times_to_spam) + " times!```")

    embed=discord.Embed(title="Spam Messages!", color=0xff0000)
    embed.add_field(name="Requested by: ", value=f"{ctx.author}", inline=False)
    embed.add_field(name="Number of Messages: ", value=f"{number_of_times_to_spam}", inline=False)
    embed.add_field(name="Message: ", value=f"{message}", inline=False)
    await ctx.send(embed=embed)

    # if os.path.exists("spam_log.txt"):
    #   pass
    # else:
    #   fm = open("spam_log.txt", "w", encoding="utf-8")
    #   fm.write(" ")
    #   fm.close()

    # ft = open("spam_log.txt", "w+", encoding="utf-8")
    # ft.write(f' ')
    # ft.close()
    
    # ft = open("spam_log.txt", "a", encoding="utf-8")
    # ft.write(f'{ctx.author} - Requested to spam {number_of_times_to_spam} in {ctx.guild.name}')
    # ft.close()

    await loading_message.delete()

    for iteration, x in enumerate(range(int(number_of_times_to_spam))):
        await ctx.send(message)
        time.sleep(0.5)


# @commands.is_owner()
@client.command()
async def megaspamlol(ctx, *, number_of_times_spam_secret=10):
  if ctx.author.id == bot_owner_id_zeacer:
    embed=discord.Embed(title="MEGA SPAM LOL", description="The very secret feature of this bot has been used!", color=0xff0000)
    await ctx.send(embed=embed)
    for iteration, x in enumerate(range(int(number_of_times_spam_secret))):
        await ctx.send("@everyone @here lol")
        time.sleep(0.5)
  else:
    embednw=discord.Embed(title="NO PERMISSIONS", color=0xff0000)
    embednw.add_field(name="LOL NOPE!", value="You have no permission to use this command!", inline=True)
    await ctx.send(embed=embednw)

@client.command()
async def bored(ctx):
    loading_message = await ctx.send(embed=please_wait_emb)
    bored_activity_get = bored_activity()
    await loading_message.delete()
    await ctx.send("```" + bored_activity_get + "```")

@client.command()
async def color(ctx):
    loading_message = await ctx.send(embed=please_wait_emb)
    give_random_color_get = give_rand_color()
    await loading_message.delete()
    await ctx.send("```" + give_random_color_get + "```")

@client.command()
async def btc(ctx):
    loading_message = await ctx.send(embed=please_wait_emb)
    give_bitcoin_status_get = get_bitcoin_status()
    await loading_message.delete()
    await ctx.send("```" + give_bitcoin_status_get + "```")

@client.command()
async def covidlow(ctx):
  loading_message = await ctx.send(embed=please_wait_emb)
  r = requests.get('https://coronavirus-19-api.herokuapp.com/all') 
  data = r.json()
  confirmed_cases = data["cases"]
  deaths = data["deaths"]
  recovered = data["recovered"]
  
  em = discord.Embed(title="COVID-19 Stats Global - Low Info", color=0xff0000)
  em.set_thumbnail(url="https://www.apsf.org/wp-content/uploads/newsletters/2020/3502/coronavirus-covid-19.png")
  em.add_field(name="Confirmed Cases", value=confirmed_cases)
  em.add_field(name="Deaths", value=deaths)
  em.add_field(name="Recovered", value=recovered) 
  await loading_message.delete()
  await ctx.send(embed=em)

@client.command(aliases=["covidlk"])
async def covidsl(ctx):
  loading_message = await ctx.send(embed=please_wait_emb)
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

@client.command(aliases=["covidall"])
async def covid(ctx):
  loading_message = await ctx.send(embed=please_wait_emb)
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


@client.command()
async def wiki(ctx, *, word_to_search):
    loading_message = await ctx.send(embed=please_wait_emb)
    embed=discord.Embed(title="Wikipedia Search", description="Search Wikipedia without visiting!", color=0xff0000)
    embed.add_field(name="Content", value=f"{search_wikipedia(word_to_search)}", inline=True)
    await loading_message.delete()
    await ctx.send(embed=embed)

@client.command()
async def tinyurl(ctx, *, link):
    loading_message = await ctx.send(embed=please_wait_emb)
    r = requests.get(f'http://tinyurl.com/api-create.php?url={link}').text
    em = discord.Embed(color=0xff0000)
    em.add_field(name="Shortened Link", value=r, inline=False)
    await loading_message.delete()
    await ctx.send(embed=em)

@client.command()
async def dadjoke(ctx):
  loading_message = await ctx.send(embed=please_wait_emb)
  headers = {
    "Accept": "application/json"
  }
  async with aiohttp.ClientSession()as session:
    async with session.get("https://icanhazdadjoke.com", headers=headers) as req:
      r = await req.json()
  await loading_message.delete()
  await ctx.send("```" + r["joke"] + "```")

@client.command()
async def joke(ctx):
  loading_message = await ctx.send(embed=please_wait_emb)
  r = requests.get("https://v2.jokeapi.dev/joke/Any")
  c = r.json()
  # print(c)
  try:
    joke = c["joke"]
  except:
    pass
  try:
    joke = c["setup"]
  except:
    pass
  # await ctx.send("```" + joke + "```")
  embed=discord.Embed(title="a Joke", color=0xff0000)
  embed.add_field(name="", value=f"{joke}", inline=True)
  await loading_message.delete()
  await ctx.send(embed=embed)

@client.command(aliases=["server-icon"])
async def iconserver(ctx):
  loading_message = await ctx.send(embed=please_wait_emb)
  em = discord.Embed(title=ctx.guild.name)
  em.set_image(url=ctx.guild.icon_url)
  await loading_message.delete()
  await ctx.send(embed=em)

@client.command()
async def mac(ctx, mac):
  loading_message = await ctx.send(embed=please_wait_emb)
  r = requests.get('http://api.macvendors.com/' + mac)
  em = discord.Embed(title='MAC Lookup Result', description=r.text, colour=0xff0000)
  em.set_author(name='MAC Finder', icon_url='https://regmedia.co.uk/2016/09/22/wifi_icon_shutterstock.jpg?x=1200&y=794')
  await loading_message.delete()
  await ctx.send(embed=em)

@client.command()
async def bitcoin(ctx):
  loading_message = await ctx.send(embed=please_wait_emb)
  r = requests.get('https://min-api.cryptocompare.com/data/price?fsym=BTC&tsyms=USD,EUR')
  r = r.json()
  usd = r['USD']
  eur = r['EUR']
  em = discord.Embed(description=f'USD: `{str(usd)}$`\nEUR: `{str(eur)}€`')
  em.set_author(name='Bitcoin', icon_url='https://cdn.pixabay.com/photo/2013/12/08/12/12/bitcoin-225079_960_720.png')
  await loading_message.delete()
  await ctx.send(embed=em)

@client.command()
async def eth(ctx):
  loading_message = await ctx.send(embed=please_wait_emb)
  r = requests.get('https://min-api.cryptocompare.com/data/price?fsym=ETH&tsyms=USD,EUR')
  r = r.json()
  usd = r['USD']
  eur = r['EUR']
  em = discord.Embed(description=f'USD: `{str(usd)}$`\nEUR: `{str(eur)}€`')
  em.set_author(name='Ethereum', icon_url='https://cdn.discordapp.com/attachments/271256875205525504/374282740218200064/2000px-Ethereum_logo.png')
  await loading_message.delete()
  await ctx.send(embed=em)

@client.command(aliases=['wouldyourather', 'would-you-rather', 'wyrq'])
async def wyr(ctx):
  loading_message = await ctx.send(embed=please_wait_emb)
  r = requests.get('https://www.conversationstarters.com/wyrqlist.php').text
  soup = BeautifulSoup(r, 'html.parser')
  qa = soup.find(id='qa').text
  qor = soup.find(id='qor').text
  qb = soup.find(id='qb').text
  em = discord.Embed(description=f'{qa}\n{qor}\n{qb}', color=0xff0000)
  await loading_message.delete()
  await ctx.send(embed=em)

@client.command()
async def hastebin(ctx, *, message):
  loading_message = await ctx.send(embed=please_wait_emb)
  r = requests.post("https://hastebin.com/documents", data=message).json()
  # await ctx.send(f"<https://hastebin.com/{r['key']}>")
  em = discord.Embed(title='Hastebin ', description=f"https://hastebin.com/{r['key']}", color=0xff0000)
  em.set_author(name='Hastebin', icon_url='https://www.saashub.com/images/app/service_logos/10/2e5b036c770f/large.png?1528818030')
  await loading_message.delete()
  await ctx.send(embed=em)

@client.command()
async def asciiart(ctx, *, text):
  loading_message = await ctx.send(embed=please_wait_emb)
  r = requests.get(f'http://artii.herokuapp.com/make?text={urllib.parse.quote_plus(text)}').text
  if len('```'+r+'```') > 2000:
    return
  await loading_message.delete()
  await ctx.send(f"```{r}```")

@client.command()
async def anal(ctx):
  loading_message = await ctx.send(embed=please_wait_emb)
  r = requests.get("https://nekos.life/api/v2/img/anal")
  res = r.json()
  em = discord.Embed(color=0xff0000)
  em.set_image(url=res['url'])
  await loading_message.delete()
  await ctx.send(embed=em)

@client.command()
async def erofeet(ctx):
  loading_message = await ctx.send(embed=please_wait_emb)
  r = requests.get("https://nekos.life/api/v2/img/erofeet")
  res = r.json()
  em = discord.Embed(color=0xff0000)
  em.set_image(url=res['url'])
  await loading_message.delete()
  await ctx.send(embed=em)

@client.command()
async def feet(ctx):
  loading_message = await ctx.send(embed=please_wait_emb)
  r = requests.get("https://nekos.life/api/v2/img/feetg")
  res = r.json()
  em = discord.Embed(color=0xff0000)
  em.set_image(url=res['url'])
  await loading_message.delete()
  await ctx.send(embed=em)

@client.command()
async def hentai(ctx):
  loading_message = await ctx.send(embed=please_wait_emb)
  r = requests.get("https://nekos.life/api/v2/img/Random_hentai_gif")
  res = r.json()
  em = discord.Embed()
  em.set_image(url=res['url'])
  await loading_message.delete()
  await ctx.send(embed=em)

@client.command()
async def boobs(ctx):
  loading_message = await ctx.send(embed=please_wait_emb)
  r = requests.get("https://nekos.life/api/v2/img/boobs")
  res = r.json()
  em = discord.Embed(color=0xff0000)
  em.set_image(url=res['url'])
  await loading_message.delete()
  await ctx.send(embed=em)

@client.command()
async def tits(ctx):
  loading_message = await ctx.send(embed=please_wait_emb)
  r = requests.get("https://nekos.life/api/v2/img/tits")
  res = r.json()
  em = discord.Embed(color=0xff0000)
  em.set_image(url=res['url'])
  await loading_message.delete()
  await ctx.send(embed=em)

@client.command()
async def blowjob(ctx):
  loading_message = await ctx.send(embed=please_wait_emb)
  r = requests.get("https://nekos.life/api/v2/img/blowjob")
  res = r.json()
  em = discord.Embed(color=0xff0000)
  em.set_image(url=res['url'])
  await loading_message.delete()
  await ctx.send(embed=em)

@client.command()
async def lewd(ctx):
  loading_message = await ctx.send(embed=please_wait_emb)
  r = requests.get("https://nekos.life/api/v2/img/nsfw_neko_gif")
  res = r.json()
  em = discord.Embed(color=0xff0000)
  em.set_image(url=res['url'])
  await loading_message.delete()
  await ctx.send(embed=em)

@client.command()
async def lesbian(ctx):
  loading_message = await ctx.send(embed=please_wait_emb)
  r = requests.get("https://nekos.life/api/v2/img/les")
  res = r.json()
  em = discord.Embed(color=0xff0000)
  em.set_image(url=res['url'])
  await loading_message.delete()
  await ctx.send(embed=em)

@client.command()
async def feed(ctx, user: discord.Member):
  loading_message = await ctx.send(embed=please_wait_emb)
  r = requests.get("https://nekos.life/api/v2/img/feed")
  res = r.json()
  em = discord.Embed(description=user.mention, color=0xff0000)
  em.set_image(url=res['url'])
  await loading_message.delete()
  await ctx.send(embed=em)

@client.command()
async def tickle(ctx, user: discord.Member):
  loading_message = await ctx.send(embed=please_wait_emb)
  r = requests.get("https://nekos.life/api/v2/img/tickle")
  res = r.json()
  em = discord.Embed(description=user.mention, color=0xff0000)
  em.set_image(url=res['url'])
  await loading_message.delete()
  await ctx.send(embed=em)

@client.command()
async def hit(ctx, user: discord.Member):
  loading_message = await ctx.send(embed=please_wait_emb)
  r = requests.get("https://nekos.life/api/v2/img/slap")
  res = r.json()
  em = discord.Embed(description=user.mention, color=0xff0000)
  em.set_image(url=res['url'])
  await loading_message.delete()
  await ctx.send(embed=em)

@client.command()
async def hug(ctx, user: discord.Member):
  loading_message = await ctx.send(embed=please_wait_emb)
  r = requests.get("https://nekos.life/api/v2/img/hug")
  res = r.json()
  em = discord.Embed(description=user.mention, color=0xff0000)
  em.set_image(url=res['url'])
  await loading_message.delete()
  await ctx.send(embed=em)

@client.command()
async def smug(ctx, user: discord.Member):
  loading_message = await ctx.send(embed=please_wait_emb)
  r = requests.get("https://nekos.life/api/v2/img/smug")
  res = r.json()
  em = discord.Embed(description=user.mention, color=0xff0000)
  em.set_image(url=res['url'])
  await loading_message.delete()
  await ctx.send(embed=em)

@client.command()
async def pat(ctx, user: discord.Member):
  loading_message = await ctx.send(embed=please_wait_emb)
  r = requests.get("https://nekos.life/api/v2/img/pat")
  res = r.json()
  em = discord.Embed(description=user.mention, color=0xff0000)
  em.set_image(url=res['url'])
  await loading_message.delete()
  await ctx.send(embed=em)

@client.command()
async def kiss(ctx, user: discord.Member):
  loading_message = await ctx.send(embed=please_wait_emb)
  r = requests.get("https://nekos.life/api/v2/img/kiss")
  res = r.json()
  em = discord.Embed(description=user.mention, color=0xff0000)
  em.set_image(url=res['url'])
  await loading_message.delete()
  await ctx.send(embed=em)

@client.command()
async def reverse(ctx, *, message):
  message = message[::-1]
  embed=discord.Embed(title="Reverse Text", description=f"{message}", color=0xff0000)
  await ctx.send(embed=embed)
  # await ctx.send(message)

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

@client.command()
async def xmr(ctx):
  loading_message = await ctx.send(embed=please_wait_emb)
  r = requests.get("https://min-api.cryptocompare.com/data/price?fsym=XMR&tsyms=USD,EUR")
  NegroPuket = r.json()
  eur = NegroPuket['EUR']
  usd = NegroPuket['USD']
  embedic = discord.Embed(description=f'EUR: `{str(eur)}€`\nUSD: `{str(usd)}$`', color=0xff0000)
  embedic.set_author(name='Monero', icon_url='https://cdn.freebiesupply.com/logos/large/2x/monero-logo-png-transparent.png')
  await loading_message.delete()
  await ctx.send(embed=embedic)

@client.command()
async def doge(ctx):
  loading_message = await ctx.send(embed=please_wait_emb)
  r = requests.get("https://min-api.cryptocompare.com/data/price?fsym=DOGE&tsyms=USD,EUR")
  NegroPuketDOGE = r.json()
  eur = NegroPuketDOGE['EUR']
  usd = NegroPuketDOGE['USD']
  embedic = discord.Embed(description=f'EUR: `{str(eur)}€`\nUSD: `{str(usd)}$`', color=0xff0000)
  embedic.set_author(name='Dogecoin', icon_url='https://cdn.coindoo.com/2019/10/dogecoin-logo.png')
  await loading_message.delete()
  await ctx.send(embed=embedic)


@client.command()
async def xrp(ctx):
  loading_message = await ctx.send(embed=please_wait_emb)
  r = requests.get("https://min-api.cryptocompare.com/data/price?fsym=XRP&tsyms=USD,EUR")
  kekistan = r.json()
  eur = kekistan['EUR']
  usd = kekistan['USD']
  embedic = discord.Embed(description=f'EUR: `{str(eur)}€`\nUSD: `{str(usd)}$`', color=0xff0000)
  embedic.set_author(name='Ripple', icon_url='https://cdn.freebiesupply.com/logos/large/2x/ripple-2-logo-png-transparent.png')
  await loading_message.delete()
  await ctx.send(embed=embedic)

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

@client.command(aliases=['dong', 'penis', 'pp', 'psize', 'dicksize', 'penissize'])
async def dick(ctx, *, user: discord.User = None):
  loading_message = await ctx.send(embed=please_wait_emb)
  if user is None:
    user = ctx.author
    size = random.randint(2, 20)
    em = discord.Embed(title=f"{user}'s Dick size:", description=f"{size} Inches", colour=0xff0000)
    await loading_message.delete()
    await ctx.send(embed=em)
    if size < 6:
      await ctx.send(f"{user.mention} - Your dick is very small that a girl will not just feel theres something in, Just get a new life!")
  else:
    size = random.randint(2, 20)
    em = discord.Embed(title=f"{user.mention}'s Dick size:", description=f"{size} Inches", colour=0xff0000)
    await loading_message.delete()
    await ctx.send(embed=em)
    if size < 6:
      await ctx.send(f"{user.mention} - Your dick is very small that a girl will not just feel theres something in, Just get a new life!")




@client.command()
async def panda(ctx):
  loading_message = await ctx.send(embed=please_wait_emb)
  r = requests.get("https://some-random-api.ml/img/panda").json()
  embed = discord.Embed(color=0xff0000)
  embed.set_author(name="a Panda.", icon_url="https://cdn.freebiesupply.com/logos/large/2x/panda-7-logo-png-transparent.png") 
  embed.set_image(url=str(r["link"]))
  await loading_message.delete()
  await ctx.send(embed=embed)    

@client.command(aliases=["lol"])
async def meme(ctx):
  loading_message = await ctx.send(embed=please_wait_emb)
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

@client.command()
async def dog(ctx):
  loading_message = await ctx.send(embed=please_wait_emb)
  r = requests.get("https://some-random-api.ml/img/dog").json()
  embed = discord.Embed(color=0xff0000)
  embed.set_author(name="a Dog." , icon_url="https://t4.ftcdn.net/jpg/03/66/78/13/360_F_366781345_oEr9wc8yWhYRPZe6CGyFWS6QolZIf2fJ.jpg") 
  embed.set_image(url=str(r["link"]))
  await loading_message.delete()
  await ctx.send(embed=embed)    

@client.command()
async def cat(ctx):
  loading_message = await ctx.send(embed=please_wait_emb)
  r = requests.get("https://some-random-api.ml/img/cat").json()
  embed = discord.Embed(color=0xff0000)
  embed.set_author(name="a Cat.", icon_url="https://i.pinimg.com/736x/d6/0c/7e/d60c7e8983fdbd7c7a27fd42fb3d61ba.jpg") 
  embed.set_image(url=str(r["link"]))
  await loading_message.delete()
  await ctx.send(embed=embed)   

@client.command(aliases=['pfp', 'avatar'])
async def av(ctx, *, user: discord.User = None):
  loading_message = await ctx.send(embed=please_wait_emb)
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

@client.command(aliases=["guildinfo", "serverinfo", "si"])
async def infoserver(ctx):
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
  embed.set_thumbnail(url=f"{ctx.guild.icon_url}")
  await loading_message.delete()
  await ctx.send(embed=embed)

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
  embed = discord.Embed(color=0xff0000)
  embed.set_author(name=ctx.guild.name, icon_url=ctx.guild.icon_url)   
  embed.set_image(url=ctx.guild.icon_url)
  await loading_message.delete()
  await ctx.send(embed=embed)

@client.command(aliases=["account-creation-date", "account-date"])
async def accdate(ctx, *, user: discord.User = None):
  loading_message = await ctx.send(embed=please_wait_emb)
  if user is None:
    user = ctx.author      
  date_format = "%a, %d %b %Y %I:%M %p"
  em = discord.Embed(description=user.mention, color=0xff0000)
  em.set_author(name=str(user), icon_url=user.avatar_url)
  em.set_thumbnail(url=user.avatar_url)
  em.add_field(name="Registered", value=user.created_at.strftime(date_format))
  await loading_message.delete()
  return await ctx.send(embed=em)

@client.command(aliases=["userinfo", "uinfo", "user-info"])
async def whoareyou(ctx, target: Optional[discord.Member]):
  loading_message = await ctx.send(embed=please_wait_emb)
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
  
  await loading_message.delete()
  await ctx.send(embed=embed)



@client.command(aliases=["e_base64"])
async def e_b64(ctx, *, args):
  loading_message = await ctx.send(embed=please_wait_emb)
  msg = base64.b64encode('{}'.format(args).encode('ascii'))
  enc = str(msg)
  enc = enc[2:len(enc)-1]
  embed=discord.Embed(title="to Base64", description=f"{enc}", color=0xff0000)
  await loading_message.delete()
  await ctx.send(embed=embed)

@client.command()
async def e_md5(ctx, *, args):
  loading_message = await ctx.send(embed=please_wait_emb)
  msg = hashlib.md5(args.encode())
  slpake =  msg.hexdigest()
  embed=discord.Embed(title="to MD5", description=f"{slpake}", color=0xff0000)
  await loading_message.delete()
  await ctx.send(embed=embed)

@client.command()
async def e_sha1(ctx, *, args):
  loading_message = await ctx.send(embed=please_wait_emb)
  msg = hashlib.sha1(args.encode())
  slpuka =  msg.hexdigest()
  embed=discord.Embed(title="to MD5", description=f"{slpuka}", color=0xff0000)
  await loading_message.delete()
  await ctx.send(embed=embed)

@client.command()
async def e_sha224(ctx, *, args):
  loading_message = await ctx.send(embed=please_wait_emb)
  msg = hashlib.sha3_224(args.encode())
  crnja =  msg.hexdigest()
  embed=discord.Embed(title="to MD5", description=f"{crnja}", color=0xff0000)
  await loading_message.delete()
  await ctx.send(embed=embed)

@client.command()
async def e_sha512(ctx, *, args):
  loading_message = await ctx.send(embed=please_wait_emb)
  msg = hashlib.sha3_512(args.encode())
  crnja =  msg.hexdigest()
  embed=discord.Embed(title="to MD5", description=f"{crnja}", color=0xff0000)
  await loading_message.delete()
  await ctx.send(embed=embed)

@client.command(aliases=["leet"])
async def e_leet(ctx, *, args):
  loading_message = await ctx.send(embed=please_wait_emb)
  encoded = args.replace('e', '3').replace('a', '4').replace('i', '!').replace('u', '|_|').replace('U', '|_|').replace('E', '3').replace('I', '!').replace('A', '4').replace('o','0').replace('O','0').replace('t','7').replace('T','7').replace('l','1').replace('L','1').replace('k','|<').replace('K','|<').replace('CK','X').replace('ck','x').replace('Ck','X').replace('cK','x')
  embed=discord.Embed(title="to MD5", description=f"{encoded}", color=0xff0000)
  await loading_message.delete()
  await ctx.send(embed=embed)

@client.command(aliases=["addition"])
async def add(ctx, number_1, number_2):
  loading_message = await ctx.send(embed=please_wait_emb)
  ans = float(number_1) + float(number_2)
  em = discord.Embed(description=f"Question: {number_1} + {number_2}\n\nAnswer: {ans}", color=0xff0000)
  em.set_author(name="Addition")
  await loading_message.delete()
  await ctx.send(embed=em)

@client.command(aliases=["substraction", "substract"])
async def subs(ctx, number_1, number_2):
  loading_message = await ctx.send(embed=please_wait_emb)
  ans = float(number_1) - float(number_2)
  em = discord.Embed(description=f"Question: {number_1} - {number_2}\n\nAnswer: {ans}", color=0xff0000)
  em.set_author(name="Substraction")
  await loading_message.delete()
  await ctx.send(embed=em)

@client.command(aliases=["multiplication", "multiply"])
async def mul(ctx, number_1, number_2):
  loading_message = await ctx.send(embed=please_wait_emb)
  ans = float(number_1) * float(number_2)
  em = discord.Embed(description=f"Question: {number_1} x {number_2}\n\nAnswer: {ans}", color=0xff0000)
  em.set_author(name="Multiplication")
  await loading_message.delete()
  await ctx.send(embed=em)

@client.command(aliases=["division", "divide"])
async def div(ctx, number_1, number_2):
  loading_message = await ctx.send(embed=please_wait_emb)
  ans = float(number_1) / float(number_2)
  em = discord.Embed(description=f"Question: {number_1} / {number_2}\n\nAnswer: {ans}", color=0xff0000)
  em.set_author(name="Division")
  await loading_message.delete()
  await ctx.send(embed=em)

@client.command(aliases=["echo"])
async def say(ctx, *, word_to_say):
  await ctx.message.delete()
  await ctx.send(str(word_to_say))

@client.command(aliases=["dog-facts", "dogfacts", "dog-fact"])
async def dogfact(ctx):
  loading_message = await ctx.send(embed=please_wait_emb)
  r = requests.get('https://some-random-api.ml/facts/dog')
  c = r.json()
  fact = c["fact"]

  em = discord.Embed(title='Dog Fact', description=fact, color=0xff0000)
  em.set_author(name='Random Dog Fact', icon_url='https://post.medicalnewstoday.com/wp-content/uploads/sites/3/2020/02/322868_1100-800x825.jpg')
  await loading_message.delete()
  await ctx.send(embed=em)

@client.command(aliases=["cat-facts", "catfacts", "cat-fact"])
async def catfact(ctx):
  loading_message = await ctx.send(embed=please_wait_emb)
  r = requests.get('https://some-random-api.ml/facts/cat')
  c = r.json()
  fact = c["fact"]

  em = discord.Embed(title='Cat Fact', description=fact, color=0xff0000)
  em.set_author(name='Random Cat Fact', icon_url='https://i.guim.co.uk/img/media/26392d05302e02f7bf4eb143bb84c8097d09144b/446_167_3683_2210/master/3683.jpg?width=1200&height=1200&quality=85&auto=format&fit=crop&s=49ed3252c0b2ffb49cf8b508892e452d')
  await loading_message.delete()
  await ctx.send(embed=em)

@client.command(aliases=["elephant-facts", "elephantfacts", "elephant-fact"])
async def elephantfact(ctx):
  loading_message = await ctx.send(embed=please_wait_emb)
  r = requests.get('https://some-random-api.ml/facts/elephant')
  c = r.json()
  fact = c["fact"]

  em = discord.Embed(title='Elephant Fact', description=fact, color=0xff0000)
  em.set_author(name='Random Elephant Fact', icon_url='https://c402277.ssl.cf1.rackcdn.com/photos/14206/images/hero_small/WW187785.jpg?1576774644')
  await loading_message.delete()
  await ctx.send(embed=em)

@client.command(aliases=["panda-facts", "pandafacts", "panda-fact"])
async def pandafact(ctx):
  loading_message = await ctx.send(embed=please_wait_emb)
  r = requests.get('https://some-random-api.ml/facts/panda')
  c = r.json()
  fact = c["fact"]

  em = discord.Embed(title='Panda Fact', description=fact, color=0xff0000)
  em.set_author(name='Random panda Fact', icon_url='https://www.chinasage.info/imgs/BabyGiantPanda.jpg')
  await loading_message.delete()
  await ctx.send(embed=em)

@client.command(aliases=["fox-facts", "foxfacts", "fox-fact"])
async def foxfact(ctx):
  loading_message = await ctx.send(embed=please_wait_emb)
  r = requests.get('https://some-random-api.ml/facts/fox')
  c = r.json()
  fact = c["fact"]

  em = discord.Embed(title='Fox Fact', description=fact, color=0xff0000)
  em.set_author(name='Random Fox Fact', icon_url='https://images.wsj.net/im-355811?width=620&size=1.5')
  await loading_message.delete()
  await ctx.send(embed=em)

@client.command(aliases=["bird-facts", "birdfacts", "bird-fact"])
async def birdfact(ctx):
  loading_message = await ctx.send(embed=please_wait_emb)
  r = requests.get('https://some-random-api.ml/facts/bird')
  c = r.json()
  fact = c["fact"]

  em = discord.Embed(title='Bird Fact', description=fact, color=0xff0000)
  em.set_author(name='Random Bird Fact', icon_url='https://res.cloudinary.com/dk-find-out/image/upload/q_80,w_960,f_auto/DCTM_Penguin_UK_DK_AL526630_wkmzns.jpg')
  await loading_message.delete()
  await ctx.send(embed=em)

@client.command(aliases=["koala-facts", "koalafacts", "koala-fact"])
async def koalafact(ctx):
  loading_message = await ctx.send(embed=please_wait_emb)
  r = requests.get('https://some-random-api.ml/facts/koala')
  c = r.json()
  fact = c["fact"]
  em = discord.Embed(title='Koala Fact', description=fact, color=0xff0000)
  em.set_author(name='Random Koala Fact', icon_url='https://cdn.britannica.com/26/162626-050-3534626F/Koala.jpg')
  await loading_message.delete()
  await ctx.send(embed=em)

@client.command(aliases=["red-panda", "red-panda-image", "red-panda-img"])
async def redpanda(ctx):
  loading_message = await ctx.send(embed=please_wait_emb)
  r = requests.get('https://some-random-api.ml/img/red_panda')
  c = r.json()
  fact = c["link"]
  em = discord.Embed(title='a Red Panda', description=fact, color=0xff0000)
  em.set_author(name='a Random Red Panda', icon_url='https://cdn.vox-cdn.com/thumbor/erBglLkGU0eWF6c2PsEWHT2_TE0=/12x0:4907x3263/1400x1400/filters:focal(12x0:4907x3263):format(jpeg)/cdn.vox-cdn.com/uploads/chorus_image/image/49388585/16071828377_85109fdee4_o.0.0.jpg')
  await loading_message.delete()
  await ctx.send(embed=em)

@client.command(aliases=["birds", "bird-image", "bird-img"])
async def bird(ctx):
  loading_message = await ctx.send(embed=please_wait_emb)
  r = requests.get('https://some-random-api.ml/img/birb')
  c = r.json()
  fact = c["link"]
  em = discord.Embed(title='a Bird', description=fact, color=0xff0000)
  em.set_author(name='a Random Bird', icon_url='https://ichef.bbci.co.uk/news/976/cpsprodpb/67CF/production/_108857562_mediaitem108857561.jpg')
  await loading_message.delete()
  await ctx.send(embed=em)


@client.command(aliases=["foxes", "fox-image", "fox-img"])
async def fox(ctx):
  loading_message = await ctx.send(embed=please_wait_emb)
  r = requests.get('https://some-random-api.ml/img/fox')
  c = r.json()
  fact = c["link"]
  em = discord.Embed(title='a Fox', color=0xff0000)
  em.set_author(name='a Random Fox', icon_url='https://images.unsplash.com/photo-1615602127413-459bdb48cf45?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=1000&q=80')
  em.set_image(url=fact)
  await loading_message.delete()
  await ctx.send(embed=em)

@client.command(aliases=["a-wink", "winks"])
async def wink(ctx):
  loading_message = await ctx.send(embed=please_wait_emb)
  r = requests.get('https://some-random-api.ml/animu/wink')
  c = r.json()
  fact = c["link"]
  em = discord.Embed(title='a wink', color=0xff0000)
  em.set_author(name='wink')
  em.set_image(url=fact)
  await loading_message.delete()
  await ctx.send(embed=em)

@client.command(aliases=["a-pikachu", "pikachuu"])
async def pikachu(ctx):
  loading_message = await ctx.send(embed=please_wait_emb)
  r = requests.get('https://some-random-api.ml/img/pikachu')
  c = r.json()
  fact = c["link"]
  em = discord.Embed(title='a Pickachu', color=0xff0000)
  em.set_author(name='a Random Pickachu')
  em.set_image(url=fact)
  await loading_message.delete()
  await ctx.send(embed=em)

@client.command(aliases=["gay-colors", "gay-colours"])
async def gay(ctx, *, messagelink):
  loading_message = await ctx.send(embed=please_wait_emb)
  weblink = 'https://some-random-api.ml/canvas/gay?avatar=' + messagelink
  r = requests.get(weblink)
  em = discord.Embed(title='Gay Picture', color=0xff0000)
  em.set_author(name='a Gay colored Picture')
  em.set_image(url=weblink)
  await loading_message.delete()
  await ctx.send(embed=em)

@client.command(aliases=["glass-colors", "glass-colours", "glassy-colors", "glassy-colours"])
async def glass(ctx, *, messagelink):
  loading_message = await ctx.send(embed=please_wait_emb)
  weblink = 'https://some-random-api.ml/canvas/glass/?avatar=' + messagelink
  em = discord.Embed(title='Glassy Picture', color=0xff0000)
  em.set_author(name='a Glassy colored Picture')
  em.set_image(url=weblink)
  await loading_message.delete()
  await ctx.send(embed=em)

@client.command(aliases=["wasted-colors", "wasted-colours", "wasted-image", "wasted-img"])
async def wasted(ctx, *, messagelink, color=0xff0000):
  loading_message = await ctx.send(embed=please_wait_emb)
  weblink = 'https://some-random-api.ml/canvas/glass/?avatar=' + messagelink
  em = discord.Embed(title='a Wasted Picture', color=0xff0000)
  em.set_author(name='Wasted Picture')
  em.set_image(url=weblink)
  await loading_message.delete()
  await ctx.send(embed=em)

@client.command()
async def triggered(ctx, *, messagelink):
  loading_message = await ctx.send(embed=please_wait_emb)
  weblink = 'https://some-random-api.ml/canvas/triggered?avatar=' + messagelink
  em = discord.Embed(title='a TRIGGERED Picture', color=0xff0000)
  em.set_author(name='Triggered Picture')
  em.set_image(url=weblink)
  await loading_message.delete()
  await ctx.send(embed=em)

@client.command(aliases=["bandw", "black-and-white"])
async def grayscale(ctx, *, messagelink):
  loading_message = await ctx.send(embed=please_wait_emb)
  weblink = 'https://some-random-api.ml/canvas/greyscale?avatar=' + messagelink
  em = discord.Embed(title='a Black and White Picture', color=0xff0000)
  em.set_author(name='Black and White Picture')
  em.set_image(url=weblink)
  await loading_message.delete()
  await ctx.send(embed=em)

@client.command(aliases=["invert-img", "invert-colors", "invert-image"])
async def invert(ctx, *, messagelink):
  loading_message = await ctx.send(embed=please_wait_emb)
  weblink = 'https://some-random-api.ml/canvas/invert?avatar=' + messagelink
  em = discord.Embed(title='a Inverted Picture', color=0xff0000)
  em.set_author(name='Inverted Picture')
  em.set_image(url=weblink)
  await loading_message.delete()
  await ctx.send(embed=em)

@client.command(aliases=["bright-img", "bright-colors", "bright-image", "bright"])
async def brightness(ctx, *, messagelink):
  weblink = 'https://some-random-api.ml/canvas/brightness?avatar=' + messagelink
  em = discord.Embed(title='a Brightened Picture', color=0xff0000)
  em.set_author(name='Brightened Picture')
  em.set_image(url=weblink)
  await ctx.send(embed=em)

@client.command(aliases=["threshold-img", "threshold-colors", "threshold-image", "thresh"])
async def threshold(ctx, *, messagelink):
  loading_message = await ctx.send(embed=please_wait_emb)
  weblink = 'https://some-random-api.ml/canvas/threshold?avatar=' + messagelink
  em = discord.Embed(title='a Threshold Picture', color=0xff0000)
  em.set_author(name='Threshold Picture')
  em.set_image(url=weblink)
  await loading_message.delete()
  await ctx.send(embed=em)

@client.command(aliases=["sepia-image", "sepia-color"])
async def sepia(ctx, *, messagelink):
  loading_message = await ctx.send(embed=please_wait_emb)
  weblink = 'https://some-random-api.ml/canvas/greyscale?avatar=' + messagelink
  em = discord.Embed(title='a Sepia Picture', color=0xff0000)
  em.set_author(name='Sepia Picture')
  em.set_image(url=weblink)
  await loading_message.delete()
  await ctx.send(embed=em)

@client.command(aliases=["red-image", "red-color"])
async def red(ctx, *, messagelink):
  loading_message = await ctx.send(embed=please_wait_emb)
  weblink = 'https://some-random-api.ml/canvas/red?avatar=' + messagelink
  em = discord.Embed(title='a Red Picture', color=0xff0000)
  em.set_author(name='Red Picture')
  em.set_image(url=weblink)
  await loading_message.delete()
  await ctx.send(embed=em)

@client.command(aliases=["green-image", "green-color"])
async def green(ctx, *, messagelink):
  loading_message = await ctx.send(embed=please_wait_emb)
  weblink = 'https://some-random-api.ml/canvas/green?avatar=' + messagelink
  em = discord.Embed(title='a Green Picture', color=0xff0000)
  em.set_author(name='Green Picture')
  em.set_image(url=weblink)
  await loading_message.delete()
  await ctx.send(embed=em)

@client.command(aliases=["blue-image", "blue-color"])
async def blue(ctx, *, messagelink):
  loading_message = await ctx.send(embed=please_wait_emb)
  weblink = 'https://some-random-api.ml/canvas/blue?avatar=' + messagelink
  em = discord.Embed(title='a Blue Picture', color=0xff0000)
  em.set_author(name='Blue Picture')
  em.set_image(url=weblink)
  await loading_message.delete()
  await ctx.send(embed=em)

@client.command(aliases=["tint-image", "tint-color"])
async def tint(ctx, colorTotint, *, messagelink):
  loading_message = await ctx.send(embed=please_wait_emb)
  weblink = 'https://some-random-api.ml/canvas/color?avatar=' + messagelink + "&color=%" + colorTotint
  em = discord.Embed(title='a Tinted Picture', color=0xff0000)
  embed_text = "Picture tinted in " + colorTotint
  em.set_author(name=embed_text)
  em.set_image(url=weblink)
  await loading_message.delete()
  await ctx.send(embed=em)

@client.command(aliases=["pixelate-image"])
async def pixelate(ctx, *, messagelink):
  loading_message = await ctx.send(embed=please_wait_emb)
  weblink = 'https://some-random-api.ml/canvas/pixelate' + messagelink
  em = discord.Embed(title='a Blue Picture', color=0xff0000)
  em.set_author(name='Blue Picture')
  em.set_image(url=weblink)
  await loading_message.delete()
  await ctx.send(embed=em)

@client.command(aliases=["ytc", "youtubecomment", "youtube-comment", "yt-comment", "you-tube-comment"])
async def ytcomment(ctx, usernameofu, commentmsg, profilepictureLink="https://static.wikia.nocookie.net/ba0628fe-3bc1-42c3-9c0c-aa91ba24f03c/scale-to-width/370", mode="dark"):
  loading_message = await ctx.send(embed=please_wait_emb)
  weblink = "https://some-random-api.ml/canvas/youtube-comment?username=" + usernameofu.replace("_", "%20") + "&comment=" + commentmsg.replace("_", "%20") + "&avatar=" + profilepictureLink + "&dark=true"
  # em = discord.Embed(title='a picture of a YouTube Comment')
  # em.set_author(name='Fake YouTube Comment')
  # em.set_image(url=weblink)
  # await ctx.send(embed=em)
  await loading_message.delete()
  await ctx.send(weblink)

@client.command()
async def pokemon(ctx, pokemonName="pikachu", mode="new"):
  loading_message = await ctx.send(embed=please_wait_emb)
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


@client.command(aliases=["mincraft-info", "mincraft-user-info", "minecraftinfo"])
async def mcinfo(ctx, *, MinecraftUserName):
  loading_message = await ctx.send(embed=please_wait_emb)
  weblink = "https://some-random-api.ml/mc?username=" + MinecraftUserName
  r = requests.get(weblink)
  c = r.json()
  mcinfo_test = f"""Username: {c["username"]}
UUID: {c["uuid"]}
Name History: {c["name_history"]}
"""
  await loading_message.delete()
  await ctx.send("```" + mcinfo_test + "```")

@client.command(aliases=["lyrics-of", "find-lyrics"])
async def lyricsof(ctx, *, song_name):
  loading_message = await ctx.send(embed=please_wait_emb)
  weblink = "https://some-random-api.ml/lyrics?title=" + song_name
  r = requests.get(weblink)
  c = r.json()
  author = c["author"]
  title = c["title"]
  lyrics = c["lyrics"]
  msg_to_send_song_info = f"""Title: {title}
Author: {author}

Lyrics:
{lyrics}
""" 
  await loading_message.delete()
  try:  
    part1 = msg_to_send_song_info[:1999]
    await ctx.send(part1)
  except:
    pass
  try:
    part2 = msg_to_send_song_info[1999:3998]
    await ctx.send(part2)
  except:
    pass
  try:
    part3 = msg_to_send_song_info[3998:5997]
    await ctx.send(part3)
  except:
    pass
  try:
    part4 = msg_to_send_song_info[5997:7996]
    await ctx.send(part4)
  except:
    pass
  try:
    part5 = msg_to_send_song_info[7996:9995]
    await ctx.send(part5)
  except:
    pass
  try:
    part6 = msg_to_send_song_info[9995:11994]
    await ctx.send(part6)
  except:
    pass
  try:
    part7 = msg_to_send_song_info[11994:13993]
    await ctx.send(part7)
  except:
    pass
  try:
    part8 = msg_to_send_song_info[13993:15992]
    await ctx.send(part8)
  except:
    pass
  try:
    part9 = msg_to_send_song_info[15992:17991]
    await ctx.send(part9)
  except:
    pass
  try:
    part10 = msg_to_send_song_info[17991:19990]
    await ctx.send(part10)
  except:
    pass

  try:
    links = c["links"]
    await ctx.send(links["genius"])
  except:
    pass

@client.command(aliases=["to-binary", "e_binary"])
async def binary(ctx, *, ToBinaryText):
  loading_message = await ctx.send(embed=please_wait_emb)
  r = requests.get('https://some-random-api.ml/binary?text=' + ToBinaryText)
  c = r.json()
  fact = c["binary"]
  shit = 'Text to binary'
  em = discord.Embed(color=0xff0000)
  AandQ = f'The message entered converted to binary is: \n\n{str(fact)}'
  em.add_field(name=shit, value=AandQ)
  await loading_message.delete()
  await ctx.send(embed=em)

@client.command(aliases=["b2t", "d_binary", "decode_binary"])
async def b_2txt(ctx, *, ToTextBinary):
  loading_message = await ctx.send(embed=please_wait_emb)
  r = requests.get('https://some-random-api.ml/binary?decode=' + ToTextBinary)
  c = r.json()
  fact = c["text"]
  shit = 'Binary to Text'
  em = discord.Embed(color=0xff0000)
  AandQ = f'The binary entered converted to Text is: \n\n{str(fact)}'
  em.add_field(name=shit, value=AandQ)
  await loading_message.delete()
  await ctx.send(embed=em)

@client.command(aliases=["b642t", "d_b64", "d_base64"])
async def b64_2txt(ctx, *, ToTextBase64):
  loading_message = await ctx.send(embed=please_wait_emb)
  r = requests.get('https://some-random-api.ml/base64?decode=' + ToTextBase64)
  c = r.json()
  fact = c["text"]
  shit = 'Base64 to Text'
  em = discord.Embed(color=0xff0000)
  AandQ = f'Base64 entered converted to Text is: \n\n{str(fact)}'
  em.add_field(name=shit, value=AandQ)
  await loading_message.delete()
  await ctx.send(embed=em)

@client.command(alieases=["guess-age"])
async def guessage(ctx, *, nameToSearch):
  loading_message = await ctx.send(embed=please_wait_emb)
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
  
  guessed_age_info = f"""[+] Name: {name}
[+] Age: {age}
[+] Count: {count}"""

  await loading_message.delete()
  await ctx.send("```" + guessed_age_info + "```")

@client.command()
async def monstor(ctx):
  loading_message = await ctx.send(embed=please_wait_emb)
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

@client.command()
async def cleanuri(ctx, *, websiteurl):
  loading_message = await ctx.send(embed=please_wait_emb)
  url = 'https://cleanuri.com/api/v1/shorten'
  myobj = {'url': f'{websiteurl}'}  
  r = requests.post(url, data = myobj).json()
  shorten_url = r['result_url']
  em = discord.Embed(color=0xff0000)
  em.add_field(name="Shortened Link", value=shorten_url, inline=False)
  await loading_message.delete()
  await ctx.send(embed=em)

@client.command(aliases=["generate-pwd", "gen-pwd", "generate-password", "gen-password"])
async def genpwd(ctx, *, numberofcharacters):
  loading_message = await ctx.send(embed=please_wait_emb)
  url = f"https://passwordinator.herokuapp.com/generate?num=true&char=true&caps=true&len={numberofcharacters}"
  r = requests.get(url)
  c = r.json()
  em = discord.Embed(color=0xff0000)
  em.add_field(name="a Secure Password", value=c['data'], inline=False)
  await loading_message.delete()
  await ctx.send(embed=em)

@client.command()
async def advice(ctx):
  loading_message = await ctx.send(embed=please_wait_emb)
  r = requests.get("https://api.adviceslip.com/advice").json()
  c = r['slip']['advice']
  await loading_message.delete()
  await ctx.send(f"```{c}```")

@client.command(aliases=["chuck-norris-joke", "chuck-joke"])
async def chuckjoke(ctx):
  loading_message = await ctx.send(embed=please_wait_emb)
  url = f"https://api.chucknorris.io/jokes/random"
  r = requests.get(url).json()
  joke = r['value']
  thumb = r['icon_url']

  embed = discord.Embed(color=0xff0000)
  embed.add_field(name="a Chuck Norris Joke", value=joke, inline=False)
  embed.set_thumbnail(url=thumb)
  await loading_message.delete()
  await ctx.send(embed=embed)

@commands.has_permissions(kick_members=True)
@client.command(aliases=["changenickname", "change-nickname", "change-nick"])
async def cnick(ctx, member: discord.Member, *, nick):
  loading_message = await ctx.send(embed=please_wait_emb)
  await member.edit(nick=nick)
  await loading_message.delete()
  await ctx.send(f'Nickname of {member.mention} has been changed - requested by {ctx.author.mention}')

@client.command()
async def poll(ctx, *, message):
  loading_message = await ctx.send(embed=please_wait_emb)
  emb = discord.Embed(title=" POLL ", description=f'{message}', color=0xff0000)
  await loading_message.delete()
  msg = await ctx.send(embed=emb)
  await msg.add_reaction('👍')
  await msg.add_reaction('👎')

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
    # await ctx.send(f"{member.mention} was muted by {ctx.author.mention} \nReason: {reason}")
    em = discord.Embed()
    em.add_field(name=f"✅ {member} was muted", value=f"by {ctx.author.mention}")
    await loading_message.delete()
    await ctx.send(embed=em)
  else:
    await member.add_roles(role)
    # await ctx.send(f"{member.mention} was muted by {ctx.author.mention} \nReason: {reason}")
    em = discord.Embed()
    em.add_field(name=f"✅ {member} was muted", value=f"by {ctx.author.mention}")
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
    # await ctx.send(f"{member.mention} was unmuted by {ctx.author.mention}")
    em = discord.Embed(color=0xff0000)
    em.add_field(name=f"✅ {member} was unmuted", value=f"by {ctx.author.mention}")
    await loading_message.delete()
    await ctx.send(embed=em)
  except Exception as e:
    em = discord.Embed(color=0xff0000)
    em.add_field(name=f"⛔ An Error has occured", value=f"{e}")
    # await ctx.send()
    await loading_message.delete()
    await ctx.send(embed=em)


@client.command()
async def daddy(ctx):
  loading_message = await ctx.send(embed=please_wait_emb)
  await ctx.send(f'{ctx.author.mention}a gay fag caught in 4k requesting for dick pics!')
  r = requests.get("https://nekos.life/api/v2/img/Random_hentai_gif")
  res = r.json()
  em = discord.Embed(color=0xff0000)
  em.set_image(url=res['url'])
  await loading_message.delete()
  await ctx.send(embed=em)
  await ctx.send(f'{ctx.author.mention} my dear mate, go fap for this! you will never get dick pics!')

@client.command()
async def slap(ctx, user: discord.Member, *, reason):
  await ctx.send(f'{user.mention} is being slapped by {ctx.author.mention} \nReason: {reason}')

@client.command(aliases=["clearscreennodelete", "clear-screen-no-delete", "clearscreen"])
async def csnd(ctx):
  await ctx.send(f'Clearing some screen space - \n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\nRequested by {ctx.author.mention}')

@client.command()
async def afk(ctx, *, message):
  loading_message = await ctx.send(embed=please_wait_emb)
  member = ctx.author
  await member.edit(nick=f'[AFK] {member} {message}')
  await loading_message.delete()
  await ctx.send(f"{member.mention} changed to AFK {message}")

@client.command(aliases=["about"])
async def info(ctx):
  loading_message = await ctx.send(embed=please_wait_emb)
  em = discord.Embed(title="Your Bot", color=0xFF0000)
  # em.set_thumbnail(url="https://cdn.discordapp.com/avatars/858303945167208448/a1351d02002332f7f614979f9b5326ba.png?size=4096")
  em.set_thumbnail(url=bot_info_cmnd_thumbnail_link)
  em.add_field(name="Version", value=f'{bot_current_version}')
  em.add_field(name="Creator", value=f'{bot_creator_name}')
  em.add_field(name="Servers", value=f'{len(client.guilds)}')
  em.add_field(name="Link", value=f'https://github.com/hirusha-adi/Discord-Bot')
  await loading_message.delete()
  await ctx.send(embed=em)

@commands.has_permissions(manage_channels=True)
@client.command()
async def slowmode(ctx, seconds: int):
  loading_message = await ctx.send(embed=please_wait_emb)
  await ctx.channel.edit(slowmode_delay = seconds)
  # await ctx.send(f'Set the slowmode delay in this channel to {seconds} seconds by {ctx.author.mention}')
  if seconds == 1:
    sec = "second"
  else:
    sec = "seconds"
  embed=discord.Embed(color=0xff0000)
  embed.add_field(name="Channel Settings - Slowmode", value=f"**+ Set slow mode to:** {seconds} {sec}\n**+ By:** {ctx.author.mention}", inline=False)
  await loading_message.delete()
  await ctx.send(embed=embed)

@commands.has_permissions(manage_messages=True)
@client.command(aliases=["new-emoji", "emojinew", "newemojis", "add-emoji", "addemoji"])
async def newemoji(ctx, name, link, filetyple):
  loading_message = await ctx.send(embed=please_wait_emb)
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
    em.add_field(name="Name", value=f'{name}')
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

@commands.has_permissions(administrator=True)
@client.command()
async def make_server_new_roles(ctx):
  loading_message = await ctx.send(embed=please_wait_emb)
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
  embed.add_field(name="Roles in the server", value=f'{all_roles_in_server}', inline=False)
  embed.set_footer(text=datetime.datetime.now())
  await loading_message.delete()
  await ctx.send(embed=embed)

@client.command()
async def howdie(ctx, member: discord.Member = "none"):
  loading_message = await ctx.send(embed=please_wait_emb)
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
    embed=discord.Embed(color=0xff0000)
    embed.add_field(name=f"{ctx.author.name}", value=f"{random.choice(dying_methods)}.", inline=False)
    await loading_message.delete()
    await ctx.send(embed=embed)
    # await ctx.send(f'{ctx.author.mention} {random.choice(dying_methods)}.')
  else:
    embed=discord.Embed(color=0xff0000)
    embed.add_field(name=f"{member.name}", value=f"{random.choice(dying_methods)}.", inline=False)
    await loading_message.delete()
    await ctx.send(embed=embed)
    # await ctx.send(f'{member.mention} {random.choice(dying_methods)}.')

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
    await loading_message.delete()
    await ctx.send(file=discord.File(f'igtemp.jpg'))
    await ctx.send(f"Profile link: https://instagram.com/{ig_uname}")
    try:
      os.system(f"rm igtemp.jpg")
    except:
      os.remove(f'{ig_uname}')
  except Exception as e:
    await ctx.send(f"Error: {e}")
  
@client.command()
async def ascii(ctx, *, text):
  loading_message = await ctx.send(embed=please_wait_emb)
  ascii_art_creating_function_get = ascii_art_func(text)
  await loading_message.delete()
  await ctx.send(f'``` {ascii_art_creating_function_get} ```')

@client.command(aliases=["propose"])
async def howpropose(ctx, *, name="your crush/gf"):
  loading_message = await ctx.send(embed=please_wait_emb)
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


@client.command()
async def chatbot(ctx, command="main"):
  loading_message = await ctx.send(embed=please_wait_emb)
  old_wl = ("1", "1.0", "one", "first", "olddays")
  bp = bot_prefix
  if command in old_wl:
    emh1 = discord.Embed(title=f'Chat Bot', description=f'Lonely Bot v2.0', color=0xFF0000)
    emh1.set_thumbnail(url=r"https://cdn.discordapp.com/attachments/863706778743341076/874579616210239488/Avatar.png")
    emh1.add_field(name=f'NOTICE', value=f'This project is now seperate from this!', inline=True)
    emh1.add_field(name=f'Invite Link', value=f'https://discord.com/api/oauth2/authorize?client_id=863712001724776488&permissions=139653925952&scope=bot', inline=True)
    await loading_message.delete()
    await ctx.send(embed=emh1)

  elif command == "main":
    emh2 = discord.Embed(title=f'Chat Bot', description=f'Setup', color=0xFF0000)
    emh2.set_thumbnail(url=r"https://cdn.discordapp.com/attachments/863706778743341076/874579616210239488/Avatar.png")
    emh2.add_field(name=f'How to start?', value=f'DM the Channel ID to `ZeaCeR#5641`', inline=True)
    emh2.add_field(name=f'Help', value=f'use `{bp}chatbot help` to Help', inline=True)
    await loading_message.delete()
    await ctx.send(embed=emh2)

  elif command == "history":
    emh3 = discord.Embed(title=f'Chat Bot', description=f'Chatbot History', color=0xFF0000)
    emh3.set_thumbnail(url=r"https://cdn.discordapp.com/attachments/863706778743341076/874579616210239488/Avatar.png")
    emh3.add_field(name=f'History', value=f'First Started as `Lonely Bot#7613`', inline=True)
    await loading_message.delete()
    await ctx.send(embed=emh3)
  
  elif command == "list":
    emh4 = discord.Embed(title=f'Chat Bot - Channel List', description=f'all activated channels', color=0xFF0000)
    emh4.set_thumbnail(url=r"https://cdn.discordapp.com/attachments/863706778743341076/874579616210239488/Avatar.png")
    emh4.add_field(name=f'List', value='863706778743341076 \n874577378746175508\n', inline=True)
    await loading_message.delete()
    await ctx.send(embed=emh4)

  elif command == "help":
    emh2 = discord.Embed(title=f'Chat Bot - Help', description=f'Setup', color=0xFF0000)
    emh2.set_thumbnail(url=r"https://cdn.discordapp.com/attachments/863706778743341076/874579616210239488/Avatar.png")
    emh2.add_field(name=f'History', value=f'`{bp}chatbot history` to see the beginning of the chatbot project', inline=True)
    emh2.add_field(name=f'List Active Channels', value=f'`{bp}chatbot help` to see the list of active channels of chatbot', inline=True)
    emh2.add_field(name=f'Old Days', value=f'`{bp}chatbot olddays`', inline=True)
    await loading_message.delete()
    await ctx.send(embed=emh2)

@client.command()
async def google(ctx, *, whatToSearch):
  loading_message = await ctx.send(embed=please_wait_emb)
  embed=discord.Embed(title="Google Search", description="Link to query", color=0xFF0000)
  embed.add_field(name="Name", value=f"https://www.google.com/search?q={whatToSearch}", inline=True)
  await loading_message.delete()
  await ctx.send(embed=embed)

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
    await loading_message.delete()
    await ctx.send(f"Error: {e}")

@client.command()
async def addrole(ctx, member: discord.Member, *, role):
  loading_message = await ctx.send(embed=please_wait_emb)
  """Add a role to a user (case sensitive)"""
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

@client.command()
async def removerole(ctx, member: discord.Member, *, role):
    loading_message = await ctx.send(embed=please_wait_emb)
    """Remove a role (case sensitive)"""
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

@client.command()
async def slots(ctx):
  loading_message = await ctx.send(embed=please_wait_emb)
  responses = ["🍋" , "🍊", "🍉", ":seven:", ]
  embed=discord.Embed(title="🎰 Slot Machine 🎰", description=random.choice(responses) + random.choice(responses) + random.choice(responses), color=0xFF0000)
  embed.set_footer(text="You need triple 7's to win.")
  await loading_message.delete()
  await ctx.send(embed=embed)


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
{bp}guessage Name -> will gues the age of the name, show the number of people with the same name"""

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
    em3.add_field(name=f'{bp}guildicon', value=f'`{bp}serverinfo` - Current server icon', inline=True)
    em3.add_field(name=f'{bp}accdate', value=f'`{bp}accdate [@user]` - See the account creation date', inline=True)
    em3.add_field(name=f'{bp}userinfo', value=f'`{bp}userinfo [@user]` - See the public account information', inline=True)
    em3.add_field(name=f'{bp}ig_pfp', value=f'`{bp}ig_pfp [@ig_username]` - Get the Instagram profile picture of anyone!', inline=True)
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

    await loading_message.delete()
    await ctx.send(embed=em5)
    # await ctx.send(embed=em7)

  elif category.lower() in images_wl:
    em6 = discord.Embed(title=f'Images', description=f'use >Help [category]', color=0xff0000)
    em6.set_thumbnail(url=bot_info_cmnd_thumbnail_link)
    em6.add_field(name=f'{bp}feed', value=f'`{bp}feed [@user]` - Send an Image/GIF', inline=True)
    em6.add_field(name=f'{bp}tickle', value=f'`{bp}tickle [@user]` - Send an Image/GIF', inline=True)
    em6.add_field(name=f'{bp}hit', value=f'`{bp}hit [@user]` - Send an Image/GIF', inline=True)
    em6.add_field(name=f'{bp}hug', value=f'`{bp}hug [@user]` - Send an Image/GIF', inline=True)
    em6.add_field(name=f'{bp}smug', value=f'`{bp}smug [@user]` - Send an Image/GIF', inline=True)
    em6.add_field(name=f'{bp}pat', value=f'`{bp}pat [@user]` - Send an Image/GIF', inline=True)
    em6.add_field(name=f'{bp}kiss', value=f'`{bp}kiss [@user]` - Send an Image/GIF', inline=True)
    em6.add_field(name=f'{bp}monstor', value=f'`{bp}monstor` - Send an Image/GIF', inline=True)
    em6.add_field(name=f'{bp}wink', value=f'`{bp}wink` - Send an Image/GIF', inline=True)
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
    em9.add_field(name=f'{bp}d_b64', value=f'`{bp}d_binary [b64]` - Convert From Base64 to text', inline=True)
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
    await loading_message.delete()
    await ctx.send(embed=em11)
  
  elif category.lower() in animals_wl:
    em12 = discord.Embed(title=f'Animals', description=f'use >Help [category]', color=0xff0000)
    em12.set_thumbnail(url=bot_info_cmnd_thumbnail_link)
    em12.add_field(name=f'{bp}meme', value=f'`{bp}meme` - a Good Funni Meme', inline=True)
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
    await loading_message.delete()
    await ctx.send(embed=em12)






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

@client.event
async def on_message(message):
  bp = bot_prefix
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
  
  await client.process_commands(message)



keep_alive()

client.run(token)