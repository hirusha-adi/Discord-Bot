# IM NOT VERY CONFIDENT WITH DOING THIS!





# import discord, sqlite3
# from discord.ext import commands
# from json import load as loadjson

# from platform import system as pltfsys



# class BankGame(commands.Cog):
#     def __init__(self, client: commands.Bot):
#         self.client = client

#         # Loading config.json and its important content for this file
#         self.botconfigdata = loadjson(open("config.json", "r"))
#         self.bot_prefix = self.botconfigdata["msg-prefix"]
#         self.bot_inv_link = self.botconfigdata["invite-link"]

#         # This is the please-wait/Loading embed
#         self.please_wait_emb = discord.Embed(title="Please Wait", description="``` Processing Your Request ```", color=0xff0000)
#         self.please_wait_emb.set_author(name="YourBot")
#         self.please_wait_emb.set_thumbnail(url="https://c.tenor.com/I6kN-6X7nhAAAAAj/loading-buffering.gif")
#         self.please_wait_emb.set_footer(text="Bot created by ZeaCeR#5641")

#         self.database_name = "bankgame.db"


#     def create(self):
#         conn = sqlite3.connect(self.database_name)
#         cur = conn.cursor()
#         cur.execute("CREATE TABLE IF NOT EXISTS game (id INTEGER PRIMARY KEY, balance integer)")
#         # id - integer - primary key
#         # balance - integer
#         conn.commit()
#         conn.close()

#     def insert(self, id):
#         conn = sqlite3.connect(self.database_name)
#         cur = conn.cursor()
#         # cur.execute("INSERT INTO game VALUES (?,?)", (id, balance))
#         cur.execute("INSERT INTO game IF NOT EXISTS VALUES (?, 1)", (id,))
#         conn.commit()
#         conn.close()

#     def view_all(self):
#         conn = sqlite3.connect(self.database_name)
#         cur = conn.cursor()
#         cur.execute("SELECT * FROM game")
#         rows = cur.fetchall()
#         conn.close()
#         return rows

#     def view(self, id):
#         conn = sqlite3.connect(self.database_name)
#         cur = conn.cursor()
#         cur.execute("SELECT * FROM game WHERE id=(?)", (id,))
#         rows = cur.fetchall()
#         conn.close()
#         return rows

#     def delete(self, id):
#         conn = sqlite3.connect(self.database_name)
#         cur = conn.cursor()
#         cur.execute("DELETE FROM game WHERE id=?", (id,))
#         conn.commit()
#         conn.close()

#     def update(self, id, newbalance):
#         conn = sqlite3.connect(self.database_name)
#         cur = conn.cursor()
#         cur.execute("UPDATE game SET balance=? WHERE id=?", (newbalance, id))
#         conn.commit()
#         conn.close()
    
#     create()

#     @commands.command(aliases=["ginit", "ginitialize"])
#     async def gstart(self, ctx, *, userm: discord.Member =None):
#         # Check if a user is mentioned
#         if userm == None:
#             userm = ctx.author
        
#         # Create the db and the table if it doesnt exists
#         self.create()

#         userid = userm.id

#         # Adding the user to the db with discord id and 1 balance
#         self.insert(userid)

#         await ctx.send(f"[+] Created {userid} ({userm.name}) in table: game in: game.db; with default balance: 1")


#     @commands.command()
#     async def gbal(self, ctx, userm: discord.Member =None):
#         # Check if a user is mentioned
#         if userm == None:
#             userm = ctx.author
        
#         userid = userm.id

#         # Create the db and the table if it doesnt exists
#         result = self.view(userid)

#         await ctx.send(f"[+] User: {userm} ({userid}) has a balance of {result}")
        



































# def setup(client: commands.Bot):
#     client.add_cog(BankGame(client))














