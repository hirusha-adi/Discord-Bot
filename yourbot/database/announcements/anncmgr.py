
class AnnouncementsManagingChannels:

    announcements_managing_channellist = []
    with open("yourbot/database/Announcements/Announcements_channels.txt", "r") as file:
        lines = file.readlines()
        for line in lines:
            try:
                announcements_managing_channellist.append(int(line))
            except ValueError:
                print(
                    "[!!] Please check for empty files in Announcements_channels.txt")
            except Exception as e:
                print("Error", e)


def add_channel_to_Announcements_managing_channellist(id: int = None):
    with open("yourbot/database/Announcements/Announcements_channels.txt", "a") as file:
        file.write(f"\n{id}")

    if not (int(id) in AnnouncementsManagingChannels.announcements_managing_channellist):
        AnnouncementsManagingChannels.announcements_managing_channellist.append(
            int(id))


class AnnouncementsSendingChannels:

    announcements_sending_channellist = []
    with open("yourbot/database/Announcements/Announcements_channels.txt", "r") as file:
        lines = file.readlines()
        for line in lines:
            try:
                announcements_sending_channellist.append(int(line))
            except ValueError:
                print(
                    "[!!] Please check for empty files in Announcements_channels.txt")
            except Exception as e:
                print("Error", e)


def add_channel_to_Announcements_sending_channellist(id: int = None):
    with open("yourbot/database/Announcements/Announcements_channels.txt", "a") as file:
        file.write(f"\n{id}")

    if not (int(id) in AnnouncementsSendingChannels.announcements_sending_channellist):
        AnnouncementsSendingChannels.announcements_sending_channellist.append(
            int(id))
