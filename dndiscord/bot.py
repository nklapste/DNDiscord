"""dndiscord bot api"""

from logging import getLogger
from random import randint
from discord.ext import commands
import re
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


class BaseCommands:
    """General use commands"""

    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def roll(self, dice: str):
        """Rolls a dice in NdN format."""
        try:
            if re.match("\d+d\d+", dice):
                rolls, limit = map(int, dice.split('d'))
            elif re.match("d\d+", dice):
                limit = int(dice.strip('d'))
                rolls = 1
        except Exception:
            await self.bot.say('Format has to be in NdN or dN!')
            return

        result = ', '.join(str(randint(1, limit)) for _ in range(rolls))

        await self.bot.say(result)


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
BOT.add_cog(BaseCommands(BOT))
