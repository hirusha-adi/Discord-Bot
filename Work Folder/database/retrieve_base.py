import json


class BotBase:

    # Opening the json file
    with open("database/base.json", "r", encoding="utf8") as embedsf:
        embeddata = json.load(embedsf)

    BOT_VERSION = embeddata["INFO"]["VERSION"]

    CREATOR_NAME = embeddata["CREATOR"]["NAME"]
    CREATOR_ID = embeddata["CREATOR"]["ID"]

    LOGGING_STATUS = embeddata["LOGGING"]["STATUS"]
    LOGGING_CHANNEL_ID = embeddata["LOGGING"]["CHANNEL_ID"]

    INVITE_MESSAGE = embeddata["INVITE"]["MESSAGE"]
    INVITE_LINK = embeddata["INVITE"]["LINK"]

    SOURCE_CODE_LINK = embeddata["STATUS"]["SOURCE_LINK"]
    STATUS_ANNOUNCEMENTS = embeddata["STATUS"]["ANNOUNCEMENTS"]
    STATUS_ERRORS = embeddata["STATUS"]["ERRORS"]

    BOT_READY_MESSAGE = embeddata["BOT_READY_MESSAGE"]








