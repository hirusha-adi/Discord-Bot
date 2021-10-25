import json

# https://github.com/Darkempire78/Raid-Protect-Discord-Bot/blob/master/Tools/utils.py
# I learned a lot here!
# This was possible thanks to github user `Darkempire78`


def getConfig(guildID):
    with open("yourbot/database/scinfo/config.json", "r") as config:
        data = json.load(config)
    if str(guildID) not in data["guilds"]:
        defaultConfig = {
            "prefix": ">",
            "antiProfanity": True,
            "antiNudity": True,
            "antiSpam": True,
            "allowSpam": [],
            "captcha": False,
            "captchaChannel": False,
            "logChannel": 1,
            "temporaryRole": 1,
            "minAccountDate": 86400,
            "logServerCommands": True
        }
        updateConfig(guildID, defaultConfig)
        return defaultConfig
    return data["guilds"][str(guildID)]


def updateConfig(guildID, data):
    with open("yourbot/database/scinfo/config.json", "r") as config:
        config = json.load(config)
        config["guilds"][str(guildID)] = data
        newdata = json.dumps(config, indent=4, ensure_ascii=False)
    with open("yourbot/database/scinfo/config.json", "w") as config:
        config.write(newdata)


async def getGuildPrefix(bot, message):
    if not message.guild:
        return "?"
    else:
        config = getConfig(message.guild.id)
        return config["prefix"]
