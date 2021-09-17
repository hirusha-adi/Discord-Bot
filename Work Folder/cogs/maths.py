import discord, requests, aiohttp
from discord.ext import commands
from json import load as loadjson
from json import loads as loadjsonstring


class Mathematics(commands.Cog):
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



    @commands.command(aliases=["addition"])
    async def add(self, ctx, number_1, number_2):
        loading_message = await ctx.send(embed=self.please_wait_emb)
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

    @commands.command(aliases=["substraction", "substract"])
    async def subs(self, ctx, number_1, number_2):
        loading_message = await ctx.send(embed=self.please_wait_emb)

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

    
    @commands.command(aliases=["multiplication", "multiply"])
    async def mul(self, ctx, number_1, number_2):
        loading_message = await ctx.send(embed=self.please_wait_emb)

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


    @commands.command(aliases=["division", "divide"])
    async def div(self, ctx, number_1, number_2):
        loading_message = await ctx.send(embed=self.please_wait_emb)

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








def setup(client: commands.Bot):
    client.add_cog(Mathematics(client))

