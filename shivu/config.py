class Config(object):
    LOGGER = True

    # Get this value from my.telegram.org/apps
    OWNER_ID = "6954636450"
    sudo_users = "6954636450","5629555417","7618952261","7224129219","7249975273","6347440084"
    GROUP_ID = -1002265178229
    TOKEN = "7841699829:AAEgFBEzVU-kDfL8R4qcULlAA5WdexU8XfQ"
    mongo_url = "mongodb+srv://bak01072007:bak123456@waifu2.5ahbyyu.mongodb.net/"
    PHOTO_URL = ["https://files.catbox.moe/umhazg.jpg", "https://files.catbox.moe/itvfzl.jpg"]
    SUPPORT_CHAT = "-1002265178229"
    UPDATE_CHAT = "-1002036001760"
    BOT_USERNAME = "@Dynamic_Catcher_bot"
    CHARA_CHANNEL_ID = "-1002472821477"
    api_id = 25976808
    api_hash = "30591a977139ed41fb5d736eaa090aa0"

    
class Production(Config):
    LOGGER = True


class Development(Config):
    LOGGER = True
    LOGGER = True
