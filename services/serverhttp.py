import requests
import json

def get_players(bot):
    playerList = {
        'status':False,
        'players': {},
        'departments': {
            "Texas Department of Safety": [],
            "Webb County Sherrifs Office": [],
            "San Antonio Police Department": [],
            "Fire & EMS": [],
            "Civs": []
        }
    }

    try:
        r = requests.get(bot.server + "players.json", timeout=2)
        players = json.loads(r.text)
        playerList['status'] = True
    except:
        return playerList

    for player in players:
        name = player['name']
        sign = name[0:4]

        playerList['players'][name] = player

        if sign in bot.leo_breakdown:
            playerList['departments'][bot.leo_breakdown[sign]].append(name)
        else:
            playerList['departments']["Civs"].append(name)

    playerList['total'] = len(playerList['players'].keys())

    return playerList

def check_server(bot):
    try:
        r = requests.get(bot.server + "players.json", timeout=2)
        return True
    except:
        return False
