import discord
import os
import json
import datetime
from discord.ext import commands
from platform import system as pltfsys
from random import randint as randomint
import urllib
import aiohttp
import textwrap
import yourbot.database.retrieve_embeds as getembed
import yourbot.database.retrieve_base as getbase
import yourbot.others.installerm as ybinstaller

try:
    import requests
except:
    ybinstaller.pip_install("requests")
    import requests

# for `covidcustom` command - the command that returns a graph
try:
    from matplotlib import pyplot
except:
    ybinstaller.pip_install("matplotlib")
    from matplotlib import pyplot

try:
    import pandas as pd
except:
    ybinstaller.pip_install("pandas")
    import pandas as pd


try:
    import wikipedia
except:
    ybinstaller.pip_install("wikipedia")
    import wikipedia

try:
    from PIL import Image, ImageFont, ImageDraw
except:
    ybinstaller.pip_install("Pillow")
    from PIL import Image, ImageFont, ImageDraw


class Information(commands.Cog, description="Gather information easily without leaving discord!"):
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

    @commands.command(aliases=["ipinfo", "infoip", "ip-info", "info-ip"],
                      breif="find IP address information",
                      description="Find information of the given IPv4 Address and country information. `ip_from_user` should be a IPv4 and a valid Public IP",
                      help="Find information of the given IPv4 Address and country information. `ip_from_user` should be a IPv4 and a valid Public IP")
    async def ip(self, ctx, *, ip_from_user):
        loading_message = await ctx.send(embed=self.please_wait_emb)

        try:
            r = requests.get(f"https://ipapi.co/{ip_from_user}/json").json()
            rc = requests.get(
                f"https://api.worldbank.org/v2/country/{r['country_code']}?format=json").json()

            embed = discord.Embed(title="IP Information",
                                  color=getembed.Common.COLOR)
            embed.set_thumbnail(
                url="https://user-images.githubusercontent.com/36286877/127773181-c98b63be-b18b-4d8b-a8b6-9426bd031b7c.png")
            embed.set_footer(text=f"Requested by {ctx.author.name}")
            embed.set_author(name=getembed.Common.AUTHOR,
                             icon_url=getembed.Common.AUTHOR_LINK)
            embed.add_field(name="IP Info", value="IP Address: " + str(r["ip"]) + "\nCity: " + str(r["city"]) + "\nRegion: " + str(r["region"]) + "\nCountry Name: " + str(r["country_name"]) + "\nLatitude: " + str(r["latitude"]) + "\nLongitude: " + str(r["longitude"]) + "\nTime Zone: " + str(r["timezone"]) + "\nUTC Offset: " + str(r["utc_offset"]) + "\nPostal Code: " + str(r["postal"]) + str("\nISP: " + r["org"]) + "\nASN: " + str(r["asn"]) + "\nCountry Code: " + str(
                r["country_code"]) + "\nCountry TLD: " + str(r["country_tld"]) + "\nPopulation: " + str(r["country_population"]) + "\nCurrency: " + str(r["currency"]) + "\n Curreny Name: " + str(r["currency_name"]) + "\nCountry Area: " + str(r["country_area"]) + "\nLanguages: " + str(r["languages"]) + "\nCalling Code: " + str(r["country_calling_code"]) + "\nGOOGLE MAPS Link: " + f"https://maps.google.com/?q={r['latitude']},{r['longitude']}", inline=False)
            embed.add_field(name="Country Info", value="ID: " + str(rc[1][0]["id"]) + "\niso2Code: " + str(rc[1][0]["iso2Code"]) + "\nName" + str(rc[1][0]["name"]) + "\n\nRegion: " + "\n   ID: " + str(rc[1][0]["region"]["id"]) + "\n   iso2Code: " + str(rc[1][0]["region"]["iso2code"]) + "\n   Value: " + str(rc[1][0]["region"]["value"]) + "\n\nAdmin Region: " + "\n   ID: " + str(rc[1][0]["adminregion"]["id"]) + "\n   iso2Code: " + str(rc[1][0]["adminregion"]["iso2code"]) + "\n   Value: " + str(rc[1][0]["adminregion"]["value"]) + "\n\nIncome Level: " + "\n   ID: " + str(
                rc[1][0]["incomeLevel"]["id"]) + "\n   iso2Code: " + str(rc[1][0]["incomeLevel"]["iso2code"]) + "\n   Value: " + str(rc[1][0]["incomeLevel"]["value"]) + "\n\nLending Type: " + "\n   ID: " + str(rc[1][0]["lendingType"]["id"]) + "\n   iso2Code: " + str(rc[1][0]["lendingType"]["iso2code"]) + "\n   Value: " + str(rc[1][0]["lendingType"]["value"]) + "\n\nCapital City: " + str(rc[1][0]["capitalCity"]) + "\nLongitude: " + str(rc[1][0]["longitude"]) + "\nLatitude: " + str(rc[1][0]["latitude"]), inline=False)
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

    @commands.command(aliases=["country-info", "country", "infocountry", "country-information"],
                      breif="find country information",
                      description="Find information of a country. the `countrycode` should be like `sg` for Singapore and `uk` for United Kingdom. This command is powered by the WordBank API",
                      help="Find information of a country. the `countrycode` should be like `sg` for Singapore and `uk` for United Kingdom. This command is powered by the WordBank API")
    async def countryinfo(self, ctx, *, countrycodeig):
        # MAKE SURE TO ENTER THE COUNTRY CODE AND NOT THE COUNTRY NAME
        # eg- sg ( for Singapore ), us for ( United States )
        loading_message = await ctx.send(embed=self.please_wait_emb)

        try:
            rc = requests.get(
                f"https://api.worldbank.org/v2/country/{countrycodeig}?format=json").json()

            embed = discord.Embed(
                title="Country Information", color=getembed.Common.COLOR)
            embed.set_thumbnail(
                url="https://user-images.githubusercontent.com/36286877/129850352-33345963-273b-42bf-b2bc-5523c8158229.png")
            embed.set_footer(text=f"Requested by {ctx.author.name}")
            embed.set_author(name=getembed.Common.AUTHOR,
                             icon_url=getembed.Common.AUTHOR_LINK)
            embed.add_field(name="Country Info", value="ID: " + str(rc[1][0]["id"]) + "\niso2Code: " + str(rc[1][0]["iso2Code"]) + "\nName" + str(rc[1][0]["name"]) + "\n\nRegion: " + "\n   ID: " + str(rc[1][0]["region"]["id"]) + "\n   iso2Code: " + str(rc[1][0]["region"]["iso2code"]) + "\n   Value: " + str(rc[1][0]["region"]["value"]) + "\n\nAdmin Region: " + "\n   ID: " + str(rc[1][0]["adminregion"]["id"]) + "\n   iso2Code: " + str(rc[1][0]["adminregion"]["iso2code"]) + "\n   Value: " + str(rc[1][0]["adminregion"]["value"]) + "\n\nIncome Level: " + "\n   ID: " + str(
                rc[1][0]["incomeLevel"]["id"]) + "\n   iso2Code: " + str(rc[1][0]["incomeLevel"]["iso2code"]) + "\n   Value: " + str(rc[1][0]["incomeLevel"]["value"]) + "\n\nLending Type: " + "\n   ID: " + str(rc[1][0]["lendingType"]["id"]) + "\n   iso2Code: " + str(rc[1][0]["lendingType"]["iso2code"]) + "\n   Value: " + str(rc[1][0]["lendingType"]["value"]) + "\n\nCapital City: " + str(rc[1][0]["capitalCity"]) + "\nLongitude: " + str(rc[1][0]["longitude"]) + "\nLatitude: " + str(rc[1][0]["latitude"]), inline=False)
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
        breif="Bitcoin price",
        description="get the realtime bitcoin price. this command uses the coindesk API",
        help="get the realtime bitcoin price. this command uses the coindesk API")
    async def btc(self, ctx):
        loading_message = await ctx.send(embed=self.please_wait_emb)

        try:
            r = requests.get(
                'https://api.coindesk.com/v1/bpi/currentprice/btc.json').json()
            value = r['bpi']['USD']['rate']
            give_bitcoin_status_get = value
            await loading_message.delete()
            await ctx.send("```" + give_bitcoin_status_get + "```")

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
        breif="Random color generator",
        description="Generate a color (hex code). The embed color is of the random generated color.",
        help="Generate a color (hex code). The embed color is of the random generated color.")
    async def color(self, ctx):
        loading_message = await ctx.send(embed=self.please_wait_emb)

        try:
            give_random_color_get = discord.Color(
                randomint(0x000000, 0xFFFFFF))

            # await loading_message.delete()
            # await ctx.send("```" + give_random_color_get + "```")

            embed3 = discord.Embed(
                title="Color generator", description=f" ```{give_random_color_get}``` ", color=give_random_color_get)
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

    @commands.command(
        breif="main Covid-19 information - Global",
        description="send the main information of the current covid-19 status globally",
        help="send the main information of the current covid-19 status globally")
    async def covidlow(self, ctx):
        loading_message = await ctx.send(embed=self.please_wait_emb)

        try:
            # This is not very accurate
            r = requests.get('https://coronavirus-19-api.herokuapp.com/all')
            data = r.json()
            confirmed_cases = data["cases"]
            deaths = data["deaths"]
            recovered = data["recovered"]

            em = discord.Embed(
                title="COVID-19 Stats Global - Low Info", color=getembed.Common.COLOR)
            em.set_footer(text=f"Requested by {ctx.author.name}")
            em.set_author(name=getembed.Common.AUTHOR,
                          icon_url=getembed.Common.AUTHOR_LINK)
            em.set_thumbnail(
                url="https://www.apsf.org/wp-content/uploads/newsletters/2020/3502/coronavirus-covid-19.png")
            em.add_field(name="Confirmed Cases", value=confirmed_cases)
            em.add_field(name="Deaths", value=deaths)
            em.add_field(name="Recovered", value=recovered)
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

    @commands.command(aliases=["covidlk"],
                      breif="Covid-19 information - Sri Lanka",
                      description="send the all information of the current covid-19 status in Sri Lanka",
                      help="send the all information of the current covid-19 status Sri Lanka")
    async def covidsl(self, ctx):
        loading_message = await ctx.send(embed=self.please_wait_emb)

        try:
            # This uses the official API provided by the Sri Lankan Government to gather the needed data
            r = requests.get(
                "https://www.hpb.health.gov.lk/api/get-current-statistical")
            c = r.json()
            data = c['data']

            update_date_time = data['update_date_time']
            local_new_cases = data['local_new_cases']
            local_total_cases = data['local_total_cases']
            local_total_number_of_individuals_in_hospitals = data[
                'local_total_number_of_individuals_in_hospitals']
            local_deaths = data['local_deaths']
            local_new_deaths = data['local_new_deaths']
            local_recovered = data['local_recovered']
            local_active_cases = data['local_active_cases']

            em = discord.Embed(
                title="COVID-19 Statistics - Sri Lanka", color=getembed.Common.COLOR)
            em.set_footer(text=f"Requested by {ctx.author.name}")
            em.set_author(name=getembed.Common.AUTHOR,
                          icon_url=getembed.Common.AUTHOR_LINK)
            em.set_thumbnail(
                url="https://www.apsf.org/wp-content/uploads/newsletters/2020/3502/coronavirus-covid-19.png")
            em.add_field(name="Last Updated", value=update_date_time)
            em.add_field(name="Total Cases", value=local_total_cases)
            em.add_field(name="New Cases", value=local_new_cases)
            em.add_field(name="Total individuals in hospitals",
                         value=local_total_number_of_individuals_in_hospitals)
            em.add_field(name="Total Deaths", value=local_deaths)
            em.add_field(name="New Deaths", value=local_new_deaths)
            em.add_field(name="Total Recovered", value=local_recovered)
            em.add_field(name="Active Cases", value=local_active_cases)
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

    @commands.command(aliases=["covidall"],
                      breif="Covid-19 information - Global",
                      description="send all information of the current covid-19 status globally",
                      help="send all information of the current covid-19 status globally")
    async def covid(self, ctx):
        loading_message = await ctx.send(embed=self.please_wait_emb)

        try:
            # This uses the official API provided by the Sri Lankan Government to gather the needed data
            r = requests.get(
                "https://www.hpb.health.gov.lk/api/get-current-statistical")
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

            em = discord.Embed(
                title="COVID-19 Stats Global - All Info", color=getembed.Common.COLOR)
            em.set_footer(text=f"Requested by {ctx.author.name}")
            em.set_author(name=getembed.Common.AUTHOR,
                          icon_url=getembed.Common.AUTHOR_LINK)
            em.set_thumbnail(
                url="https://www.apsf.org/wp-content/uploads/newsletters/2020/3502/coronavirus-covid-19.png")
            em.add_field(name="Last Updated", value=update_date_time)
            em.add_field(name="New Cases", value=global_new_cases)
            em.add_field(name="Total Cases", value=global_total_cases)
            em.add_field(name="Total Deaths", value=global_deaths)
            em.add_field(name="New Deaths", value=global_new_deaths)
            em.add_field(name="Total Recovered", value=global_recovered)
            em.add_field(name="Total PCR Testing Count",
                         value=total_pcr_testing_count)
            em.add_field(name="Total Antigen Testing Count",
                         value=total_antigen_testing_count)
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

    @commands.command(
        breif="seacrh wikipedia",
        description="Send the first two sentences in the wikipedia summary",
        help="Send the first two sentences in the wikipedia summary")
    async def wiki(self, ctx, *, word_to_search):
        loading_message = await ctx.send(embed=self.please_wait_emb)
        try:
            embed = discord.Embed(
                title="Wikipedia Search", description="Search Wikipedia without visiting!", color=getembed.Common.COLOR)
            embed.set_footer(text=f"Requested by {ctx.author.name}")
            embed.set_author(name=getembed.Common.AUTHOR,
                             icon_url=getembed.Common.AUTHOR_LINK)
            # embed.add_field(name="Content", value=f"``` {search_wikipedia(word_to_search)} ```", inline=True)
            embed.add_field(
                name="Content", value=f"``` {wikipedia.summary(word_to_search, sentences = 2)} ```", inline=True)
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
        breif="MAC Address information",
        description="Find the vendor of the MAC Address.",
        help="Find the vendor of the MAC Address.")
    async def mac(self, ctx, *, mac):
        loading_message = await ctx.send(embed=self.please_wait_emb)

        try:
            r = requests.get('http://api.macvendors.com/' + mac)

            embed = discord.Embed(title="MAC Lookup",
                                  color=getembed.Common.COLOR)
            embed.set_author(name=getembed.Common.AUTHOR,
                             icon_url=getembed.Common.AUTHOR_LINK)
            embed.set_thumbnail(
                url="https://regmedia.co.uk/2016/09/22/wifi_icon_shutterstock.jpg?x=1200&y=794")
            embed.add_field(name="Result", value=f"{r.text}", inline=False)
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
        breif="Bitcoin price",
        description="get the realtime bitcoin price. this command uses the cryptocompare API",
        help="get the realtime bitcoin price. this command uses the cryptocompare API")
    async def bitcoin(self, ctx):
        loading_message = await ctx.send(embed=self.please_wait_emb)

        try:
            r = requests.get(
                'https://min-api.cryptocompare.com/data/price?fsym=BTC&tsyms=USD,EUR')
            r = r.json()

            usd = r['USD']
            eur = r['EUR']

            embed = discord.Embed(title="Bitcoin", color=getembed.Common.COLOR)
            embed.set_author(name=getembed.Common.AUTHOR,
                             icon_url=getembed.Common.AUTHOR_LINK)
            embed.set_thumbnail(
                url="https://cdn.pixabay.com/photo/2013/12/08/12/12/bitcoin-225079_960_720.png")
            embed.add_field(name="USD", value=f"{usd}$", inline=False)
            embed.add_field(name="EUR", value=f"{eur}€", inline=False)
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
        breif="Etherium price",
        description="get the realtime Etherium price. this command uses the cryptocompare API",
        help="get the realtime Etherium price. this command uses the cryptocompare API")
    async def eth(self, ctx):
        loading_message = await ctx.send(embed=self.please_wait_emb)

        try:
            r = requests.get(
                'https://min-api.cryptocompare.com/data/price?fsym=ETH&tsyms=USD,EUR')
            r = r.json()

            usd = r['USD']
            eur = r['EUR']

            embed = discord.Embed(
                title="Ethereum", color=getembed.Common.COLOR)
            embed.set_author(name=getembed.Common.AUTHOR,
                             icon_url=getembed.Common.AUTHOR_LINK)
            embed.set_thumbnail(
                url="https://cdn.discordapp.com/attachments/271256875205525504/374282740218200064/2000px-Ethereum_logo.png")
            embed.add_field(name="USD", value=f"{usd}$", inline=False)
            embed.add_field(name="EUR", value=f"{eur}€", inline=False)
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
        breif="DogeCoin price",
        description="get the realtime DogeCoin price. this command uses the cryptocompare API",
        help="get the realtime DogeCoin price. this command uses the cryptocompare API")
    async def doge(self, ctx):
        loading_message = await ctx.send(embed=self.please_wait_emb)

        try:
            r = requests.get(
                "https://min-api.cryptocompare.com/data/price?fsym=DOGE&tsyms=USD,EUR")
            NegroPuketDOGE = r.json()

            eur = NegroPuketDOGE['EUR']
            usd = NegroPuketDOGE['USD']

            embed = discord.Embed(
                title="Doge Coin", color=getembed.Common.COLOR)
            embed.set_author(name=getembed.Common.AUTHOR,
                             icon_url=getembed.Common.AUTHOR_LINK)
            embed.set_thumbnail(
                url="https://cdn.discordapp.com/attachments/877796755234783273/879741979183968286/Dogecoin_Logo.png")
            embed.add_field(name="USD", value=f"{usd}", inline=False)
            embed.add_field(name="EUR", value=f"{eur}", inline=True)
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
        breif="Monero price",
        description="get the realtime Monero price. this command uses the cryptocompare API",
        help="get the realtime Monero price. this command uses the cryptocompare API")
    async def xmr(self, ctx):
        loading_message = await ctx.send(embed=self.please_wait_emb)

        try:
            r = requests.get(
                "https://min-api.cryptocompare.com/data/price?fsym=XMR&tsyms=USD,EUR")
            NegroPuket = r.json()

            eur = NegroPuket['EUR']
            usd = NegroPuket['USD']

            embed = discord.Embed(title="XMR", color=getembed.Common.COLOR)
            embed.set_author(name=getembed.Common.AUTHOR,
                             icon_url=getembed.Common.AUTHOR_LINK)
            embed.set_thumbnail(
                url="https://cdn.discordapp.com/attachments/877796755234783273/879739662837633074/monero-logo-png-transparent.png")
            embed.add_field(name="USD", value=f"{usd}", inline=False)
            embed.add_field(name="EUR", value=f"{eur}", inline=True)
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
        breif="Ripple price",
        description="get the realtime Ripple price. this command uses the cryptocompare API",
        help="get the realtime Ripple price. this command uses the cryptocompare API")
    async def xrp(self, ctx):
        loading_message = await ctx.send(embed=self.please_wait_emb)

        try:
            r = requests.get(
                "https://min-api.cryptocompare.com/data/price?fsym=XRP&tsyms=USD,EUR")
            kekistan = r.json()

            eur = kekistan['EUR']
            usd = kekistan['USD']

            embed = discord.Embed(
                title="Doge Coin", color=getembed.Common.COLOR)
            embed.set_author(name=getembed.Common.AUTHOR,
                             icon_url=getembed.Common.AUTHOR_LINK)
            embed.set_thumbnail(
                url="https://cdn.discordapp.com/attachments/877796755234783273/879741815237017680/52.png")
            embed.add_field(name="USD", value=f"{usd}", inline=False)
            embed.add_field(name="EUR", value=f"{eur}", inline=True)
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
        breif="Pokemon information",
        description="find information about pokemon characters. defaults to pikachu. if `mode` is new, this will send a nice embed or else, it will send a ugly message. Make sure the `pokemonName` doesn't have spaces in it!",
        help="find information about pokemon characters. defaults to pikachu. if `mode` is new, this will send a nice embed or else, it will send a ugly message. Make sure the `pokemonName` doesn't have spaces in it!")
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
            # under sprites
            normal_sprites = sprites["normal"]
            animated_sprites = sprites["animated"]
            # under family
            evolutionstage = family["evolutionStage"]
            evolutionsLine = family["evolutionLine"]

            if mode == "new":
                embed = discord.Embed(
                    title="Pokemon!", color=getembed.Common.COLOR)
                embed.set_thumbnail(url=str(normal_sprites))
                embed.add_field(name="General", value="**+ Name:** " + str(name) + "\n**+ ID:** " + str(id) + "\n**+ Type:** " + str(typep) + "\n**+ Species:** " + str(species) + "\n**+ Abilities:** " + str(abilities) +
                                "\n**+Height:** " + str(height) + "\n**+ Weight:** " + str(weight) + "\n**+ Base Experience:** " + str(base_experience) + "\n**+ Gender:** " + str(gender) + "\n**Egg Group:** " + str(egg_group), inline=False)
                embed.add_field(name="Stats", value="**+ HP:** " + str(hp) + "\n**+ Attack:** " + str(attack) + "\n**+ Defense:** " + str(
                    defense) + "\n**+ SP Attack:** " + str(sp_atk) + "\n**+ SP Defense:** " + str(sp_def) + "\n**+ Total:** " + str(total), inline=False)
                embed.add_field(name="Family", value="**+ Evolution:** " + str(
                    evolutionstage) + "\n**+ Evolution Line:** " + str(evolutionsLine), inline=False)
                embed.add_field(name="Sprites", value="**+ Normal:** " + str(
                    normal_sprites) + "\n**+ Animated:** " + str(animated_sprites), inline=False)
                embed.add_field(name="Other", value="**+ Description:** " + str(
                    description) + "\n**+ Generation:** " + str(generation), inline=False)
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
            embed3 = discord.Embed(title=getembed.ErrorEmbeds.TITLE,
                                   description=getembed.ErrorEmbeds.DESCRIPTION, color=getembed.ErrorEmbeds.COLOR)
            embed3.set_author(name=getembed.Common.AUTHOR,
                              icon_url=getembed.Common.AUTHOR_LINK)
            embed3.set_thumbnail(url=getembed.ErrorEmbeds.THUMBNAIL)
            embed3.add_field(name="Error:", value=f"{e}", inline=False)
            embed3.set_footer(text=f"Requested by {ctx.author.name}")
            await loading_message.delete()
            await ctx.send(embed=embed3)

    @commands.command(aliases=["mincraft-info", "mincraft-user-info", "minecraftinfo"],
                      breif="Minecraft account information",
                      description="Find information about a minecraft account with the username!",
                      help="Find information about a minecraft account with the username!")
    async def mcinfo(self, ctx, *, MinecraftUserName):
        loading_message = await ctx.send(embed=self.please_wait_emb)

        try:
            weblink = "https://some-random-api.ml/mc?username=" + MinecraftUserName
            r = requests.get(weblink)
            c = r.json()

            embed = discord.Embed(
                title="Minecraft Account Info", color=getembed.Common.COLOR)
            embed.set_author(name=getembed.Common.AUTHOR,
                             icon_url=getembed.Common.AUTHOR_LINK)
            embed.set_thumbnail(
                url="https://cdn.discordapp.com/attachments/877796755234783273/880022933706260530/418cEZfh8-L.jpg")
            embed.add_field(name="Username",
                            value=f"{c['username']}", inline=False)
            embed.add_field(name="UUID", value=f"{c['uuid']}", inline=False)
            try:
                embed.add_field(name=" Name History",
                                value=f"{c['name_history']}", inline=False)
            except:
                pass
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

    @commands.command(aliases=["lyricsof", "lyric"],
                      breif="Song Lyrics",
                      description="Enter the song name as `search` and the bot will send the lyrics of the given song in an embed with some additional information!",
                      help="Enter the song name as `search` and the bot will send the lyrics of the given song in an embed with some additional information!")
    async def lyrics(self, ctx, *, search=None):
        """Send lyrics of any given song! (only English songs have been tested so far)

        Args:
            ctx (commands.Context)
            search (String): Song name. Defaults to None.

        Returns:
            Sends the embed to the user with some error handling

        Thanks to: https://some-random-api.ml/docs/examples/Python#discord-bot-lyrics-example
        """
        loading_message = await ctx.send(embed=self.please_wait_emb)

        try:
            if not search:  # if user hasnt given an argument, throw a error and come out of the command
                embed = discord.Embed(
                    title="No search argument!",
                    description="You havent entered anything, so i couldnt find lyrics!",
                    color=getembed.Common.COLOR
                )
                try:
                    await loading_message.delete()
                except:
                    pass
                return await ctx.reply(embed=embed)
                # ctx.reply is available only on discord.py version 1.6.0, if you have a version lower than that use ctx.send

            # url-encode the song provided so it can be passed on to the API
            song = urllib.parse.quote(search)

            async with aiohttp.ClientSession() as lyricsSession:
                # define jsondata and fetch from API
                async with lyricsSession.get(f'https://some-random-api.ml/lyrics?title={song}') as jsondata:
                    if not 300 > jsondata.status >= 200:  # if an unexpected HTTP status code is recieved from the website, throw an error and come out of the command
                        try:
                            await loading_message.delete()
                        except:
                            pass
                        return await ctx.send(f'Recieved poor status code of {jsondata.status}')

                    lyricsData = await jsondata.json()  # load the json data into its json form

            error = lyricsData.get('error')
            if error:  # checking if there is an error recieved by the API, and if there is then throwing an error message and returning out of the command
                try:
                    await loading_message.delete()
                except:
                    pass
                return await ctx.send(f'Recieved unexpected error: {error}')

            songLyrics = lyricsData['lyrics']  # the lyrics
            songArtist = lyricsData['author']  # the author's name
            songTitle = lyricsData['title']  # the song's title
            # the song's picture/thumbnail
            songThumbnail = lyricsData['thumbnail']['genius']

            # sometimes the song's lyrics can be above 4096 characters, and if it is then we will not be able to send it in one single message on Discord due to the character limit
            # this is why we split the song into chunks of 4096 characters and send each part individually
            for chunk in textwrap.wrap(songLyrics, 4096, replace_whitespace=False):
                embed = discord.Embed(
                    title=songTitle,
                    description=chunk,
                    color=getembed.Common.COLOR,
                    timestamp=datetime.datetime.utcnow()
                )
                embed.set_author(name=getembed.Common.AUTHOR,
                                 icon_url=getembed.Common.AUTHOR_LINK)
                embed.set_thumbnail(url=songThumbnail)
                try:
                    await loading_message.delete()
                except:
                    pass
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

    @commands.command(aliases=["fn"],
                      breif="Fortnite Account Information",
                      description="send the account username as `args`. will send a image with matches, wins, win percentage, kills, deaths, k/d and kpm in all solom duo, squad game modes + overall information",
                      help="send the account username as `args`. will send a image with matches, wins, win percentage, kills, deaths, k/d and kpm in all solom duo, squad game modes + overall information")
    async def fortnite(self, ctx, *args):
        loading_message = await ctx.send(embed=self.please_wait_emb)
        try:
            username = list(args)
            format_player_name = '%20'.join(username)
            print("recievd args")

            try:
                request_url = f'https://fortnite-api.com/v1/stats/br/v2?name={format_player_name}'
                fortnite_response = json.loads(requests.get(
                    request_url, params={'displayName': username}).content)
                # print("recieved API response")
            except Exception as e:
                try:
                    await loading_message.delete()
                except:
                    pass
                await ctx.send(f"Unable to get information: {e}")
                return

            if fortnite_response['status'] == 200:
                # Images
                fortnite_template_image = Image.open(
                    'yourbot/assets/fortnite_template.png')
                # print("opened image")

                # Fonts
                username_font = ImageFont.truetype(
                    'yourbot/assets/theboldfont.ttf', 50)
                stats_font = ImageFont.truetype(
                    'yourbot/assets/theboldfont.ttf', 40)
                # print("fonts - ok")

                # Positions
                username_position = 135, 163

                # Overall stats
                overall_wins_position = 43, 300
                overall_win_rate_position = 155, 300
                overall_kd_position = 285, 300
                overall_kpm_position = 400, 300
                overall_matches_position = 63, 450
                overall_kills_position = 210, 450
                overall_deaths_position = 350, 450

                # Solo stats
                solo_matches_position = 540, 130
                solo_wins_position = 685, 130
                solo_win_rate_position = 795, 130
                solo_kills_position = 910, 130
                solo_deaths_position = 1050, 130
                solo_kd_position = 1170, 130
                solo_kpm_position = 1270, 130

                # Duo stats
                duo_matches_position = 540, 345
                duo_wins_position = 685, 345
                duo_win_rate_position = 795, 345
                duo_kills_position = 910, 345
                duo_deaths_position = 1050, 345
                duo_kd_position = 1170, 345
                duo_kpm_position = 1270, 345

                # Squad stats
                squad_matches_position = 540, 560
                squad_wins_position = 685, 560
                squad_win_rate_position = 795, 560
                squad_kills_position = 910, 560
                squad_deaths_position = 1050, 560
                squad_kd_position = 1170, 560
                squad_kpm_position = 1270, 560

                # print("position variables - ok")

                # Draws
                draw_on_image = ImageDraw.Draw(fortnite_template_image)

                print("Draw - ok")

                # Username
                draw_on_image.text(username_position, fortnite_response['data']['account']['name'], 'white',
                                   font=username_font)

                # print("Text - ok")

                # Overall stats
                if fortnite_response['data']['stats']['all']['overall'] is not None:
                    draw_on_image.text(overall_wins_position,
                                       str(fortnite_response['data']['stats']
                                           ['all']['overall']['wins']),
                                       'white', font=stats_font)
                    draw_on_image.text(overall_win_rate_position,
                                       str(round(
                                           fortnite_response['data']['stats']['all']['overall']['winRate'], 2)),
                                       'white', font=stats_font)
                    draw_on_image.text(overall_kd_position,
                                       str(round(
                                           fortnite_response['data']['stats']['all']['overall']['kd'], 2)),
                                       'white', font=stats_font)
                    draw_on_image.text(overall_kpm_position,
                                       str(round(
                                           fortnite_response['data']['stats']['all']['overall']['killsPerMatch'], 2)),
                                       'white', font=stats_font)
                    draw_on_image.text(overall_matches_position,
                                       str(fortnite_response['data']['stats']
                                           ['all']['overall']['matches']),
                                       'white', font=stats_font)
                    draw_on_image.text(overall_kills_position,
                                       str(fortnite_response['data']['stats']
                                           ['all']['overall']['kills']),
                                       'white', font=stats_font)
                    draw_on_image.text(overall_deaths_position,
                                       str(fortnite_response['data']['stats']
                                           ['all']['overall']['deaths']),
                                       'white', font=stats_font)

                    # print("write ok")

                # Solo stats
                if fortnite_response['data']['stats']['all']['solo'] is not None:
                    draw_on_image.text(duo_matches_position,
                                       str(fortnite_response['data']['stats']
                                           ['all']['solo']['matches']),
                                       'white', font=stats_font)
                    draw_on_image.text(duo_wins_position, str(fortnite_response['data']['stats']['all']['solo']['wins']),
                                       'white', font=stats_font)
                    draw_on_image.text(duo_win_rate_position,
                                       str(round(
                                           fortnite_response['data']['stats']['all']['solo']['winRate'], 2)),
                                       'white', font=stats_font)
                    draw_on_image.text(duo_kills_position,
                                       str(fortnite_response['data']
                                           ['stats']['all']['solo']['kills']),
                                       'white', font=stats_font)
                    draw_on_image.text(duo_deaths_position,
                                       str(fortnite_response['data']
                                           ['stats']['all']['solo']['deaths']),
                                       'white', font=stats_font)
                    draw_on_image.text(duo_kd_position,
                                       str(round(
                                           fortnite_response['data']['stats']['all']['solo']['kd'], 2)),
                                       'white', font=stats_font)
                    draw_on_image.text(duo_kpm_position,
                                       str(round(
                                           fortnite_response['data']['stats']['all']['solo']['killsPerMatch'], 2)),
                                       'white', font=stats_font)

                    # print("write ok")

                # Duo stats
                if fortnite_response['data']['stats']['all']['duo'] is not None:
                    draw_on_image.text(solo_matches_position,
                                       str(fortnite_response['data']
                                           ['stats']['all']['duo']['matches']),
                                       'white', font=stats_font)
                    draw_on_image.text(solo_wins_position, str(fortnite_response['data']['stats']['all']['duo']['wins']),
                                       'white', font=stats_font)
                    draw_on_image.text(solo_win_rate_position,
                                       str(round(
                                           fortnite_response['data']['stats']['all']['duo']['winRate'], 2)),
                                       'white', font=stats_font)
                    draw_on_image.text(solo_kills_position,
                                       str(fortnite_response['data']
                                           ['stats']['all']['duo']['kills']),
                                       'white', font=stats_font)
                    draw_on_image.text(solo_deaths_position,
                                       str(fortnite_response['data']
                                           ['stats']['all']['duo']['deaths']),
                                       'white', font=stats_font)
                    draw_on_image.text(solo_kd_position,
                                       str(round(
                                           fortnite_response['data']['stats']['all']['duo']['kd'], 2)),
                                       'white', font=stats_font)
                    draw_on_image.text(solo_kpm_position,
                                       str(round(
                                           fortnite_response['data']['stats']['all']['duo']['killsPerMatch'], 2)),
                                       'white', font=stats_font)

                    # print("write ok")

                # Squad stats
                if fortnite_response['data']['stats']['all']['squad'] is not None:
                    draw_on_image.text(squad_matches_position,
                                       str(fortnite_response['data']['stats']
                                           ['all']['squad']['matches']),
                                       'white', font=stats_font)
                    draw_on_image.text(squad_wins_position, str(fortnite_response['data']['stats']['all']['squad']['wins']),
                                       'white', font=stats_font)
                    draw_on_image.text(squad_win_rate_position,
                                       str(round(
                                           fortnite_response['data']['stats']['all']['squad']['winRate'], 2)),
                                       'white', font=stats_font)
                    draw_on_image.text(squad_kills_position,
                                       str(fortnite_response['data']
                                           ['stats']['all']['squad']['kills']),
                                       'white', font=stats_font)
                    draw_on_image.text(squad_deaths_position,
                                       str(fortnite_response['data']['stats']
                                           ['all']['squad']['deaths']),
                                       'white', font=stats_font)
                    draw_on_image.text(squad_kd_position,
                                       str(round(
                                           fortnite_response['data']['stats']['all']['squad']['kd'], 2)),
                                       'white', font=stats_font)
                    draw_on_image.text(squad_kpm_position,
                                       str(round(
                                           fortnite_response['data']['stats']['all']['squad']['killsPerMatch'], 2)),
                                       'white', font=stats_font)

                    # print("write ok")

                # print("saving image")
                # Save image
                fortnite_template_image.convert(
                    'RGB').save('fortnite.jpg', 'JPEG')
                # print("Image saved")

                try:
                    await loading_message.delete()
                except:
                    pass
                await ctx.send(file=discord.File('fortnite.jpg'))

            else:
                try:
                    await loading_message.delete()
                except:
                    pass
                await ctx.send(f":no_entry: **{fortnite_response['error']}**")

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

        finally:
            try:
                os.remove("fortnite.jpg")
            except:
                os.system("rm -rf fortnite.jpg")

    @commands.command(aliases=["covidcus", "covidcustom"],
                      breif="Covid Deaths in a country",
                      description="send a graph with the deaths of the specified country. THIS IS STILL NOT PERFECT AND THIS COMMAND WILL BE COMPLETED SOON! MAYBE USING THIS COMMAND RIGHT NOW WILL BREAK THE BOT. IM NOT SURE LOL",
                      help="send a graph with the deaths of the specified country. THIS IS STILL NOT PERFECT AND THIS COMMAND WILL BE COMPLETED SOON! MAYBE USING THIS COMMAND RIGHT NOW WILL BREAK THE BOT. IM NOT SURE LOL")
    async def covidc(self, ctx, *, country: str):
        loading_message = await ctx.send(embed=self.please_wait_emb)

        try:
            try:
                covid_request_url = urllib.request.Request(
                    f'https://api.covid19api.com/dayone/country/{country}')
                request_result = json.loads(urllib.request.urlopen(
                    covid_request_url).read().decode('utf-8'))
            except Exception as e:
                embed3 = discord.Embed(
                    title=":red_square: Error!", description="The command was unable to run successfully! ", color=getembed.Common.COLOR)
                embed3.set_author(name=getembed.Common.AUTHOR,
                                  icon_url=getembed.Common.AUTHOR_LINK)
                embed3.set_thumbnail(
                    url="https://cdn.discordapp.com/attachments/877796755234783273/879298565380386846/sign-red-error-icon-1.png")
                embed3.add_field(name="Error:", value=f"{e}", inline=False)
                embed3.set_footer(text=f"Requested by {ctx.author.name}")
                await loading_message.delete()
                await ctx.send(embed=embed3)
                return

            data_set = [(datetime.datetime.strptime(date_index['Date'], '%Y-%m-%dT%H:%M:%SZ').strftime('%b'), death_index['Deaths'])
                        for date_index, death_index in zip(request_result, request_result)]

            # Plot
            data_frame = pd.DataFrame(data_set)
            data_frame.plot(x=0, y=1, color='#00012C', label='Months')

            # Label
            pyplot.title(f'Showing Deaths in {country}')
            pyplot.xlabel('Months')
            pyplot.ylabel('Number of Deaths')

            # Legend
            pyplot.legend(loc='upper left')

            # Color
            pyplot.axes().set_facecolor('#9A1622')

            pyplot.savefig('covid_death_graph.png', bbox_inches='tight')

            await loading_message.delete()

            await ctx.send(file=discord.File('covid_death_graph.png'))

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

        finally:
            try:
                os.remove("covid_death_graph.png")
            except:
                os.system("rm -rf covid_death_graph.png")


def setup(client: commands.Bot):
    client.add_cog(Information(client))
