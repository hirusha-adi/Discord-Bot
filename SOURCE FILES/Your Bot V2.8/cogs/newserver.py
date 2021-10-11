import discord
from discord.ext import commands

class ForNewlyCreatedServers(commands.Cog):
    def __init__(self, client: commands.Bot):
        self.client = client
        
        # Bot starting time, we find the time delta of this to send the uptime
        # self.start_time = None
        
        # This is the please-wait/Loading embed
        self.please_wait_emb = discord.Embed(title="Please Wait", description="``` Processing Your Request ```", color=0xff0000)
        self.please_wait_emb.set_author(name="YourBot")
        self.please_wait_emb.set_thumbnail(url="https://c.tenor.com/I6kN-6X7nhAAAAAj/loading-buffering.gif")
        self.please_wait_emb.set_footer(text="Bot created by ZeaCeR#5641")


    @commands.has_permissions(administrator=True)
    @commands.command()
    async def make_server_new_roles(self, ctx):

        loading_message = await ctx.send(embed=self.please_wait_emb)

        try:
            guild = ctx.guild
            role8 = discord.utils.get(ctx.guild.roles, name="Owner")
            if role8 not in guild.roles:
                perms8 = discord.Permissions(
                    add_reactions=True,
                    administrator=True,
                    attach_files=True,
                    ban_members=True,
                    change_nickname=True,
                    connect=True,
                    create_instant_invite=True,
                    deafen_members=True,
                    embed_links=True,
                    external_emojis=True,
                    kick_members=True,
                    manage_channels=True,
                    manage_emojis=True,
                    manage_guild=True,
                    manage_messages=True,
                    manage_nicknames=True,
                    manage_permissions=True,
                    manage_roles=True,
                    manage_webhooks=True,
                    mention_everyone=True,
                    move_members=True,
                    mute_members=True,
                    priority_speaker=True,
                    view_guild_insights=True, 
                    view_channel=True, 
                    view_audit_log=True,
                    use_voice_activation=True,
                    use_slash_commands=True,
                    use_external_emojis=True,
                    stream=True, 
                    speak=True,
                    send_tts_messages=True,
                    send_messages=True,
                    request_to_speak=True,
                    read_messages=True,
                    read_message_history=True)
                await guild.create_role(name="Owner", permissions=perms8)
            
            role7 = discord.utils.get(ctx.guild.roles, name="Administrator")
            if role7 not in guild.roles:
                perms7 = discord.Permissions(
                    add_reactions=True,
                    administrator=True,
                    attach_files=True,
                    ban_members=True,
                    change_nickname=True,
                    connect=True,
                    create_instant_invite=True,
                    deafen_members=True,
                    embed_links=True,
                    external_emojis=True,
                    kick_members=True,
                    manage_channels=True,
                    manage_emojis=True,
                    manage_guild=True,
                    manage_messages=True,
                    manage_nicknames=True,
                    manage_permissions=True,
                    manage_roles=True,
                    manage_webhooks=True,
                    mention_everyone=True,
                    move_members=True,
                    mute_members=True,
                    priority_speaker=True,
                    view_guild_insights=True, 
                    view_channel=True, 
                    view_audit_log=True,
                    use_voice_activation=True,
                    use_slash_commands=True,
                    use_external_emojis=True,
                    stream=True, 
                    speak=True,
                    send_tts_messages=True,
                    send_messages=True,
                    request_to_speak=True,
                    read_messages=True,
                    read_message_history=True)
                await guild.create_role(name="Administrator", permissions=perms7)
            
            role5 = discord.utils.get(ctx.guild.roles, name="BOT")
            if role5 not in guild.roles:
                perms5 = discord.Permissions(
                    add_reactions=True,
                    administrator=False,
                    attach_files=True,
                    ban_members=False,
                    change_nickname=True,
                    connect=True,
                    create_instant_invite=True,
                    deafen_members=False,
                    embed_links=True,
                    external_emojis=True,
                    kick_members=False,
                    manage_channels=False,
                    manage_emojis=False,
                    manage_guild=False,
                    manage_messages=False,
                    manage_nicknames=False,
                    manage_permissions=False,
                    manage_roles=False,
                    manage_webhooks=False,
                    mention_everyone=False,
                    move_members=False,
                    mute_members=False,
                    priority_speaker=True,
                    view_guild_insights=True, 
                    view_channel=True, 
                    view_audit_log=False,
                    use_voice_activation=True,
                    use_slash_commands=True,
                    use_external_emojis=True,
                    stream=True,
                    speak=True,
                    send_tts_messages=False,
                    send_messages=True,
                    request_to_speak=True,
                    read_messages=True,
                    read_message_history=True)
                await guild.create_role(name="BOT", permissions=perms5)
            
            role6 = discord.utils.get(ctx.guild.roles, name="Moderator")
            if role6 not in guild.roles:
                perms6 = discord.Permissions(
                    add_reactions=True,
                    administrator=False,
                    attach_files=True,
                    ban_members=False,
                    change_nickname=True,
                    connect=True,
                    create_instant_invite=True,
                    deafen_members=True,
                    embed_links=True,
                    external_emojis=True,
                    kick_members=True,
                    manage_channels=False,
                    manage_emojis=True,
                    manage_guild=False,
                    manage_messages=True,
                    manage_nicknames=True,
                    manage_permissions=False,
                    manage_roles=False,
                    manage_webhooks=False,
                    mention_everyone=False,
                    move_members=True,
                    mute_members=True,
                    priority_speaker=True,
                    view_guild_insights=True, 
                    view_channel=True, 
                    view_audit_log=True,
                    use_voice_activation=True,
                    use_slash_commands=True,
                    use_external_emojis=True,
                    stream=True, 
                    speak=True,
                    send_tts_messages=True,
                    send_messages=True,
                    request_to_speak=True,
                    read_messages=True,
                    read_message_history=True)
                await guild.create_role(name="Moderator", permissions=perms6)
            
            role3 = discord.utils.get(ctx.guild.roles, name="Senior")
            if role3 not in guild.roles:
                perms3 = discord.Permissions(
                    add_reactions=True,
                    administrator=False,
                    attach_files=True,
                    ban_members=False,
                    change_nickname=True,
                    connect=True,
                    create_instant_invite=True,
                    deafen_members=False,
                    embed_links=True,
                    external_emojis=True,
                    kick_members=False,
                    manage_channels=False,
                    manage_emojis=False,
                    manage_guild=False,
                    manage_messages=False,
                    manage_nicknames=False,
                    manage_permissions=False,
                    manage_roles=False,
                    manage_webhooks=True,
                    mention_everyone=False,
                    move_members=False,
                    mute_members=False,
                    priority_speaker=True,
                    view_guild_insights=True, 
                    view_channel=True, 
                    view_audit_log=True,
                    use_voice_activation=True,
                    use_slash_commands=True,
                    use_external_emojis=True,
                    stream=True,
                    speak=True,
                    send_tts_messages=False,
                    send_messages=True,
                    request_to_speak=True,
                    read_messages=True,
                    read_message_history=True)
                await guild.create_role(name="Senior", permissions=perms3)
            
            role2 = discord.utils.get(ctx.guild.roles, name="Junior")
            if role2 not in guild.roles:
                perms2 = discord.Permissions(
                    add_reactions=True,
                    administrator=False,
                    attach_files=True,
                    ban_members=False,
                    change_nickname=True,
                    connect=True,
                    create_instant_invite=True,
                    deafen_members=False,
                    embed_links=True,
                    external_emojis=True,
                    kick_members=False,
                    manage_channels=False,
                    manage_emojis=False,
                    manage_guild=False,
                    manage_messages=False,
                    manage_nicknames=False,
                    manage_permissions=False,
                    manage_roles=False,
                    manage_webhooks=False,
                    mention_everyone=False,
                    move_members=False,
                    mute_members=False,
                    priority_speaker=True,
                    view_guild_insights=True, 
                    view_channel=True, 
                    view_audit_log=False,
                    use_voice_activation=True,
                    use_slash_commands=True,
                    use_external_emojis=True,
                    stream=True,
                    speak=True,
                    send_tts_messages=False,
                    send_messages=True,
                    request_to_speak=True,
                    read_messages=True,
                    read_message_history=True)
                await guild.create_role(name="Junior", permissions=perms2)

            role1 = discord.utils.get(ctx.guild.roles, name="Rookie")
            if role1 not in guild.roles:
                perms1 = discord.Permissions(
                    add_reactions=True,
                    administrator=False,
                    attach_files=True,
                    ban_members=False,
                    change_nickname=True,
                    connect=True,
                    create_instant_invite=True,
                    deafen_members=False,
                    embed_links=True,
                    external_emojis=True,
                    kick_members=False,
                    manage_channels=False,
                    manage_emojis=False,
                    manage_guild=False,
                    manage_messages=False,
                    manage_nicknames=False,
                    manage_permissions=False,
                    manage_roles=False,
                    manage_webhooks=False,
                    mention_everyone=False,
                    move_members=False,
                    mute_members=False,
                    priority_speaker=False,
                    view_guild_insights=True, 
                    view_channel=True, 
                    view_audit_log=False,
                    use_voice_activation=True,
                    use_slash_commands=True,
                    use_external_emojis=True,
                    stream=True,
                    speak=True,
                    send_tts_messages=False,
                    send_messages=True,
                    request_to_speak=True,
                    read_messages=True,
                    read_message_history=False)
                await guild.create_role(name="Rookie", permissions=perms1)
            
            embed = discord.Embed(title=f'Server Roles Starter Template', description=f'Requested by {ctx.author.mention}', color=0xff0000)
            embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/856461730695217172/868832176496594944/Avatar.png")
            embed.add_field(name="Created Roles", value=f'Owner\nAdministrator\nBOT\nModerator\nSenior\nJunior\nRookie', inline=False)
            all_roles_in_server = ", ".join([str(r.mention) for r in ctx.guild.roles])
            embed.set_author(name="YourBot", icon_url="https://cdn.discordapp.com/attachments/877796755234783273/879295069834850324/Avatar.png")
            embed.add_field(name="Roles in the server", value=f'{all_roles_in_server}', inline=False)
            embed.set_footer(text=f"Requested by {ctx.author.name}")
            # embed.set_footer(text=datetime.datetime.now())
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
    client.add_cog(ForNewlyCreatedServers(client))





