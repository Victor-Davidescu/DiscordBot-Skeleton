############################################################
# Author: Victor Florian Davidescu
# Project: Discord Bot - Skeleton
############################################################

# Imported modules
import logging
import discord      # Third-party
import coloredlogs  # Third-party

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
    def __init__(self, status, activityType, activityName):
        super().__init__()
        self.status = status
        self.activityType = activityType
        self.activityName = activityName


    ############################################################
    # Function: Set status
    ############################################################
    async def ChangePresence(self):
        """
        Change the bot presence
        """

        # Set the status of the bot based on the received configuration
        if self.status == "AWAY":
            self.status = discord.Status.idle
            logger.warning("Bot status set to idle.")

        elif self.status == "INVISIBLE":
            self.status = discord.Status.invisible
            logger.warning("Bot status set to invisible, activity cannot be visible.")

        else:
            self.status = discord.Status.online
            logger.info("Bot status set to online.")

        # Set an activity for the bot
        if self.activityType == "GAME":
            self.activityType = discord.Game(self.activityName)
            logger.info("Bot activity set to game with description: {0}".format(self.activityName))

        else:
            self.activityType = None

        # Change bot presence
        try:
            await self.change_presence(status=self.status, activity=self.activityType)
            logger.debug("Successfully changed the bot presence.")

        except Exception as error:
            logging.error("Could not change the presence. {0}".format(error))


    ############################################################
    # Function:
    ############################################################
    async def on_ready(self):
        logger.info("Bot is ready, logged as {0}.".format(self.user))
        await self.ChangePresence()


    ############################################################
    # Function:
    ############################################################
    async def on_message(self, message):
        logger.debug("Message from {0.author}: {0.content}".format(message))

        # Check if the message is not from itself
        if message.author != self.user:
            pass
