import discord, requests, hashlib, urllib, base64
from discord.ext import commands
from json import load as loadjson
from random import choice as randomchoice

class BotGeneralCommands(commands.Cog):
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


    @commands.command(aliases=["8ball", "eightball"])
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

            answer = randomchoice(responses, color=0xff0000)
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



























def setup(client: commands.Bot):
    client.add_cog(BotGeneralCommands(client))
