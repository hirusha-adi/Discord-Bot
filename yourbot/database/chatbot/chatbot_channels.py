import json


class ChatBotChannels:
    with open("yourbot/database/chatbot/chatbot_settings.json", "r", encoding="utf8") as embedsf:
        embeddata = json.load(embedsf)

    CHANNEL_SLEEP_TIME = int(embeddata["CHANNEL_SLEEP_TIME"])

    channel_ids = []
    with open("yourbot/database/chatbot_channel_list.txt", "r") as file:
        lines = file.readlines()
        for line in lines:
            try:
                channel_ids.append(int(line))
            except ValueError:
                print(
                    "[!!] Please check for empty lines in: chatbot_channel_list.txt")
            except Exception as e:
                print("Error", e)


def add_channel(id: int = None):
    # Adding to file
    with open("yourbot/database/chatbot/chatbot_channel_list.txt", "a") as file:
        file.write(f"\n{id}")

    # Adding to the cuurent channel_ids list to work until the bot is restarted
    if not (int(id) in ChatBotChannels.channel_ids):
        ChatBotChannels.channel_ids.append(int(id))
