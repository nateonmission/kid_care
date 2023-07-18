import os

PROJECT_TITLE = "Kid Care Tracker"
FAVICON_PATH = "http://www.directionsresearch.com/images/favicon.png"
DESCRIPTION = """Repo: [https://github.com/nateonmission/kid_care](https://github.com/nateonmission/kid_care)"""
VERSION = "0.1"


try:
    envi = str(os.environ["TARGET_ENV"])
except Exception:
    envi = ""

ROOT_PATH = ""



