# encoding: utf-8
# ref: https://docs.python.org/2/howto/logging.html#handler-basic
import logging
import logging.handlers

# create logger
logger = logging.getLogger("status_check")
logger.setLevel(logging.DEBUG)

# create handler
LOG_FILE='/data/logs/status_check.log'
handler = logging.handlers.RotatingFileHandler(LOG_FILE, maxBytes = 100*1024*1024, backupCount = 5)
handler.setLevel(logging.DEBUG)

# create formatter
fmt = '%(asctime)s - %(filename)s:%(lineno)s - %(name)s - %(message)s'
formatter = logging.Formatter(fmt)

# add formatter to handler 
handler.setFormatter(formatter)

# add formatter to logger
logger.addHandler(handler)


# "application code"
logger.debug('debug message')
logger.info('info message')
logger.warn('warn message')
logger.error('error message')
logger.critical('critical message')
