# import sys

# import loguru

# # from app.api.v1.core import config

# logger = loguru.logger

# logger.remove()
# fmt = "<dim><green>{time:YYYY-MM-DD HH:mm:ss.SSS}</> <red>|</> <cyan>{extra[request_id]}</cyan></> <red>|</> <magenta>{name: >30}.py</> <red>|</> <magenta>{function: >20}() : {line: <4}</> <red>|</> <level>{level: <8} - {message}</>"
# logger.add(sys.stdout, format=fmt, level="INFO")