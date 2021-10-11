import discord, os, asyncio
from discord.ext import commands
from json import load as loadjson
from platform import system as pltfsys
from random import randint as randomint
import urllib, aiohttp, textwrap

try:
    import requests
except:
    if pltfsys().lower().startswith('win'):
        os.system("pip install requests")
    else:
        os.system("pip3 install requests")
    import requests

try:
    import wikipedia
except:
    if pltfsys().lower().startswith('win'):
        os.system("pip install wikipedia")
    else:
        os.system("pip3 install wikipedia")
    import wikipedia




class ModerationCommands(commands.Cog):
    def __init__(self, client: commands.Bot):
        self.client = client

        # Loading config.json and its important content for this file
        self.botconfigdata = loadjson(open("config.json", "r"))
        self.bot_prefix = self.botconfigdata["msg-prefix"]
        self.bot_creator_id = self.botconfigdata["ownerid"]

        # This is the please-wait/Loading embed
        self.please_wait_emb = discord.Embed(title="Please Wait", description="``` Processing Your Request ```", color=0xff0000)
        self.please_wait_emb.set_author(name="YourBot")
        self.please_wait_emb.set_thumbnail(url="https://c.tenor.com/I6kN-6X7nhAAAAAj/loading-buffering.gif")
        self.please_wait_emb.set_footer(text="Bot created by ZeaCeR#5641")

    @commands.command(aliases=["ipinfo", "infoip", "ip-info", "info-ip"])
    async def ip(self, ctx, *, ip_from_user):
        loading_message = await ctx.send(embed=self.please_wait_emb)

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


    @commands.command(alises=["country-info", "country", "infocountry", "country-information"])
    async def countryinfo(self, ctx, *, countrycodeig):
        # MAKE SURE TO ENTER THE COUNTRY CODE AND NOT THE COUNTRY NAME
        # eg- sg ( for Singapore ), us for ( United States )
        loading_message = await ctx.send(embed=self.please_wait_emb)

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


    @commands.command()
    async def btc(self, ctx):
        loading_message = await ctx.send(embed=self.please_wait_emb)

        try:
            r = requests.get('https://api.coindesk.com/v1/bpi/currentprice/btc.json').json()
            value = r['bpi']['USD']['rate']
            give_bitcoin_status_get = value
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

        
    @commands.command()
    async def color(self, ctx):
        loading_message = await ctx.send(embed=self.please_wait_emb)

        try:
            give_random_color_get = discord.Color(randomint(0x000000, 0xFFFFFF))
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


    @commands.command()
    async def covidlow(self, ctx):
        loading_message = await ctx.send(embed=self.please_wait_emb)

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


    @commands.command(aliases=["covidlk"])
    async def covidsl(self, ctx):
        loading_message = await ctx.send(embed=self.please_wait_emb)

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


    @commands.command(aliases=["covidall"])
    async def covid(self, ctx):
        loading_message = await ctx.send(embed=self.please_wait_emb)

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


    @commands.command()
    async def wiki(self, ctx, *, word_to_search):
        loading_message = await ctx.send(embed=self.please_wait_emb)
        try:
            embed=discord.Embed(title="Wikipedia Search", description="Search Wikipedia without visiting!", color=0xff0000)
            embed.set_footer(text=f"Requested by {ctx.author.name}")
            embed.set_author(name="YourBot", icon_url="https://cdn.discordapp.com/attachments/877796755234783273/879295069834850324/Avatar.png")
            # embed.add_field(name="Content", value=f"``` {search_wikipedia(word_to_search)} ```", inline=True)
            embed.add_field(name="Content", value=f"``` {wikipedia.summary(word_to_search, sentences = 2)} ```", inline=True)
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
    async def mac(self, ctx, *, mac):
        loading_message = await ctx.send(embed=self.please_wait_emb)

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

    @commands.command()
    async def bitcoin(self, ctx):
        loading_message = await ctx.send(embed=self.please_wait_emb)
        
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
    
    
    @commands.command()
    async def eth(self, ctx):
        loading_message = await ctx.send(embed=self.please_wait_emb)

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


    @commands.command()
    async def doge(self, ctx):
        loading_message = await ctx.send(embed=self.please_wait_emb)

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


    @commands.command()
    async def xmr(self, ctx):
        loading_message = await ctx.send(embed=self.please_wait_emb)

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

    @commands.command()
    async def xrp(self, ctx):
        loading_message = await ctx.send(embed=self.please_wait_emb)

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

        
    @commands.command()
    async def pokemon(self, ctx, pokemonName="pikachu", mode="new"):
        loading_message = await ctx.send(embed=self.please_wait_emb)

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


    @commands.command(aliases=["mincraft-info", "mincraft-user-info", "minecraftinfo"])
    async def mcinfo(self, ctx, *, MinecraftUserName):
        loading_message = await ctx.send(embed=self.please_wait_emb)

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

        
    @commands.command(aliases=["lyricsof"])
    async def lyrics(self, ctx, *, search = None):
        loading_message = await ctx.send(embed=self.please_wait_emb)

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















def setup(client: commands.Bot):
    client.add_cog(ModerationCommands(client))
