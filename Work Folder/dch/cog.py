import os
import discord
from discord.ext import commands


class MyHelpCommand(commands.HelpCommand):
    def __init__(self, **options):
        super().__init__(**options)
        try:
            color = os.environ['DCH_COLOR']
            color = color.replace('#', '')
            color = int(color, 16)
            self.color = discord.Color(color)
        except:
            self.color = discord.Color.blurple()


    async def send_bot_help(self, mapping):
        ctx = self.context

        cogs = []

        for cog in ctx.bot.cogs.values():
            if await ctx.bot.is_owner(ctx.author):
                cogs.append(cog)
            else:
                cog_commands = [
                    command
                    for command in cog.get_commands()
                    if command.hidden == False and command.enabled == True
                ]
                if len(cog_commands) > 0:
                    cogs.append(cog)

        embed = discord.Embed(
            color=self.color,
            timestamp=ctx.message.created_at,
            description=f"Use `{self.clean_prefix}help <Category>` to get help on a category\n\n",
        )

        for cog in cogs:
            if await ctx.bot.is_owner(ctx.author):
                cog_commands = [command for command in cog.get_commands()]
            else:
                cog_commands = [
                    command
                    for command in cog.get_commands()
                    if command.hidden == False and command.enabled == True
                ]

            if len(cog_commands) > 0:
                cog_help = cog.description or "No description provided"
                cog_help += "\n"

                embed.add_field(name=cog.qualified_name, value=cog_help)

        embed.set_thumbnail(url=ctx.bot.user.avatar_url)
        await ctx.send(embed=embed)

    # Main Help
    async def send_cog_help(self, cog):
        ctx = self.context
        pre = self.clean_prefix

        embed = discord.Embed(
            color=self.color, timestamp=ctx.message.created_at, description=""
        )

        if await ctx.bot.is_owner(ctx.author):
            shown_commands = [command for command in cog.get_commands()]
        else:
            shown_commands = [
                command
                for command in cog.get_commands()
                if command.hidden == False and command.enabled == True
            ]

        if len(shown_commands) == 0:
            return await ctx.send("This cog has no command.")

        if cog.description:
            cog_help = cog.description
        else:
            cog_help = "No description provided for this cog"

        embed.title = f"{cog.qualified_name}"
        embed.description += f"{cog_help}\nUse `{self.clean_prefix}help <command>` to get help on a command.\n\n**Commands :** \n"

        for command in shown_commands:
            embed.description += f"▪︎ {pre}{command.qualified_name} "
            if command.signature:
                embed.description += f"{command.signature} \n"
            else:
                embed.description += "\n"

        embed.set_thumbnail(url=ctx.bot.user.avatar_url)
        await ctx.send(embed=embed)

    # Command Help
    async def send_command_help(self, command):
        ctx = self.context

        embed = discord.Embed(
            color=self.color,
            timestamp=ctx.message.created_at,
            description="",
        )

        if (
            command.hidden == True or command.enabled == False
        ) and await ctx.bot.is_owner(ctx.author) == False:
            return await ctx.send(
                f'No command called "{command.qualified_name}" found.'
            )

        if command.signature:
            embed.title = f"{command.qualified_name} {command.signature} \n"
        else:
            embed.title = f"{command.qualified_name}\n"

        embed.description = command.help or "No description provided"

        if len(command.aliases) > 0:
            embed.description += "\nAliases : " + ", ".join(command.aliases)

        embed.set_thumbnail(url=ctx.bot.user.avatar_url)
        await ctx.send(embed=embed)

    # Group Help
    async def send_group_help(self, group):
        ctx = self.context
        pre = self.clean_prefix

        embed = discord.Embed(
            color=self.color, timestamp=ctx.message.created_at
        )

        if group.signature:
            embed.title = f"{group.qualified_name} {group.signature}"
        else:
            embed.title = group.qualified_name + " - group"

        embed.description = group.help or "No description provided."
        embed.description += f"\nUse `{pre}help {group.qualified_name} <sub_command>` to get help on a group command. \n\n**Subcommands : **\n"

        if await ctx.bot.is_owner(ctx.author):
            group_commands = [command for command in group.commands]
            if len(group_commands) == 0:
                return await ctx.send("This group doesn't have any sub command")
        else:
            group_commands = [
                command
                for command in group.commands
                if command.hidden == False and command.enabled == True
            ]

        if len(group_commands) == 0:
            return await ctx.send(f'No command called "{group.qualified_name}" found.')

        for command in group_commands:
            if command.signature:
                command_help = f"▪︎ {pre}{command.qualified_name} {command.signature} \n"
            else:
                command_help = f"▪︎ {pre}{command.qualified_name} \n"

            embed.description += command_help

        embed.set_thumbnail(url=ctx.bot.user.avatar_url)
        await ctx.send(embed=embed)


class Help(commands.Cog):
    """Help command cog"""

    def __init__(self, client):
        self.client = client
        self.client._original_help_command = client.help_command
        client.help_command = MyHelpCommand()
        client.help_command.cog = self

    def cog_unload(self):
        self.client.help_command = self.client._original_help_command


def setup(client):
    client.add_cog(Help(client))
