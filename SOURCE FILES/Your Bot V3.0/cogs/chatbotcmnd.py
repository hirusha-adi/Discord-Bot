import discord, requests
from discord.ext import commands
from json import load as loadjson


class ChatBotCommands(commands.Cog):
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




    @commands.command()
    async def chatbot(self, ctx, command="main"):
        loading_message = await ctx.send(embed=self.please_wait_emb)

        try:
            old_wl = ("1", "1.0", "one", "first", "olddays")
            bp = self.bot_prefix
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










def setup(client: commands.Bot):
    client.add_cog(ChatBotCommands(client))

