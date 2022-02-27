import discord
import yourbot.database.embeds.retrieve_embeds as getembed
import yourbot.database.main.retrieve_base as getbase
from discord.ext import commands


class Texts(commands.Cog, description="Text commands + Send simple texts"):
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

    @commands.command(aliases=["echo"])
    async def say(self, ctx, *, word_to_say):
        await ctx.message.delete()
        await ctx.send(str(word_to_say))

    @commands.command(alises=["dmpriv", "dmp"],
                      breif="Direct Message - Anonymous",
                      description="Send a direct message to anyone in a server anonymously",
                      help="Send a direct message to anyone in a server anonymously")
    async def dm_priv(self, ctx, member: discord.Member, *, messagedm):
        loading_message = await ctx.send(embed=self.please_wait_emb)

        try:
            member.send(messagedm)
            embed = discord.Embed(
                title="Direct Message sent", description=f"to {member.name}", color=getembed.Common.COLOR)
            embed.set_author(name=getembed.Common.AUTHOR,
                             icon_url=getembed.Common.AUTHOR_LINK)
            embed.add_field(name="Message", value=f"{messagedm}", inline=False)
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

    @commands.command(alises=["dms", "dmstright"],
                      breif="Direct Message",
                      description="Send a direct message to anyone in a server. Your name and the server you used will be given",
                      help="Send a direct message to anyone in a server. Your name and the server you used will be given")
    async def dm(self, ctx, member: discord.Member, *, messagedm):
        loading_message = await ctx.send(embed=self.please_wait_emb)

        try:
            final_msg = f"{ctx.author.name} from {ctx.guild.name} said {messagedm}"
            member.send(final_msg)
            embed = discord.Embed(
                title="Direct Message sent", description=f"to {member.name}", color=getembed.Common.COLOR)
            embed.set_author(name=getembed.Common.AUTHOR,
                             icon_url=getembed.Common.AUTHOR_LINK)
            embed.add_field(name="Message", value=f"{final_msg}", inline=False)
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

    @commands.command()
    async def shrug(self, ctx):
        await ctx.message.delete()
        shrug = r'¯\_(ツ)_/¯'
        await ctx.send(shrug)

    @commands.command()
    async def lenny(self, ctx):
        await ctx.message.delete()
        lenny = '( ͡° ͜ʖ ͡°)'
        await ctx.send(lenny)

    @commands.command()
    async def tableflip(self, ctx):
        tableflip = '(╯°□°）╯︵ ┻━┻'
        await ctx.send(tableflip)

    @commands.command()
    async def unflip(self, ctx):
        await ctx.message.delete()
        unflip = '┬─┬ ノ( ゜-゜ノ)'
        await ctx.send(unflip)

    @commands.command()
    async def bold(ctx, *, message):
        await ctx.message.delete()
        await ctx.send('**'+message+'**')

    @commands.command()
    async def secret(ctx, *, message):
        await ctx.message.delete()
        await ctx.send('||'+message+'||')

    @commands.command()
    async def goodnight(self, ctx):
        await ctx.message.delete()
        night = '✩⋆｡ ˚ᎶᎾᎾⅅ ℕᏐᎶℍᎢ⋆｡˚✩'
        await ctx.send(night)

    @commands.command()
    async def smile(self, ctx):
        await ctx.message.delete()
        smile = '˙ ͜ʟ˙'
        await ctx.send(smile)

    @commands.command()
    async def iloveu(self, ctx):
        await ctx.message.delete()
        love = '(๑′ᴗ‵๑)Ｉ Lᵒᵛᵉᵧₒᵤ♥'
        await ctx.send(love)

    @commands.command()
    async def sword(self, ctx):
        await ctx.message.delete()
        sword = 'ס₪₪₪₪§|(Ξ≥≤≥≤≥≤ΞΞΞΞΞΞΞΞΞΞ>'
        await ctx.send(sword)

    @commands.command()
    async def what(self, ctx):
        await ctx.message.delete()
        what = '( ʘ̆ ╭͜ʖ╮ ʘ̆ )'
        await ctx.send(what)

    @commands.command()
    async def fuckyou(self, ctx):
        await ctx.message.delete()
        middlef = '╭∩╮(･◡･)╭∩╮'
        await ctx.send(middlef)

    @commands.command()
    async def txt1(self, ctx):
        await ctx.message.delete()
        middlef = r"ヾ(•ω•`)o"
        await ctx.send(middlef)

    @commands.command()
    async def txt2(self, ctx):
        await ctx.message.delete()
        middlef = r"\(￣︶￣*\))"
        await ctx.send(middlef)

    @commands.command()
    async def txt3(self, ctx):
        await ctx.message.delete()
        middlef = r"(* ￣3)(ε￣ *)"
        await ctx.send(middlef)

    @commands.command()
    async def txt4(self, ctx):
        await ctx.message.delete()
        middlef = r"－O－"
        await ctx.send(middlef)

    @commands.command()
    async def txt5(self, ctx):
        await ctx.message.delete()
        middlef = r"(*￣3￣)╭)"
        await ctx.send(middlef)

    @commands.command()
    async def txt6(self, ctx):
        await ctx.message.delete()
        middlef = r"( ´･･)ﾉ(._.`)"
        await ctx.send(middlef)

    @commands.command()
    async def txt7(self, ctx):
        await ctx.message.delete()
        middlef = r"(｡･∀･)ﾉﾞ"
        await ctx.send(middlef)

    @commands.command()
    async def txt8(self, ctx):
        await ctx.message.delete()
        middlef = r"o(*￣▽￣*)ブ"
        await ctx.send(middlef)

    @commands.command()
    async def txt9(self, ctx):
        await ctx.message.delete()
        middlef = r"(_　_)。゜zｚＺ"
        await ctx.send(middlef)

    @commands.command()
    async def txt10(self, ctx):
        await ctx.message.delete()
        middlef = r"(ToT)/~~~"
        await ctx.send(middlef)

    @commands.command()
    async def txt11(self, ctx):
        await ctx.message.delete()
        middlef = r"(∪.∪ )...zzz"
        await ctx.send(middlef)

    @commands.command()
    async def txt12(self, ctx):
        await ctx.message.delete()
        middlef = r"!(*￣(￣　*)"
        await ctx.send(middlef)

    @commands.command()
    async def txt13(self, ctx):
        await ctx.message.delete()
        middlef = r"(￣o￣) . z Z)"
        await ctx.send(middlef)

    @commands.command()
    async def txt14(self, ctx):
        await ctx.message.delete()
        middlef = r"(づ￣ 3￣)づ"
        await ctx.send(middlef)

    @commands.command()
    async def txt15(self, ctx):
        await ctx.message.delete()
        middlef = r"（＾∀＾●）ﾉｼ"
        await ctx.send(middlef)

    @commands.command()
    async def txt16(self, ctx):
        await ctx.message.delete()
        middlef = r"（づ￣3￣）づ╭❤～"
        await ctx.send(middlef)

    @commands.command()
    async def txt17(self, ctx):
        await ctx.message.delete()
        middlef = r"\(@^0^@)/"
        await ctx.send(middlef)

    @commands.command()
    async def txt18(self, ctx):
        await ctx.message.delete()
        middlef = r"ヾ(^▽^*)))"
        await ctx.send(middlef)

    @commands.command()
    async def txt19(self, ctx):
        await ctx.message.delete()
        middlef = r"(～﹃～)~zZ"
        await ctx.send(middlef)

    @commands.command()
    async def txt20(self, ctx):
        await ctx.message.delete()
        middlef = r"☆⌒(*＾-゜)v"
        await ctx.send(middlef)

    @commands.command()
    async def txt21(self, ctx):
        await ctx.message.delete()
        middlef = r"(￣o￣) . z Z"
        await ctx.send(middlef)

    @commands.command()
    async def txt22(self, ctx):
        await ctx.message.delete()
        middlef = r"(*￣;(￣ *)"
        await ctx.send(middlef)

    @commands.command()
    async def txt23(self, ctx):
        await ctx.message.delete()
        middlef = r"||ヽ(*￣▽￣*)ノミ|Ю"
        await ctx.send(middlef)

    @commands.command()
    async def txt24(self, ctx):
        await ctx.message.delete()
        middlef = r"☆⌒(*＾-゜)v"
        await ctx.send(middlef)

    @commands.command()
    async def txt25(self, ctx):
        await ctx.message.delete()
        middlef = r"(＾Ｕ＾)ノ~ＹＯ)"
        await ctx.send(middlef)

    @commands.command()
    async def txt26(self, ctx):
        await ctx.message.delete()
        middlef = r"o(*°▽°*)o"
        await ctx.send(middlef)

    @commands.command()
    async def txt27(self, ctx):
        await ctx.message.delete()
        middlef = r"ヾ(￣▽￣) Bye~Bye~"
        await ctx.send(middlef)

    @commands.command()
    async def txt28(self, ctx):
        await ctx.message.delete()
        middlef = r"( ﾟдﾟ)つ Bye)"
        await ctx.send(middlef)

    @commands.command()
    async def txt29(self, ctx):
        await ctx.message.delete()
        middlef = r"(๑•̀ㅂ•́)و✧)"
        await ctx.send(middlef)

    @commands.command()
    async def txt30(self, ctx):
        await ctx.message.delete()
        middlef = r"(ﾉ◕ヮ◕)ﾉ*:･ﾟ✧"
        await ctx.send(middlef)

    @commands.command()
    async def txt31(self, ctx):
        await ctx.message.delete()
        middlef = r"(∩^o^)⊃━☆)"
        await ctx.send(middlef)

    @commands.command()
    async def txt32(self, ctx):
        await ctx.message.delete()
        middlef = r"✪ ω ✪"
        await ctx.send(middlef)

    @commands.command()
    async def txt33(self, ctx):
        await ctx.message.delete()
        middlef = r"d=====(￣▽￣*)b"
        await ctx.send(middlef)

    @commands.command()
    async def txt34(self, ctx):
        await ctx.message.delete()
        middlef = r"＜（＾－＾）＞"
        await ctx.send(middlef)

    @commands.command()
    async def txt35(self, ctx):
        await ctx.message.delete()
        middlef = r"o(*￣▽￣*)o"
        await ctx.send(middlef)

    @commands.command()
    async def txt36(self, ctx):
        await ctx.message.delete()
        middlef = r"o(￣▽￣)ｄ"
        await ctx.send(middlef)

    @commands.command()
    async def txt37(self, ctx):
        await ctx.message.delete()
        middlef = r"(╹ڡ╹ ))"
        await ctx.send(middlef)

    @commands.command()
    async def txt38(self, ctx):
        await ctx.message.delete()
        middlef = r"(u‿ฺu✿ฺ))"
        await ctx.send(middlef)

    @commands.command()
    async def txt39(self, ctx):
        await ctx.message.delete()
        middlef = r"♪(´▽｀)"
        await ctx.send(middlef)

    @commands.command()
    async def txt40(self, ctx):
        await ctx.message.delete()
        middlef = r"(╯▽╰ ))"
        await ctx.send(middlef)

    @commands.command()
    async def txt41(self, ctx):
        await ctx.message.delete()
        middlef = r"ヽ(✿ﾟ▽ﾟ)ノ"
        await ctx.send(middlef)

    @commands.command()
    async def txt42(self, ctx):
        await ctx.message.delete()
        middlef = r"( •̀ .̫ •́ )✧"
        await ctx.send(middlef)

    @commands.command()
    async def txt43(self, ctx):
        await ctx.message.delete()
        middlef = r"(^^ゞ"
        await ctx.send(middlef)

    @commands.command()
    async def txt44(self, ctx):
        await ctx.message.delete()
        middlef = r"(＠＾０＾)"
        await ctx.send(middlef)

    @commands.command()
    async def txt45(self, ctx):
        await ctx.message.delete()
        middlef = r"（。＾▽＾）"
        await ctx.send(middlef)

    @commands.command()
    async def txt46(self, ctx):
        await ctx.message.delete()
        middlef = r"Ψ(￣∀￣)Ψ"
        await ctx.send(middlef)

    @commands.command()
    async def txt47(self, ctx):
        await ctx.message.delete()
        middlef = r"*★,°*:.☆(￣▽￣)/$:*.°★* 。"
        await ctx.send(middlef)

    @commands.command()
    async def txt48(self, ctx):
        await ctx.message.delete()
        middlef = r"o(≧∀≦)o"
        await ctx.send(middlef)

    @commands.command()
    async def txt49(self, ctx):
        await ctx.message.delete()
        middlef = r"(。・∀・)ノ"
        await ctx.send(middlef)

    @commands.command()
    async def txt50(self, ctx):
        await ctx.message.delete()
        middlef = r"~\(≧▽≦)/~"
        await ctx.send(middlef)

    @commands.command()
    async def txt51(self, ctx):
        await ctx.message.delete()
        middlef = r"b(￣▽￣)d"
        await ctx.send(middlef)

    @commands.command()
    async def txt52(self, ctx):
        await ctx.message.delete()
        middlef = r"o(^▽^)o"
        await ctx.send(middlef)

    @commands.command()
    async def txt53(self, ctx):
        await ctx.message.delete()
        middlef = r"(☞ﾟヮﾟ)☞"
        await ctx.send(middlef)

    @commands.command()
    async def txt54(self, ctx):
        await ctx.message.delete()
        middlef = r"☜(ﾟヮﾟ☜)"
        await ctx.send(middlef)

    @commands.command()
    async def txt55(self, ctx):
        await ctx.message.delete()
        middlef = r"☜(⌒▽⌒)☞"
        await ctx.send(middlef)

    @commands.command()
    async def txt56(self, ctx):
        await ctx.message.delete()
        middlef = r"(¬‿¬)"
        await ctx.send(middlef)

    @commands.command()
    async def txt57(self, ctx):
        await ctx.message.delete()
        middlef = r"(•_•)"
        await ctx.send(middlef)

    @commands.command()
    async def txt58(self, ctx):
        await ctx.message.delete()
        middlef = r"( •_•)>⌐■-■"
        await ctx.send(middlef)

    @commands.command()
    async def txt59(self, ctx):
        await ctx.message.delete()
        middlef = r"(⌐■_■)"
        await ctx.send(middlef)

    @commands.command()
    async def txt60(self, ctx):
        await ctx.message.delete()
        middlef = r"ヾ(⌐■_■)ノ♪"
        await ctx.send(middlef)

    @commands.command()
    async def txt61(self, ctx):
        await ctx.message.delete()
        middlef = r"(▀̿Ĺ̯▀̿ ̿)"
        await ctx.send(middlef)

    @commands.command()
    async def txt62(self, ctx):
        await ctx.message.delete()
        middlef = r"＼(ﾟｰﾟ＼)"
        await ctx.send(middlef)

    @commands.command()
    async def txt63(self, ctx):
        await ctx.message.delete()
        middlef = r"( ﾉ ﾟｰﾟ)ﾉ"
        await ctx.send(middlef)


def setup(client: commands.Bot):
    client.add_cog(Texts(client))
