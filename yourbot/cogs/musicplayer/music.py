import asyncio
import re
import discord
import wavelink
from .player import DisPlayer
from discord.ext import commands
from .checks import in_same_channel, player_connected, voice_connected
import yourbot.database.retrieve_embeds as getembeds


class Music(commands.Cog, name="Music", description="Play any music easily!"):
    """Music commands"""

    def __init__(self, bot):
        self.bot = bot
        self.URL_REG = re.compile(r"https?://(?:www\.)?.+")

        if not hasattr(self.bot, "wavelink"):
            self.bot.wavelink = wavelink.Client(bot=self.bot)

        self.bot.loop.create_task(self.start_nodes())

    async def start_nodes(self):
        await self.bot.wait_until_ready()

        for node in self.bot.lava_nodes:
            try:
                await self.bot.wavelink.initiate_node(**node)
            except Exception as e:
                print(e)

        for guild in self.bot.guilds:
            if guild.me.voice:
                player: DisPlayer = self.bot.wavelink.get_player(
                    guild.id, cls=DisPlayer
                )
                try:
                    await player.connect(guild.me.voice.channel.id)
                    print(
                        f"Connected to existing voice -> {guild.me.voice.channel.id}")
                except Exception as e:
                    print(e)

    @commands.command(name="connect", aliases=["con", "c"])
    @voice_connected()
    async def connect_(self, ctx):
        """Connect the player"""
        player: DisPlayer = self.bot.wavelink.get_player(
            ctx.guild.id, cls=DisPlayer)

        if player.is_connected:
            if not player.bound_channel:
                player.bound_channel = ctx.channel

            if player.channel_id == ctx.author.voice.channel.id:
                return await ctx.send(
                    "Player is already connected to your voice channel."
                )

            return await ctx.send(
                f"Player is connected to a different voice channel. Can' join this."
            )

        channel = ctx.author.voice.channel
        self.bot.voice_users[ctx.author.id] = channel.id

        msg = await ctx.send(f"Connecting to **`{channel.name}`**")
        await player.connect(channel.id)
        player.bound_channel = ctx.channel
        await msg.edit(
            content=f"Connected to **`{channel.name}`** and bounded to {ctx.channel.mention}"
        )

    @commands.command(name="disconnect", aliases=["dc", "leave"])
    @voice_connected()
    @player_connected()
    @in_same_channel()
    async def disconnect_(self, ctx):
        """Destroy the player"""
        player: DisPlayer = self.bot.wavelink.get_player(
            ctx.guild.id, cls=DisPlayer)
        await player.destroy()

    @commands.command(name="play", aliases=["p"])
    @voice_connected()
    async def play_(self, ctx, *, query):
        """Play or add song to queue"""
        player: DisPlayer = self.bot.wavelink.get_player(
            ctx.guild.id, cls=DisPlayer)

        if not player.is_connected:
            await ctx.invoke(self.connect_)

        if ctx.channel != player.bound_channel and player.bound_channel:
            return await ctx.send(
                f"Player is bounded to {player.bound_channel.mention}", delete_after=5
            )
        player.bound_channel = ctx.channel

        msg = await ctx.send(f"Searching for `{query}` :mag_right:")
        query = query.strip("<>")
        if not self.URL_REG.match(query):
            query = f"ytsearch:{query}"

        tracks = await self.bot.wavelink.get_tracks(query)

        if not tracks:
            return await msg.edit(content="Could not find any song with that query.")

        if isinstance(tracks, wavelink.TrackPlaylist):
            for track in tracks.tracks:
                await player.queue.put(track)

            msg.edit(
                content=f'Added the playlist **{tracks.data["playlistInfo"]["name"]}** with **{len(tracks.tracks)}** songs to the queue.'
            )
        else:
            await player.queue.put(tracks[0])

            await msg.edit(content=f"Added **{str(tracks[0])}** to the queue.")

        if not player.is_playing:
            await player.do_next()

    @commands.command()
    @voice_connected()
    @player_connected()
    @in_same_channel()
    async def skip(self, ctx):
        """Skip currently playing song"""
        player: DisPlayer = self.bot.wavelink.get_player(
            ctx.guild.id, cls=DisPlayer)

        if ctx.channel != player.bound_channel:
            return await ctx.send(
                f"Player is bounded to {player.bound_channel.mention}", delete_after=5
            )

        current_loop = player.loop
        player.loop = "NONE"

        await player.stop()

        if current_loop != "CURRENT":
            player.loop = current_loop

    @commands.command()
    @voice_connected()
    @player_connected()
    @in_same_channel()
    async def pause(self, ctx):
        """Pause the player"""
        player: DisPlayer = self.bot.wavelink.get_player(
            ctx.guild.id, cls=DisPlayer)

        if ctx.channel != player.bound_channel:
            return await ctx.send(
                f"Player is bounded to {player.bound_channel.mention}", delete_after=5
            )

        if player.is_playing:
            if player.is_paused:
                return await ctx.send("Player is already paused.")

            await player.set_pause(pause=True)
            return await ctx.send("Player is now paused.")

        await ctx.send("Player is not playing anything.")

    @commands.command()
    @player_connected()
    @voice_connected()
    @in_same_channel()
    async def resume(self, ctx):
        """Resume the player"""
        player: DisPlayer = self.bot.wavelink.get_player(
            ctx.guild.id, cls=DisPlayer)

        if ctx.channel != player.bound_channel:
            return await ctx.send(
                f"Player is bounded to {player.bound_channel.mention}", delete_after=5
            )

        if player.is_playing:
            if not player.is_paused:
                return await ctx.send("Player is not paused.")

            await player.set_pause(pause=False)
            return await ctx.send("Player is now resumed.")

        await ctx.send("Player is not playing anything.")

    @commands.command()
    @voice_connected()
    @player_connected()
    @in_same_channel()
    async def seek(self, ctx, seconds: int, reverse: bool = False):
        """Seek the player backward or forward"""
        player: DisPlayer = self.bot.wavelink.get_player(
            ctx.guild.id, cls=DisPlayer)

        if ctx.channel != player.bound_channel:
            return await ctx.send(
                f"Player is bounded to {player.bound_channel.mention}", delete_after=5
            )

        if player.is_playing:
            if not player.is_paused:
                if not reverse:
                    new_position = player.position + (seconds * 1000)
                    if new_position > player.current.length:
                        new_position = player.current.length
                else:
                    new_position = player.position - (seconds * 1000)
                    if new_position < 0:
                        new_position = 0

                await player.seek(new_position)
                return await ctx.send(f"Player has been seeked {seconds} seconds.")

            return await ctx.send(
                "Player is paused. Resume the player to use this command."
            )

        await ctx.send("Player is not playing anything.")

    @commands.command(aliases=["vol"])
    @voice_connected()
    @player_connected()
    @in_same_channel()
    async def volume(self, ctx, vol: int, forced=False):
        """Set volume"""
        player: DisPlayer = self.bot.wavelink.get_player(
            ctx.guild.id, cls=DisPlayer)

        if ctx.channel != player.bound_channel:
            return await ctx.send(
                f"Player is bounded to {player.bound_channel.mention}", delete_after=5
            )

        if vol < 0:
            return await ctx.send("Volume can't be less than 0")

        if vol > 100 and not forced:
            return await ctx.send("Volume can't greater than 100")

        await player.set_volume(vol)

    @commands.command()
    @voice_connected()
    @player_connected()
    @in_same_channel()
    async def loop(self, ctx, type: str = None):
        """Set loop to `NONE`, `CURRENT` or `PLAYLIST`"""
        player: DisPlayer = self.bot.wavelink.get_player(
            ctx.guild.id, cls=DisPlayer)

        if ctx.channel != player.bound_channel:
            return await ctx.send(
                f"Player is bounded to {player.bound_channel.mention}", delete_after=5
            )

        valid_types = ["NONE", "CURRENT", "PLAYLIST"]

        if not type:
            current_loop = player.loop
            if valid_types.index(current_loop) >= 2:
                type = "NONE"
            else:
                type = valid_types[valid_types.index(current_loop) + 1]

            queue = player.queue._queue
            if type == "PLAYLIST" and len(queue) < 1:
                type = "NONE"

        else:
            type = type.upper()

        if type not in valid_types:
            return await ctx.send("Loop type must be `NONE`, `CURRENT` or `PLAYLIST`.")

        if len(player.queue._queue) < 1 and type == "PLAYLIST":
            return await ctx.send(
                "There must be 2 songs in the queue in order to use the PLAYLIST loop"
            )

        if not player.is_playing:
            return await ctx.send("Player is not playing any track. Can't loop")

        player.loop = type

        await ctx.send(f"Player is now looping `{type}`")

    @commands.command(aliases=["np"])
    @voice_connected()
    @player_connected()
    @in_same_channel()
    async def nowplaying(self, ctx):
        """What's playing now?"""
        player: DisPlayer = self.bot.wavelink.get_player(
            ctx.guild.id, cls=DisPlayer)

        if ctx.channel != player.bound_channel:
            return await ctx.send(
                f"Player is bounded to {player.bound_channel.mention}", delete_after=5
            )

        if not player.current:
            return await ctx.send("Nothing is playing.")

        await player.invoke_player()

    @commands.command(aliases=["q"])
    @voice_connected()
    @player_connected()
    @in_same_channel()
    async def queue(self, ctx):
        """Player's current queue"""
        player: DisPlayer = self.bot.wavelink.get_player(
            ctx.guild.id, cls=DisPlayer)

        if ctx.channel != player.bound_channel:
            return await ctx.send(
                f"Player is bounded to {player.bound_channel.mention}", delete_after=5
            )

        queue = player.queue._queue
        if len(queue) < 1:
            return await ctx.send("Nothing is in the queue.")

        embed = discord.Embed(color=getembeds.Common.COLOR)
        embed.set_author(
            name="Queue", icon_url="https://cdn.shahriyar.dev/list.png")

        tracks = ""
        if player.loop == "CURRENT":
            next_song = f"Next > [{player.current.title}]({player.current.uri}) \n\n"
        else:
            next_song = ""

        if next_song:
            tracks += next_song

        for index, track in enumerate(queue):
            tracks += f"{index + 1}. [{track.title}]({track.uri}) \n"

        embed.description = tracks

        await ctx.send(embed=embed)

    @commands.command(aliases=["eq"])
    @voice_connected()
    @player_connected()
    @in_same_channel()
    async def equalizer(self, ctx):
        """Set equalizer"""
        player: DisPlayer = self.bot.wavelink.get_player(
            ctx.guild.id, cls=DisPlayer)

        if ctx.channel != player.bound_channel:
            return await ctx.send(
                f"Player is bounded to {player.bound_channel.mention}", delete_after=5
            )

        eqs = {
            "1️⃣": ["Flat", wavelink.eqs.Equalizer.flat()],
            "2️⃣": ["Boost", wavelink.eqs.Equalizer.boost()],
            "3️⃣": ["Metal", wavelink.eqs.Equalizer.metal()],
            "4️⃣": ["Piano", wavelink.eqs.Equalizer.piano()],
        }

        embed = discord.Embed(title="Select Equalizer")
        embed.description = f"Current Eq - **{player.eq.name}**\n\n1. Flat \n2. Boost\n3. Metal\n4. Piano"
        embed.set_thumbnail(url="https://cdn.shahriyar.dev/equalizer.png")

        msg = await ctx.send(embed=embed)

        await msg.add_reaction("1️⃣")
        await msg.add_reaction("2️⃣")
        await msg.add_reaction("3️⃣")
        await msg.add_reaction("4️⃣")

        def check(reaction, user):
            return (
                reaction.message.id == msg.id
                and user.id == ctx.author.id
                and reaction.emoji in ["1️⃣", "2️⃣", "3️⃣", "4️⃣"]
            )

        while True:
            try:
                reaction, user = await self.bot.wait_for(
                    "reaction_add", timeout=60.0, check=check
                )
            except:
                await msg.delete()
                break

            selected_eq = eqs[reaction.emoji][1]
            await player.set_equalizer(selected_eq)

            embed.description = (
                f"Current Eq - **{eqs[reaction.emoji][0]}**\n\n"
                "1. Flat \n2. Boost\n3. Metal\n4. Piano"
            )

            await msg.edit(embed=embed)
