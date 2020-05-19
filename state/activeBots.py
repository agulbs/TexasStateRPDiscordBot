from datetime import datetime

activeBots = {}

def set_bot(name, bot):
    if name not in activeBots:
        activeBots[name] = {
            "bot": bot,
            "startTime": datetime.now(),
            "upTime": 0
        }
    else:
        activeBots[name] = {
            "bot": bot,
            "relaunched": datetime.now(),
            "upTime": 0,
            "instances": activeBots[name]["instances"] + 1
        }

def get_bot(name):
    if name in activeBots:
        return activeBots[name]
    else:
        return None
