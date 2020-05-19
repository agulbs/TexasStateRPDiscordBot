from discord.ext import commands

class ServerInfo:
    def __init__(self, name, token, server, prefix, leo_breakdown):
        self.name = name
        self.token = token
        self.server = server
        self.prefix = prefix
        self.client = commands.Bot(command_prefix=[prefix])
        self.leo_breakdown = leo_breakdown

    def cogs(self):
        self.client.load_extension("cogs.ServerInfo")

    def run(self):
        self.client.run(self.token)

    def set_name(self, name):
        self.name = name

    def get_name(self):
        return self.name

    def set_token(self, token):
        self.token = token

    def get_token(self):
        return self.token

    def set_server(self, server):
        self.server = server

    def get_server(self):
        return self.server

    def set_prefix(self, prefix):
        self.prefix = prefix

    def get_prefix(self):
        return self.prefix

    def set_client(self, client):
        self.client = client

    def get_client(self):
        return self.client

    def set_leo_breakdown(self, leo_breakdown):
        self.leo_breakdown = leo_breakdown

    def get_leo_breakdown(self):
        return self.leo_breakdown

    def __str__(self):
        return f"token: {self.token}\nserver: {self.server}\nprefix: {self.prefix}\nclient: {self.client}\nleo_breakdown: {self.leo_breakdown}\n"
