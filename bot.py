import logging

from discord.ext import commands
from utils import constants

logging.basicConfig(level=logging.INFO)


class Bot(commands.Bot):
    def __init__(self, *args, **kwargs):
        logging.info("booted up")
        super().__init__(*args, **kwargs)


if __name__ == '__main__':
    # client = Operator()
    bot = Bot(command_prefix="$")
    bot.load_extension("commands.autistry")
    try:
        bot.run(constants.DISCORD_TOKEN)
    except Exception as exc:
        logging.error(exc)
        raise