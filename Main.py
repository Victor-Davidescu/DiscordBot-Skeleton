############################################################
# Author: Victor Florian Davidescu
# Project: Discord Bot - Skeleton
############################################################

# Modules required
import logging
import os
import sys
import coloredlogs                      # Third-party
from configparser import ConfigParser   # Third-party
from Client import Client               # Self-made

# Set up the logging messages
logger = logging.getLogger(__name__)
coloredlogs.install(level='DEBUG', logger=logger)


############################################################
# Function: Obtain Configurations
############################################################
def ObtainConfigurations():
    """
    Obtain all configuration data from the configuration file.
    """

    # Configuration file name and its path
    configFileName = "config.ini"
    configFilePath = os.path.join('.', 'data', configFileName)

    try:
        # Read the configuration file
        parser = ConfigParser()
        parser.read(configFilePath)

        # Retrieve data from default category
        token = parser.get("default", "token")
        status = parser.get("default", "status")
        activityType = parser.get("default", "activity_type")
        activityName = parser.get("default", "activity_name")

        logger.debug("Obtained successfully the configurations data.")

    except Exception as error:
        logging.critical("Could not retrieve data from configuration file: {0}".format(error))
        sys.exit("Program terminated.")

    return token, status, activityType, activityName


############################################################
# Function: Main
############################################################
def Main():
    """
    This is the main function of this program
    """

    # Obtain configuration settings from the configuration file
    token, status, activityType, activityName = ObtainConfigurations()

    # Create new discord client object
    client = Client(status, activityType, activityName)

    # Run the discord bot
    client.run(token)


############################################################
# START
############################################################
if __name__ == "__main__":
    Main()
