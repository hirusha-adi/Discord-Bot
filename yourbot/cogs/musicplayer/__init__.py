from .music import Music
from .events import MusicEvents


def setup(bot):
    bot.add_cog(Music(bot))
    bot.add_cog(MusicEvents(bot))


__version__ = "1.0.1"
