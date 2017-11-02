"""dndiscord bot api"""

from logging import getLogger

from discord.ext import commands

DESCRIPTION = """dndiscord: A Discord bot!"""  # TODO

BOT = commands.Bot(command_prefix="?", description=DESCRIPTION)

__log__ = getLogger(__name__)


@BOT.event
async def on_ready():
    """Bot startup event"""
    __log__.info("logged in as: {}".format(BOT.user.id))


@BOT.event
async def on_message(message):
    await BOT.process_commands(message)


class CharacterCreation:
    """DND character creation assistance commands"""
    pass


class Config:
    """Config commands for the dndiscord"""
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    @commands.has_permissions(administrator=True)
    async def config(self):
        pass


BOT.add_cog(Config(BOT))
