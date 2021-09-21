import discord, requests, aiohttp
from discord.ext import commands
from json import load as loadjson
from json import loads as loadjsonstring
import database.retrieve_embeds as getembed


class Mathematics(commands.Cog):
    def __init__(self, client: commands.Bot):
        self.client = client

        # Loading config.json and its important content for this file
        self.botconfigdata = loadjson(open("config.json", "r"))
        self.bot_prefix = self.botconfigdata["msg-prefix"]
        self.bot_inv_link = self.botconfigdata["invite-link"]

        # This is the please-wait/Loading embed
        self.please_wait_emb = discord.Embed(title=getembed.PleaseWait.TITLE, description=f"``` {getembed.PleaseWait.DESCRIPTION} ```", color=getembed.PleaseWait.COLOR)
        self.please_wait_emb.set_author(name=getembed.PleaseWait.AUTHOR_NAME, icon_url=getembed.PleaseWait.AUTHOR_LINK)
        self.please_wait_emb.set_thumbnail(url=getembed.PleaseWait.THUMBNAIL)
        self.please_wait_emb.set_footer(text=getembed.PleaseWait.FOOTER)
    


    @commands.command(aliases=["addition"],
    breif="Addition",
    description="Add two numbers easily!",
    help="Add two numbers easily!")
    async def add(self, ctx, number_1:int, number_2:int):
        loading_message = await ctx.send(embed=self.please_wait_emb)
        try:
            ans = float(number_1) + float(number_2)

            embed=discord.Embed(title="Addition", color=getembed.Common.COLOR)
            embed.set_author(name=getembed.Common.AUTHOR, icon_url=getembed.Common.AUTHOR_LINK)
            embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/877796755234783273/879962889509806080/addition-icon-3.jpg")
            embed.add_field(name="Query", value=f"{number_1} + {number_2}", inline=False)
            embed.add_field(name="Result", value=f"{ans}", inline=True)
            embed.set_footer(text=f"Requested by {ctx.author.name}")
            await loading_message.delete()
            await ctx.send(embed=embed)
        
        except Exception as e:
            embed3=discord.Embed(title=getembed.ErrorEmbeds.TITLE, description=getembed.ErrorEmbeds.DESCRIPTION, color=getembed.ErrorEmbeds.COLOR)
            embed3.set_author(name=getembed.Common.AUTHOR, icon_url=getembed.Common.AUTHOR_LINK)
            embed3.set_thumbnail(url=getembed.ErrorEmbeds.THUMBNAIL)
            embed3.add_field(name="Error:", value=f"{e}", inline=False)
            embed3.set_footer(text=f"Requested by {ctx.author.name}")
            await loading_message.delete()
            await ctx.send(embed=embed3)


    @commands.command(aliases=["substraction", "substract"],
    breif="Substraction",
    description="substract two numbers easily!",
    help="substract two numbers easily!")
    async def subs(self, ctx, number_1:int, number_2:int):
        loading_message = await ctx.send(embed=self.please_wait_emb)

        try:
            ans = float(number_1) - float(number_2)

            embed=discord.Embed(title="Substraction", color=getembed.Common.COLOR)
            embed.set_author(name=getembed.Common.AUTHOR, icon_url=getembed.Common.AUTHOR_LINK)
            embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/877796755234783273/879964954806083604/1043.png")
            embed.add_field(name="Query", value=f"{number_1} - {number_2}", inline=False)
            embed.add_field(name="Result", value=f"{ans}", inline=True)
            embed.set_footer(text=f"Requested by {ctx.author.name}")
            await ctx.send(embed=embed)
        
        except Exception as e:
            embed3=discord.Embed(title=getembed.ErrorEmbeds.TITLE, description=getembed.ErrorEmbeds.DESCRIPTION, color=getembed.ErrorEmbeds.COLOR)
            embed3.set_author(name=getembed.Common.AUTHOR, icon_url=getembed.Common.AUTHOR_LINK)
            embed3.set_thumbnail(url=getembed.ErrorEmbeds.THUMBNAIL)
            embed3.add_field(name="Error:", value=f"{e}", inline=False)
            embed3.set_footer(text=f"Requested by {ctx.author.name}")
            await loading_message.delete()
            await ctx.send(embed=embed3)

    
    @commands.command(aliases=["multiplication", "multiply"],
    breif="Multiplication",
    description="multiply two numbers easily!",
    help="multiply two numbers easily!")
    async def mul(self, ctx, number_1:int, number_2:int):
        loading_message = await ctx.send(embed=self.please_wait_emb)

        try:
            ans = float(number_1) * float(number_2)

            embed=discord.Embed(title="Multiplication", color=getembed.Common.COLOR)
            embed.set_author(name=getembed.Common.AUTHOR, icon_url=getembed.Common.AUTHOR_LINK)
            embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/877796755234783273/879965848603869214/43165.png")
            embed.add_field(name="Query", value=f"{number_1} x {number_2}", inline=False)
            embed.add_field(name="Result", value=f"{ans}", inline=True)
            embed.set_footer(text="Requested by {ctx.author.name}")
            await loading_message.delete()
            await ctx.send(embed=embed)
        
        except Exception as e:
            embed3=discord.Embed(title=getembed.ErrorEmbeds.TITLE, description=getembed.ErrorEmbeds.DESCRIPTION, color=getembed.ErrorEmbeds.COLOR)
            embed3.set_author(name=getembed.Common.AUTHOR, icon_url=getembed.Common.AUTHOR_LINK)
            embed3.set_thumbnail(url=getembed.ErrorEmbeds.THUMBNAIL)
            embed3.add_field(name="Error:", value=f"{e}", inline=False)
            embed3.set_footer(text=f"Requested by {ctx.author.name}")
            await loading_message.delete()
            await ctx.send(embed=embed3)


    @commands.command(aliases=["division", "divide"],
    breif="Division",
    description="divide two numbers easily!",
    help="divide two numbers easily!")
    async def div(self, ctx, number_1:int, number_2:int):
        loading_message = await ctx.send(embed=self.please_wait_emb)

        try:
            ans = float(number_1) / float(number_2)

            embed=discord.Embed(title="Division", color=getembed.Common.COLOR)
            embed.set_author(name=getembed.Common.AUTHOR, icon_url=getembed.Common.AUTHOR_LINK)
            embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/877796755234783273/879966441502294026/674233_mathematics_512x512.png")
            embed.add_field(name="Query", value=f"{number_1} / {number_2}", inline=False)
            embed.add_field(name="Result", value=f"{ans}", inline=True)
            embed.set_footer(text=f"Requested by {ctx.author.name}")
            await loading_message.delete()
            await ctx.send(embed=embed)
        
        except Exception as e:
            embed3=discord.Embed(title=getembed.ErrorEmbeds.TITLE, description=getembed.ErrorEmbeds.DESCRIPTION, color=getembed.ErrorEmbeds.COLOR)
            embed3.set_author(name=getembed.Common.AUTHOR, icon_url=getembed.Common.AUTHOR_LINK)
            embed3.set_thumbnail(url=getembed.ErrorEmbeds.THUMBNAIL)
            embed3.add_field(name="Error:", value=f"{e}", inline=False)
            embed3.set_footer(text=f"Requested by {ctx.author.name}")
            await loading_message.delete()
            await ctx.send(embed=embed3)








def setup(client: commands.Bot):
    client.add_cog(Mathematics(client))

