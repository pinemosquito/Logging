import logging

# Create logger with 'spam_application'
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

# Create file handler which logs even debug messages
filehandler = logging.FileHandler('spam.log')
filehandler.setLevel(logging.DEBUG)

# Create formatter and add it to the handlers
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
filehandler.setFormatter(formatter)

# Add the handlers to the logger
logger.addHandler(filehandler)

logger.info('creating an instance of log')

filehandler.close()
logger.removeHandler(filehandler)
