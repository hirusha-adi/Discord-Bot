import discord
from discord.ext import commands
from faker import Faker

class Startup(commands.Cog):
    def __init__(self, client: commands.Bot):
        self.client = client

        # Bot starting time, we find the time delta of this to send the uptime
        self.start_time = None

        # This is the please-wait/Loading embed
        self.please_wait_emb = discord.Embed(title="Please Wait", description="``` Processing Your Request ```", color=0xff0000)
        self.please_wait_emb.set_author(name="YourBot")
        self.please_wait_emb.set_thumbnail(url="https://c.tenor.com/I6kN-6X7nhAAAAAj/loading-buffering.gif")
        self.please_wait_emb.set_footer(text="Bot created by ZeaCeR#5641")

    @commands.command()
    async def fake(self, ctx, *, fake_mode="help"):
        loading_message = await ctx.send(embed=self.please_wait_emb)

        if fake_mode == "high":
            try:
                fake = Faker()
                simple_dict = fake.profile()
                emf = discord.Embed(title="Fake Information Generator", color=0xF00000)
                emf.set_footer(text=f"Requested by {ctx.author.name}")
                emf.set_author(name="YourBot", icon_url="https://cdn.discordapp.com/attachments/877796755234783273/879295069834850324/Avatar.png")
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
                await loading_message.delete()
                await ctx.send(embed=emf)
            except Exception as e:
                embed2=discord.Embed(title=":red_square: Error!", description="The command was unable to run successfully! ", color=0xff0000)
                embed2.set_author(name="YourBot", icon_url="https://cdn.discordapp.com/attachments/877796755234783273/879295069834850324/Avatar.png")
                embed2.set_thumbnail(url="https://cdn.discordapp.com/attachments/877796755234783273/879298565380386846/sign-red-error-icon-1.png")
                embed2.add_field(name="Error:", value=f"{e}", inline=False)
                embed2.set_footer(text=f"Requested by {ctx.author.name}")
                await loading_message.delete()
                await ctx.send(embed=embed2)

        elif fake_mode == "name":
            faker = Faker()
            try:
                USname = faker.name()
                emf2 = discord.Embed(title="Fake Information Generator", color=0xF00000)
                emf2.set_thumbnail(url="https://www.nicepng.com/png/detail/214-2146883_4-fake-stamp-vector-fake-news-logo-png.png")
                emf2.set_footer(text=f"Requested by {ctx.author.name}")
                emf2.set_author(name="YourBot", icon_url="https://cdn.discordapp.com/attachments/877796755234783273/879295069834850324/Avatar.png")
                emf2.add_field(name="Name", value=f"{str(USname)}")
                await loading_message.delete()
                await ctx.send(embed=emf2)
            except Exception as e:
                embed3=discord.Embed(title=":red_square: Error!", description="The command was unable to run successfully! ", color=0xff0000)
                embed3.set_author(name="YourBot", icon_url="https://cdn.discordapp.com/attachments/877796755234783273/879295069834850324/Avatar.png")
                embed3.set_thumbnail(url="https://cdn.discordapp.com/attachments/877796755234783273/879298565380386846/sign-red-error-icon-1.png")
                embed3.add_field(name="Error:", value=f"{e}", inline=False)
                embed3.set_footer(text=f"Requested by {ctx.author.name}")
                await loading_message.delete()
                await ctx.send(embed=embed3)
        
        elif fake_mode == "dob":
            faker = Faker()
            try:
                USdob = faker.date_of_birth()
                emf2 = discord.Embed(title="Fake Information Generator", color=0xF00000)
                emf2.set_thumbnail(url="https://www.nicepng.com/png/detail/214-2146883_4-fake-stamp-vector-fake-news-logo-png.png")
                emf2.set_footer(text=f"Requested by {ctx.author.name}")
                emf2.set_author(name="YourBot", icon_url="https://cdn.discordapp.com/attachments/877796755234783273/879295069834850324/Avatar.png")
                emf2.add_field(name="Date Of Birth", value=f"{str(USdob)}")
                await loading_message.delete()
                await ctx.send(embed=emf2)
            except Exception as e:
                embed3=discord.Embed(title=":red_square: Error!", description="The command was unable to run successfully! ", color=0xff0000)
                embed3.set_author(name="YourBot", icon_url="https://cdn.discordapp.com/attachments/877796755234783273/879295069834850324/Avatar.png")
                embed3.set_thumbnail(url="https://cdn.discordapp.com/attachments/877796755234783273/879298565380386846/sign-red-error-icon-1.png")
                embed3.add_field(name="Error:", value=f"{e}", inline=False)
                embed3.set_footer(text=f"Requested by {ctx.author.name}")
                await loading_message.delete()
                await ctx.send(embed=embed3)
        
        elif fake_mode == "addr":
            faker = Faker()
            try:
                USaddress = faker.address()
                emf2 = discord.Embed(title="Fake Information Generator", color=0xF00000)
                emf2.set_thumbnail(url="https://www.nicepng.com/png/detail/214-2146883_4-fake-stamp-vector-fake-news-logo-png.png")
                emf2.set_footer(text=f"Requested by {ctx.author.name}")
                emf2.set_author(name="YourBot", icon_url="https://cdn.discordapp.com/attachments/877796755234783273/879295069834850324/Avatar.png")
                emf2.add_field(name="Address", value=f"{str(USaddress)}")
                await loading_message.delete()
                await ctx.send(embed=emf2)
            except Exception as e:
                embed3=discord.Embed(title=":red_square: Error!", description="The command was unable to run successfully! ", color=0xff0000)
                embed3.set_author(name="YourBot", icon_url="https://cdn.discordapp.com/attachments/877796755234783273/879295069834850324/Avatar.png")
                embed3.set_thumbnail(url="https://cdn.discordapp.com/attachments/877796755234783273/879298565380386846/sign-red-error-icon-1.png")
                embed3.add_field(name="Error:", value=f"{e}", inline=False)
                embed3.set_footer(text=f"Requested by {ctx.author.name}")
                await loading_message.delete()
                await ctx.send(embed=embed3)
        
        elif fake_mode == "job":
            faker = Faker()
            try:
                USjob = faker.job()
                emf2 = discord.Embed(title="Fake Information Generator", color=0xF00000)
                emf2.set_thumbnail(url="https://www.nicepng.com/png/detail/214-2146883_4-fake-stamp-vector-fake-news-logo-png.png")
                emf2.set_footer(text=f"Requested by {ctx.author.name}")
                emf2.set_author(name="YourBot", icon_url="https://cdn.discordapp.com/attachments/877796755234783273/879295069834850324/Avatar.png")
                emf2.add_field(name="Job", value=f"{str(USjob)}")
                await loading_message.delete()
                await ctx.send(embed=emf2)
            except Exception as e:
                embed3=discord.Embed(title=":red_square: Error!", description="The command was unable to run successfully! ", color=0xff0000)
                embed3.set_author(name="YourBot", icon_url="https://cdn.discordapp.com/attachments/877796755234783273/879295069834850324/Avatar.png")
                embed3.set_thumbnail(url="https://cdn.discordapp.com/attachments/877796755234783273/879298565380386846/sign-red-error-icon-1.png")
                embed3.add_field(name="Error:", value=f"{e}", inline=False)
                embed3.set_footer(text=f"Requested by {ctx.author.name}")
                await loading_message.delete()
                await ctx.send(embed=embed3)
        
        elif fake_mode == "color":
            faker = Faker()
            try:
                USfavColor = faker.color_name()
                emf2 = discord.Embed(title="Fake Information Generator", color=0xF00000)
                emf2.set_thumbnail(url="https://www.nicepng.com/png/detail/214-2146883_4-fake-stamp-vector-fake-news-logo-png.png")
                emf2.set_footer(text=f"Requested by {ctx.author.name}")
                emf2.set_author(name="YourBot", icon_url="https://cdn.discordapp.com/attachments/877796755234783273/879295069834850324/Avatar.png")
                emf2.add_field(name="Color", value=f"{str(USfavColor)}")
                await loading_message.delete()
                await ctx.send(embed=emf2)
            except Exception as e:
                embed3=discord.Embed(title=":red_square: Error!", description="The command was unable to run successfully! ", color=0xff0000)
                embed3.set_author(name="YourBot", icon_url="https://cdn.discordapp.com/attachments/877796755234783273/879295069834850324/Avatar.png")
                embed3.set_thumbnail(url="https://cdn.discordapp.com/attachments/877796755234783273/879298565380386846/sign-red-error-icon-1.png")
                embed3.add_field(name="Error:", value=f"{e}", inline=False)
                embed3.set_footer(text=f"Requested by {ctx.author.name}")
                await loading_message.delete()
                await ctx.send(embed=embed3)

        elif fake_mode == "zipcode":
            faker = Faker()
            try:
                USzip = faker.zipcode()
                emf2 = discord.Embed(title="Fake Information Generator", color=0xF00000)
                emf2.set_thumbnail(url="https://www.nicepng.com/png/detail/214-2146883_4-fake-stamp-vector-fake-news-logo-png.png")
                emf2.set_footer(text=f"Requested by {ctx.author.name}")
                emf2.set_author(name="YourBot", icon_url="https://cdn.discordapp.com/attachments/877796755234783273/879295069834850324/Avatar.png")
                emf2.add_field(name="Zip Code", value=f"{str(USzip)}")
                await loading_message.delete()
                await ctx.send(embed=emf2)
            except Exception as e:
                embed3=discord.Embed(title=":red_square: Error!", description="The command was unable to run successfully! ", color=0xff0000)
                embed3.set_author(name="YourBot", icon_url="https://cdn.discordapp.com/attachments/877796755234783273/879295069834850324/Avatar.png")
                embed3.set_thumbnail(url="https://cdn.discordapp.com/attachments/877796755234783273/879298565380386846/sign-red-error-icon-1.png")
                embed3.add_field(name="Error:", value=f"{e}", inline=False)
                embed3.set_footer(text=f"Requested by {ctx.author.name}")
                await loading_message.delete()
                await ctx.send(embed=embed3)
        
        elif fake_mode == "city":
            faker = Faker()
            try:
                UScity = faker.city()
                emf2 = discord.Embed(title="Fake Information Generator", color=0xF00000)
                emf2.set_thumbnail(url="https://www.nicepng.com/png/detail/214-2146883_4-fake-stamp-vector-fake-news-logo-png.png")
                emf2.set_footer(text=f"Requested by {ctx.author.name}")
                emf2.set_author(name="YourBot", icon_url="https://cdn.discordapp.com/attachments/877796755234783273/879295069834850324/Avatar.png")
                emf2.add_field(name="City", value=f"{str(UScity)}")
                await loading_message.delete()
                await ctx.send(embed=emf2)
            except Exception as e:
                embed3=discord.Embed(title=":red_square: Error!", description="The command was unable to run successfully! ", color=0xff0000)
                embed3.set_author(name="YourBot", icon_url="https://cdn.discordapp.com/attachments/877796755234783273/879295069834850324/Avatar.png")
                embed3.set_thumbnail(url="https://cdn.discordapp.com/attachments/877796755234783273/879298565380386846/sign-red-error-icon-1.png")
                embed3.add_field(name="Error:", value=f"{e}", inline=False)
                embed3.set_footer(text=f"Requested by {ctx.author.name}")
                await loading_message.delete()
                await ctx.send(embed=embed3)
        
        elif fake_mode == "licenseplate":
            faker = Faker()
            try:
                USnumberPlate = faker.license_plate()
                emf2 = discord.Embed(title="Fake Information Generator", color=0xF00000)
                emf2.set_thumbnail(url="https://www.nicepng.com/png/detail/214-2146883_4-fake-stamp-vector-fake-news-logo-png.png")
                emf2.set_footer(text=f"Requested by {ctx.author.name}")
                emf2.set_author(name="YourBot", icon_url="https://cdn.discordapp.com/attachments/877796755234783273/879295069834850324/Avatar.png")
                emf2.add_field(name="License Plate", value=f"{str(USnumberPlate)}")
                await loading_message.delete()
                await ctx.send(embed=emf2)
            except Exception as e:
                embed3=discord.Embed(title=":red_square: Error!", description="The command was unable to run successfully! ", color=0xff0000)
                embed3.set_author(name="YourBot", icon_url="https://cdn.discordapp.com/attachments/877796755234783273/879295069834850324/Avatar.png")
                embed3.set_thumbnail(url="https://cdn.discordapp.com/attachments/877796755234783273/879298565380386846/sign-red-error-icon-1.png")
                embed3.add_field(name="Error:", value=f"{e}", inline=False)
                embed3.set_footer(text=f"Requested by {ctx.author.name}")
                await loading_message.delete()
                await ctx.send(embed=embed3)
        
        elif fake_mode == "bban":
            faker = Faker()
            try:
                USbasicBankAccountNumber = faker.bban()
                emf2 = discord.Embed(title="Fake Information Generator", color=0xF00000)
                emf2.set_thumbnail(url="https://www.nicepng.com/png/detail/214-2146883_4-fake-stamp-vector-fake-news-logo-png.png")
                emf2.set_footer(text=f"Requested by {ctx.author.name}")
                emf2.set_author(name="YourBot", icon_url="https://cdn.discordapp.com/attachments/877796755234783273/879295069834850324/Avatar.png")
                emf2.add_field(name="Basic Bank Account", value=f"{str(USbasicBankAccountNumber)}")
                await loading_message.delete()
                await ctx.send(embed=emf2)
            except Exception as e:
                embed3=discord.Embed(title=":red_square: Error!", description="The command was unable to run successfully! ", color=0xff0000)
                embed3.set_author(name="YourBot", icon_url="https://cdn.discordapp.com/attachments/877796755234783273/879295069834850324/Avatar.png")
                embed3.set_thumbnail(url="https://cdn.discordapp.com/attachments/877796755234783273/879298565380386846/sign-red-error-icon-1.png")
                embed3.add_field(name="Error:", value=f"{e}", inline=False)
                embed3.set_footer(text=f"Requested by {ctx.author.name}")
                await loading_message.delete()
                await ctx.send(embed=embed3)
        
        elif fake_mode == "iban":
            faker = Faker()
            try:
                USinternationalBankAccountNumber = faker.iban()
                emf2 = discord.Embed(title="Fake Information Generator", color=0xF00000)
                emf2.set_thumbnail(url="https://www.nicepng.com/png/detail/214-2146883_4-fake-stamp-vector-fake-news-logo-png.png")
                emf2.set_footer(text=f"Requested by {ctx.author.name}")
                emf2.set_author(name="YourBot", icon_url="https://cdn.discordapp.com/attachments/877796755234783273/879295069834850324/Avatar.png")
                emf2.add_field(name="International Bank Account", value=f"{str(USinternationalBankAccountNumber)}")
                await loading_message.delete()
                await ctx.send(embed=emf2)
            except Exception as e:
                embed3=discord.Embed(title=":red_square: Error!", description="The command was unable to run successfully! ", color=0xff0000)
                embed3.set_author(name="YourBot", icon_url="https://cdn.discordapp.com/attachments/877796755234783273/879295069834850324/Avatar.png")
                embed3.set_thumbnail(url="https://cdn.discordapp.com/attachments/877796755234783273/879298565380386846/sign-red-error-icon-1.png")
                embed3.add_field(name="Error:", value=f"{e}", inline=False)
                embed3.set_footer(text=f"Requested by {ctx.author.name}")
                await loading_message.delete()
                await ctx.send(embed=embed3)
        
        elif fake_mode == "bs":
            faker = Faker()
            try:
                USbs = faker.bs()
                emf2 = discord.Embed(title="Fake Information Generator", color=0xF00000)
                emf2.set_thumbnail(url="https://www.nicepng.com/png/detail/214-2146883_4-fake-stamp-vector-fake-news-logo-png.png")
                emf2.set_footer(text=f"Requested by {ctx.author.name}")
                emf2.set_author(name="YourBot", icon_url="https://cdn.discordapp.com/attachments/877796755234783273/879295069834850324/Avatar.png")
                emf2.add_field(name="BS", value=f"{str(USbs)}")
                await loading_message.delete()
                await ctx.send(embed=emf2)
            except Exception as e:
                embed3=discord.Embed(title=":red_square: Error!", description="The command was unable to run successfully! ", color=0xff0000)
                embed3.set_author(name="YourBot", icon_url="https://cdn.discordapp.com/attachments/877796755234783273/879295069834850324/Avatar.png")
                embed3.set_thumbnail(url="https://cdn.discordapp.com/attachments/877796755234783273/879298565380386846/sign-red-error-icon-1.png")
                embed3.add_field(name="Error:", value=f"{e}", inline=False)
                embed3.set_footer(text=f"Requested by {ctx.author.name}")
                await loading_message.delete()
                await ctx.send(embed=embed3)
        
        elif fake_mode == "cc":
            faker = Faker()
            try:
                UScreditcard = faker.credit_card_full()
                emf2 = discord.Embed(title="Fake Information Generator", color=0xF00000)
                emf2.set_thumbnail(url="https://www.nicepng.com/png/detail/214-2146883_4-fake-stamp-vector-fake-news-logo-png.png")
                emf2.set_footer(text=f"Requested by {ctx.author.name}")
                emf2.set_author(name="YourBot", icon_url="https://cdn.discordapp.com/attachments/877796755234783273/879295069834850324/Avatar.png")
                emf2.add_field(name="Credit Card", value=f"{str(UScreditcard)}")
                await loading_message.delete()
                await ctx.send(embed=emf2)
            except Exception as e:
                embed3=discord.Embed(title=":red_square: Error!", description="The command was unable to run successfully! ", color=0xff0000)
                embed3.set_author(name="YourBot", icon_url="https://cdn.discordapp.com/attachments/877796755234783273/879295069834850324/Avatar.png")
                embed3.set_thumbnail(url="https://cdn.discordapp.com/attachments/877796755234783273/879298565380386846/sign-red-error-icon-1.png")
                embed3.add_field(name="Error:", value=f"{e}", inline=False)
                embed3.set_footer(text=f"Requested by {ctx.author.name}")
                await loading_message.delete()
                await ctx.send(embed=embed3)
        
        elif fake_mode == "cemail":
            faker = Faker()
            try:
                UScompanyemail = faker.company_email()
                emf2 = discord.Embed(title="Fake Information Generator", color=0xF00000)
                emf2.set_thumbnail(url="https://www.nicepng.com/png/detail/214-2146883_4-fake-stamp-vector-fake-news-logo-png.png")
                emf2.set_footer(text=f"Requested by {ctx.author.name}")
                emf2.set_author(name="YourBot", icon_url="https://cdn.discordapp.com/attachments/877796755234783273/879295069834850324/Avatar.png")
                emf2.add_field(name="Email", value=f"{str(UScompanyemail)}")
                await loading_message.delete()
                await ctx.send(embed=emf2)
            except Exception as e:
                embed3=discord.Embed(title=":red_square: Error!", description="The command was unable to run successfully! ", color=0xff0000)
                embed3.set_author(name="YourBot", icon_url="https://cdn.discordapp.com/attachments/877796755234783273/879295069834850324/Avatar.png")
                embed3.set_thumbnail(url="https://cdn.discordapp.com/attachments/877796755234783273/879298565380386846/sign-red-error-icon-1.png")
                embed3.add_field(name="Error:", value=f"{e}", inline=False)
                embed3.set_footer(text=f"Requested by {ctx.author.name}")
                await loading_message.delete()
                await ctx.send(embed=embed3)
        
        elif fake_mode == "pno":
            faker = Faker()
            try:
                USphoneNumber = faker.phone_number()
                emf2 = discord.Embed(title="Fake Information Generator", color=0xF00000)
                emf2.set_thumbnail(url="https://www.nicepng.com/png/detail/214-2146883_4-fake-stamp-vector-fake-news-logo-png.png")
                emf2.set_footer(text=f"Requested by {ctx.author.name}")
                emf2.set_author(name="YourBot", icon_url="https://cdn.discordapp.com/attachments/877796755234783273/879295069834850324/Avatar.png")
                emf2.add_field(name="Phone Number", value=f"{str(USphoneNumber)}")
                await loading_message.delete()
                await ctx.send(embed=emf2)
            except Exception as e:
                embed3=discord.Embed(title=":red_square: Error!", description="The command was unable to run successfully! ", color=0xff0000)
                embed3.set_author(name="YourBot", icon_url="https://cdn.discordapp.com/attachments/877796755234783273/879295069834850324/Avatar.png")
                embed3.set_thumbnail(url="https://cdn.discordapp.com/attachments/877796755234783273/879298565380386846/sign-red-error-icon-1.png")
                embed3.add_field(name="Error:", value=f"{e}", inline=False)
                embed3.set_footer(text=f"Requested by {ctx.author.name}")
                await loading_message.delete()
                await ctx.send(embed=embed3)
        
        elif fake_mode == "cp":
            faker = Faker()
            try:
                UScatchPhrase = faker.catch_phrase()
                emf2 = discord.Embed(title="Fake Information Generator", color=0xF00000)
                emf2.set_thumbnail(url="https://www.nicepng.com/png/detail/214-2146883_4-fake-stamp-vector-fake-news-logo-png.png")
                emf2.set_footer(text=f"Requested by {ctx.author.name}")
                emf2.set_author(name="YourBot", icon_url="https://cdn.discordapp.com/attachments/877796755234783273/879295069834850324/Avatar.png")
                emf2.add_field(name="Catch Phrase", value=f"{str(UScatchPhrase)}")
                await loading_message.delete()
                await ctx.send(embed=emf2)
            except Exception as e:
                embed3=discord.Embed(title=":red_square: Error!", description="The command was unable to run successfully! ", color=0xff0000)
                embed3.set_author(name="YourBot", icon_url="https://cdn.discordapp.com/attachments/877796755234783273/879295069834850324/Avatar.png")
                embed3.set_thumbnail(url="https://cdn.discordapp.com/attachments/877796755234783273/879298565380386846/sign-red-error-icon-1.png")
                embed3.add_field(name="Error:", value=f"{e}", inline=False)
                embed3.set_footer(text=f"Requested by {ctx.author.name}")
                await loading_message.delete()
                await ctx.send(embed=embed3)
        
        elif fake_mode == "ssn":
            faker = Faker()
            try:
                USssa = faker.ssn()
                emf2 = discord.Embed(title="Fake Information Generator", color=0xF00000)
                emf2.set_thumbnail(url="https://www.nicepng.com/png/detail/214-2146883_4-fake-stamp-vector-fake-news-logo-png.png")
                emf2.set_footer(text=f"Requested by {ctx.author.name}")
                emf2.set_author(name="YourBot", icon_url="https://cdn.discordapp.com/attachments/877796755234783273/879295069834850324/Avatar.png")
                emf2.add_field(name="SSN", value=f"{str(USssa)}")
                await loading_message.delete()
                await ctx.send(embed=emf2)
            except Exception as e:
                embed3=discord.Embed(title=":red_square: Error!", description="The command was unable to run successfully! ", color=0xff0000)
                embed3.set_author(name="YourBot", icon_url="https://cdn.discordapp.com/attachments/877796755234783273/879295069834850324/Avatar.png")
                embed3.set_thumbnail(url="https://cdn.discordapp.com/attachments/877796755234783273/879298565380386846/sign-red-error-icon-1.png")
                embed3.add_field(name="Error:", value=f"{e}", inline=False)
                embed3.set_footer(text=f"Requested by {ctx.author.name}")
                await loading_message.delete()
                await ctx.send(embed=embed3)
        
        elif fake_mode == "low":
            fake_low = Faker()
            try:
                shitthing_simple = fake_low.simple_profile()
                # fake_info_low_info = "Name: " + str(shitthing_simple['name']) + "\nSex: " + str(shitthing_simple['sex']) + "\nAddress: " + str(shitthing_simple['address']) + "\nMail: " + str(shitthing_simple['mail']) + "\nBirthday: " + str(shitthing_simple['birthdate'])
                emf2 = discord.Embed(title="Fake Information Generator", color=0xF00000)
                emf2.set_thumbnail(url="https://www.nicepng.com/png/detail/214-2146883_4-fake-stamp-vector-fake-news-logo-png.png")
                emf2.set_footer(text=f"Requested by {ctx.author.name}")
                emf2.set_author(name="YourBot", icon_url="https://cdn.discordapp.com/attachments/877796755234783273/879295069834850324/Avatar.png")
                emf2.add_field(name="Name", value=f"{str(shitthing_simple['name'])}")
                emf2.add_field(name="Sex", value=f"{str(shitthing_simple['sex'])}")
                emf2.add_field(name="Address", value=f"{str(shitthing_simple['address'])}")
                emf2.add_field(name="Mail", value=f"{str(shitthing_simple['mail'])}")
                emf2.add_field(name="Birthday", value=f"{str(shitthing_simple['birthdate'])}")
                await loading_message.delete()
                await ctx.send(embed=emf2)
            except Exception as e:
                embed3=discord.Embed(title=":red_square: Error!", description="The command was unable to run successfully! ", color=0xff0000)
                embed3.set_author(name="YourBot", icon_url="https://cdn.discordapp.com/attachments/877796755234783273/879295069834850324/Avatar.png")
                embed3.set_thumbnail(url="https://cdn.discordapp.com/attachments/877796755234783273/879298565380386846/sign-red-error-icon-1.png")
                embed3.add_field(name="Error:", value=f"{e}", inline=False)
                embed3.set_footer(text=f"Requested by {ctx.author.name}")
                await loading_message.delete()
                await ctx.send(embed=embed3)
            
        elif fake_mode == "country":
            faker = Faker()
            try:
                USssa = faker.country()
                emf2 = discord.Embed(title="Fake Information Generator", color=0xF00000)
                emf2.set_thumbnail(url="https://www.nicepng.com/png/detail/214-2146883_4-fake-stamp-vector-fake-news-logo-png.png")
                emf2.set_footer(text=f"Requested by {ctx.author.name}")
                emf2.set_author(name="YourBot", icon_url="https://cdn.discordapp.com/attachments/877796755234783273/879295069834850324/Avatar.png")
                emf2.add_field(name="Country", value=f"{str(USssa)}")
                await loading_message.delete()
                await ctx.send(embed=emf2)
            except Exception as e:
                embed3=discord.Embed(title=":red_square: Error!", description="The command was unable to run successfully! ", color=0xff0000)
                embed3.set_author(name="YourBot", icon_url="https://cdn.discordapp.com/attachments/877796755234783273/879295069834850324/Avatar.png")
                embed3.set_thumbnail(url="https://cdn.discordapp.com/attachments/877796755234783273/879298565380386846/sign-red-error-icon-1.png")
                embed3.add_field(name="Error:", value=f"{e}", inline=False)
                embed3.set_footer(text=f"Requested by {ctx.author.name}")
                await loading_message.delete()
                await ctx.send(embed=embed3)
        
        elif fake_mode == "postcode":
            faker = Faker()
            try:
                USssa = faker.postcode()
                emf2 = discord.Embed(title="Fake Information Generator", color=0xF00000)
                emf2.set_thumbnail(url="https://www.nicepng.com/png/detail/214-2146883_4-fake-stamp-vector-fake-news-logo-png.png")
                emf2.set_footer(text=f"Requested by {ctx.author.name}")
                emf2.set_author(name="YourBot", icon_url="https://cdn.discordapp.com/attachments/877796755234783273/879295069834850324/Avatar.png")
                emf2.add_field(name="Postcode", value=f"{str(USssa)}")
                await loading_message.delete()
                await ctx.send(embed=emf2)
            except Exception as e:
                embed3=discord.Embed(title=":red_square: Error!", description="The command was unable to run successfully! ", color=0xff0000)
                embed3.set_author(name="YourBot", icon_url="https://cdn.discordapp.com/attachments/877796755234783273/879295069834850324/Avatar.png")
                embed3.set_thumbnail(url="https://cdn.discordapp.com/attachments/877796755234783273/879298565380386846/sign-red-error-icon-1.png")
                embed3.add_field(name="Error:", value=f"{e}", inline=False)
                embed3.set_footer(text=f"Requested by {ctx.author.name}")
                await loading_message.delete()
                await ctx.send(embed=embed3)
        
        elif fake_mode == "street addr":
            faker = Faker()
            try:
                USssa = faker.street_address()
                emf2 = discord.Embed(title="Fake Information Generator", color=0xF00000)
                emf2.set_thumbnail(url="https://www.nicepng.com/png/detail/214-2146883_4-fake-stamp-vector-fake-news-logo-png.png")
                emf2.set_footer(text=f"Requested by {ctx.author.name}")
                emf2.set_author(name="YourBot", icon_url="https://cdn.discordapp.com/attachments/877796755234783273/879295069834850324/Avatar.png")
                emf2.add_field(name="Street Address", value=f"{str(USssa)}")
                await loading_message.delete()
                await ctx.send(embed=emf2)
            except Exception as e:
                embed3=discord.Embed(title=":red_square: Error!", description="The command was unable to run successfully! ", color=0xff0000)
                embed3.set_author(name="YourBot", icon_url="https://cdn.discordapp.com/attachments/877796755234783273/879295069834850324/Avatar.png")
                embed3.set_thumbnail(url="https://cdn.discordapp.com/attachments/877796755234783273/879298565380386846/sign-red-error-icon-1.png")
                embed3.add_field(name="Error:", value=f"{e}", inline=False)
                embed3.set_footer(text=f"Requested by {ctx.author.name}")
                await loading_message.delete()
                await ctx.send(embed=embed3)
        
        elif fake_mode == "street name":
            faker = Faker()
            try:
                USssa = faker.street_name()
                emf2 = discord.Embed(title="Fake Information Generator", color=0xF00000)
                emf2.set_thumbnail(url="https://www.nicepng.com/png/detail/214-2146883_4-fake-stamp-vector-fake-news-logo-png.png")
                emf2.set_footer(text=f"Requested by {ctx.author.name}")
                emf2.set_author(name="YourBot", icon_url="https://cdn.discordapp.com/attachments/877796755234783273/879295069834850324/Avatar.png")
                emf2.add_field(name="Street Name", value=f"{str(USssa)}")
                await loading_message.delete()
                await ctx.send(embed=emf2)
            except Exception as e:
                embed3=discord.Embed(title=":red_square: Error!", description="The command was unable to run successfully! ", color=0xff0000)
                embed3.set_author(name="YourBot", icon_url="https://cdn.discordapp.com/attachments/877796755234783273/879295069834850324/Avatar.png")
                embed3.set_thumbnail(url="https://cdn.discordapp.com/attachments/877796755234783273/879298565380386846/sign-red-error-icon-1.png")
                embed3.add_field(name="Error:", value=f"{e}", inline=False)
                embed3.set_footer(text=f"Requested by {ctx.author.name}")
                await loading_message.delete()
                await ctx.send(embed=embed3)
        
        elif fake_mode == "aba":
            faker = Faker()
            try:
                USssa = faker.aba()
                emf2 = discord.Embed(title="Fake Information Generator", color=0xF00000)
                emf2.set_thumbnail(url="https://www.nicepng.com/png/detail/214-2146883_4-fake-stamp-vector-fake-news-logo-png.png")
                emf2.set_footer(text=f"Requested by {ctx.author.name}")
                emf2.set_author(name="YourBot", icon_url="https://cdn.discordapp.com/attachments/877796755234783273/879295069834850324/Avatar.png")
                emf2.add_field(name="ABA", value=f"{str(USssa)}")
                await loading_message.delete()
                await ctx.send(embed=emf2)
            except Exception as e:
                embed3=discord.Embed(title=":red_square: Error!", description="The command was unable to run successfully! ", color=0xff0000)
                embed3.set_author(name="YourBot", icon_url="https://cdn.discordapp.com/attachments/877796755234783273/879295069834850324/Avatar.png")
                embed3.set_thumbnail(url="https://cdn.discordapp.com/attachments/877796755234783273/879298565380386846/sign-red-error-icon-1.png")
                embed3.add_field(name="Error:", value=f"{e}", inline=False)
                embed3.set_footer(text=f"Requested by {ctx.author.name}")
                await loading_message.delete()
                await ctx.send(embed=embed3)
        
        elif fake_mode == "bank country":
            faker = Faker()
            try:
                USssa = faker.bank_country()
                emf2 = discord.Embed(title="Fake Information Generator", color=0xF00000)
                emf2.set_thumbnail(url="https://www.nicepng.com/png/detail/214-2146883_4-fake-stamp-vector-fake-news-logo-png.png")
                emf2.set_footer(text=f"Requested by {ctx.author.name}")
                emf2.set_author(name="YourBot", icon_url="https://cdn.discordapp.com/attachments/877796755234783273/879295069834850324/Avatar.png")
                emf2.add_field(name="Bank Cuntry", value=f"{str(USssa)}")
                await loading_message.delete()
                await ctx.send(embed=emf2)
            except Exception as e:
                embed3=discord.Embed(title=":red_square: Error!", description="The command was unable to run successfully! ", color=0xff0000)
                embed3.set_author(name="YourBot", icon_url="https://cdn.discordapp.com/attachments/877796755234783273/879295069834850324/Avatar.png")
                embed3.set_thumbnail(url="https://cdn.discordapp.com/attachments/877796755234783273/879298565380386846/sign-red-error-icon-1.png")
                embed3.add_field(name="Error:", value=f"{e}", inline=False)
                embed3.set_footer(text=f"Requested by {ctx.author.name}")
                await loading_message.delete()
                await ctx.send(embed=embed3)
        
        elif fake_mode == "ean":
        # The usage is like 'fake ean 10' - 10 is the length
            faker = Faker()
            try:
                nu_of_time = fake_mode.split(" ")[-1]

                USssa = faker.ean(length=int(nu_of_time))
                emf2 = discord.Embed(title="Fake Information Generator", color=0xF00000)
                emf2.set_thumbnail(url="https://www.nicepng.com/png/detail/214-2146883_4-fake-stamp-vector-fake-news-logo-png.png")
                emf2.set_footer(text=f"Requested by {ctx.author.name}")
                emf2.set_author(name="YourBot", icon_url="https://cdn.discordapp.com/attachments/877796755234783273/879295069834850324/Avatar.png")
                emf2.add_field(name="EAN Barcode", value=f"{str(USssa)}")
                await loading_message.delete()
                await ctx.send(embed=emf2)
            except Exception as e:
                embed3=discord.Embed(title=":red_square: Error!", description="The command was unable to run successfully! ", color=0xff0000)
                embed3.set_author(name="YourBot", icon_url="https://cdn.discordapp.com/attachments/877796755234783273/879295069834850324/Avatar.png")
                embed3.set_thumbnail(url="https://cdn.discordapp.com/attachments/877796755234783273/879298565380386846/sign-red-error-icon-1.png")
                embed3.add_field(name="Error:", value=f"{e}", inline=False)
                embed3.set_footer(text=f"Requested by {ctx.author.name}")
                await loading_message.delete()
                await ctx.send(embed=embed3)
        
        elif fake_mode == "company suffix":
            faker = Faker()
            try:
                USssa = faker.company_suffix()
                emf2 = discord.Embed(title="Fake Information Generator", color=0xF00000)
                emf2.set_thumbnail(url="https://www.nicepng.com/png/detail/214-2146883_4-fake-stamp-vector-fake-news-logo-png.png")
                emf2.set_footer(text=f"Requested by {ctx.author.name}")
                emf2.set_author(name="YourBot", icon_url="https://cdn.discordapp.com/attachments/877796755234783273/879295069834850324/Avatar.png")
                emf2.add_field(name="Company Suffix", value=f"{str(USssa)}")
                await loading_message.delete()
                await ctx.send(embed=emf2)
            except Exception as e:
                embed3=discord.Embed(title=":red_square: Error!", description="The command was unable to run successfully! ", color=0xff0000)
                embed3.set_author(name="YourBot", icon_url="https://cdn.discordapp.com/attachments/877796755234783273/879295069834850324/Avatar.png")
                embed3.set_thumbnail(url="https://cdn.discordapp.com/attachments/877796755234783273/879298565380386846/sign-red-error-icon-1.png")
                embed3.add_field(name="Error:", value=f"{e}", inline=False)
                embed3.set_footer(text=f"Requested by {ctx.author.name}")
                await loading_message.delete()
                await ctx.send(embed=embed3)
        
        elif fake_mode == "cc ex":
            faker = Faker()
            try:
                USssa = faker.credit_card_expire()
                emf2 = discord.Embed(title="Fake Information Generator", color=0xF00000)
                emf2.set_thumbnail(url="https://www.nicepng.com/png/detail/214-2146883_4-fake-stamp-vector-fake-news-logo-png.png")
                emf2.set_footer(text=f"Requested by {ctx.author.name}")
                emf2.set_author(name="YourBot", icon_url="https://cdn.discordapp.com/attachments/877796755234783273/879295069834850324/Avatar.png")
                emf2.add_field(name="Credit Card Expire Date", value=f"{str(USssa)}")
                await loading_message.delete()
                await ctx.send(embed=emf2)
            except Exception as e:
                embed3=discord.Embed(title=":red_square: Error!", description="The command was unable to run successfully! ", color=0xff0000)
                embed3.set_author(name="YourBot", icon_url="https://cdn.discordapp.com/attachments/877796755234783273/879295069834850324/Avatar.png")
                embed3.set_thumbnail(url="https://cdn.discordapp.com/attachments/877796755234783273/879298565380386846/sign-red-error-icon-1.png")
                embed3.add_field(name="Error:", value=f"{e}", inline=False)
                embed3.set_footer(text=f"Requested by {ctx.author.name}")
                await loading_message.delete()
                await ctx.send(embed=embed3)

        elif fake_mode == "cc no":
            faker = Faker()
            try:
                USssa = faker.credit_card_number()
                emf2 = discord.Embed(title="Fake Information Generator", color=0xF00000)
                emf2.set_thumbnail(url="https://www.nicepng.com/png/detail/214-2146883_4-fake-stamp-vector-fake-news-logo-png.png")
                emf2.set_footer(text=f"Requested by {ctx.author.name}")
                emf2.set_author(name="YourBot", icon_url="https://cdn.discordapp.com/attachments/877796755234783273/879295069834850324/Avatar.png")
                emf2.add_field(name="Credit Card Number", value=f"{str(USssa)}")
                await loading_message.delete()
                await ctx.send(embed=emf2)
            except Exception as e:
                embed3=discord.Embed(title=":red_square: Error!", description="The command was unable to run successfully! ", color=0xff0000)
                embed3.set_author(name="YourBot", icon_url="https://cdn.discordapp.com/attachments/877796755234783273/879295069834850324/Avatar.png")
                embed3.set_thumbnail(url="https://cdn.discordapp.com/attachments/877796755234783273/879298565380386846/sign-red-error-icon-1.png")
                embed3.add_field(name="Error:", value=f"{e}", inline=False)
                embed3.set_footer(text=f"Requested by {ctx.author.name}")
                await loading_message.delete()
                await ctx.send(embed=embed3)
        
        elif fake_mode == "cc pr":
            faker = Faker()
            try:
                USssa = faker.credit_card_provider()
                emf2 = discord.Embed(title="Fake Information Generator", color=0xF00000)
                emf2.set_thumbnail(url="https://www.nicepng.com/png/detail/214-2146883_4-fake-stamp-vector-fake-news-logo-png.png")
                emf2.set_footer(text=f"Requested by {ctx.author.name}")
                emf2.set_author(name="YourBot", icon_url="https://cdn.discordapp.com/attachments/877796755234783273/879295069834850324/Avatar.png")
                emf2.add_field(name="Credit Card Provider", value=f"{str(USssa)}")
                await loading_message.delete()
                await ctx.send(embed=emf2)
            except Exception as e:
                embed3=discord.Embed(title=":red_square: Error!", description="The command was unable to run successfully! ", color=0xff0000)
                embed3.set_author(name="YourBot", icon_url="https://cdn.discordapp.com/attachments/877796755234783273/879295069834850324/Avatar.png")
                embed3.set_thumbnail(url="https://cdn.discordapp.com/attachments/877796755234783273/879298565380386846/sign-red-error-icon-1.png")
                embed3.add_field(name="Error:", value=f"{e}", inline=False)
                embed3.set_footer(text=f"Requested by {ctx.author.name}")
                await loading_message.delete()
                await ctx.send(embed=embed3)
        
        elif fake_mode == "cc cvv":
            faker = Faker()
            try:
                USssa = faker.credit_card_security_code()
                emf2 = discord.Embed(title="Fake Information Generator", color=0xF00000)
                emf2.set_thumbnail(url="https://www.nicepng.com/png/detail/214-2146883_4-fake-stamp-vector-fake-news-logo-png.png")
                emf2.set_footer(text=f"Requested by {ctx.author.name}")
                emf2.set_author(name="YourBot", icon_url="https://cdn.discordapp.com/attachments/877796755234783273/879295069834850324/Avatar.png")
                emf2.add_field(name="Credit Card CVV", value=f"{str(USssa)}")
                await loading_message.delete()
                await ctx.send(embed=emf2)
            except Exception as e:
                embed3=discord.Embed(title=":red_square: Error!", description="The command was unable to run successfully! ", color=0xff0000)
                embed3.set_author(name="YourBot", icon_url="https://cdn.discordapp.com/attachments/877796755234783273/879295069834850324/Avatar.png")
                embed3.set_thumbnail(url="https://cdn.discordapp.com/attachments/877796755234783273/879298565380386846/sign-red-error-icon-1.png")
                embed3.add_field(name="Error:", value=f"{e}", inline=False)
                embed3.set_footer(text=f"Requested by {ctx.author.name}")
                await loading_message.delete()
                await ctx.send(embed=embed3)
        
        elif fake_mode == "crypto":
            faker = Faker()
            try:
                USssa = faker.cryptocurrency()
                emf2 = discord.Embed(title="Fake Information Generator", color=0xF00000)
                emf2.set_thumbnail(url="https://www.nicepng.com/png/detail/214-2146883_4-fake-stamp-vector-fake-news-logo-png.png")
                emf2.set_footer(text=f"Requested by {ctx.author.name}")
                emf2.set_author(name="YourBot", icon_url="https://cdn.discordapp.com/attachments/877796755234783273/879295069834850324/Avatar.png")
                emf2.add_field(name="Cryptocurrency", value=f"Short Name: {USssa[0]} \nFull Name: {USssa[1]}")
                await loading_message.delete()
                await ctx.send(embed=emf2)
            except Exception as e:
                embed3=discord.Embed(title=":red_square: Error!", description="The command was unable to run successfully! ", color=0xff0000)
                embed3.set_author(name="YourBot", icon_url="https://cdn.discordapp.com/attachments/877796755234783273/879295069834850324/Avatar.png")
                embed3.set_thumbnail(url="https://cdn.discordapp.com/attachments/877796755234783273/879298565380386846/sign-red-error-icon-1.png")
                embed3.add_field(name="Error:", value=f"{e}", inline=False)
                embed3.set_footer(text=f"Requested by {ctx.author.name}")
                await loading_message.delete()
                await ctx.send(embed=embed3)
        
        elif fake_mode == "crypto code":
            faker = Faker()
            try:
                USssa = faker.cryptocurrency_code()
                emf2 = discord.Embed(title="Fake Information Generator", color=0xF00000)
                emf2.set_thumbnail(url="https://www.nicepng.com/png/detail/214-2146883_4-fake-stamp-vector-fake-news-logo-png.png")
                emf2.set_footer(text=f"Requested by {ctx.author.name}")
                emf2.set_author(name="YourBot", icon_url="https://cdn.discordapp.com/attachments/877796755234783273/879295069834850324/Avatar.png")
                emf2.add_field(name="Cryptocurrency Code", value=f"{USssa}")
                await loading_message.delete()
                await ctx.send(embed=emf2)
            except Exception as e:
                embed3=discord.Embed(title=":red_square: Error!", description="The command was unable to run successfully! ", color=0xff0000)
                embed3.set_author(name="YourBot", icon_url="https://cdn.discordapp.com/attachments/877796755234783273/879295069834850324/Avatar.png")
                embed3.set_thumbnail(url="https://cdn.discordapp.com/attachments/877796755234783273/879298565380386846/sign-red-error-icon-1.png")
                embed3.add_field(name="Error:", value=f"{e}", inline=False)
                embed3.set_footer(text=f"Requested by {ctx.author.name}")
                await loading_message.delete()
                await ctx.send(embed=embed3)
        
        elif fake_mode == "crypto name":
            faker = Faker()
            try:
                USssa = faker.cryptocurrency_name()
                emf2 = discord.Embed(title="Fake Information Generator", color=0xF00000)
                emf2.set_thumbnail(url="https://www.nicepng.com/png/detail/214-2146883_4-fake-stamp-vector-fake-news-logo-png.png")
                emf2.set_footer(text=f"Requested by {ctx.author.name}")
                emf2.set_author(name="YourBot", icon_url="https://cdn.discordapp.com/attachments/877796755234783273/879295069834850324/Avatar.png")
                emf2.add_field(name="Cryptocurrency Name", value=f"{USssa}")
                await loading_message.delete()
                await ctx.send(embed=emf2)
            except Exception as e:
                embed3=discord.Embed(title=":red_square: Error!", description="The command was unable to run successfully! ", color=0xff0000)
                embed3.set_author(name="YourBot", icon_url="https://cdn.discordapp.com/attachments/877796755234783273/879295069834850324/Avatar.png")
                embed3.set_thumbnail(url="https://cdn.discordapp.com/attachments/877796755234783273/879298565380386846/sign-red-error-icon-1.png")
                embed3.add_field(name="Error:", value=f"{e}", inline=False)
                embed3.set_footer(text=f"Requested by {ctx.author.name}")
                await loading_message.delete()
                await ctx.send(embed=embed3)
        
        elif fake_mode == "curr":
            faker = Faker()
            try:
                USssa = faker.currency()
                emf2 = discord.Embed(title="Fake Information Generator", color=0xF00000)
                emf2.set_thumbnail(url="https://www.nicepng.com/png/detail/214-2146883_4-fake-stamp-vector-fake-news-logo-png.png")
                emf2.set_footer(text=f"Requested by {ctx.author.name}")
                emf2.set_author(name="YourBot", icon_url="https://cdn.discordapp.com/attachments/877796755234783273/879295069834850324/Avatar.png")
                emf2.add_field(name="Currency", value=f"Short Name: {USssa[0]} \nFull Name: {USssa[1]}")
                await loading_message.delete()
                await ctx.send(embed=emf2)
            except Exception as e:
                embed3=discord.Embed(title=":red_square: Error!", description="The command was unable to run successfully! ", color=0xff0000)
                embed3.set_author(name="YourBot", icon_url="https://cdn.discordapp.com/attachments/877796755234783273/879295069834850324/Avatar.png")
                embed3.set_thumbnail(url="https://cdn.discordapp.com/attachments/877796755234783273/879298565380386846/sign-red-error-icon-1.png")
                embed3.add_field(name="Error:", value=f"{e}", inline=False)
                embed3.set_footer(text=f"Requested by {ctx.author.name}")
                await loading_message.delete()
                await ctx.send(embed=embed3)
        
        elif fake_mode == "curr code":
            faker = Faker()
            try:
                USssa = faker.currency_code()
                emf2 = discord.Embed(title="Fake Information Generator", color=0xF00000)
                emf2.set_thumbnail(url="https://www.nicepng.com/png/detail/214-2146883_4-fake-stamp-vector-fake-news-logo-png.png")
                emf2.set_footer(text=f"Requested by {ctx.author.name}")
                emf2.set_author(name="YourBot", icon_url="https://cdn.discordapp.com/attachments/877796755234783273/879295069834850324/Avatar.png")
                emf2.add_field(name="Currency Code", value=f"{USssa}")
                await loading_message.delete()
                await ctx.send(embed=emf2)
            except Exception as e:
                embed3=discord.Embed(title=":red_square: Error!", description="The command was unable to run successfully! ", color=0xff0000)
                embed3.set_author(name="YourBot", icon_url="https://cdn.discordapp.com/attachments/877796755234783273/879295069834850324/Avatar.png")
                embed3.set_thumbnail(url="https://cdn.discordapp.com/attachments/877796755234783273/879298565380386846/sign-red-error-icon-1.png")
                embed3.add_field(name="Error:", value=f"{e}", inline=False)
                embed3.set_footer(text=f"Requested by {ctx.author.name}")
                await loading_message.delete()
                await ctx.send(embed=embed3)
        
        elif fake_mode == "curr name":
            faker = Faker()
            try:
                USssa = faker.currency_name()
                emf2 = discord.Embed(title="Fake Information Generator", color=0xF00000)
                emf2.set_thumbnail(url="https://www.nicepng.com/png/detail/214-2146883_4-fake-stamp-vector-fake-news-logo-png.png")
                emf2.set_footer(text=f"Requested by {ctx.author.name}")
                emf2.set_author(name="YourBot", icon_url="https://cdn.discordapp.com/attachments/877796755234783273/879295069834850324/Avatar.png")
                emf2.add_field(name="Currency Code", value=f"{USssa}")
                await loading_message.delete()
                await ctx.send(embed=emf2)
            except Exception as e:
                embed3=discord.Embed(title=":red_square: Error!", description="The command was unable to run successfully! ", color=0xff0000)
                embed3.set_author(name="YourBot", icon_url="https://cdn.discordapp.com/attachments/877796755234783273/879295069834850324/Avatar.png")
                embed3.set_thumbnail(url="https://cdn.discordapp.com/attachments/877796755234783273/879298565380386846/sign-red-error-icon-1.png")
                embed3.add_field(name="Error:", value=f"{e}", inline=False)
                embed3.set_footer(text=f"Requested by {ctx.author.name}")
                await loading_message.delete()
                await ctx.send(embed=embed3)
        
        elif fake_mode.lower().startswith("curr symbol"):
            faker = Faker()
            try:
                try:
                    currcode = fake_mode.split(' ')[-1]
                    USssa = faker.currency_symbol(code=str(currcode))
                except:
                    USssa = faker.currency_symbol()
                emf2 = discord.Embed(title="Fake Information Generator", color=0xF00000)
                emf2.set_thumbnail(url="https://www.nicepng.com/png/detail/214-2146883_4-fake-stamp-vector-fake-news-logo-png.png")
                emf2.set_footer(text=f"Requested by {ctx.author.name}")
                emf2.set_author(name="YourBot", icon_url="https://cdn.discordapp.com/attachments/877796755234783273/879295069834850324/Avatar.png")
                emf2.add_field(name="Currency Code", value=f"{USssa}")
                await loading_message.delete()
                await ctx.send(embed=emf2)
            except Exception as e:
                embed3=discord.Embed(title=":red_square: Error!", description="The command was unable to run successfully! ", color=0xff0000)
                embed3.set_author(name="YourBot", icon_url="https://cdn.discordapp.com/attachments/877796755234783273/879295069834850324/Avatar.png")
                embed3.set_thumbnail(url="https://cdn.discordapp.com/attachments/877796755234783273/879298565380386846/sign-red-error-icon-1.png")
                embed3.add_field(name="Error:", value=f"{e}", inline=False)
                embed3.set_footer(text=f"Requested by {ctx.author.name}")
                await loading_message.delete()
                await ctx.send(embed=embed3)
        
        elif fake_mode == "pricetag":
            faker = Faker()
            try:
                USssa = faker.pricetag()
                emf2 = discord.Embed(title="Fake Information Generator", color=0xF00000)
                emf2.set_thumbnail(url="https://www.nicepng.com/png/detail/214-2146883_4-fake-stamp-vector-fake-news-logo-png.png")
                emf2.set_footer(text=f"Requested by {ctx.author.name}")
                emf2.set_author(name="YourBot", icon_url="https://cdn.discordapp.com/attachments/877796755234783273/879295069834850324/Avatar.png")
                emf2.add_field(name="Pricetag", value=f"{USssa}")
                await loading_message.delete()
                await ctx.send(embed=emf2)
            except Exception as e:
                embed3=discord.Embed(title=":red_square: Error!", description="The command was unable to run successfully! ", color=0xff0000)
                embed3.set_author(name="YourBot", icon_url="https://cdn.discordapp.com/attachments/877796755234783273/879295069834850324/Avatar.png")
                embed3.set_thumbnail(url="https://cdn.discordapp.com/attachments/877796755234783273/879298565380386846/sign-red-error-icon-1.png")
                embed3.add_field(name="Error:", value=f"{e}", inline=False)
                embed3.set_footer(text=f"Requested by {ctx.author.name}")
                await loading_message.delete()
                await ctx.send(embed=embed3)
        
        elif fake_mode == "date":
            faker = Faker()
            try:
                USssa = faker.date()
                emf2 = discord.Embed(title="Fake Information Generator", color=0xF00000)
                emf2.set_thumbnail(url="https://www.nicepng.com/png/detail/214-2146883_4-fake-stamp-vector-fake-news-logo-png.png")
                emf2.set_footer(text=f"Requested by {ctx.author.name}")
                emf2.set_author(name="YourBot", icon_url="https://cdn.discordapp.com/attachments/877796755234783273/879295069834850324/Avatar.png")
                emf2.add_field(name="Date", value=f"{USssa}")
                await loading_message.delete()
                await ctx.send(embed=emf2)
            except Exception as e:
                embed3=discord.Embed(title=":red_square: Error!", description="The command was unable to run successfully! ", color=0xff0000)
                embed3.set_author(name="YourBot", icon_url="https://cdn.discordapp.com/attachments/877796755234783273/879295069834850324/Avatar.png")
                embed3.set_thumbnail(url="https://cdn.discordapp.com/attachments/877796755234783273/879298565380386846/sign-red-error-icon-1.png")
                embed3.add_field(name="Error:", value=f"{e}", inline=False)
                embed3.set_footer(text=f"Requested by {ctx.author.name}")
                await loading_message.delete()
                await ctx.send(embed=embed3)
        
        elif fake_mode == "century":
            faker = Faker()
            try:
                USssa = faker.century()
                emf2 = discord.Embed(title="Fake Information Generator", color=0xF00000)
                emf2.set_thumbnail(url="https://www.nicepng.com/png/detail/214-2146883_4-fake-stamp-vector-fake-news-logo-png.png")
                emf2.set_footer(text=f"Requested by {ctx.author.name}")
                emf2.set_author(name="YourBot", icon_url="https://cdn.discordapp.com/attachments/877796755234783273/879295069834850324/Avatar.png")
                emf2.add_field(name="Century", value=f"{USssa}")
                await loading_message.delete()
                await ctx.send(embed=emf2)
            except Exception as e:
                embed3=discord.Embed(title=":red_square: Error!", description="The command was unable to run successfully! ", color=0xff0000)
                embed3.set_author(name="YourBot", icon_url="https://cdn.discordapp.com/attachments/877796755234783273/879295069834850324/Avatar.png")
                embed3.set_thumbnail(url="https://cdn.discordapp.com/attachments/877796755234783273/879298565380386846/sign-red-error-icon-1.png")
                embed3.add_field(name="Error:", value=f"{e}", inline=False)
                embed3.set_footer(text=f"Requested by {ctx.author.name}")
                await loading_message.delete()
                await ctx.send(embed=embed3)
        
        elif fake_mode == "file name":
            faker = Faker()
            try:
                USssa = faker.file_name()
                emf2 = discord.Embed(title="Fake Information Generator", color=0xF00000)
                emf2.set_thumbnail(url="https://www.nicepng.com/png/detail/214-2146883_4-fake-stamp-vector-fake-news-logo-png.png")
                emf2.set_footer(text=f"Requested by {ctx.author.name}")
                emf2.set_author(name="YourBot", icon_url="https://cdn.discordapp.com/attachments/877796755234783273/879295069834850324/Avatar.png")
                emf2.add_field(name="File Name", value=f"{USssa}")
                await loading_message.delete()
                await ctx.send(embed=emf2)
            except Exception as e:
                embed3=discord.Embed(title=":red_square: Error!", description="The command was unable to run successfully! ", color=0xff0000)
                embed3.set_author(name="YourBot", icon_url="https://cdn.discordapp.com/attachments/877796755234783273/879295069834850324/Avatar.png")
                embed3.set_thumbnail(url="https://cdn.discordapp.com/attachments/877796755234783273/879298565380386846/sign-red-error-icon-1.png")
                embed3.add_field(name="Error:", value=f"{e}", inline=False)
                embed3.set_footer(text=f"Requested by {ctx.author.name}")
                await loading_message.delete()
                await ctx.send(embed=embed3)
        
        elif fake_mode == "file ex":
            faker = Faker()
            try:
                USssa = faker.file_extension()
                emf2 = discord.Embed(title="Fake Information Generator", color=0xF00000)
                emf2.set_thumbnail(url="https://www.nicepng.com/png/detail/214-2146883_4-fake-stamp-vector-fake-news-logo-png.png")
                emf2.set_footer(text=f"Requested by {ctx.author.name}")
                emf2.set_author(name="YourBot", icon_url="https://cdn.discordapp.com/attachments/877796755234783273/879295069834850324/Avatar.png")
                emf2.add_field(name="File Extension", value=f"{USssa}")
                await loading_message.delete()
                await ctx.send(embed=emf2)
            except Exception as e:
                embed3=discord.Embed(title=":red_square: Error!", description="The command was unable to run successfully! ", color=0xff0000)
                embed3.set_author(name="YourBot", icon_url="https://cdn.discordapp.com/attachments/877796755234783273/879295069834850324/Avatar.png")
                embed3.set_thumbnail(url="https://cdn.discordapp.com/attachments/877796755234783273/879298565380386846/sign-red-error-icon-1.png")
                embed3.add_field(name="Error:", value=f"{e}", inline=False)
                embed3.set_footer(text=f"Requested by {ctx.author.name}")
                await loading_message.delete()
                await ctx.send(embed=embed3)
        
        elif fake_mode == "file path":
            faker = Faker()
            try:
                USssa = faker.file_path()
                emf2 = discord.Embed(title="Fake Information Generator", color=0xF00000)
                emf2.set_thumbnail(url="https://www.nicepng.com/png/detail/214-2146883_4-fake-stamp-vector-fake-news-logo-png.png")
                emf2.set_footer(text=f"Requested by {ctx.author.name}")
                emf2.set_author(name="YourBot", icon_url="https://cdn.discordapp.com/attachments/877796755234783273/879295069834850324/Avatar.png")
                emf2.add_field(name="File Extension", value=f"{USssa}")
                await loading_message.delete()
                await ctx.send(embed=emf2)
            except Exception as e:
                embed3=discord.Embed(title=":red_square: Error!", description="The command was unable to run successfully! ", color=0xff0000)
                embed3.set_author(name="YourBot", icon_url="https://cdn.discordapp.com/attachments/877796755234783273/879295069834850324/Avatar.png")
                embed3.set_thumbnail(url="https://cdn.discordapp.com/attachments/877796755234783273/879298565380386846/sign-red-error-icon-1.png")
                embed3.add_field(name="Error:", value=f"{e}", inline=False)
                embed3.set_footer(text=f"Requested by {ctx.author.name}")
                await loading_message.delete()
                await ctx.send(embed=embed3)
        
        elif fake_mode.lower().startswith("mime"):
            faker = Faker()
            try:
                subcall = fake_mode.split(" ")
                try:
                    subc = faker.mime_type(subcall[-1])
                    USssa = faker.mime_type(category=subc)
                except:
                    USssa = faker.mime_type(category=subc)

                emf2 = discord.Embed(title="Fake Information Generator", color=0xF00000)
                emf2.set_thumbnail(url="https://www.nicepng.com/png/detail/214-2146883_4-fake-stamp-vector-fake-news-logo-png.png")
                emf2.set_footer(text=f"Requested by {ctx.author.name}")
                emf2.set_author(name="YourBot", icon_url="https://cdn.discordapp.com/attachments/877796755234783273/879295069834850324/Avatar.png")
                emf2.add_field(name="File Extension", value=f"{USssa}")
                await loading_message.delete()
                await ctx.send(embed=emf2)
            except Exception as e:
                embed3=discord.Embed(title=":red_square: Error!", description="The command was unable to run successfully! ", color=0xff0000)
                embed3.set_author(name="YourBot", icon_url="https://cdn.discordapp.com/attachments/877796755234783273/879295069834850324/Avatar.png")
                embed3.set_thumbnail(url="https://cdn.discordapp.com/attachments/877796755234783273/879298565380386846/sign-red-error-icon-1.png")
                embed3.add_field(name="Error:", value=f"{e}", inline=False)
                embed3.set_footer(text=f"Requested by {ctx.author.name}")
                await loading_message.delete()
                await ctx.send(embed=embed3)
        
        elif fake_mode == "unix device":
            faker = Faker()
            try:
                USssa = faker.unix_device()
                emf2 = discord.Embed(title="Fake Information Generator", color=0xF00000)
                emf2.set_thumbnail(url="https://www.nicepng.com/png/detail/214-2146883_4-fake-stamp-vector-fake-news-logo-png.png")
                emf2.set_footer(text=f"Requested by {ctx.author.name}")
                emf2.set_author(name="YourBot", icon_url="https://cdn.discordapp.com/attachments/877796755234783273/879295069834850324/Avatar.png")
                emf2.add_field(name="Unix Device", value=f"{USssa}")
                await loading_message.delete()
                await ctx.send(embed=emf2)
            except Exception as e:
                embed3=discord.Embed(title=":red_square: Error!", description="The command was unable to run successfully! ", color=0xff0000)
                embed3.set_author(name="YourBot", icon_url="https://cdn.discordapp.com/attachments/877796755234783273/879295069834850324/Avatar.png")
                embed3.set_thumbnail(url="https://cdn.discordapp.com/attachments/877796755234783273/879298565380386846/sign-red-error-icon-1.png")
                embed3.add_field(name="Error:", value=f"{e}", inline=False)
                embed3.set_footer(text=f"Requested by {ctx.author.name}")
                await loading_message.delete()
                await ctx.send(embed=embed3)
        
        elif fake_mode == "unix partition":
            faker = Faker()
            try:
                USssa = faker.unix_partition()
                emf2 = discord.Embed(title="Fake Information Generator", color=0xF00000)
                emf2.set_thumbnail(url="https://www.nicepng.com/png/detail/214-2146883_4-fake-stamp-vector-fake-news-logo-png.png")
                emf2.set_footer(text=f"Requested by {ctx.author.name}")
                emf2.set_author(name="YourBot", icon_url="https://cdn.discordapp.com/attachments/877796755234783273/879295069834850324/Avatar.png")
                emf2.add_field(name="Unix Partition", value=f"{USssa}")
                await loading_message.delete()
                await ctx.send(embed=emf2)
            except Exception as e:
                embed3=discord.Embed(title=":red_square: Error!", description="The command was unable to run successfully! ", color=0xff0000)
                embed3.set_author(name="YourBot", icon_url="https://cdn.discordapp.com/attachments/877796755234783273/879295069834850324/Avatar.png")
                embed3.set_thumbnail(url="https://cdn.discordapp.com/attachments/877796755234783273/879298565380386846/sign-red-error-icon-1.png")
                embed3.add_field(name="Error:", value=f"{e}", inline=False)
                embed3.set_footer(text=f"Requested by {ctx.author.name}")
                await loading_message.delete()
                await ctx.send(embed=embed3)
        
        elif fake_mode == "email":
            faker = Faker()
            try:
                USssa = faker.ascii_email()
                emf2 = discord.Embed(title="Fake Information Generator", color=0xF00000)
                emf2.set_thumbnail(url="https://www.nicepng.com/png/detail/214-2146883_4-fake-stamp-vector-fake-news-logo-png.png")
                emf2.set_footer(text=f"Requested by {ctx.author.name}")
                emf2.set_author(name="YourBot", icon_url="https://cdn.discordapp.com/attachments/877796755234783273/879295069834850324/Avatar.png")
                emf2.add_field(name="Email Address", value=f"{USssa}")
                await loading_message.delete()
                await ctx.send(embed=emf2)
            except Exception as e:
                embed3=discord.Embed(title=":red_square: Error!", description="The command was unable to run successfully! ", color=0xff0000)
                embed3.set_author(name="YourBot", icon_url="https://cdn.discordapp.com/attachments/877796755234783273/879295069834850324/Avatar.png")
                embed3.set_thumbnail(url="https://cdn.discordapp.com/attachments/877796755234783273/879298565380386846/sign-red-error-icon-1.png")
                embed3.add_field(name="Error:", value=f"{e}", inline=False)
                embed3.set_footer(text=f"Requested by {ctx.author.name}")
                await loading_message.delete()
                await ctx.send(embed=embed3)
        
        elif fake_mode == "email free":
            faker = Faker()
            try:
                USssa = faker.ascii_free_email()
                emf2 = discord.Embed(title="Fake Information Generator", color=0xF00000)
                emf2.set_thumbnail(url="https://www.nicepng.com/png/detail/214-2146883_4-fake-stamp-vector-fake-news-logo-png.png")
                emf2.set_footer(text=f"Requested by {ctx.author.name}")
                emf2.set_author(name="YourBot", icon_url="https://cdn.discordapp.com/attachments/877796755234783273/879295069834850324/Avatar.png")
                emf2.add_field(name="Email Address", value=f"{USssa}")
                await loading_message.delete()
                await ctx.send(embed=emf2)
            except Exception as e:
                embed3=discord.Embed(title=":red_square: Error!", description="The command was unable to run successfully! ", color=0xff0000)
                embed3.set_author(name="YourBot", icon_url="https://cdn.discordapp.com/attachments/877796755234783273/879295069834850324/Avatar.png")
                embed3.set_thumbnail(url="https://cdn.discordapp.com/attachments/877796755234783273/879298565380386846/sign-red-error-icon-1.png")
                embed3.add_field(name="Error:", value=f"{e}", inline=False)
                embed3.set_footer(text=f"Requested by {ctx.author.name}")
                await loading_message.delete()
                await ctx.send(embed=embed3)
        
        elif fake_mode == "domain":
            faker = Faker()
            try:
                USssa = faker.domain_name()
                emf2 = discord.Embed(title="Fake Information Generator", color=0xF00000)
                emf2.set_thumbnail(url="https://www.nicepng.com/png/detail/214-2146883_4-fake-stamp-vector-fake-news-logo-png.png")
                emf2.set_footer(text=f"Requested by {ctx.author.name}")
                emf2.set_author(name="YourBot", icon_url="https://cdn.discordapp.com/attachments/877796755234783273/879295069834850324/Avatar.png")
                emf2.add_field(name="Email Address", value=f"{USssa}")
                await loading_message.delete()
                await ctx.send(embed=emf2)
            except Exception as e:
                embed3=discord.Embed(title=":red_square: Error!", description="The command was unable to run successfully! ", color=0xff0000)
                embed3.set_author(name="YourBot", icon_url="https://cdn.discordapp.com/attachments/877796755234783273/879295069834850324/Avatar.png")
                embed3.set_thumbnail(url="https://cdn.discordapp.com/attachments/877796755234783273/879298565380386846/sign-red-error-icon-1.png")
                embed3.add_field(name="Error:", value=f"{e}", inline=False)
                embed3.set_footer(text=f"Requested by {ctx.author.name}")
                await loading_message.delete()
                await ctx.send(embed=embed3)
        
        elif fake_mode == "hostname":
            faker = Faker()
            try:
                USssa = faker.hostname()
                emf2 = discord.Embed(title="Fake Information Generator", color=0xF00000)
                emf2.set_thumbnail(url="https://www.nicepng.com/png/detail/214-2146883_4-fake-stamp-vector-fake-news-logo-png.png")
                emf2.set_footer(text=f"Requested by {ctx.author.name}")
                emf2.set_author(name="YourBot", icon_url="https://cdn.discordapp.com/attachments/877796755234783273/879295069834850324/Avatar.png")
                emf2.add_field(name="Hostname", value=f"{USssa}")
                await loading_message.delete()
                await ctx.send(embed=emf2)
            except Exception as e:
                embed3=discord.Embed(title=":red_square: Error!", description="The command was unable to run successfully! ", color=0xff0000)
                embed3.set_author(name="YourBot", icon_url="https://cdn.discordapp.com/attachments/877796755234783273/879295069834850324/Avatar.png")
                embed3.set_thumbnail(url="https://cdn.discordapp.com/attachments/877796755234783273/879298565380386846/sign-red-error-icon-1.png")
                embed3.add_field(name="Error:", value=f"{e}", inline=False)
                embed3.set_footer(text=f"Requested by {ctx.author.name}")
                await loading_message.delete()
                await ctx.send(embed=embed3)
        
        elif fake_mode == "http method":
            faker = Faker()
            try:
                USssa = faker.http_method()
                emf2 = discord.Embed(title="Fake Information Generator", color=0xF00000)
                emf2.set_thumbnail(url="https://www.nicepng.com/png/detail/214-2146883_4-fake-stamp-vector-fake-news-logo-png.png")
                emf2.set_footer(text=f"Requested by {ctx.author.name}")
                emf2.set_author(name="YourBot", icon_url="https://cdn.discordapp.com/attachments/877796755234783273/879295069834850324/Avatar.png")
                emf2.add_field(name="HTTP METHOD", value=f"{USssa}")
                await loading_message.delete()
                await ctx.send(embed=emf2)
            except Exception as e:
                embed3=discord.Embed(title=":red_square: Error!", description="The command was unable to run successfully! ", color=0xff0000)
                embed3.set_author(name="YourBot", icon_url="https://cdn.discordapp.com/attachments/877796755234783273/879295069834850324/Avatar.png")
                embed3.set_thumbnail(url="https://cdn.discordapp.com/attachments/877796755234783273/879298565380386846/sign-red-error-icon-1.png")
                embed3.add_field(name="Error:", value=f"{e}", inline=False)
                embed3.set_footer(text=f"Requested by {ctx.author.name}")
                await loading_message.delete()
                await ctx.send(embed=embed3)
        
        elif fake_mode == "iana":
            faker = Faker()
            try:
                USssa = faker.iana_id()
                emf2 = discord.Embed(title="Fake Information Generator", color=0xF00000)
                emf2.set_thumbnail(url="https://www.nicepng.com/png/detail/214-2146883_4-fake-stamp-vector-fake-news-logo-png.png")
                emf2.set_footer(text=f"Requested by {ctx.author.name}")
                emf2.set_author(name="YourBot", icon_url="https://cdn.discordapp.com/attachments/877796755234783273/879295069834850324/Avatar.png")
                emf2.add_field(name="IANA Registrar ID", value=f"{USssa}")
                await loading_message.delete()
                await ctx.send(embed=emf2)
            except Exception as e:
                embed3=discord.Embed(title=":red_square: Error!", description="The command was unable to run successfully! ", color=0xff0000)
                embed3.set_author(name="YourBot", icon_url="https://cdn.discordapp.com/attachments/877796755234783273/879295069834850324/Avatar.png")
                embed3.set_thumbnail(url="https://cdn.discordapp.com/attachments/877796755234783273/879298565380386846/sign-red-error-icon-1.png")
                embed3.add_field(name="Error:", value=f"{e}", inline=False)
                embed3.set_footer(text=f"Requested by {ctx.author.name}")
                await loading_message.delete()
                await ctx.send(embed=embed3)
        
        elif fake_mode == "img url":
            faker = Faker()
            try:
                USssa = faker.image_url()
                emf2 = discord.Embed(title="Fake Information Generator", color=0xF00000)
                emf2.set_thumbnail(url="https://www.nicepng.com/png/detail/214-2146883_4-fake-stamp-vector-fake-news-logo-png.png")
                emf2.set_footer(text=f"Requested by {ctx.author.name}")
                emf2.set_author(name="YourBot", icon_url="https://cdn.discordapp.com/attachments/877796755234783273/879295069834850324/Avatar.png")
                emf2.add_field(name="Image URL", value=f"{USssa}")
                await loading_message.delete()
                await ctx.send(embed=emf2)
            except Exception as e:
                embed3=discord.Embed(title=":red_square: Error!", description="The command was unable to run successfully! ", color=0xff0000)
                embed3.set_author(name="YourBot", icon_url="https://cdn.discordapp.com/attachments/877796755234783273/879295069834850324/Avatar.png")
                embed3.set_thumbnail(url="https://cdn.discordapp.com/attachments/877796755234783273/879298565380386846/sign-red-error-icon-1.png")
                embed3.add_field(name="Error:", value=f"{e}", inline=False)
                embed3.set_footer(text=f"Requested by {ctx.author.name}")
                await loading_message.delete()
                await ctx.send(embed=embed3)
        
        elif fake_mode == "ipv4":
            faker = Faker()
            try:
                USssa = faker.ipv4()
                emf2 = discord.Embed(title="Fake Information Generator", color=0xF00000)
                emf2.set_thumbnail(url="https://www.nicepng.com/png/detail/214-2146883_4-fake-stamp-vector-fake-news-logo-png.png")
                emf2.set_footer(text=f"Requested by {ctx.author.name}")
                emf2.set_author(name="YourBot", icon_url="https://cdn.discordapp.com/attachments/877796755234783273/879295069834850324/Avatar.png")
                emf2.add_field(name="IPv4", value=f"{USssa}")
                await loading_message.delete()
                await ctx.send(embed=emf2)
            except Exception as e:
                embed3=discord.Embed(title=":red_square: Error!", description="The command was unable to run successfully! ", color=0xff0000)
                embed3.set_author(name="YourBot", icon_url="https://cdn.discordapp.com/attachments/877796755234783273/879295069834850324/Avatar.png")
                embed3.set_thumbnail(url="https://cdn.discordapp.com/attachments/877796755234783273/879298565380386846/sign-red-error-icon-1.png")
                embed3.add_field(name="Error:", value=f"{e}", inline=False)
                embed3.set_footer(text=f"Requested by {ctx.author.name}")
                await loading_message.delete()
                await ctx.send(embed=embed3)
        
        elif fake_mode == "ipv4 class":
            faker = Faker()
            try:
                USssa = faker.ipv4_network_class()
                emf2 = discord.Embed(title="Fake Information Generator", color=0xF00000)
                emf2.set_thumbnail(url="https://www.nicepng.com/png/detail/214-2146883_4-fake-stamp-vector-fake-news-logo-png.png")
                emf2.set_footer(text=f"Requested by {ctx.author.name}")
                emf2.set_author(name="YourBot", icon_url="https://cdn.discordapp.com/attachments/877796755234783273/879295069834850324/Avatar.png")
                emf2.add_field(name="IPv4 Netwrok Class", value=f"{USssa}")
                await loading_message.delete()
                await ctx.send(embed=emf2)
            except Exception as e:
                embed3=discord.Embed(title=":red_square: Error!", description="The command was unable to run successfully! ", color=0xff0000)
                embed3.set_author(name="YourBot", icon_url="https://cdn.discordapp.com/attachments/877796755234783273/879295069834850324/Avatar.png")
                embed3.set_thumbnail(url="https://cdn.discordapp.com/attachments/877796755234783273/879298565380386846/sign-red-error-icon-1.png")
                embed3.add_field(name="Error:", value=f"{e}", inline=False)
                embed3.set_footer(text=f"Requested by {ctx.author.name}")
                await loading_message.delete()
                await ctx.send(embed=embed3)
        
        elif fake_mode == "ipv4 private":
            faker = Faker()
            try:
                USssa = faker.ipv4_private()
                emf2 = discord.Embed(title="Fake Information Generator", color=0xF00000)
                emf2.set_thumbnail(url="https://www.nicepng.com/png/detail/214-2146883_4-fake-stamp-vector-fake-news-logo-png.png")
                emf2.set_footer(text=f"Requested by {ctx.author.name}")
                emf2.set_author(name="YourBot", icon_url="https://cdn.discordapp.com/attachments/877796755234783273/879295069834850324/Avatar.png")
                emf2.add_field(name="a Private IPv4 Address", value=f"{USssa}")
                await loading_message.delete()
                await ctx.send(embed=emf2)
            except Exception as e:
                embed3=discord.Embed(title=":red_square: Error!", description="The command was unable to run successfully! ", color=0xff0000)
                embed3.set_author(name="YourBot", icon_url="https://cdn.discordapp.com/attachments/877796755234783273/879295069834850324/Avatar.png")
                embed3.set_thumbnail(url="https://cdn.discordapp.com/attachments/877796755234783273/879298565380386846/sign-red-error-icon-1.png")
                embed3.add_field(name="Error:", value=f"{e}", inline=False)
                embed3.set_footer(text=f"Requested by {ctx.author.name}")
                await loading_message.delete()
                await ctx.send(embed=embed3)
        
        elif fake_mode == "ipv4 public":
            faker = Faker()
            try:
                USssa = faker.ipv4_public()
                emf2 = discord.Embed(title="Fake Information Generator", color=0xF00000)
                emf2.set_thumbnail(url="https://www.nicepng.com/png/detail/214-2146883_4-fake-stamp-vector-fake-news-logo-png.png")
                emf2.set_footer(text=f"Requested by {ctx.author.name}")
                emf2.set_author(name="YourBot", icon_url="https://cdn.discordapp.com/attachments/877796755234783273/879295069834850324/Avatar.png")
                emf2.add_field(name="a Public IPv4 Address", value=f"{USssa}")
                await loading_message.delete()
                await ctx.send(embed=emf2)
            except Exception as e:
                embed3=discord.Embed(title=":red_square: Error!", description="The command was unable to run successfully! ", color=0xff0000)
                embed3.set_author(name="YourBot", icon_url="https://cdn.discordapp.com/attachments/877796755234783273/879295069834850324/Avatar.png")
                embed3.set_thumbnail(url="https://cdn.discordapp.com/attachments/877796755234783273/879298565380386846/sign-red-error-icon-1.png")
                embed3.add_field(name="Error:", value=f"{e}", inline=False)
                embed3.set_footer(text=f"Requested by {ctx.author.name}")
                await loading_message.delete()
                await ctx.send(embed=embed3)
        
        elif fake_mode == "ipv6":
            faker = Faker()
            try:
                USssa = faker.ipv6()
                emf2 = discord.Embed(title="Fake Information Generator", color=0xF00000)
                emf2.set_thumbnail(url="https://www.nicepng.com/png/detail/214-2146883_4-fake-stamp-vector-fake-news-logo-png.png")
                emf2.set_footer(text=f"Requested by {ctx.author.name}")
                emf2.set_author(name="YourBot", icon_url="https://cdn.discordapp.com/attachments/877796755234783273/879295069834850324/Avatar.png")
                emf2.add_field(name="IPv6", value=f"{USssa}")
                await loading_message.delete()
                await ctx.send(embed=emf2)
            except Exception as e:
                embed3=discord.Embed(title=":red_square: Error!", description="The command was unable to run successfully! ", color=0xff0000)
                embed3.set_author(name="YourBot", icon_url="https://cdn.discordapp.com/attachments/877796755234783273/879295069834850324/Avatar.png")
                embed3.set_thumbnail(url="https://cdn.discordapp.com/attachments/877796755234783273/879298565380386846/sign-red-error-icon-1.png")
                embed3.add_field(name="Error:", value=f"{e}", inline=False)
                embed3.set_footer(text=f"Requested by {ctx.author.name}")
                await loading_message.delete()
                await ctx.send(embed=embed3)
        
        elif fake_mode == "macaddr":
            faker = Faker()
            try:
                USssa = faker.mac_address()
                emf2 = discord.Embed(title="Fake Information Generator", color=0xF00000)
                emf2.set_thumbnail(url="https://www.nicepng.com/png/detail/214-2146883_4-fake-stamp-vector-fake-news-logo-png.png")
                emf2.set_footer(text=f"Requested by {ctx.author.name}")
                emf2.set_author(name="YourBot", icon_url="https://cdn.discordapp.com/attachments/877796755234783273/879295069834850324/Avatar.png")
                emf2.add_field(name="Mac Address", value=f"{USssa}")
                await loading_message.delete()
                await ctx.send(embed=emf2)
            except Exception as e:
                embed3=discord.Embed(title=":red_square: Error!", description="The command was unable to run successfully! ", color=0xff0000)
                embed3.set_author(name="YourBot", icon_url="https://cdn.discordapp.com/attachments/877796755234783273/879295069834850324/Avatar.png")
                embed3.set_thumbnail(url="https://cdn.discordapp.com/attachments/877796755234783273/879298565380386846/sign-red-error-icon-1.png")
                embed3.add_field(name="Error:", value=f"{e}", inline=False)
                embed3.set_footer(text=f"Requested by {ctx.author.name}")
                await loading_message.delete()
                await ctx.send(embed=embed3)
        
        elif fake_mode == "nic handle":
            faker = Faker()
            try:
                USssa = faker.nic_handle()
                emf2 = discord.Embed(title="Fake Information Generator", color=0xF00000)
                emf2.set_thumbnail(url="https://www.nicepng.com/png/detail/214-2146883_4-fake-stamp-vector-fake-news-logo-png.png")
                emf2.set_footer(text=f"Requested by {ctx.author.name}")
                emf2.set_author(name="YourBot", icon_url="https://cdn.discordapp.com/attachments/877796755234783273/879295069834850324/Avatar.png")
                emf2.add_field(name="NIC Handle", value=f"{USssa}")
                await loading_message.delete()
                await ctx.send(embed=emf2)
            except Exception as e:
                embed3=discord.Embed(title=":red_square: Error!", description="The command was unable to run successfully! ", color=0xff0000)
                embed3.set_author(name="YourBot", icon_url="https://cdn.discordapp.com/attachments/877796755234783273/879295069834850324/Avatar.png")
                embed3.set_thumbnail(url="https://cdn.discordapp.com/attachments/877796755234783273/879298565380386846/sign-red-error-icon-1.png")
                embed3.add_field(name="Error:", value=f"{e}", inline=False)
                embed3.set_footer(text=f"Requested by {ctx.author.name}")
                await loading_message.delete()
                await ctx.send(embed=embed3)
        
        elif fake_mode == "port":
            faker = Faker()
            try:
                USssa = faker.port_number()
                emf2 = discord.Embed(title="Fake Information Generator", color=0xF00000)
                emf2.set_thumbnail(url="https://www.nicepng.com/png/detail/214-2146883_4-fake-stamp-vector-fake-news-logo-png.png")
                emf2.set_footer(text=f"Requested by {ctx.author.name}")
                emf2.set_author(name="YourBot", icon_url="https://cdn.discordapp.com/attachments/877796755234783273/879295069834850324/Avatar.png")
                emf2.add_field(name="Port Number", value=f"{USssa}")
                await loading_message.delete()
                await ctx.send(embed=emf2)
            except Exception as e:
                embed3=discord.Embed(title=":red_square: Error!", description="The command was unable to run successfully! ", color=0xff0000)
                embed3.set_author(name="YourBot", icon_url="https://cdn.discordapp.com/attachments/877796755234783273/879295069834850324/Avatar.png")
                embed3.set_thumbnail(url="https://cdn.discordapp.com/attachments/877796755234783273/879298565380386846/sign-red-error-icon-1.png")
                embed3.add_field(name="Error:", value=f"{e}", inline=False)
                embed3.set_footer(text=f"Requested by {ctx.author.name}")
                await loading_message.delete()
                await ctx.send(embed=embed3)
        
        elif fake_mode == "ripeid":
            faker = Faker()
            try:
                USssa = faker.ripe_id()
                emf2 = discord.Embed(title="Fake Information Generator", color=0xF00000)
                emf2.set_thumbnail(url="https://www.nicepng.com/png/detail/214-2146883_4-fake-stamp-vector-fake-news-logo-png.png")
                emf2.set_footer(text=f"Requested by {ctx.author.name}")
                emf2.set_author(name="YourBot", icon_url="https://cdn.discordapp.com/attachments/877796755234783273/879295069834850324/Avatar.png")
                emf2.add_field(name="Port Number", value=f"{USssa}")
                await loading_message.delete()
                await ctx.send(embed=emf2)
            except Exception as e:
                embed3=discord.Embed(title=":red_square: Error!", description="The command was unable to run successfully! ", color=0xff0000)
                embed3.set_author(name="YourBot", icon_url="https://cdn.discordapp.com/attachments/877796755234783273/879295069834850324/Avatar.png")
                embed3.set_thumbnail(url="https://cdn.discordapp.com/attachments/877796755234783273/879298565380386846/sign-red-error-icon-1.png")
                embed3.add_field(name="Error:", value=f"{e}", inline=False)
                embed3.set_footer(text=f"Requested by {ctx.author.name}")
                await loading_message.delete()
                await ctx.send(embed=embed3)
        
        elif fake_mode == "slug":
            faker = Faker()
            try:
                USssa = faker.slug()
                emf2 = discord.Embed(title="Fake Information Generator", color=0xF00000)
                emf2.set_thumbnail(url="https://www.nicepng.com/png/detail/214-2146883_4-fake-stamp-vector-fake-news-logo-png.png")
                emf2.set_footer(text=f"Requested by {ctx.author.name}")
                emf2.set_author(name="YourBot", icon_url="https://cdn.discordapp.com/attachments/877796755234783273/879295069834850324/Avatar.png")
                emf2.add_field(name="Slug", value=f"{USssa}")
                await loading_message.delete()
                await ctx.send(embed=emf2)
            except Exception as e:
                embed3=discord.Embed(title=":red_square: Error!", description="The command was unable to run successfully! ", color=0xff0000)
                embed3.set_author(name="YourBot", icon_url="https://cdn.discordapp.com/attachments/877796755234783273/879295069834850324/Avatar.png")
                embed3.set_thumbnail(url="https://cdn.discordapp.com/attachments/877796755234783273/879298565380386846/sign-red-error-icon-1.png")
                embed3.add_field(name="Error:", value=f"{e}", inline=False)
                embed3.set_footer(text=f"Requested by {ctx.author.name}")
                await loading_message.delete()
                await ctx.send(embed=embed3)
        
        elif fake_mode == "tld":
            faker = Faker()
            try:
                USssa = faker.tld()
                emf2 = discord.Embed(title="Fake Information Generator", color=0xF00000)
                emf2.set_thumbnail(url="https://www.nicepng.com/png/detail/214-2146883_4-fake-stamp-vector-fake-news-logo-png.png")
                emf2.set_footer(text=f"Requested by {ctx.author.name}")
                emf2.set_author(name="YourBot", icon_url="https://cdn.discordapp.com/attachments/877796755234783273/879295069834850324/Avatar.png")
                emf2.add_field(name="TLD", value=f"{USssa}")
                await loading_message.delete()
                await ctx.send(embed=emf2)
            except Exception as e:
                embed3=discord.Embed(title=":red_square: Error!", description="The command was unable to run successfully! ", color=0xff0000)
                embed3.set_author(name="YourBot", icon_url="https://cdn.discordapp.com/attachments/877796755234783273/879295069834850324/Avatar.png")
                embed3.set_thumbnail(url="https://cdn.discordapp.com/attachments/877796755234783273/879298565380386846/sign-red-error-icon-1.png")
                embed3.add_field(name="Error:", value=f"{e}", inline=False)
                embed3.set_footer(text=f"Requested by {ctx.author.name}")
                await loading_message.delete()
                await ctx.send(embed=embed3)
        
        elif fake_mode == "uri":
            faker = Faker()
            try:
                USssa = faker.uri()
                emf2 = discord.Embed(title="Fake Information Generator", color=0xF00000)
                emf2.set_thumbnail(url="https://www.nicepng.com/png/detail/214-2146883_4-fake-stamp-vector-fake-news-logo-png.png")
                emf2.set_footer(text=f"Requested by {ctx.author.name}")
                emf2.set_author(name="YourBot", icon_url="https://cdn.discordapp.com/attachments/877796755234783273/879295069834850324/Avatar.png")
                emf2.add_field(name="URI", value=f"{USssa}")
                await loading_message.delete()
                await ctx.send(embed=emf2)
            except Exception as e:
                embed3=discord.Embed(title=":red_square: Error!", description="The command was unable to run successfully! ", color=0xff0000)
                embed3.set_author(name="YourBot", icon_url="https://cdn.discordapp.com/attachments/877796755234783273/879295069834850324/Avatar.png")
                embed3.set_thumbnail(url="https://cdn.discordapp.com/attachments/877796755234783273/879298565380386846/sign-red-error-icon-1.png")
                embed3.add_field(name="Error:", value=f"{e}", inline=False)
                embed3.set_footer(text=f"Requested by {ctx.author.name}")
                await loading_message.delete()
                await ctx.send(embed=embed3)
        
        elif fake_mode == "uri ex":
            faker = Faker()
            try:
                USssa = faker.uri_extension()
                emf2 = discord.Embed(title="Fake Information Generator", color=0xF00000)
                emf2.set_thumbnail(url="https://www.nicepng.com/png/detail/214-2146883_4-fake-stamp-vector-fake-news-logo-png.png")
                emf2.set_footer(text=f"Requested by {ctx.author.name}")
                emf2.set_author(name="YourBot", icon_url="https://cdn.discordapp.com/attachments/877796755234783273/879295069834850324/Avatar.png")
                emf2.add_field(name="URI Extension", value=f"{USssa}")
                await loading_message.delete()
                await ctx.send(embed=emf2)
            except Exception as e:
                embed3=discord.Embed(title=":red_square: Error!", description="The command was unable to run successfully! ", color=0xff0000)
                embed3.set_author(name="YourBot", icon_url="https://cdn.discordapp.com/attachments/877796755234783273/879295069834850324/Avatar.png")
                embed3.set_thumbnail(url="https://cdn.discordapp.com/attachments/877796755234783273/879298565380386846/sign-red-error-icon-1.png")
                embed3.add_field(name="Error:", value=f"{e}", inline=False)
                embed3.set_footer(text=f"Requested by {ctx.author.name}")
                await loading_message.delete()
                await ctx.send(embed=embed3)
        
        elif fake_mode == "url":
            faker = Faker()
            try:
                USssa = faker.url()
                emf2 = discord.Embed(title="Fake Information Generator", color=0xF00000)
                emf2.set_thumbnail(url="https://www.nicepng.com/png/detail/214-2146883_4-fake-stamp-vector-fake-news-logo-png.png")
                emf2.set_footer(text=f"Requested by {ctx.author.name}")
                emf2.set_author(name="YourBot", icon_url="https://cdn.discordapp.com/attachments/877796755234783273/879295069834850324/Avatar.png")
                emf2.add_field(name="URL", value=f"{USssa}")
                await loading_message.delete()
                await ctx.send(embed=emf2)
            except Exception as e:
                embed3=discord.Embed(title=":red_square: Error!", description="The command was unable to run successfully! ", color=0xff0000)
                embed3.set_author(name="YourBot", icon_url="https://cdn.discordapp.com/attachments/877796755234783273/879295069834850324/Avatar.png")
                embed3.set_thumbnail(url="https://cdn.discordapp.com/attachments/877796755234783273/879298565380386846/sign-red-error-icon-1.png")
                embed3.add_field(name="Error:", value=f"{e}", inline=False)
                embed3.set_footer(text=f"Requested by {ctx.author.name}")
                await loading_message.delete()
                await ctx.send(embed=embed3)
        
        elif fake_mode == "username":
            faker = Faker()
            try:
                USssa = faker.user_name()
                emf2 = discord.Embed(title="Fake Information Generator", color=0xF00000)
                emf2.set_thumbnail(url="https://www.nicepng.com/png/detail/214-2146883_4-fake-stamp-vector-fake-news-logo-png.png")
                emf2.set_footer(text=f"Requested by {ctx.author.name}")
                emf2.set_author(name="YourBot", icon_url="https://cdn.discordapp.com/attachments/877796755234783273/879295069834850324/Avatar.png")
                emf2.add_field(name="Username", value=f"{USssa}")
                await loading_message.delete()
                await ctx.send(embed=emf2)
            except Exception as e:
                embed3=discord.Embed(title=":red_square: Error!", description="The command was unable to run successfully! ", color=0xff0000)
                embed3.set_author(name="YourBot", icon_url="https://cdn.discordapp.com/attachments/877796755234783273/879295069834850324/Avatar.png")
                embed3.set_thumbnail(url="https://cdn.discordapp.com/attachments/877796755234783273/879298565380386846/sign-red-error-icon-1.png")
                embed3.add_field(name="Error:", value=f"{e}", inline=False)
                embed3.set_footer(text=f"Requested by {ctx.author.name}")
                await loading_message.delete()
                await ctx.send(embed=embed3)
        
        elif fake_mode == "isbn10":
            faker = Faker()
            try:
                USssa = faker.isbn10()
                emf2 = discord.Embed(title="Fake Information Generator", color=0xF00000)
                emf2.set_thumbnail(url="https://www.nicepng.com/png/detail/214-2146883_4-fake-stamp-vector-fake-news-logo-png.png")
                emf2.set_footer(text=f"Requested by {ctx.author.name}")
                emf2.set_author(name="YourBot", icon_url="https://cdn.discordapp.com/attachments/877796755234783273/879295069834850324/Avatar.png")
                emf2.add_field(name="ISBN 10", value=f"{USssa}")
                await loading_message.delete()
                await ctx.send(embed=emf2)
            except Exception as e:
                embed3=discord.Embed(title=":red_square: Error!", description="The command was unable to run successfully! ", color=0xff0000)
                embed3.set_author(name="YourBot", icon_url="https://cdn.discordapp.com/attachments/877796755234783273/879295069834850324/Avatar.png")
                embed3.set_thumbnail(url="https://cdn.discordapp.com/attachments/877796755234783273/879298565380386846/sign-red-error-icon-1.png")
                embed3.add_field(name="Error:", value=f"{e}", inline=False)
                embed3.set_footer(text=f"Requested by {ctx.author.name}")
                await loading_message.delete()
                await ctx.send(embed=embed3)
        
        elif fake_mode == "isbn13":
            faker = Faker()
            try:
                USssa = faker.isbn13()
                emf2 = discord.Embed(title="Fake Information Generator", color=0xF00000)
                emf2.set_thumbnail(url="https://www.nicepng.com/png/detail/214-2146883_4-fake-stamp-vector-fake-news-logo-png.png")
                emf2.set_footer(text=f"Requested by {ctx.author.name}")
                emf2.set_author(name="YourBot", icon_url="https://cdn.discordapp.com/attachments/877796755234783273/879295069834850324/Avatar.png")
                emf2.add_field(name="ISBN 13", value=f"{USssa}")
                await loading_message.delete()
                await ctx.send(embed=emf2)
            except Exception as e:
                embed3=discord.Embed(title=":red_square: Error!", description="The command was unable to run successfully! ", color=0xff0000)
                embed3.set_author(name="YourBot", icon_url="https://cdn.discordapp.com/attachments/877796755234783273/879295069834850324/Avatar.png")
                embed3.set_thumbnail(url="https://cdn.discordapp.com/attachments/877796755234783273/879298565380386846/sign-red-error-icon-1.png")
                embed3.add_field(name="Error:", value=f"{e}", inline=False)
                embed3.set_footer(text=f"Requested by {ctx.author.name}")
                await loading_message.delete()
                await ctx.send(embed=embed3)
        
        elif fake_mode == "paragraph":
            faker = Faker()
            try:
                USssa = faker.paragraphs()
                emf2 = discord.Embed(title="Fake Information Generator", color=0xF00000)
                emf2.set_thumbnail(url="https://www.nicepng.com/png/detail/214-2146883_4-fake-stamp-vector-fake-news-logo-png.png")
                emf2.set_footer(text=f"Requested by {ctx.author.name}")
                emf2.set_author(name="YourBot", icon_url="https://cdn.discordapp.com/attachments/877796755234783273/879295069834850324/Avatar.png")
                emf2.add_field(name="Paragraph", value=f"{''.join(USssa)}")
                await loading_message.delete()
                await ctx.send(embed=emf2)
            except Exception as e:
                embed3=discord.Embed(title=":red_square: Error!", description="The command was unable to run successfully! ", color=0xff0000)
                embed3.set_author(name="YourBot", icon_url="https://cdn.discordapp.com/attachments/877796755234783273/879295069834850324/Avatar.png")
                embed3.set_thumbnail(url="https://cdn.discordapp.com/attachments/877796755234783273/879298565380386846/sign-red-error-icon-1.png")
                embed3.add_field(name="Error:", value=f"{e}", inline=False)
                embed3.set_footer(text=f"Requested by {ctx.author.name}")
                await loading_message.delete()
                await ctx.send(embed=embed3)
        
        elif fake_mode == "sentence":
            faker = Faker()
            try:
                USssa = faker.sentence()
                emf2 = discord.Embed(title="Fake Information Generator", color=0xF00000)
                emf2.set_thumbnail(url="https://www.nicepng.com/png/detail/214-2146883_4-fake-stamp-vector-fake-news-logo-png.png")
                emf2.set_footer(text=f"Requested by {ctx.author.name}")
                emf2.set_author(name="YourBot", icon_url="https://cdn.discordapp.com/attachments/877796755234783273/879295069834850324/Avatar.png")
                emf2.add_field(name="Sentence", value=f"{USssa}")
                await loading_message.delete()
                await ctx.send(embed=emf2)
            except Exception as e:
                embed3=discord.Embed(title=":red_square: Error!", description="The command was unable to run successfully! ", color=0xff0000)
                embed3.set_author(name="YourBot", icon_url="https://cdn.discordapp.com/attachments/877796755234783273/879295069834850324/Avatar.png")
                embed3.set_thumbnail(url="https://cdn.discordapp.com/attachments/877796755234783273/879298565380386846/sign-red-error-icon-1.png")
                embed3.add_field(name="Error:", value=f"{e}", inline=False)
                embed3.set_footer(text=f"Requested by {ctx.author.name}")
                await loading_message.delete()
                await ctx.send(embed=embed3)
        
        elif fake_mode == "text":
            faker = Faker()
            try:
                USssa = faker.texts()
                emf2 = discord.Embed(title="Fake Information Generator", color=0xF00000)
                emf2.set_thumbnail(url="https://www.nicepng.com/png/detail/214-2146883_4-fake-stamp-vector-fake-news-logo-png.png")
                emf2.set_footer(text=f"Requested by {ctx.author.name}")
                emf2.set_author(name="YourBot", icon_url="https://cdn.discordapp.com/attachments/877796755234783273/879295069834850324/Avatar.png")
                emf2.add_field(name="Text", value=f"{USssa}")
                await loading_message.delete()
                await ctx.send(embed=emf2)
            except Exception as e:
                embed3=discord.Embed(title=":red_square: Error!", description="The command was unable to run successfully! ", color=0xff0000)
                embed3.set_author(name="YourBot", icon_url="https://cdn.discordapp.com/attachments/877796755234783273/879295069834850324/Avatar.png")
                embed3.set_thumbnail(url="https://cdn.discordapp.com/attachments/877796755234783273/879298565380386846/sign-red-error-icon-1.png")
                embed3.add_field(name="Error:", value=f"{e}", inline=False)
                embed3.set_footer(text=f"Requested by {ctx.author.name}")
                await loading_message.delete()
                await ctx.send(embed=embed3)
        
        elif fake_mode == "word":
            faker = Faker()
            try:
                USssa = faker.word()
                emf2 = discord.Embed(title="Fake Information Generator", color=0xF00000)
                emf2.set_thumbnail(url="https://www.nicepng.com/png/detail/214-2146883_4-fake-stamp-vector-fake-news-logo-png.png")
                emf2.set_footer(text=f"Requested by {ctx.author.name}")
                emf2.set_author(name="YourBot", icon_url="https://cdn.discordapp.com/attachments/877796755234783273/879295069834850324/Avatar.png")
                emf2.add_field(name="Word", value=f"{USssa}")
                await loading_message.delete()
                await ctx.send(embed=emf2)
            except Exception as e:
                embed3=discord.Embed(title=":red_square: Error!", description="The command was unable to run successfully! ", color=0xff0000)
                embed3.set_author(name="YourBot", icon_url="https://cdn.discordapp.com/attachments/877796755234783273/879295069834850324/Avatar.png")
                embed3.set_thumbnail(url="https://cdn.discordapp.com/attachments/877796755234783273/879298565380386846/sign-red-error-icon-1.png")
                embed3.add_field(name="Error:", value=f"{e}", inline=False)
                embed3.set_footer(text=f"Requested by {ctx.author.name}")
                await loading_message.delete()
                await ctx.send(embed=embed3)
        
        elif fake_mode == "fname":
            faker = Faker()
            try:
                USssa = faker.first_name()
                emf2 = discord.Embed(title="Fake Information Generator", color=0xF00000)
                emf2.set_thumbnail(url="https://www.nicepng.com/png/detail/214-2146883_4-fake-stamp-vector-fake-news-logo-png.png")
                emf2.set_footer(text=f"Requested by {ctx.author.name}")
                emf2.set_author(name="YourBot", icon_url="https://cdn.discordapp.com/attachments/877796755234783273/879295069834850324/Avatar.png")
                emf2.add_field(name="First Name", value=f"{USssa}")
                await loading_message.delete()
                await ctx.send(embed=emf2)
            except Exception as e:
                embed3=discord.Embed(title=":red_square: Error!", description="The command was unable to run successfully! ", color=0xff0000)
                embed3.set_author(name="YourBot", icon_url="https://cdn.discordapp.com/attachments/877796755234783273/879295069834850324/Avatar.png")
                embed3.set_thumbnail(url="https://cdn.discordapp.com/attachments/877796755234783273/879298565380386846/sign-red-error-icon-1.png")
                embed3.add_field(name="Error:", value=f"{e}", inline=False)
                embed3.set_footer(text=f"Requested by {ctx.author.name}")
                await loading_message.delete()
                await ctx.send(embed=embed3)
        
        elif fake_mode == "fname male":
            faker = Faker()
            try:
                USssa = faker.first_name_male()
                emf2 = discord.Embed(title="Fake Information Generator", color=0xF00000)
                emf2.set_thumbnail(url="https://www.nicepng.com/png/detail/214-2146883_4-fake-stamp-vector-fake-news-logo-png.png")
                emf2.set_footer(text=f"Requested by {ctx.author.name}")
                emf2.set_author(name="YourBot", icon_url="https://cdn.discordapp.com/attachments/877796755234783273/879295069834850324/Avatar.png")
                emf2.add_field(name="First Name - Male", value=f"{USssa}")
                await loading_message.delete()
                await ctx.send(embed=emf2)
            except Exception as e:
                embed3=discord.Embed(title=":red_square: Error!", description="The command was unable to run successfully! ", color=0xff0000)
                embed3.set_author(name="YourBot", icon_url="https://cdn.discordapp.com/attachments/877796755234783273/879295069834850324/Avatar.png")
                embed3.set_thumbnail(url="https://cdn.discordapp.com/attachments/877796755234783273/879298565380386846/sign-red-error-icon-1.png")
                embed3.add_field(name="Error:", value=f"{e}", inline=False)
                embed3.set_footer(text=f"Requested by {ctx.author.name}")
                await loading_message.delete()
                await ctx.send(embed=embed3)
        
        elif fake_mode == "fname female":
            faker = Faker()
            try:
                USssa = faker.first_name_male()
                emf2 = discord.Embed(title="Fake Information Generator", color=0xF00000)
                emf2.set_thumbnail(url="https://www.nicepng.com/png/detail/214-2146883_4-fake-stamp-vector-fake-news-logo-png.png")
                emf2.set_footer(text=f"Requested by {ctx.author.name}")
                emf2.set_author(name="YourBot", icon_url="https://cdn.discordapp.com/attachments/877796755234783273/879295069834850324/Avatar.png")
                emf2.add_field(name="First Name - Female", value=f"{USssa}")
                await loading_message.delete()
                await ctx.send(embed=emf2)
            except Exception as e:
                embed3=discord.Embed(title=":red_square: Error!", description="The command was unable to run successfully! ", color=0xff0000)
                embed3.set_author(name="YourBot", icon_url="https://cdn.discordapp.com/attachments/877796755234783273/879295069834850324/Avatar.png")
                embed3.set_thumbnail(url="https://cdn.discordapp.com/attachments/877796755234783273/879298565380386846/sign-red-error-icon-1.png")
                embed3.add_field(name="Error:", value=f"{e}", inline=False)
                embed3.set_footer(text=f"Requested by {ctx.author.name}")
                await loading_message.delete()
                await ctx.send(embed=embed3)
        
        elif fake_mode == "fname nb":
            faker = Faker()
            try:
                USssa = faker.first_name_nonbinary()
                emf2 = discord.Embed(title="Fake Information Generator", color=0xF00000)
                emf2.set_thumbnail(url="https://www.nicepng.com/png/detail/214-2146883_4-fake-stamp-vector-fake-news-logo-png.png")
                emf2.set_footer(text=f"Requested by {ctx.author.name}")
                emf2.set_author(name="YourBot", icon_url="https://cdn.discordapp.com/attachments/877796755234783273/879295069834850324/Avatar.png")
                emf2.add_field(name="First Name - Non Binary", value=f"{USssa}")
                await loading_message.delete()
                await ctx.send(embed=emf2)
            except Exception as e:
                embed3=discord.Embed(title=":red_square: Error!", description="The command was unable to run successfully! ", color=0xff0000)
                embed3.set_author(name="YourBot", icon_url="https://cdn.discordapp.com/attachments/877796755234783273/879295069834850324/Avatar.png")
                embed3.set_thumbnail(url="https://cdn.discordapp.com/attachments/877796755234783273/879298565380386846/sign-red-error-icon-1.png")
                embed3.add_field(name="Error:", value=f"{e}", inline=False)
                embed3.set_footer(text=f"Requested by {ctx.author.name}")
                await loading_message.delete()
                await ctx.send(embed=embed3)
        
        elif fake_mode == "lang":
            faker = Faker()
            try:
                USssa = faker.language_name()
                emf2 = discord.Embed(title="Fake Information Generator", color=0xF00000)
                emf2.set_thumbnail(url="https://www.nicepng.com/png/detail/214-2146883_4-fake-stamp-vector-fake-news-logo-png.png")
                emf2.set_footer(text=f"Requested by {ctx.author.name}")
                emf2.set_author(name="YourBot", icon_url="https://cdn.discordapp.com/attachments/877796755234783273/879295069834850324/Avatar.png")
                emf2.add_field(name="Language Name", value=f"{USssa}")
                await loading_message.delete()
                await ctx.send(embed=emf2)
            except Exception as e:
                embed3=discord.Embed(title=":red_square: Error!", description="The command was unable to run successfully! ", color=0xff0000)
                embed3.set_author(name="YourBot", icon_url="https://cdn.discordapp.com/attachments/877796755234783273/879295069834850324/Avatar.png")
                embed3.set_thumbnail(url="https://cdn.discordapp.com/attachments/877796755234783273/879298565380386846/sign-red-error-icon-1.png")
                embed3.add_field(name="Error:", value=f"{e}", inline=False)
                embed3.set_footer(text=f"Requested by {ctx.author.name}")
                await loading_message.delete()
                await ctx.send(embed=embed3)
        
        elif fake_mode == "lname":
            faker = Faker()
            try:
                USssa = faker.last_name()
                emf2 = discord.Embed(title="Fake Information Generator", color=0xF00000)
                emf2.set_thumbnail(url="https://www.nicepng.com/png/detail/214-2146883_4-fake-stamp-vector-fake-news-logo-png.png")
                emf2.set_footer(text=f"Requested by {ctx.author.name}")
                emf2.set_author(name="YourBot", icon_url="https://cdn.discordapp.com/attachments/877796755234783273/879295069834850324/Avatar.png")
                emf2.add_field(name="Last Name", value=f"{USssa}")
                await loading_message.delete()
                await ctx.send(embed=emf2)
            except Exception as e:
                embed3=discord.Embed(title=":red_square: Error!", description="The command was unable to run successfully! ", color=0xff0000)
                embed3.set_author(name="YourBot", icon_url="https://cdn.discordapp.com/attachments/877796755234783273/879295069834850324/Avatar.png")
                embed3.set_thumbnail(url="https://cdn.discordapp.com/attachments/877796755234783273/879298565380386846/sign-red-error-icon-1.png")
                embed3.add_field(name="Error:", value=f"{e}", inline=False)
                embed3.set_footer(text=f"Requested by {ctx.author.name}")
                await loading_message.delete()
                await ctx.send(embed=embed3)
        
        elif fake_mode == "lname male":
            faker = Faker()
            try:
                USssa = faker.last_name_male()
                emf2 = discord.Embed(title="Fake Information Generator", color=0xF00000)
                emf2.set_thumbnail(url="https://www.nicepng.com/png/detail/214-2146883_4-fake-stamp-vector-fake-news-logo-png.png")
                emf2.set_footer(text=f"Requested by {ctx.author.name}")
                emf2.set_author(name="YourBot", icon_url="https://cdn.discordapp.com/attachments/877796755234783273/879295069834850324/Avatar.png")
                emf2.add_field(name="Last Name - Male", value=f"{USssa}")
                await loading_message.delete()
                await ctx.send(embed=emf2)
            except Exception as e:
                embed3=discord.Embed(title=":red_square: Error!", description="The command was unable to run successfully! ", color=0xff0000)
                embed3.set_author(name="YourBot", icon_url="https://cdn.discordapp.com/attachments/877796755234783273/879295069834850324/Avatar.png")
                embed3.set_thumbnail(url="https://cdn.discordapp.com/attachments/877796755234783273/879298565380386846/sign-red-error-icon-1.png")
                embed3.add_field(name="Error:", value=f"{e}", inline=False)
                embed3.set_footer(text=f"Requested by {ctx.author.name}")
                await loading_message.delete()
                await ctx.send(embed=embed3)
        
        elif fake_mode == "lname female":
            faker = Faker()
            try:
                USssa = faker.last_name_female()
                emf2 = discord.Embed(title="Fake Information Generator", color=0xF00000)
                emf2.set_thumbnail(url="https://www.nicepng.com/png/detail/214-2146883_4-fake-stamp-vector-fake-news-logo-png.png")
                emf2.set_footer(text=f"Requested by {ctx.author.name}")
                emf2.set_author(name="YourBot", icon_url="https://cdn.discordapp.com/attachments/877796755234783273/879295069834850324/Avatar.png")
                emf2.add_field(name="Last Name - Female", value=f"{USssa}")
                await loading_message.delete()
                await ctx.send(embed=emf2)
            except Exception as e:
                embed3=discord.Embed(title=":red_square: Error!", description="The command was unable to run successfully! ", color=0xff0000)
                embed3.set_author(name="YourBot", icon_url="https://cdn.discordapp.com/attachments/877796755234783273/879295069834850324/Avatar.png")
                embed3.set_thumbnail(url="https://cdn.discordapp.com/attachments/877796755234783273/879298565380386846/sign-red-error-icon-1.png")
                embed3.add_field(name="Error:", value=f"{e}", inline=False)
                embed3.set_footer(text=f"Requested by {ctx.author.name}")
                await loading_message.delete()
                await ctx.send(embed=embed3)
        
        elif fake_mode == "lname nb":
            faker = Faker()
            try:
                USssa = faker.last_name_nonbinary()
                emf2 = discord.Embed(title="Fake Information Generator", color=0xF00000)
                emf2.set_thumbnail(url="https://www.nicepng.com/png/detail/214-2146883_4-fake-stamp-vector-fake-news-logo-png.png")
                emf2.set_footer(text=f"Requested by {ctx.author.name}")
                emf2.set_author(name="YourBot", icon_url="https://cdn.discordapp.com/attachments/877796755234783273/879295069834850324/Avatar.png")
                emf2.add_field(name="Last Name - Non Binary", value=f"{USssa}")
                await loading_message.delete()
                await ctx.send(embed=emf2)
            except Exception as e:
                embed3=discord.Embed(title=":red_square: Error!", description="The command was unable to run successfully! ", color=0xff0000)
                embed3.set_author(name="YourBot", icon_url="https://cdn.discordapp.com/attachments/877796755234783273/879295069834850324/Avatar.png")
                embed3.set_thumbnail(url="https://cdn.discordapp.com/attachments/877796755234783273/879298565380386846/sign-red-error-icon-1.png")
                embed3.add_field(name="Error:", value=f"{e}", inline=False)
                embed3.set_footer(text=f"Requested by {ctx.author.name}")
                await loading_message.delete()
                await ctx.send(embed=embed3)
        


        elif fake_mode == "name female":
            faker = Faker()
            try:
                USssa = faker.name_female()
                emf2 = discord.Embed(title="Fake Information Generator", color=0xF00000)
                emf2.set_thumbnail(url="https://www.nicepng.com/png/detail/214-2146883_4-fake-stamp-vector-fake-news-logo-png.png")
                emf2.set_footer(text=f"Requested by {ctx.author.name}")
                emf2.set_author(name="YourBot", icon_url="https://cdn.discordapp.com/attachments/877796755234783273/879295069834850324/Avatar.png")
                emf2.add_field(name="Name - Female", value=f"{USssa}")
                await loading_message.delete()
                await ctx.send(embed=emf2)
            except Exception as e:
                embed3=discord.Embed(title=":red_square: Error!", description="The command was unable to run successfully! ", color=0xff0000)
                embed3.set_author(name="YourBot", icon_url="https://cdn.discordapp.com/attachments/877796755234783273/879295069834850324/Avatar.png")
                embed3.set_thumbnail(url="https://cdn.discordapp.com/attachments/877796755234783273/879298565380386846/sign-red-error-icon-1.png")
                embed3.add_field(name="Error:", value=f"{e}", inline=False)
                embed3.set_footer(text=f"Requested by {ctx.author.name}")
                await loading_message.delete()
                await ctx.send(embed=embed3)
        
        elif fake_mode == "name male":
            faker = Faker()
            try:
                USssa = faker.name_male()
                emf2 = discord.Embed(title="Fake Information Generator", color=0xF00000)
                emf2.set_thumbnail(url="https://www.nicepng.com/png/detail/214-2146883_4-fake-stamp-vector-fake-news-logo-png.png")
                emf2.set_footer(text=f"Requested by {ctx.author.name}")
                emf2.set_author(name="YourBot", icon_url="https://cdn.discordapp.com/attachments/877796755234783273/879295069834850324/Avatar.png")
                emf2.add_field(name="Name - Male", value=f"{USssa}")
                await loading_message.delete()
                await ctx.send(embed=emf2)
            except Exception as e:
                embed3=discord.Embed(title=":red_square: Error!", description="The command was unable to run successfully! ", color=0xff0000)
                embed3.set_author(name="YourBot", icon_url="https://cdn.discordapp.com/attachments/877796755234783273/879295069834850324/Avatar.png")
                embed3.set_thumbnail(url="https://cdn.discordapp.com/attachments/877796755234783273/879298565380386846/sign-red-error-icon-1.png")
                embed3.add_field(name="Error:", value=f"{e}", inline=False)
                embed3.set_footer(text=f"Requested by {ctx.author.name}")
                await loading_message.delete()
                await ctx.send(embed=embed3)
        
        elif fake_mode == "name nb":
            faker = Faker()
            try:
                USssa = faker.name_nonbinary()
                emf2 = discord.Embed(title="Fake Information Generator", color=0xF00000)
                emf2.set_thumbnail(url="https://www.nicepng.com/png/detail/214-2146883_4-fake-stamp-vector-fake-news-logo-png.png")
                emf2.set_footer(text=f"Requested by {ctx.author.name}")
                emf2.set_author(name="YourBot", icon_url="https://cdn.discordapp.com/attachments/877796755234783273/879295069834850324/Avatar.png")
                emf2.add_field(name="Name - Non Binary", value=f"{USssa}")
                await loading_message.delete()
                await ctx.send(embed=emf2)
            except Exception as e:
                embed3=discord.Embed(title=":red_square: Error!", description="The command was unable to run successfully! ", color=0xff0000)
                embed3.set_author(name="YourBot", icon_url="https://cdn.discordapp.com/attachments/877796755234783273/879295069834850324/Avatar.png")
                embed3.set_thumbnail(url="https://cdn.discordapp.com/attachments/877796755234783273/879298565380386846/sign-red-error-icon-1.png")
                embed3.add_field(name="Error:", value=f"{e}", inline=False)
                embed3.set_footer(text=f"Requested by {ctx.author.name}")
                await loading_message.delete()
                await ctx.send(embed=embed3)
        
        elif fake_mode == "prefix":
            faker = Faker()
            try:
                USssa = faker.prefix()
                emf2 = discord.Embed(title="Fake Information Generator", color=0xF00000)
                emf2.set_thumbnail(url="https://www.nicepng.com/png/detail/214-2146883_4-fake-stamp-vector-fake-news-logo-png.png")
                emf2.set_footer(text=f"Requested by {ctx.author.name}")
                emf2.set_author(name="YourBot", icon_url="https://cdn.discordapp.com/attachments/877796755234783273/879295069834850324/Avatar.png")
                emf2.add_field(name="Prefix", value=f"{USssa}")
                await loading_message.delete()
                await ctx.send(embed=emf2)
            except Exception as e:
                embed3=discord.Embed(title=":red_square: Error!", description="The command was unable to run successfully! ", color=0xff0000)
                embed3.set_author(name="YourBot", icon_url="https://cdn.discordapp.com/attachments/877796755234783273/879295069834850324/Avatar.png")
                embed3.set_thumbnail(url="https://cdn.discordapp.com/attachments/877796755234783273/879298565380386846/sign-red-error-icon-1.png")
                embed3.add_field(name="Error:", value=f"{e}", inline=False)
                embed3.set_footer(text=f"Requested by {ctx.author.name}")
                await loading_message.delete()
                await ctx.send(embed=embed3)
        
        elif fake_mode == "suffix":
            faker = Faker()
            try:
                USssa = faker.prefix()
                emf2 = discord.Embed(title="Fake Information Generator", color=0xF00000)
                emf2.set_thumbnail(url="https://www.nicepng.com/png/detail/214-2146883_4-fake-stamp-vector-fake-news-logo-png.png")
                emf2.set_footer(text=f"Requested by {ctx.author.name}")
                emf2.set_author(name="YourBot", icon_url="https://cdn.discordapp.com/attachments/877796755234783273/879295069834850324/Avatar.png")
                emf2.add_field(name="Prefix", value=f"{USssa}")
                await loading_message.delete()
                await ctx.send(embed=emf2)
            except Exception as e:
                embed3=discord.Embed(title=":red_square: Error!", description="The command was unable to run successfully! ", color=0xff0000)
                embed3.set_author(name="YourBot", icon_url="https://cdn.discordapp.com/attachments/877796755234783273/879295069834850324/Avatar.png")
                embed3.set_thumbnail(url="https://cdn.discordapp.com/attachments/877796755234783273/879298565380386846/sign-red-error-icon-1.png")
                embed3.add_field(name="Error:", value=f"{e}", inline=False)
                embed3.set_footer(text=f"Requested by {ctx.author.name}")
                await loading_message.delete()
                await ctx.send(embed=embed3)
        
        elif fake_mode == "callingcode":
            faker = Faker()
            try:
                USssa = faker.country_calling_code()
                emf2 = discord.Embed(title="Fake Information Generator", color=0xF00000)
                emf2.set_thumbnail(url="https://www.nicepng.com/png/detail/214-2146883_4-fake-stamp-vector-fake-news-logo-png.png")
                emf2.set_footer(text=f"Requested by {ctx.author.name}")
                emf2.set_author(name="YourBot", icon_url="https://cdn.discordapp.com/attachments/877796755234783273/879295069834850324/Avatar.png")
                emf2.add_field(name="Calling Code", value=f"{USssa}")
                await loading_message.delete()
                await ctx.send(embed=emf2)
            except Exception as e:
                embed3=discord.Embed(title=":red_square: Error!", description="The command was unable to run successfully! ", color=0xff0000)
                embed3.set_author(name="YourBot", icon_url="https://cdn.discordapp.com/attachments/877796755234783273/879295069834850324/Avatar.png")
                embed3.set_thumbnail(url="https://cdn.discordapp.com/attachments/877796755234783273/879298565380386846/sign-red-error-icon-1.png")
                embed3.add_field(name="Error:", value=f"{e}", inline=False)
                embed3.set_footer(text=f"Requested by {ctx.author.name}")
                await loading_message.delete()
                await ctx.send(embed=embed3)
        
        elif fake_mode == "msisdn":
            faker = Faker()
            try:
                USssa = faker.msisdn()
                emf2 = discord.Embed(title="Fake Information Generator", color=0xF00000)
                emf2.set_thumbnail(url="https://www.nicepng.com/png/detail/214-2146883_4-fake-stamp-vector-fake-news-logo-png.png")
                emf2.set_footer(text=f"Requested by {ctx.author.name}")
                emf2.set_author(name="YourBot", icon_url="https://cdn.discordapp.com/attachments/877796755234783273/879295069834850324/Avatar.png")
                emf2.add_field(name="MSISDN", value=f"{USssa}")
                await loading_message.delete()
                await ctx.send(embed=emf2)
            except Exception as e:
                embed3=discord.Embed(title=":red_square: Error!", description="The command was unable to run successfully! ", color=0xff0000)
                embed3.set_author(name="YourBot", icon_url="https://cdn.discordapp.com/attachments/877796755234783273/879295069834850324/Avatar.png")
                embed3.set_thumbnail(url="https://cdn.discordapp.com/attachments/877796755234783273/879298565380386846/sign-red-error-icon-1.png")
                embed3.add_field(name="Error:", value=f"{e}", inline=False)
                embed3.set_footer(text=f"Requested by {ctx.author.name}")
                await loading_message.delete()
                await ctx.send(embed=embed3)
        
        elif fake_mode == "apt":
            faker = Faker()
            try:
                USssa = faker.android_platform_token()
                emf2 = discord.Embed(title="Fake Information Generator", color=0xF00000)
                emf2.set_thumbnail(url="https://www.nicepng.com/png/detail/214-2146883_4-fake-stamp-vector-fake-news-logo-png.png")
                emf2.set_footer(text=f"Requested by {ctx.author.name}")
                emf2.set_author(name="YourBot", icon_url="https://cdn.discordapp.com/attachments/877796755234783273/879295069834850324/Avatar.png")
                emf2.add_field(name="Android Platform Token", value=f"{USssa}")
                await loading_message.delete()
                await ctx.send(embed=emf2)
            except Exception as e:
                embed3=discord.Embed(title=":red_square: Error!", description="The command was unable to run successfully! ", color=0xff0000)
                embed3.set_author(name="YourBot", icon_url="https://cdn.discordapp.com/attachments/877796755234783273/879295069834850324/Avatar.png")
                embed3.set_thumbnail(url="https://cdn.discordapp.com/attachments/877796755234783273/879298565380386846/sign-red-error-icon-1.png")
                embed3.add_field(name="Error:", value=f"{e}", inline=False)
                embed3.set_footer(text=f"Requested by {ctx.author.name}")
                await loading_message.delete()
                await ctx.send(embed=embed3)
        
        elif fake_mode == "chrome":
            faker = Faker()
            try:
                USssa = faker.chrome()
                emf2 = discord.Embed(title="Fake Information Generator", color=0xF00000)
                emf2.set_thumbnail(url="https://www.nicepng.com/png/detail/214-2146883_4-fake-stamp-vector-fake-news-logo-png.png")
                emf2.set_footer(text=f"Requested by {ctx.author.name}")
                emf2.set_author(name="YourBot", icon_url="https://cdn.discordapp.com/attachments/877796755234783273/879295069834850324/Avatar.png")
                emf2.add_field(name="User Agent - Chrome", value=f"{USssa}")
                await loading_message.delete()
                await ctx.send(embed=emf2)
            except Exception as e:
                embed3=discord.Embed(title=":red_square: Error!", description="The command was unable to run successfully! ", color=0xff0000)
                embed3.set_author(name="YourBot", icon_url="https://cdn.discordapp.com/attachments/877796755234783273/879295069834850324/Avatar.png")
                embed3.set_thumbnail(url="https://cdn.discordapp.com/attachments/877796755234783273/879298565380386846/sign-red-error-icon-1.png")
                embed3.add_field(name="Error:", value=f"{e}", inline=False)
                embed3.set_footer(text=f"Requested by {ctx.author.name}")
                await loading_message.delete()
                await ctx.send(embed=embed3)
        
        elif fake_mode == "firefox":
            faker = Faker()
            try:
                USssa = faker.firefox()
                emf2 = discord.Embed(title="Fake Information Generator", color=0xF00000)
                emf2.set_thumbnail(url="https://www.nicepng.com/png/detail/214-2146883_4-fake-stamp-vector-fake-news-logo-png.png")
                emf2.set_footer(text=f"Requested by {ctx.author.name}")
                emf2.set_author(name="YourBot", icon_url="https://cdn.discordapp.com/attachments/877796755234783273/879295069834850324/Avatar.png")
                emf2.add_field(name="User Agent - FireFox", value=f"{USssa}")
                await loading_message.delete()
                await ctx.send(embed=emf2)
            except Exception as e:
                embed3=discord.Embed(title=":red_square: Error!", description="The command was unable to run successfully! ", color=0xff0000)
                embed3.set_author(name="YourBot", icon_url="https://cdn.discordapp.com/attachments/877796755234783273/879295069834850324/Avatar.png")
                embed3.set_thumbnail(url="https://cdn.discordapp.com/attachments/877796755234783273/879298565380386846/sign-red-error-icon-1.png")
                embed3.add_field(name="Error:", value=f"{e}", inline=False)
                embed3.set_footer(text=f"Requested by {ctx.author.name}")
                await loading_message.delete()
                await ctx.send(embed=embed3)
        
        elif fake_mode == "ie":
            faker = Faker()
            try:
                USssa = faker.internet_explorer()
                emf2 = discord.Embed(title="Fake Information Generator", color=0xF00000)
                emf2.set_thumbnail(url="https://www.nicepng.com/png/detail/214-2146883_4-fake-stamp-vector-fake-news-logo-png.png")
                emf2.set_footer(text=f"Requested by {ctx.author.name}")
                emf2.set_author(name="YourBot", icon_url="https://cdn.discordapp.com/attachments/877796755234783273/879295069834850324/Avatar.png")
                emf2.add_field(name="User Agent - Internet Explorer", value=f"{USssa}")
                await loading_message.delete()
                await ctx.send(embed=emf2)
            except Exception as e:
                embed3=discord.Embed(title=":red_square: Error!", description="The command was unable to run successfully! ", color=0xff0000)
                embed3.set_author(name="YourBot", icon_url="https://cdn.discordapp.com/attachments/877796755234783273/879295069834850324/Avatar.png")
                embed3.set_thumbnail(url="https://cdn.discordapp.com/attachments/877796755234783273/879298565380386846/sign-red-error-icon-1.png")
                embed3.add_field(name="Error:", value=f"{e}", inline=False)
                embed3.set_footer(text=f"Requested by {ctx.author.name}")
                await loading_message.delete()
                await ctx.send(embed=embed3)
        
        elif fake_mode == "iospt":
            faker = Faker()
            try:
                USssa = faker.ios_platform_token()
                emf2 = discord.Embed(title="Fake Information Generator", color=0xF00000)
                emf2.set_thumbnail(url="https://www.nicepng.com/png/detail/214-2146883_4-fake-stamp-vector-fake-news-logo-png.png")
                emf2.set_footer(text=f"Requested by {ctx.author.name}")
                emf2.set_author(name="YourBot", icon_url="https://cdn.discordapp.com/attachments/877796755234783273/879295069834850324/Avatar.png")
                emf2.add_field(name="IOS Platform Token", value=f"{USssa}")
                await loading_message.delete()
                await ctx.send(embed=emf2)
            except Exception as e:
                embed3=discord.Embed(title=":red_square: Error!", description="The command was unable to run successfully! ", color=0xff0000)
                embed3.set_author(name="YourBot", icon_url="https://cdn.discordapp.com/attachments/877796755234783273/879295069834850324/Avatar.png")
                embed3.set_thumbnail(url="https://cdn.discordapp.com/attachments/877796755234783273/879298565380386846/sign-red-error-icon-1.png")
                embed3.add_field(name="Error:", value=f"{e}", inline=False)
                embed3.set_footer(text=f"Requested by {ctx.author.name}")
                await loading_message.delete()
                await ctx.send(embed=embed3)
        
        elif fake_mode == "linuxpt":
            faker = Faker()
            try:
                USssa = faker.linux_platform_token()
                emf2 = discord.Embed(title="Fake Information Generator", color=0xF00000)
                emf2.set_thumbnail(url="https://www.nicepng.com/png/detail/214-2146883_4-fake-stamp-vector-fake-news-logo-png.png")
                emf2.set_footer(text=f"Requested by {ctx.author.name}")
                emf2.set_author(name="YourBot", icon_url="https://cdn.discordapp.com/attachments/877796755234783273/879295069834850324/Avatar.png")
                emf2.add_field(name="Linux Platform Token", value=f"{USssa}")
                await loading_message.delete()
                await ctx.send(embed=emf2)
            except Exception as e:
                embed3=discord.Embed(title=":red_square: Error!", description="The command was unable to run successfully! ", color=0xff0000)
                embed3.set_author(name="YourBot", icon_url="https://cdn.discordapp.com/attachments/877796755234783273/879295069834850324/Avatar.png")
                embed3.set_thumbnail(url="https://cdn.discordapp.com/attachments/877796755234783273/879298565380386846/sign-red-error-icon-1.png")
                embed3.add_field(name="Error:", value=f"{e}", inline=False)
                embed3.set_footer(text=f"Requested by {ctx.author.name}")
                await loading_message.delete()
                await ctx.send(embed=embed3)
        
        elif fake_mode == "linuxproc":
            faker = Faker()
            try:
                USssa = faker.linux_processor()
                emf2 = discord.Embed(title="Fake Information Generator", color=0xF00000)
                emf2.set_thumbnail(url="https://www.nicepng.com/png/detail/214-2146883_4-fake-stamp-vector-fake-news-logo-png.png")
                emf2.set_footer(text=f"Requested by {ctx.author.name}")
                emf2.set_author(name="YourBot", icon_url="https://cdn.discordapp.com/attachments/877796755234783273/879295069834850324/Avatar.png")
                emf2.add_field(name="Linux Processor", value=f"{USssa}")
                await loading_message.delete()
                await ctx.send(embed=emf2)
            except Exception as e:
                embed3=discord.Embed(title=":red_square: Error!", description="The command was unable to run successfully! ", color=0xff0000)
                embed3.set_author(name="YourBot", icon_url="https://cdn.discordapp.com/attachments/877796755234783273/879295069834850324/Avatar.png")
                embed3.set_thumbnail(url="https://cdn.discordapp.com/attachments/877796755234783273/879298565380386846/sign-red-error-icon-1.png")
                embed3.add_field(name="Error:", value=f"{e}", inline=False)
                embed3.set_footer(text=f"Requested by {ctx.author.name}")
                await loading_message.delete()
                await ctx.send(embed=embed3)
        
        elif fake_mode == "macpt":
            faker = Faker()
            try:
                USssa = faker.mac_platform_token()
                emf2 = discord.Embed(title="Fake Information Generator", color=0xF00000)
                emf2.set_thumbnail(url="https://www.nicepng.com/png/detail/214-2146883_4-fake-stamp-vector-fake-news-logo-png.png")
                emf2.set_footer(text=f"Requested by {ctx.author.name}")
                emf2.set_author(name="YourBot", icon_url="https://cdn.discordapp.com/attachments/877796755234783273/879295069834850324/Avatar.png")
                emf2.add_field(name="MAC - Platform Token", value=f"{USssa}")
                await loading_message.delete()
                await ctx.send(embed=emf2)
            except Exception as e:
                embed3=discord.Embed(title=":red_square: Error!", description="The command was unable to run successfully! ", color=0xff0000)
                embed3.set_author(name="YourBot", icon_url="https://cdn.discordapp.com/attachments/877796755234783273/879295069834850324/Avatar.png")
                embed3.set_thumbnail(url="https://cdn.discordapp.com/attachments/877796755234783273/879298565380386846/sign-red-error-icon-1.png")
                embed3.add_field(name="Error:", value=f"{e}", inline=False)
                embed3.set_footer(text=f"Requested by {ctx.author.name}")
                await loading_message.delete()
                await ctx.send(embed=embed3)
        
        elif fake_mode == "macprocessor":
            faker = Faker()
            try:
                USssa = faker.mac_processor()
                emf2 = discord.Embed(title="Fake Information Generator", color=0xF00000)
                emf2.set_thumbnail(url="https://www.nicepng.com/png/detail/214-2146883_4-fake-stamp-vector-fake-news-logo-png.png")
                emf2.set_footer(text=f"Requested by {ctx.author.name}")
                emf2.set_author(name="YourBot", icon_url="https://cdn.discordapp.com/attachments/877796755234783273/879295069834850324/Avatar.png")
                emf2.add_field(name="MAC Processor", value=f"{USssa}")
                await loading_message.delete()
                await ctx.send(embed=emf2)
            except Exception as e:
                embed3=discord.Embed(title=":red_square: Error!", description="The command was unable to run successfully! ", color=0xff0000)
                embed3.set_author(name="YourBot", icon_url="https://cdn.discordapp.com/attachments/877796755234783273/879295069834850324/Avatar.png")
                embed3.set_thumbnail(url="https://cdn.discordapp.com/attachments/877796755234783273/879298565380386846/sign-red-error-icon-1.png")
                embed3.add_field(name="Error:", value=f"{e}", inline=False)
                embed3.set_footer(text=f"Requested by {ctx.author.name}")
                await loading_message.delete()
                await ctx.send(embed=embed3)
        
        elif fake_mode == "opera":
            faker = Faker()
            try:
                USssa = faker.opera()
                emf2 = discord.Embed(title="Fake Information Generator", color=0xF00000)
                emf2.set_thumbnail(url="https://www.nicepng.com/png/detail/214-2146883_4-fake-stamp-vector-fake-news-logo-png.png")
                emf2.set_footer(text=f"Requested by {ctx.author.name}")
                emf2.set_author(name="YourBot", icon_url="https://cdn.discordapp.com/attachments/877796755234783273/879295069834850324/Avatar.png")
                emf2.add_field(name="User Agent - Opera", value=f"{USssa}")
                await loading_message.delete()
                await ctx.send(embed=emf2)
            except Exception as e:
                embed3=discord.Embed(title=":red_square: Error!", description="The command was unable to run successfully! ", color=0xff0000)
                embed3.set_author(name="YourBot", icon_url="https://cdn.discordapp.com/attachments/877796755234783273/879295069834850324/Avatar.png")
                embed3.set_thumbnail(url="https://cdn.discordapp.com/attachments/877796755234783273/879298565380386846/sign-red-error-icon-1.png")
                embed3.add_field(name="Error:", value=f"{e}", inline=False)
                embed3.set_footer(text=f"Requested by {ctx.author.name}")
                await loading_message.delete()
                await ctx.send(embed=embed3)
        
        elif fake_mode == "safari":
            faker = Faker()
            try:
                USssa = faker.opera()
                emf2 = discord.Embed(title="Fake Information Generator", color=0xF00000)
                emf2.set_thumbnail(url="https://www.nicepng.com/png/detail/214-2146883_4-fake-stamp-vector-fake-news-logo-png.png")
                emf2.set_footer(text=f"Requested by {ctx.author.name}")
                emf2.set_author(name="YourBot", icon_url="https://cdn.discordapp.com/attachments/877796755234783273/879295069834850324/Avatar.png")
                emf2.add_field(name="User Agent - Safari", value=f"{USssa}")
                await loading_message.delete()
                await ctx.send(embed=emf2)
            except Exception as e:
                embed3=discord.Embed(title=":red_square: Error!", description="The command was unable to run successfully! ", color=0xff0000)
                embed3.set_author(name="YourBot", icon_url="https://cdn.discordapp.com/attachments/877796755234783273/879295069834850324/Avatar.png")
                embed3.set_thumbnail(url="https://cdn.discordapp.com/attachments/877796755234783273/879298565380386846/sign-red-error-icon-1.png")
                embed3.add_field(name="Error:", value=f"{e}", inline=False)
                embed3.set_footer(text=f"Requested by {ctx.author.name}")
                await loading_message.delete()
                await ctx.send(embed=embed3)
        
        elif fake_mode == "winpt":
            faker = Faker()
            try:
                USssa = faker.windows_platform_token()
                emf2 = discord.Embed(title="Fake Information Generator", color=0xF00000)
                emf2.set_thumbnail(url="https://www.nicepng.com/png/detail/214-2146883_4-fake-stamp-vector-fake-news-logo-png.png")
                emf2.set_footer(text=f"Requested by {ctx.author.name}")
                emf2.set_author(name="YourBot", icon_url="https://cdn.discordapp.com/attachments/877796755234783273/879295069834850324/Avatar.png")
                emf2.add_field(name="Windows - Platform Token", value=f"{USssa}")
                await loading_message.delete()
                await ctx.send(embed=emf2)
            except Exception as e:
                embed3=discord.Embed(title=":red_square: Error!", description="The command was unable to run successfully! ", color=0xff0000)
                embed3.set_author(name="YourBot", icon_url="https://cdn.discordapp.com/attachments/877796755234783273/879295069834850324/Avatar.png")
                embed3.set_thumbnail(url="https://cdn.discordapp.com/attachments/877796755234783273/879298565380386846/sign-red-error-icon-1.png")
                embed3.add_field(name="Error:", value=f"{e}", inline=False)
                embed3.set_footer(text=f"Requested by {ctx.author.name}")
                await loading_message.delete()
                await ctx.send(embed=embed3)
        
        elif fake_mode == "ua":
            faker = Faker()
            try:
                USssa = faker.user_agent()
                emf2 = discord.Embed(title="Fake Information Generator", color=0xF00000)
                emf2.set_thumbnail(url="https://www.nicepng.com/png/detail/214-2146883_4-fake-stamp-vector-fake-news-logo-png.png")
                emf2.set_footer(text=f"Requested by {ctx.author.name}")
                emf2.set_author(name="YourBot", icon_url="https://cdn.discordapp.com/attachments/877796755234783273/879295069834850324/Avatar.png")
                emf2.add_field(name="User Agent", value=f"{USssa}")
                await loading_message.delete()
                await ctx.send(embed=emf2)
            except Exception as e:
                embed3=discord.Embed(title=":red_square: Error!", description="The command was unable to run successfully! ", color=0xff0000)
                embed3.set_author(name="YourBot", icon_url="https://cdn.discordapp.com/attachments/877796755234783273/879295069834850324/Avatar.png")
                embed3.set_thumbnail(url="https://cdn.discordapp.com/attachments/877796755234783273/879298565380386846/sign-red-error-icon-1.png")
                embed3.add_field(name="Error:", value=f"{e}", inline=False)
                embed3.set_footer(text=f"Requested by {ctx.author.name}")
                await loading_message.delete()
                await ctx.send(embed=embed3)
        

def setup(client: commands.Bot):
    client.add_cog(Startup(client))
