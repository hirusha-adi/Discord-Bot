import discord
from discord.ext import commands
import yourbot.database.retrieve_embeds as getembed
import yourbot.database.retrieve_base as getbase
import yourbot.database.announcements.anncmgr as anncmgr

class Announcements(commands.Cog, description="Setup modmail in your server easily!"):
    def __init__(self, client: commands.Bot):
        self.client = client

        self.bot_prefix = getbase.Main.MSG_PREFIX
        self.bot_inv_link = getbase.Main.INVITE_LINK

        # This is the please-wait/Loading embed
        self.please_wait_emb = discord.Embed(title=getembed.PleaseWait.TITLE, description=f"``` {getembed.PleaseWait.DESCRIPTION} ```", color=getembed.PleaseWait.COLOR)
        self.please_wait_emb.set_author(name=getembed.PleaseWait.AUTHOR_NAME, icon_url=getembed.PleaseWait.AUTHOR_LINK)
        self.please_wait_emb.set_thumbnail(url=getembed.PleaseWait.THUMBNAIL)
        self.please_wait_emb.set_footer(text=getembed.PleaseWait.FOOTER)
    

    @commands.has_permissions(administrator=True)
    @commands.command()
    async def set_announcement(self, ctx):
        loading_message = await ctx.send(embed=self.please_wait_emb)
        try:
            guild = ctx.guild
            new_channel = await guild.create_text_channel("modmail-manage")
            await ctx.channel.set_permissions(ctx.guild.default_role, send_messages=False)
            await new_channel.set_permissions(ctx.guild.default_role, view_channel=False)
            anncmgr.add_channel_to_modmail_sending_channellist(guild.id)
            anncmgr.add_channel_to_modmail_managing_channellist(new_channel.id)
            await ctx.send(f"Check <@{new_channel.id}> to easily manage modmails with embeds")

        except Exception as e:
            embed2=discord.Embed(title=getembed.ErrorEmbeds.TITLE, description=getembed.ErrorEmbeds.DESCRIPTION, color=getembed.ErrorEmbeds.COLOR)
            embed2.set_author(name=getembed.Common.AUTHOR, icon_url=getembed.Common.AUTHOR_LINK)
            embed2.set_thumbnail(url=getembed.ErrorEmbeds.THUMBNAIL)
            embed2.add_field(name="Error:", value=f"{e}", inline=False)
            embed2.set_footer(text=f"Requested by {ctx.author.name}")
            await loading_message.delete()
            await ctx.send(embed=embed2)










def setup(client: commands.Bot):
    client.add_cog(Announcements(client))

