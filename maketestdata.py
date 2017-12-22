# for logging stuff
import logging
import time
import random
from logging.handlers import RotatingFileHandler

# name of log
logFile = 'test.log'
# create logger
logger = logging.getLogger('crdl-logger')
logger.setLevel(logging.DEBUG)
# add a file handler
hdlr = logging.FileHandler(logFile)
hdlr = RotatingFileHandler(logFile, mode='a', maxBytes=10*1024*1024, backupCount=2, encoding=None, delay=0)
hdlr.setLevel(logging.DEBUG) # log all msg to file
# create formatter
formatter = logging.Formatter('%(asctime)s, %(message)s', "%H:%M:%S" )
hdlr.setFormatter(formatter)
# add the handler to the logger
logger.addHandler(hdlr)

# Testing of the loggers
logger.info('------ NEW LOG ------')

while True:
    logger.info(random.uniform(0, 1.))
    time.sleep(0.01)