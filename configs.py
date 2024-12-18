from os import path, getenv

class Config:
    API_ID = int(getenv("API_ID", "27705761"))
    API_HASH = getenv("API_HASH", "822cb334ca4527a134aae97f9fe44fd6")
    BOT_TOKEN = getenv("BOT_TOKEN", "7688784612:AAG2i-qcDpxY3GNe7hdipfWCXToXW42kO2g")
    FSUB = getenv("FSUB", "https://t.me/TheAllLink")
    CHID = int(getenv("CHID", "your channel id"))
    SUDO = list(map(int, getenv("SUDO").split()))
    MONGO_URI = getenv("MONGO_URI", "mongodb+srv://akashrabha2005:781120@cluster0.pv6yd2f.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
    
cfg = Config()
