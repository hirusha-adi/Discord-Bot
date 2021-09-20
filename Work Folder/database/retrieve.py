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








