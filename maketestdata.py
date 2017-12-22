# for logging stuff
import logging
import os
import time
import random

# Create a class that extends the FileHandler class from logging.FileHandler
class FileHandlerWithHeader(logging.FileHandler):

    # Pass the file name and header string to the constructor.
    def __init__(self, filename, header,  mode='a', encoding=None, delay=0):
        # Store the header information.
        self.header = header

        # Determine if the file pre-exists
        self.file_pre_exists = os.path.exists(filename)

        # Call the parent __init__
        logging.FileHandler.__init__(self, filename, mode, encoding, delay)

        # Write the header if delay is False and a file stream was created.
        if not delay and self.stream is not None:
            self.stream.write('%s\n' % header)

    def emit(self, record):
        # Create the file stream if not already created.
        if self.stream is None:
            self.stream = self._open()

            # If the file pre_exists, it should already have a header.
            # Else write the header to the file so that it is the first line.
            if not self.file_pre_exists:
                self.stream.write('%s\n' % self.header)

        # Call the parent class emit function.
        logging.FileHandler.emit(self, record)

# Create a logger and set the logging level.
logger = logging.getLogger("test.log")
logger.setLevel(logging.INFO)

# Create a file handler from our new FileHandlerWith Header class and set the
# logging level.
fh = FileHandlerWithHeader('test.log','timestamp,sensor',  delay=True)
fh.setLevel(logging.INFO)

# Add formatter to the file handler.
formatter = logging.Formatter('%(asctime)s.%(msecs)03d,%(message)s','%H:%M:%S')
fh.setFormatter(formatter)

# Add the handler to the logger.
logger.addHandler(fh)

while True:
    logger.info(random.uniform(0., 100.))
    time.sleep(0.01)