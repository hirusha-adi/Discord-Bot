import json


class BotBase:

    # Opening the json file
    with open("yourbot/database/main/base.json", "r", encoding="utf8") as embedsf:
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


class Main:
    # Opening the json file
    with open("yourbot/database/main/base.json", "r", encoding="utf8") as embedsf:
        embeddata = json.load(embedsf)

    MSG_PREFIX = embeddata["MAIN"]["MSG_PREFIX"]
    INVITE_LINK = embeddata["MAIN"]["INVITE_LINK"]
    OWNER_ID = embeddata["MAIN"]["OWNER_ID"]
    LOG_USER_DATA = embeddata["MAIN"]["LOG_USER_DATA"]
    LOG_CHANNEL_ID = embeddata["MAIN"]["LOG_CHANNEL_ID"]
