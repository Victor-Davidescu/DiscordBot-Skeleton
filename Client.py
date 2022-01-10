############################################################
# Author: Victor Florian Davidescu
# Project: Discord Bot - Skeleton
############################################################

# Imported modules
import logging
import discord  # Third-party
import coloredlogs  # Third-party
from Commands import Commands
from Configurations import Configurations

# Set up the logging messages
logger = logging.getLogger(__name__)
coloredlogs.install(level='DEBUG', logger=logger)


############################################################
# Class: Client (Discord Bot)
############################################################
class Client(discord.Client):

    ############################################################
    # Constructor
    ############################################################
    def __init__(self, config: Configurations):
        super().__init__()
        self.config = config

    ############################################################
    # Function: Set status
    ############################################################
    async def ChangePresence(self):
        """
        Change the bot presence
        """

        # Bot - Status
        # Check if the bot requires to be invisible
        if self.config.invisible == "TRUE":
            logger.warning("Bot status set to invisible.")
            status = discord.Status.invisible
        else:
            status = discord.Status.online

        # Bot - Activity
        # Set an activity for the bot
        if self.config.activityType == "GAME":
            self.config.activityType = discord.Game(self.config.activityName)
            logger.info("Bot activity set to game with description: {0}".format(self.config.activityName))
        else:
            self.config.activityType = None

        # Change bot presence
        try:
            await self.change_presence(status=status, activity=self.config.activityType)
            logger.debug("Successfully changed the bot presence.")

        except Exception as error:
            logger.error("Could not change the presence. {0}".format(error))

    ############################################################
    # Function:
    ############################################################
    async def on_ready(self):
        logger.info("Bot is ready, logged as {0}.".format(self.user))
        await self.ChangePresence()

    ############################################################
    # Function:
    ############################################################
    async def on_message(self, message: discord.Message):
        logger.debug("Message from {0.author}: {0.content}".format(message))

        # Check if the message is not from itself
        if message.author != self.user:

            # Check if the message starts with a command prefix
            if message.content.startswith(self.config.commandPrefix):
                logger.debug("Command prefix detected.")
                pass
