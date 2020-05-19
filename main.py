import sys
import configparser
from pathlib import Path
from pprint import pprint
from bots.TXSRPBot import ServerInfo
from discord.ext import commands, tasks
from services.serverhttp import check_server
from state.activeBots import set_bot, get_bot

server_flag = True

if __name__ == '__main__':
    cfg = configparser.ConfigParser()
    conf_file = Path("./config.ini")
    conf_reqs = ("token", "prefix", "server")
    confs = {}

    if conf_file.is_file():
        cfg.read(conf_file)
    else:
        print("Cannot locate 'config.ini' file.")
        sys.exit(0)

    for req in conf_reqs:
        if cfg.has_option(req, req):
            confs[req] = cfg.get(req, req)
        else:
            print(f"conf.ini missing {req}.")
            sys.exit(0)

    # TODO: load from db
    confs['name'] = 'texasStateRolePlayServerInfo'
    confs['leo_breakdown'] = {
        '[1D-': "Texas Department of Safety",
        '[1C-': "Webb County Sherrifs Office",
        '[1E-': "San Antonio Police Department",
        '[1A-': "Fire & EMS",
        '<LT>': "Fire & EMS"
    }

    tsbot = ServerInfo(**confs)
    set_bot(confs['name'], tsbot)

@tsbot.client.event
async def on_ready():
    print(f'Successfully logged in and booted...!')
    server_status.start()

@tasks.loop(seconds=10.0)
async def server_status():
    global server_flag

    channel = tsbot.client.get_channel(690321470924259612)

    sf = server_flag
    server_flag = check_server(tsbot)

    if sf != server_flag:
        if server_flag:
            await channel.send("Server is back up")
            print("Server is back up")
        else:
            await channel.send("Server is down")
            print("Server is down")

tsbot.cogs()
tsbot.run()

# bot_info = get_bot("texasStateRolePlayServerInfo")
# print(tsbot)
# print(bot_info)
