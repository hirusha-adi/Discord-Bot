from keep_alive import keep_alive

import discord
from discord.ext import commands
import os
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

botconfigdata = json.load(open("config.json", "r"))
bot_prefix = botconfigdata["msg-prefix"]

client = commands.Bot(command_prefix = bot_prefix)

token = os.environ['TOKEN']

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

def get_quote():
    r = requests.get("https://zenquotes.io/api/random")
    json_data = json.loads(r.text)
    quote = json_data[0]['q'] + " - " + json_data[0]['a']
    return(quote)

def get_covid_info():
  r = requests.get('https://coronavirus-19-api.herokuapp.com/all') 
  data = r.json()
  covid_data = f'[+] Confirmed Cases : {data["cases"]} \n[+] Deaths : {data["deaths"]} \n[+] Recovered : {data["recovered"]}'
  return covid_data

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
    bp = bot_prefix
    fake_help = f"""{bp}fake high -> Generate a fake profile with high amount of  information
{bp}fake name -> create a fake name
{bp} fake dob -> create a fake Date of Birth
{bp}fake addr -> create a fake address
{bp}fake job -> create a fake job
{bp}fake color -> create a fake color
{bp}fake zipcode -> create a fake zipcode
{bp}fake city -> create a fake city
{bp}fake lp -> create a fake Lisence Number Plate
{bp}fake bban -> create a random Basic Bank Account Number
{bp}fake iban -> create a random International Bank Account Number
{bp}fake bs -> create a fake BS / Degree
{bp}fake cc -> create credit card details ( not valid )
{bp}fake pno -> create a fake phone number
{bp}fake cemail -> create a company email number
{bp}fake cp -> create a random catch phrase
{bp}fake ssn -> create a fake ssn number
    """
    return fake_help
  
  else:
    return "[-] Please enter a valid option, type '>fake help' for help"

def ipinfoshit(ipfromuser):
    r = requests.get('http://ip-api.com/json/' + str(ipfromuser)) # include the ip
    data = r.json()
    ipinfo = f'\n[+] Status: {data["status"]} \n[+] Country: {data["country"]} \n[+] Country Code: {data["countryCode"]} \n[+] Region: {data["region"]} \n[+] Region Name: {data["regionName"]} \n[+] City: {data["city"]} \n[+] ZIP: {data["zip"]} \n[+] Latitude: {data["lat"]} \n[+] Longitude: {data["lon"]} \n[+] TimeZone: {data["timezone"]} \n[+] ISP: {data["isp"]} \n[+] Organization: {data["org"]} \n[+] ASN: {data["as"]} \n[+] Query: {data["query"]} \n'
    return ipinfo








# https://www.youtube.com/watch?v=yrHbGhem6I4





















bot_status_message = botconfigdata["bot-status-message"]

@client.event
async def on_ready():
  await client.change_presence(status=discord.Status.idle, activity=discord.Game(bot_status_message))
  print('Bot is ready!')

@client.event
async def on_member_join(member):
    print(f'{member} has joined a server')

@client.event
async def on_member_remove(member):
    print(f'{member} has left the server')

# ctx is for 'context'
@client.command() 
async def ping(ctx):
    try:
        await ctx.send(f'```[+] Ping: {round(client.latency * 1000)}ms```')
    except Exception as e:
        await ctx.send("```" + e + "```")

@client.command()
@commands.has_permissions(manage_messages=True)
async def clear(ctx, amount=5):
    await ctx.channel.purge(limit=amount)

@client.command(aliases=["8ball", "eightball"])
async def _8ball(ctx, *, question):
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
    await ctx.send(embed=embed)


@commands.has_permissions(kick_members=True)
@client.command()
async def kick(ctx, member : discord.Member, *, reason=None): # call the member as in member object from discord module
    try:
        await member.kick(reason=reason)
        ban = discord.Embed(title=f":boom: Kicked {member.name}!", description=f"Reason: {reason}\nBy: {ctx.author.mention}")
        await ctx.channel.send(embed=ban)
        await member.send(embed=ban)
    except Exception as e:
        await ctx.send("```" + str(e) + "```")

@commands.has_permissions(ban_members=True)
@client.command()
async def ban(ctx, user: discord.Member, *, reason="No reason provided"):
    try:
        await user.ban(reason=reason)
        ban = discord.Embed(title=f":boom: Banned {user.name}!", description=f"Reason: {reason}\nBy: {ctx.author.mention}")
        await ctx.channel.send(embed=ban)
        await user.send(embed=ban)
    except Exception as e:
        await ctx.send("```" + str(e) + "```")

@client.command()
async def unban(ctx, *, member):
    banned_users = await ctx.guild.bans() # a named tuple containing user object and the reason for ban
    member_name, member_discriminator = member.split("#")

    for ban_entry in banned_users:
        user = ban_entry.user

        if (user.name, user.discriminator) == (member_name, member_discriminator):
            await ctx.guild.unban(user)
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
    await ctx.send("```" + get_quote() + "```")

@client.command()
async def fake(ctx, *, fake_mode):
    await ctx.send("```" + FAKE_PROFILE(fake_mode) + "```")

@client.command()
async def ip(ctx, *, ip_from_user):
    await ctx.send("```" + ipinfoshit(ip_from_user) + "```")

@client.command()
async def mfp(ctx, *, how_many):
    fake_how_many = int(how_many)
    if fake_how_many <= 80:
      await ctx.send("```Sending " + str(how_many) + " Fake Profiles```")
      for i in range(fake_how_many):
          await ctx.send("```" + CREATE_FAKE_PROFILES_MANY() + "```")
    else:
      await ctx.send("```Please use a number below 80```")

@client.command()
async def pervert(ctx):
    ctx.send("```" + show_pervert_text() + "```")

@client.command()
async def nitro(ctx, *, number_of_times):
    if int(number_of_times) <= 20:
        await ctx.send("```Sending " + str(number_of_times) + " Random Nitro Codes!```")
        for iteration, x in enumerate(range(int(number_of_times))):
            await ctx.send(give_nice_codes())
            time.sleep(0.5)
    else:
        ctx.send("```Please enter a value less than 20```")

@client.command()
async def spam(ctx, number_of_times_to_spam, *, message):
    await ctx.send("```Spaming " + str(number_of_times_to_spam) + " times!```")
    for iteration, x in enumerate(range(int(number_of_times_to_spam))):
        await ctx.send(message)
        time.sleep(0.5)

@client.command()
async def spamsecretzeacergarca(ctx, *, number_of_times_spam_secret):
    await ctx.send("```Spaming " + str(number_of_times_spam_secret) + " times!```")
    for iteration, x in enumerate(range(int(number_of_times_spam_secret))):
        await ctx.send("@everyone @here lol")
        time.sleep(0.5)

@client.command()
async def bored(ctx):
    await ctx.send("```" + bored_activity() + "```")

@client.command()
async def color(ctx):
    await ctx.send("```" + give_rand_color() + "```")

@client.command()
async def btc(ctx):
    await ctx.send("```" + get_bitcoin_status() + "```")

@client.command()
async def covid(ctx):
    await ctx.send("```" + get_covid_info() + "```")

@client.command()
async def wiki(ctx, *, word_to_search):
    await ctx.send("```" + search_wikipedia(word_to_search) + "```")

@client.command()
async def tinyurl(ctx, *, link):
    r = requests.get(f'http://tinyurl.com/api-create.php?url={link}').text
    em = discord.Embed()
    em.add_field(name="Shortened Link", value=r, inline=False)
    await ctx.send(embed=em)

@client.command()
async def dadjoke(ctx):
  headers = {
    "Accept": "application/json"
  }
  async with aiohttp.ClientSession()as session:
    async with session.get("https://icanhazdadjoke.com", headers=headers) as req:
      r = await req.json()
  await ctx.send("```" + r["joke"] + "```")

@client.command()
async def joke(ctx):
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
  await ctx.send("```" + joke + "```")

@client.command()
async def iconserver(ctx):
  em = discord.Embed(title=ctx.guild.name)
  em.set_image(url=ctx.guild.icon_url)
  await ctx.send(embed=em)

@client.command()
async def mac(ctx, mac):
  r = requests.get('http://api.macvendors.com/' + mac)
  em = discord.Embed(title='MAC Lookup Result', description=r.text, colour=0xDEADBF)
  em.set_author(name='MAC Finder', icon_url='https://regmedia.co.uk/2016/09/22/wifi_icon_shutterstock.jpg?x=1200&y=794')
  await ctx.send(embed=em)

@client.command()
async def bitcoin(ctx):
  r = requests.get('https://min-api.cryptocompare.com/data/price?fsym=BTC&tsyms=USD,EUR')
  r = r.json()
  usd = r['USD']
  eur = r['EUR']
  em = discord.Embed(description=f'USD: `{str(usd)}$`\nEUR: `{str(eur)}€`')
  em.set_author(name='Bitcoin', icon_url='https://cdn.pixabay.com/photo/2013/12/08/12/12/bitcoin-225079_960_720.png')
  await ctx.send(embed=em)

@client.command()
async def eth(ctx):
  r = requests.get('https://min-api.cryptocompare.com/data/price?fsym=ETH&tsyms=USD,EUR')
  r = r.json()
  usd = r['USD']
  eur = r['EUR']
  em = discord.Embed(description=f'USD: `{str(usd)}$`\nEUR: `{str(eur)}€`')
  em.set_author(name='Ethereum', icon_url='https://cdn.discordapp.com/attachments/271256875205525504/374282740218200064/2000px-Ethereum_logo.png')
  await ctx.send(embed=em)

@client.command(aliases=['wouldyourather', 'would-you-rather', 'wyrq'])
async def wyr(ctx):
  r = requests.get('https://www.conversationstarters.com/wyrqlist.php').text
  soup = BeautifulSoup(r, 'html.parser')
  qa = soup.find(id='qa').text
  qor = soup.find(id='qor').text
  qb = soup.find(id='qb').text
  em = discord.Embed(description=f'{qa}\n{qor}\n{qb}')
  await ctx.send(embed=em)

@client.command()
async def hastebin(ctx, *, message):
  r = requests.post("https://hastebin.com/documents", data=message).json()
  await ctx.send(f"<https://hastebin.com/{r['key']}>")

@client.command()
async def ascii(ctx, *, text):
  r = requests.get(f'http://artii.herokuapp.com/make?text={urllib.parse.quote_plus(text)}').text
  if len('```'+r+'```') > 2000:
    return
  await ctx.send(f"```{r}```")

@client.command()
async def anal(ctx):
  r = requests.get("https://nekos.life/api/v2/img/anal")
  res = r.json()
  em = discord.Embed()
  em.set_image(url=res['url'])
  await ctx.send(embed=em)

@client.command()
async def erofeet(ctx):
  r = requests.get("https://nekos.life/api/v2/img/erofeet")
  res = r.json()
  em = discord.Embed()
  em.set_image(url=res['url'])
  await ctx.send(embed=em)

@client.command()
async def feet(ctx):
  r = requests.get("https://nekos.life/api/v2/img/feetg")
  res = r.json()
  em = discord.Embed()
  em.set_image(url=res['url'])
  await ctx.send(embed=em)

@client.command()
async def hentai(ctx):
  r = requests.get("https://nekos.life/api/v2/img/Random_hentai_gif")
  res = r.json()
  em = discord.Embed()
  em.set_image(url=res['url'])
  await ctx.send(embed=em)

@client.command()
async def boobs(ctx):
  r = requests.get("https://nekos.life/api/v2/img/boobs")
  res = r.json()
  em = discord.Embed()
  em.set_image(url=res['url'])
  await ctx.send(embed=em)

@client.command()
async def tits(ctx):
  r = requests.get("https://nekos.life/api/v2/img/tits")
  res = r.json()
  em = discord.Embed()
  em.set_image(url=res['url'])
  await ctx.send(embed=em)

@client.command()
async def blowjob(ctx):
  r = requests.get("https://nekos.life/api/v2/img/blowjob")
  res = r.json()
  em = discord.Embed()
  em.set_image(url=res['url'])
  await ctx.send(embed=em)

@client.command()
async def lewd(ctx):
  r = requests.get("https://nekos.life/api/v2/img/nsfw_neko_gif")
  res = r.json()
  em = discord.Embed()
  em.set_image(url=res['url'])
  await ctx.send(embed=em)

@client.command()
async def lesbian(ctx):
  r = requests.get("https://nekos.life/api/v2/img/les")
  res = r.json()
  em = discord.Embed()
  em.set_image(url=res['url'])
  await ctx.send(embed=em)

@client.command()
async def feed(ctx, user: discord.Member):
  r = requests.get("https://nekos.life/api/v2/img/feed")
  res = r.json()
  em = discord.Embed(description=user.mention)
  em.set_image(url=res['url'])
  await ctx.send(embed=em)

@client.command()
async def tickle(ctx, user: discord.Member):
  r = requests.get("https://nekos.life/api/v2/img/tickle")
  res = r.json()
  em = discord.Embed(description=user.mention)
  em.set_image(url=res['url'])
  await ctx.send(embed=em)

@client.command()
async def slap(ctx, user: discord.Member):
  r = requests.get("https://nekos.life/api/v2/img/slap")
  res = r.json()
  em = discord.Embed(description=user.mention)
  em.set_image(url=res['url'])
  await ctx.send(embed=em)

@client.command()
async def hug(ctx, user: discord.Member):
  r = requests.get("https://nekos.life/api/v2/img/hug")
  res = r.json()
  em = discord.Embed(description=user.mention)
  em.set_image(url=res['url'])
  await ctx.send(embed=em)

@client.command()
async def smug(ctx, user: discord.Member):
  r = requests.get("https://nekos.life/api/v2/img/smug")
  res = r.json()
  em = discord.Embed(description=user.mention)
  em.set_image(url=res['url'])
  await ctx.send(embed=em)

@client.command()
async def pat(ctx, user: discord.Member):
  r = requests.get("https://nekos.life/api/v2/img/pat")
  res = r.json()
  em = discord.Embed(description=user.mention)
  em.set_image(url=res['url'])
  await ctx.send(embed=em)

@client.command()
async def kiss(ctx, user: discord.Member):
  r = requests.get("https://nekos.life/api/v2/img/kiss")
  res = r.json()
  em = discord.Embed(description=user.mention)
  em.set_image(url=res['url'])
  await ctx.send(embed=em)

@client.command()
async def reverse(ctx, *, message):
  message = message[::-1]
  await ctx.send(message)

@client.command()
async def shrug(ctx):
    shrug = r'¯\_(ツ)_/¯'
    await ctx.send(shrug)

@client.command()
async def lenny(ctx):
    lenny = '( ͡° ͜ʖ ͡°)'
    await ctx.send(lenny)

@client.command()
async def tableflip(ctx):
    tableflip = '(╯°□°）╯︵ ┻━┻'
    await ctx.send(tableflip)

@client.command()
async def unflip(ctx):
    unflip = '┬─┬ ノ( ゜-゜ノ)'
    await ctx.send(unflip)

@client.command()
async def bold(ctx, *, message):
    await ctx.send('**'+message+'**')

@client.command()
async def secret(ctx, *, message):
    await ctx.send('||'+message+'||')

@client.command()
async def xmr(ctx):
  r = requests.get("https://min-api.cryptocompare.com/data/price?fsym=XMR&tsyms=USD,EUR")
  NegroPuket = r.json()
  eur = NegroPuket['EUR']
  usd = NegroPuket['USD']
  embedic = discord.Embed(description=f'EUR: `{str(eur)}€`\nUSD: `{str(usd)}$`')
  embedic.set_author(name='Monero', icon_url='https://cdn.freebiesupply.com/logos/large/2x/monero-logo-png-transparent.png')
  await ctx.send(embed=embedic)

@client.command()
async def doge(ctx):
  r = requests.get("https://min-api.cryptocompare.com/data/price?fsym=DOGE&tsyms=USD,EUR")
  NegroPuketDOGE = r.json()
  eur = NegroPuketDOGE['EUR']
  usd = NegroPuketDOGE['USD']
  embedic = discord.Embed(description=f'EUR: `{str(eur)}€`\nUSD: `{str(usd)}$`')
  embedic.set_author(name='Dogecoin', icon_url='https://cdn.coindoo.com/2019/10/dogecoin-logo.png')
  await ctx.send(embed=embedic)


@client.command()
async def xrp(ctx):
  r = requests.get("https://min-api.cryptocompare.com/data/price?fsym=XRP&tsyms=USD,EUR")
  kekistan = r.json()
  eur = kekistan['EUR']
  usd = kekistan['USD']
  embedic = discord.Embed(description=f'EUR: `{str(eur)}€`\nUSD: `{str(usd)}$`')
  embedic.set_author(name='Ripple', icon_url='https://cdn.freebiesupply.com/logos/large/2x/ripple-2-logo-png-transparent.png')
  await ctx.send(embed=embedic)

@client.command()
async def goodnight(ctx):
  night = '✩⋆｡ ˚ᎶᎾᎾⅅ ℕᏐᎶℍᎢ⋆｡˚✩'
  await ctx.send(night)

@client.command()
async def smile(ctx):
  smile = '˙ ͜ʟ˙'
  await ctx.send(smile)

@client.command()
async def iloveu(ctx):
  love = '(๑′ᴗ‵๑)Ｉ Lᵒᵛᵉᵧₒᵤ♥'
  await ctx.send(love)

@client.command()
async def sword(ctx):
  sword = 'ס₪₪₪₪§|(Ξ≥≤≥≤≥≤ΞΞΞΞΞΞΞΞΞΞ>'
  await ctx.send(sword)

@client.command()
async def what(ctx):
  what = '( ʘ̆ ╭͜ʖ╮ ʘ̆ )'
  await ctx.send(what)

@client.command()
async def fuckyou(ctx):
  middlef = '╭∩╮(･◡･)╭∩╮'
  await ctx.send(middlef)

@client.command(aliases=['dong', 'penis', 'pp', 'psize'])
async def dick(ctx, *, user: discord.User = None):
  if user is None:
    user = ctx.author
    size = random.randint(2, 20)
    em = discord.Embed(title=f"{user}'s Dick size:", description=f"{size} Inches", colour=0x0000)
    await ctx.send(embed=em)

@client.command()
async def panda(ctx):
  r = requests.get("https://some-random-api.ml/img/panda").json()
  embed = discord.Embed(color=0x0000)
  embed.set_author(name="a Panda.", icon_url="https://cdn.freebiesupply.com/logos/large/2x/panda-7-logo-png-transparent.png") 
  embed.set_image(url=str(r["link"]))
  await ctx.send(embed=embed)    

@client.command(aliases=["lol"])
async def meme(ctx):
  r = requests.get("https://some-random-api.ml/meme").json()
  embed = discord.Embed(color=0x0000)
  embed.set_author(name="a Meme.", icon_url="https://freepngimg.com/thumb/internet_meme/3-2-troll-face-meme-png-thumb.png") 
  try:
    caption = str(r["caption"])
    embed.add_field(name="Just a random Meme", value=caption)
  except:
    pass
  embed.set_image(url=str(r["image"]))
  await ctx.send(embed=embed)

@client.command()
async def dog(ctx):
  r = requests.get("https://some-random-api.ml/img/dog").json()
  embed = discord.Embed(color=0x0000)
  embed.set_author(name="a Dog." , icon_url="https://t4.ftcdn.net/jpg/03/66/78/13/360_F_366781345_oEr9wc8yWhYRPZe6CGyFWS6QolZIf2fJ.jpg") 
  embed.set_image(url=str(r["link"]))
  await ctx.send(embed=embed)    

@client.command()
async def cat(ctx):
  r = requests.get("https://some-random-api.ml/img/cat").json()
  embed = discord.Embed(color=0x0000)
  embed.set_author(name="a Cat.", icon_url="https://i.pinimg.com/736x/d6/0c/7e/d60c7e8983fdbd7c7a27fd42fb3d61ba.jpg") 
  embed.set_image(url=str(r["link"]))
  await ctx.send(embed=embed)   

@client.command(aliases=['pfp', 'avatar'])
async def av(ctx, *, user: discord.User = None):
  format = "gif"
  user = user or ctx.author
  if user.is_avatar_animated() != True:
    format = "png"
  avatar = user.avatar_url_as(format=format if format != "gif" else None)
  async with aiohttp.ClientSession() as session:
    async with session.get(str(avatar)) as resp:
      image = await resp.read()
  with io.BytesIO(image) as file:
      await ctx.send(file=discord.File(file, f"Avatar.{format}"))

@client.command(aliases=["guildinfo", "serverinfo"])
async def infoserver(ctx):
  date_format = "%a, %d %b %Y %I:%M %p"
  embed = discord.Embed(title=f"Server Info of {ctx.guild.name}:",
                            description=f"{ctx.guild.member_count} Members\n {len(ctx.guild.roles)} Roles\n {len(ctx.guild.text_channels)} Text-Channels\n {len(ctx.guild.voice_channels)} Voice-Channels\n {len(ctx.guild.categories)} Categories",
                            timestamp=datetime.datetime.utcnow(), color=0x0000)
  embed.add_field(name="Server created at", value=f"{ctx.guild.created_at.strftime(date_format)}")
  embed.add_field(name="Server Owner", value=f"<@{ctx.guild.owner_id}>")
  embed.add_field(name="Server Region", value=f"{ctx.guild.region}")
  embed.add_field(name="Server ID", value=f"{ctx.guild.id}")
  embed.add_field(name="Bots", value=len(list(filter(lambda m: m.bot, ctx.guild.members))))
  embed.add_field(name="Banned members", value=len(await ctx.guild.bans()))
  embed.add_field(name="Invites", value=len(await ctx.guild.invites()))
  embed.set_thumbnail(url=f"{ctx.guild.icon_url}")
  await ctx.send(embed=embed)


@client.command(aliases=["servericon"])
async def guildicon(ctx):
  embed = discord.Embed(color=0x0000)
  embed.set_author(name=ctx.guild.name, icon_url=ctx.guild.icon_url)   
  embed.set_image(url=ctx.guild.icon_url)
  await ctx.send(embed=embed)

@client.command(aliases=["account-creation-date", "account-date"])
async def accdate(ctx, *, user: discord.User = None):
  if user is None:
    user = ctx.author      
  date_format = "%a, %d %b %Y %I:%M %p"
  em = discord.Embed(description=user.mention)
  em.set_author(name=str(user), icon_url=user.avatar_url)
  em.set_thumbnail(url=user.avatar_url)
  em.add_field(name="Registered", value=user.created_at.strftime(date_format))
  return await ctx.send(embed=em)

@client.command(aliases=["userinfo", "uinfo", "user-info"])
async def whoareyou(ctx, target: Optional[discord.Member]):
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
  
  await ctx.send(embed=embed)



@client.command(aliases=["e_base64"])
async def e_b64(ctx, *, args):
  msg = base64.b64encode('{}'.format(args).encode('ascii'))
  enc = str(msg)
  enc = enc[2:len(enc)-1]
  await ctx.send("```" + str(enc) + "```")

@client.command()
async def e_md5(ctx, *, args):
  msg = hashlib.md5(args.encode())
  slpake =  msg.hexdigest()
  await ctx.send("```" + str(slpake) + "```")

@client.command()
async def e_sha1(ctx, *, args):
  msg = hashlib.sha1(args.encode())
  slpuka =  msg.hexdigest()
  await ctx.send("```" + str(slpuka) + "```")

@client.command()
async def e_sha224(ctx, *, args):
  msg = hashlib.sha3_224(args.encode())
  crnja =  msg.hexdigest()
  await ctx.send("```" + str(crnja) + "```")

@client.command()
async def e_sha512(ctx, *, args):
  msg = hashlib.sha3_512(args.encode())
  crnja =  msg.hexdigest()
  await ctx.send("```" + str(crnja) + "```")

@client.command(aliases=["leet"])
async def e_leet(ctx, *, args):
  encoded = args.replace('e', '3').replace('a', '4').replace('i', '!').replace('u', '|_|').replace('U', '|_|').replace('E', '3').replace('I', '!').replace('A', '4').replace('o','0').replace('O','0').replace('t','7').replace('T','7').replace('l','1').replace('L','1').replace('k','|<').replace('K','|<').replace('CK','X').replace('ck','x').replace('Ck','X').replace('cK','x')
  await ctx.send(f'```{encoded}```')

@client.command(aliases=["addition"])
async def add(ctx, number_1, number_2):
  ans = float(number_1) + float(number_2)
  em = discord.Embed(description=f"Question: {number_1} + {number_2}\n\nAnswer: {ans}")
  em.set_author(name="Addition")
  await ctx.send(embed=em)

@client.command(aliases=["substraction", "substract"])
async def subs(ctx, number_1, number_2):
  ans = float(number_1) - float(number_2)
  em = discord.Embed(description=f"Question: {number_1} - {number_2}\n\nAnswer: {ans}")
  em.set_author(name="Substraction")
  await ctx.send(embed=em)

@client.command(aliases=["multiplication", "multiply"])
async def mul(ctx, number_1, number_2):
  ans = float(number_1) * float(number_2)
  em = discord.Embed(description=f"Question: {number_1} x {number_2}\n\nAnswer: {ans}")
  em.set_author(name="Multiplication")
  await ctx.send(embed=em)

@client.command(aliases=["division", "divide"])
async def div(ctx, number_1, number_2):
  ans = float(number_1) / float(number_2)
  em = discord.Embed(description=f"Question: {number_1} / {number_2}\n\nAnswer: {ans}")
  em.set_author(name="Division")
  await ctx.send(embed=em)

@client.command(aliases=["echo"])
async def say(ctx, *, word_to_say):
  await ctx.message.delete()
  await ctx.send(str(word_to_say))

@client.command(aliases=["dog-facts", "dogfacts", "dog-fact"])
async def dogfact(ctx):
  r = requests.get('https://some-random-api.ml/facts/dog')
  c = r.json()
  fact = c["fact"]

  em = discord.Embed(title='Dog Fact', description=fact)
  em.set_author(name='Random Dog Fact', icon_url='https://post.medicalnewstoday.com/wp-content/uploads/sites/3/2020/02/322868_1100-800x825.jpg')
  await ctx.send(embed=em)

@client.command(aliases=["cat-facts", "catfacts", "cat-fact"])
async def catfact(ctx):
  r = requests.get('https://some-random-api.ml/facts/cat')
  c = r.json()
  fact = c["fact"]

  em = discord.Embed(title='Cat Fact', description=fact)
  em.set_author(name='Random Cat Fact', icon_url='https://i.guim.co.uk/img/media/26392d05302e02f7bf4eb143bb84c8097d09144b/446_167_3683_2210/master/3683.jpg?width=1200&height=1200&quality=85&auto=format&fit=crop&s=49ed3252c0b2ffb49cf8b508892e452d')
  await ctx.send(embed=em)

@client.command(aliases=["elephant-facts", "elephantfacts", "elephant-fact"])
async def elephantfact(ctx):
  r = requests.get('https://some-random-api.ml/facts/elephant')
  c = r.json()
  fact = c["fact"]

  em = discord.Embed(title='Elephant Fact', description=fact)
  em.set_author(name='Random Elephant Fact', icon_url='https://c402277.ssl.cf1.rackcdn.com/photos/14206/images/hero_small/WW187785.jpg?1576774644')
  await ctx.send(embed=em)

@client.command(aliases=["panda-facts", "pandafacts", "panda-fact"])
async def pandafact(ctx):
  r = requests.get('https://some-random-api.ml/facts/panda')
  c = r.json()
  fact = c["fact"]

  em = discord.Embed(title='Panda Fact', description=fact)
  em.set_author(name='Random panda Fact', icon_url='https://www.chinasage.info/imgs/BabyGiantPanda.jpg')
  await ctx.send(embed=em)

@client.command(aliases=["fox-facts", "foxfacts", "fox-fact"])
async def foxfact(ctx):
  r = requests.get('https://some-random-api.ml/facts/fox')
  c = r.json()
  fact = c["fact"]

  em = discord.Embed(title='Fox Fact', description=fact)
  em.set_author(name='Random Fox Fact', icon_url='https://images.wsj.net/im-355811?width=620&size=1.5')
  await ctx.send(embed=em)

@client.command(aliases=["bird-facts", "birdfacts", "bird-fact"])
async def birdfact(ctx):
  r = requests.get('https://some-random-api.ml/facts/bird')
  c = r.json()
  fact = c["fact"]

  em = discord.Embed(title='Bird Fact', description=fact)
  em.set_author(name='Random Bird Fact', icon_url='https://res.cloudinary.com/dk-find-out/image/upload/q_80,w_960,f_auto/DCTM_Penguin_UK_DK_AL526630_wkmzns.jpg')
  await ctx.send(embed=em)

@client.command(aliases=["koala-facts", "koalafacts", "koala-fact"])
async def koalafact(ctx):
  r = requests.get('https://some-random-api.ml/facts/koala')
  c = r.json()
  fact = c["fact"]
  em = discord.Embed(title='Koala Fact', description=fact)
  em.set_author(name='Random Koala Fact', icon_url='https://cdn.britannica.com/26/162626-050-3534626F/Koala.jpg')
  await ctx.send(embed=em)

@client.command(aliases=["red-panda", "red-panda-image", "red-panda-img"])
async def redpanda(ctx):
  r = requests.get('https://some-random-api.ml/img/red_panda')
  c = r.json()
  fact = c["link"]
  em = discord.Embed(title='a Red Panda', description=fact)
  em.set_author(name='a Random Red Panda', icon_url='https://cdn.vox-cdn.com/thumbor/erBglLkGU0eWF6c2PsEWHT2_TE0=/12x0:4907x3263/1400x1400/filters:focal(12x0:4907x3263):format(jpeg)/cdn.vox-cdn.com/uploads/chorus_image/image/49388585/16071828377_85109fdee4_o.0.0.jpg')
  await ctx.send(embed=em)

@client.command(aliases=["birds", "bird-image", "bird-img"])
async def bird(ctx):
  r = requests.get('https://some-random-api.ml/img/birb')
  c = r.json()
  fact = c["link"]
  em = discord.Embed(title='a Bird', description=fact)
  em.set_author(name='a Random Bird', icon_url='https://ichef.bbci.co.uk/news/976/cpsprodpb/67CF/production/_108857562_mediaitem108857561.jpg')
  await ctx.send(embed=em)


@client.command(aliases=["foxes", "fox-image", "fox-img"])
async def fox(ctx):
  r = requests.get('https://some-random-api.ml/img/fox')
  c = r.json()
  fact = c["link"]
  em = discord.Embed(title='a Fox', description=fact)
  em.set_author(name='a Random Fox', icon_url='https://images.unsplash.com/photo-1615602127413-459bdb48cf45?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=1000&q=80')
  await ctx.send(embed=em)

@client.command(aliases=["a-wink", "winks"])
async def wink(ctx):
  r = requests.get('https://some-random-api.ml/animu/wink')
  c = r.json()
  fact = c["link"]
  em = discord.Embed(title='a wink', description=fact)
  em.set_author(name='wink')
  await ctx.send(embed=em)

@client.command(aliases=["a-pikachu", "pikachuu"])
async def pikachu(ctx):
  r = requests.get('https://some-random-api.ml/img/pikachu')
  c = r.json()
  fact = c["link"]
  em = discord.Embed(title='a Pickachu', description=fact)
  em.set_author(name='a Random Pickachu')
  await ctx.send(embed=em)

@client.command(aliases=["gay-colors", "gay-colours"])
async def gay(ctx, *, messagelink):
  weblink = 'https://some-random-api.ml/canvas/gay?avatar=' + messagelink
  r = requests.get(weblink)
  em = discord.Embed(title='Gay Picture')
  em.set_author(name='a Gay colored Picture')
  em.set_image(url=weblink)
  await ctx.send(embed=em)

@client.command(aliases=["glass-colors", "glass-colours", "glassy-colors", "glassy-colours"])
async def glass(ctx, *, messagelink):
  weblink = 'https://some-random-api.ml/canvas/glass/?avatar=' + messagelink
  em = discord.Embed(title='Glassy Picture')
  em.set_author(name='a Glassy colored Picture')
  em.set_image(url=weblink)
  await ctx.send(embed=em)

@client.command(aliases=["wasted-colors", "wasted-colours", "wasted-image", "wasted-img"])
async def wasted(ctx, *, messagelink):
  weblink = 'https://some-random-api.ml/canvas/glass/?avatar=' + messagelink
  em = discord.Embed(title='a Wasted Picture')
  em.set_author(name='Wasted Picture')
  em.set_image(url=weblink)
  await ctx.send(embed=em)

@client.command()
async def triggered(ctx, *, messagelink):
  weblink = 'https://some-random-api.ml/canvas/triggered?avatar=' + messagelink
  em = discord.Embed(title='a TRIGGERED Picture')
  em.set_author(name='Triggered Picture')
  em.set_image(url=weblink)
  await ctx.send(embed=em)

@client.command(aliases=["bandw", "black-and-white"])
async def grayscale(ctx, *, messagelink):
  weblink = 'https://some-random-api.ml/canvas/greyscale?avatar=' + messagelink
  em = discord.Embed(title='a Black and White Picture')
  em.set_author(name='Black and White Picture')
  em.set_image(url=weblink)
  await ctx.send(embed=em)

@client.command(aliases=["invert-img", "invert-colors", "invert-image"])
async def invert(ctx, *, messagelink):
  weblink = 'https://some-random-api.ml/canvas/invert?avatar=' + messagelink
  em = discord.Embed(title='a Inverted Picture')
  em.set_author(name='Inverted Picture')
  em.set_image(url=weblink)
  await ctx.send(embed=em)

@client.command(aliases=["bright-img", "bright-colors", "bright-image", "bright"])
async def brightness(ctx, *, messagelink):
  weblink = 'https://some-random-api.ml/canvas/brightness?avatar=' + messagelink
  em = discord.Embed(title='a Brightened Picture')
  em.set_author(name='Brightened Picture')
  em.set_image(url=weblink)
  await ctx.send(embed=em)

@client.command(aliases=["threshold-img", "threshold-colors", "threshold-image", "thresh"])
async def threshold(ctx, *, messagelink):
  weblink = 'https://some-random-api.ml/canvas/threshold?avatar=' + messagelink
  em = discord.Embed(title='a Threshold Picture')
  em.set_author(name='Threshold Picture')
  em.set_image(url=weblink)
  await ctx.send(embed=em)

@client.command(aliases=["sepia-image", "sepia-color"])
async def sepia(ctx, *, messagelink):
  weblink = 'https://some-random-api.ml/canvas/greyscale?avatar=' + messagelink
  em = discord.Embed(title='a Sepia Picture')
  em.set_author(name='Sepia Picture')
  em.set_image(url=weblink)
  await ctx.send(embed=em)

@client.command(aliases=["red-image", "red-color"])
async def red(ctx, *, messagelink):
  weblink = 'https://some-random-api.ml/canvas/red?avatar=' + messagelink
  em = discord.Embed(title='a Red Picture')
  em.set_author(name='Red Picture')
  em.set_image(url=weblink)
  await ctx.send(embed=em)

@client.command(aliases=["green-image", "green-color"])
async def green(ctx, *, messagelink):
  weblink = 'https://some-random-api.ml/canvas/green?avatar=' + messagelink
  em = discord.Embed(title='a Green Picture')
  em.set_author(name='Green Picture')
  em.set_image(url=weblink)
  await ctx.send(embed=em)

@client.command(aliases=["blue-image", "blue-color"])
async def blue(ctx, *, messagelink):
  weblink = 'https://some-random-api.ml/canvas/blue?avatar=' + messagelink
  em = discord.Embed(title='a Blue Picture')
  em.set_author(name='Blue Picture')
  em.set_image(url=weblink)
  await ctx.send(embed=em)

@client.command(aliases=["tint-image", "tint-color"])
async def tint(ctx, colorTotint, *, messagelink):
  weblink = 'https://some-random-api.ml/canvas/color?avatar=' + messagelink + "&color=%" + colorTotint
  em = discord.Embed(title='a Tinted Picture')
  embed_text = "Picture tinted in " + colorTotint
  em.set_author(name=embed_text)
  em.set_image(url=weblink)
  await ctx.send(embed=em)

@client.command(aliases=["pixelate-image"])
async def pixelate(ctx, *, messagelink):
  weblink = 'https://some-random-api.ml/canvas/pixelate' + messagelink
  em = discord.Embed(title='a Blue Picture')
  em.set_author(name='Blue Picture')
  em.set_image(url=weblink)
  await ctx.send(embed=em)

@client.command(aliases=["ytc", "youtubecomment", "youtube-comment", "yt-comment", "you-tube-comment"])
async def ytcomment(ctx, usernameofu, commentmsg, profilepictureLink="https://static.wikia.nocookie.net/ba0628fe-3bc1-42c3-9c0c-aa91ba24f03c/scale-to-width/370", mode="dark"):
  weblink = "https://some-random-api.ml/canvas/youtube-comment?username=" + usernameofu.replace("_", "%20") + "&comment=" + commentmsg.replace("_", "%20") + "&avatar=" + profilepictureLink + "&dark=true"
  # em = discord.Embed(title='a picture of a YouTube Comment')
  # em.set_author(name='Fake YouTube Comment')
  # em.set_image(url=weblink)
  # await ctx.send(embed=em)
  await ctx.send(weblink)

@client.command()
async def pokemon(ctx, pokemonName="pikachu"):
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

  await ctx.send("```" + pokemon_thing_info + "```")

@client.command(aliases=["mincraft-info", "mincraft-user-info", "minecraftinfo"])
async def mcinfo(ctx, *, MinecraftUserName):
  weblink = "https://some-random-api.ml/mc?username=" + MinecraftUserName
  r = requests.get(weblink)
  c = r.json()
  mcinfo_test = f"""Username: {c["username"]}
UUID: {c["uuid"]}
Name History: {c["name_history"]}
"""
  await ctx.send("```" + mcinfo_test + "```")

@client.command(aliases=["lyrics-of", "find-lyrics"])
async def lyricsof(ctx, *, song_name):
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
  r = requests.get('https://some-random-api.ml/binary?text=' + ToBinaryText)
  c = r.json()
  fact = c["binary"]
  shit = 'Text to binary'
  em = discord.Embed()
  AandQ = f'The message entered converted to binary is: \n\n{str(fact)}'
  em.add_field(name=shit, value=AandQ)
  await ctx.send(embed=em)

@client.command(aliases=["b2t", "d_binary", "decode_binary"])
async def b_2txt(ctx, *, ToTextBinary):
  r = requests.get('https://some-random-api.ml/binary?decode=' + ToTextBinary)
  c = r.json()
  fact = c["text"]
  shit = 'Binary to Text'
  em = discord.Embed()
  AandQ = f'The binary entered converted to Text is: \n\n{str(fact)}'
  em.add_field(name=shit, value=AandQ)
  await ctx.send(embed=em)

@client.command(aliases=["b642t", "d_b64", "d_base64"])
async def b64_2txt(ctx, *, ToTextBase64):
  r = requests.get('https://some-random-api.ml/base64?decode=' + ToTextBase64)
  c = r.json()
  fact = c["text"]
  shit = 'Base64 to Text'
  em = discord.Embed()
  AandQ = f'Base64 entered converted to Text is: \n\n{str(fact)}'
  em.add_field(name=shit, value=AandQ)
  await ctx.send(embed=em)

@client.command(alieases=["guess-age"])
async def guessage(ctx, *, nameToSearch):
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

  await ctx.send("```" + guessed_age_info + "```")
  



@client.command(aliases=["show-help", "showhelp", "needhelp", "need-help", "pls-help", "plshelp"])
async def Help(ctx):
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
{bp}covid -> will send global covid information
{bp}wiki Sri Lanka -> will send the first two sentences about "Sri Lanka" from wikipedia
{bp}tinyurl https://youtube.com -> will shorten the given link and send it ( with tinyurl )
{bp}joke -> get a random joke
{bp}iconserver -> will send the server icon to the chat
{bp}mac ff-ff-ff-ff-ff-ff -> will show information about the given mac address
{bp}bitcoin -> will show more information about bitcoin rates
{bp}eth -> show etherium values
{bp}wyr -> a fun thing ( would you rather )
{bp}hastebin Hello ssup -> will add the text to a hastebin and send the link
{bp}ascii test -> will convert any text given to an ASCII banner (in this case, its "test")
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
"""
  help_nsfw = f"""{bp}feed @user -> will send it in an embed by tagging the user
{bp}tickle @user -> will send it in an embed by tagging the user
{bp}slap @user -> will send it in an embed by tagging the user
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
"""
  await ctx.send("```" + help_1 + "```")
  await ctx.send("```" + help_2 + "```")
  await ctx.send("```" + help_nsfw + "```")
  await ctx.send("```" + help_3 + "```")
  await ctx.send("```" + help_4 + "```")
  await ctx.send("```" + help_5 + "```")


keep_alive()

client.run(token)
