
class Users:

    blacklisted_users = []
    with open("yourbot/database/blacklist/users.txt", "r", encoding="utf8") as file:
        lines = file.readlines()
        for line in lines:
            try:
                blacklisted_users.append(int(line))
            except ValueError:
                print("[!!] Please check for empty lines in: chatbot_channel_list.txt")
            except Exception as e:
                print("Error", e)



class Servers:

    blacklisted_servers = []
    with open("yourbot/database/blacklist/servers.txt", "r", encoding="utf8") as file:
        lines = file.readlines()
        for line in lines:
            try:
                blacklisted_servers.append(int(line))
            except ValueError:
                print("[!!] Please check for empty lines in: chatbot_channel_list.txt")
            except Exception as e:
                print("Error", e)


def blacklist_user(id: int = None):

    with open("yourbot/database/blacklist/users.txt", "a", encoding="utf8") as file:
        file.write(f"\n{id}")

    if not (int(id) in Users.blacklisted_users):
        Users.blacklisted_users.append(int(id))


def blacklist_server(id: int = None):
    with open("yourbot/database/blacklist/servers.txt", "a", encoding="utf8") as file:
        file.write(f"\n{id}")

    if not (int(id) in Servers.blacklisted_servers):
        Servers.blacklisted_servers.append(int(id))



