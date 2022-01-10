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
from Configurations import Configurations

# Set up the logging messages
logger = logging.getLogger(__name__)
coloredlogs.install(level='DEBUG', logger=logger)


############################################################
# Function: Obtain Configurations
############################################################
def RetrieveConfigurations():
    """
    Obtain all configuration data from the configuration file.
    """

    # Configuration file name and its path
    configFileName = "config.ini"
    configFilePath = os.path.join('.', 'data', configFileName)

    if os.path.isfile(configFilePath):

        config = Configurations()
        default = "default"
        optional = "optional"

        try:
            # Read the configuration file
            parser = ConfigParser()
            parser.read(configFilePath)

            # Retrieve mandatory configuration
            config.token = parser.get(default, "token")
            config.commandPrefix = parser.get(default, "command_prefix")

            # Retrieve optional configurations
            config.invisible = parser.get(optional, "invisible")
            config.activityType = parser.get(optional, "activity_type")
            config.activityName = parser.get(optional, "activity_name")

        except Exception as msg:
            logging.critical("Could not retrieve data from configuration file: {0}".format(msg))
            sys.exit("Program terminated.")

        # Check if the mandatory configuration is received
        if config.token and config.commandPrefix:
            logger.debug("Obtained successfully all the mandatory configurations.")

            # Return the object containing all the configurations
            return config

        else:
            logger.critical("Did not obtain all mandatory configurations.")
            sys.exit("Program terminated.")

    else:
        logger.critical("The config file cannot be found. Expected to find at: {0}".format(configFilePath))
        sys.exit("Program terminated")


############################################################
# Function: Main
############################################################
def Main():
    """
    This is the main function of this program
    """

    # Obtain configuration settings from the configuration file
    config: Configurations = RetrieveConfigurations()

    # Create new discord client object
    client = Client(config)

    # Run the discord bot
    client.run(config.token)


############################################################
# START
############################################################
if __name__ == "__main__":
    Main()
