import discord, requests, hashlib, urllib, base64
from discord.ext import commands
from json import load as loadjson
from random import choice as randomchoice
import database.retrieve_embeds as getembed


class Games(commands.Cog):
    def __init__(self, client: commands.Bot, description="a set of simple commands"):
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


    @commands.command(aliases=["8ball", "eightball"],
    breif="the 8ball game",
    description="the simple 8ball game!",
    help="the simple 8ball game!")
    async def _8ball(self, ctx, *, question):
        loading_message = await ctx.send(embed=self.please_wait_emb)

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

            answer = randomchoice(responses, color=getembed.Common.COLOR)
            embed = discord.Embed()
            embed.add_field(name="Question", value=question, inline=False)
            embed.add_field(name="Answer", value=answer, inline=False)
            embed.set_thumbnail(url="https://www.horoscope.com/images-US/games/game-magic-8-ball-no-text.png")
            embed.set_footer(text=f"Requested by {ctx.author.mention}")
            embed.set_author(name=getembed.Common.AUTHOR, icon_url=getembed.Common.AUTHOR_LINK)
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

    @commands.command(
    breif="how does he/she die?",
    description="will send a random picked method of how he/she might die in the future!",
    help="will send a random picked method of how he/she might die in the future!")
    async def howdie(self, ctx, member: discord.Member = "none"):
        loading_message = await ctx.send(embed=self.please_wait_emb)

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
                embed=discord.Embed(title="Death...??", color=getembed.Common.COLOR)
                embed.set_author(name=getembed.Common.AUTHOR, icon_url=getembed.Common.AUTHOR_LINK)
                embed.set_footer(text=f"Requested by {ctx.author.name}")
                embed.add_field(name=f"{ctx.author.name}", value=f"{randomchoice(dying_methods)}.", inline=False)
                await loading_message.delete()
                await ctx.send(embed=embed)

            else:
                embed=discord.Embed(title="Death...??", color=getembed.Common.COLOR)
                embed.set_author(name=getembed.Common.AUTHOR, icon_url=getembed.Common.AUTHOR_LINK)
                embed.set_footer(text="Requested by {ctx.author.name}")
                embed.add_field(name=f"{member.name}", value=f"{randomchoice(dying_methods)}.", inline=False)
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



    @commands.command(breif="the slots game",
    description="the simple slots game to have some fun!",
    help="the simple slots game to have some fun!")
    async def slots(self, ctx):
        loading_message = await ctx.send(embed=self.please_wait_emb)

        try:
            responses = ["🍋" , "🍊", "🍉", ":seven:", ]
            embed=discord.Embed(title="🎰 Slot Machine 🎰", description=randomchoice(responses) + randomchoice(responses) + randomchoice(responses), color=getembed.Common.COLOR)
            embed.set_author(name=getembed.Common.AUTHOR, icon_url=getembed.Common.AUTHOR_LINK)
            embed.set_footer(text="You need triple 7's to win.")
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
    client.add_cog(Games(client))
