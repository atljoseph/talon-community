import logging
from talon import Module

mod = Module()

# Access these functions in the following way:
# - actions.user.debug("log this sting")

@mod.action_class
class Actions:
    def debug(message: str):
        """Log debug message"""
        logging.debug(message)

    def info(message: str):
        """Log info message"""
        logging.info(message)

    def warning(message: str):
        """Log warning message"""
        logging.warning(message)

    def error(message: str):
        """Log error message"""
        logging.error(message)


logging.getLogger().setLevel(logging.INFO)
# logging.getLogger().setLevel(logging.DEBUG)
