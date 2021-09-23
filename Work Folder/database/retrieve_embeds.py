import json

class PleaseWait:

    # Opening the json file
    with open("database/embeds.json", "r", encoding="utf8") as embedsf:
        embeddata = json.load(embedsf)

    # VARIABLES - Same name as in json file
    TITLE = embeddata["PLASE_WAIT_EMBED"]["TITLE"]
    DESCRIPTION = embeddata["PLASE_WAIT_EMBED"]["DESCRIPTION"]
    AUTHOR_NAME = embeddata["PLASE_WAIT_EMBED"]["AUTHOR_NAME"]
    AUTHOR_LINK = embeddata["PLASE_WAIT_EMBED"]["AUTHOR_LINK"]
    THUMBNAIL = embeddata["PLASE_WAIT_EMBED"]["THUMBNAIL"]
    FOOTER = embeddata["PLASE_WAIT_EMBED"]["FOOTER"]
    
    if embeddata["PLASE_WAIT_EMBED"]["COLOR"] == "red":
        COLOR = 0xff0000
    elif embeddata["PLASE_WAIT_EMBED"]["COLOR"] == "green":
        COLOR = 0x00ff00
    elif embeddata["PLASE_WAIT_EMBED"]["COLOR"] == "blue":
        COLOR = 0x0000ff



class Common:

    # Opening the json file
    with open("database/embeds.json", "r", encoding="utf8") as embedsf:
        embeddata = json.load(embedsf)
        
    # VARIABLES - Same name as in json file
    AUTHOR = embeddata["COMMON_FOR_ALL"]["AUTHOR"]
    AUTHOR_LINK = embeddata["COMMON_FOR_ALL"]["AUTHOR_LINK"]

    if embeddata["COMMON_FOR_ALL"]["COLOR"] == "red":
        COLOR = 0xff0000
    elif embeddata["COMMON_FOR_ALL"]["COLOR"] == "green":
        COLOR = 0x00ff00
    elif embeddata["COMMON_FOR_ALL"]["COLOR"] == "blue":
        COLOR = 0x0000ff


class ErrorEmbeds:

    # Opening the json file
    with open("database/embeds.json", "r", encoding="utf8") as embedsf:
        embeddata = json.load(embedsf)

    # VARIABLES
    # PERM_ -> for MISSING_PERMISSION
    PERM_TITLE = embeddata["ERRORS"]["MISSING_PERMISSION"]["TITLE"]
    PERM_DESCRIPTION = embeddata["ERRORS"]["MISSING_PERMISSION"]["DESCRIPTION"]
    PERM_AUTHOR_NAME = embeddata["ERRORS"]["MISSING_PERMISSION"]["AUTHOR_NAME"]
    PERM_AUTHOR_LINK = embeddata["ERRORS"]["MISSING_PERMISSION"]["AUTHOR_LINK"]
    PERM_THUMBNAIL = embeddata["ERRORS"]["MISSING_PERMISSION"]["THUMBNAIL"]

    if embeddata["ERRORS"]["MISSING_PERMISSION"]["COLOR"] == "red":
        PERM_COLOR = 0xff0000
    elif embeddata["ERRORS"]["MISSING_PERMISSION"]["COLOR"] == "green":
        PERM_COLOR = 0x00ff00
    elif embeddata["ERRORS"]["MISSING_PERMISSION"]["COLOR"] == "blue":
        PERM_COLOR = 0x0000ff

    # ARGS_ -> for MISSING_ARGUMENTS
    ARGS_TITLE = embeddata["ERRORS"]["MISSING_ARGUMENTS"]["TITLE"]
    ARGS_DESCRIPTION = embeddata["ERRORS"]["MISSING_ARGUMENTS"]["DESCRIPTION"]
    ARGS_AUTHOR_NAME = embeddata["ERRORS"]["MISSING_ARGUMENTS"]["AUTHOR_NAME"]
    ARGS_AUTHOR_LINK = embeddata["ERRORS"]["MISSING_ARGUMENTS"]["AUTHOR_LINK"]
    ARGS_THUMBNAIL = embeddata["ERRORS"]["MISSING_ARGUMENTS"]["THUMBNAIL"]
    ARGS_ERROR = embeddata["ERRORS"]["MISSING_ARGUMENTS"]["ERROR"]
    ARGS_ERROR_VALUE = embeddata["ERRORS"]["MISSING_ARGUMENTS"]["ERROR_VALUE"]
    ARGS_POSSIBLE_FIX = embeddata["ERRORS"]["MISSING_ARGUMENTS"]["POSSIBLE_FIX"]
    ARGS_POSSIBLE_FIX_VALUE = embeddata["ERRORS"]["MISSING_ARGUMENTS"]["POSSIBLE_FIX_VALUE"]

    if embeddata["ERRORS"]["MISSING_ARGUMENTS"]["COLOR"] == "red":
        ARGS_COLOR = 0xff0000
    elif embeddata["ERRORS"]["MISSING_ARGUMENTS"]["COLOR"] == "green":
        ARGS_COLOR = 0x00ff00
    elif embeddata["ERRORS"]["MISSING_ARGUMENTS"]["COLOR"] == "blue":
        ARGS_COLOR = 0x0000ff

    # COMMON
    TITLE = embeddata["ERRORS"]["COMMON"]["TITLE"]
    DESCRIPTION = embeddata["ERRORS"]["COMMON"]["DESCRIPTION"]
    THUMBNAIL = embeddata["ERRORS"]["COMMON"]["THUMBNAIL"]

    if embeddata["ERRORS"]["COMMON"]["COLOR"] == "red":
        COLOR = 0xff0000
    elif embeddata["ERRORS"]["COMMON"]["COLOR"] == "green":
        COLOR = 0x00ff00
    elif embeddata["ERRORS"]["COMMON"]["COLOR"] == "blue":
        COLOR = 0x0000ff



class FakeEmbeds:

    # Opening the json file
    with open("database/embeds.json", "r", encoding="utf8") as embedsf:
        embeddata = json.load(embedsf)

    # VARIABLES
    # The author info also comes for the error embed\
    TITLE = embeddata["FAKE_INFO"]["TITLE"]
    THUMBNAIL = embeddata["FAKE_INFO"]["THUMBNAIL"]
    AUTHOR_LINK = embeddata["FAKE_INFO"]["AUTHOR_LINK"]
    AUTHOR_NAME = embeddata["FAKE_INFO"]["AUTHOR_NAME"]

    if embeddata["FAKE_INFO"]["COLOR"] == "red":
        COLOR = 0xff0000
    elif embeddata["FAKE_INFO"]["COLOR"] == "green":
        COLOR = 0x00ff00
    elif embeddata["FAKE_INFO"]["COLOR"] == "blue":
        COLOR = 0x0000ff


class Help:
    # Opening the json file
    with open("database/embeds.json", "r", encoding="utf8") as embedsf:
        embeddata = json.load(embedsf)

    # VARIABLES
    COLOR = embeddata["HELP"]["COLOR"]


