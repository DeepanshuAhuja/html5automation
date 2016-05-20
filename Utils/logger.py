import logging

# Create a logger
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)


# Create a log handler
handler = logging.FileHandler('/Users/mayank.mahajan/PycharmProjects/html5automation/logs/logs.txt')
handler.setLevel(logging.DEBUG)

# Format Logs
formattor = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
handler.setFormatter(formattor)

# Link handler with Logger
logger.addHandler(handler)