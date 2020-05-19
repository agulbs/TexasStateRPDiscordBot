from services.serverhttp import get_players, check_server
from services.embedders import embedder
from discord.ext import commands, tasks
from state.activeBots import get_bot
from pprint import pprint
import discord
import asyncio


class ServerInfo(commands.Cog):

    def __init__(self, bot):
        self.bot = bot
        self.bot.remove_command("help")
        self.bot_info = get_bot("texasStateRolePlayServerInfo")
        self.tbot = self.bot_info['bot']

    @commands.command(
        name="help",
        description="command information",
        brief="commands",
        aliases=["h", "HELP"],
        pass_context=True,
    )
    async def helper(self, context):
        msg = (
            "```ml\n"
            "Commands:\n"
            ' .players       use ".players" to view all players online.\n'
            ' .departments   use ".departments" to view the LEO breakdown.\n'
            ' .rpstat        use ".rpstat" to see who is RPing as what.\n'
            ' .status        use ".status" to check the server status.\n'
            ' .staff         use ".staff" to load the server\'s staff.\n```'
        )
        await context.send(msg)

    @commands.command()
    async def departments(self, context):
        members = []
        depts = {}

        for guild in self.bot.guilds:
            if guild.name == "PenetratingPineapple's server":
                members = [g for g in guild.members]
                break

        for member in members:
            if member.nick is None:
                if "Civs" in depts:
                    depts["Civs"] += "\n" + member.name
                else:
                    depts["Civs"] = "```\n" + member.name
            else:
                sign = member.nick[0:4]

                if sign in self.tbot.leo_breakdown:
                    d = self.tbot.leo_breakdown[sign]
                    if d in depts:
                        depts[d] += "\n" + member.nick
                    else:
                        depts[d] = "```\n" + member.nick

        embed = embedder(0xFFFF00, "Department Breakdown")

        for dept in depts:
            value = depts[dept] + "\n```"
            embed.add_field(name=dept, value=value, inline=False)

        await context.send(embed=embed)


    @commands.command()
    async def staff(self, context):
        members = []
        roles = {
            "MODERATOR": [],
            "RECRUITER": [],
            "ADMIN": [],
            "BOT": []
        }

        for guild in self.bot.guilds:
            if guild.name == "PenetratingPineapple's server":
                members = [g for g in guild.members]
                break

        for member in members:
            for role in member.roles:
                if role.name in roles:
                    if member.nick is None:
                        roles[role.name].append(member.name)
                    else:
                        roles[role.name].append(member.nick)


    @commands.command()
    async def players(self, context):
        plyrs = get_players(self.tbot)
        total_players = 0

        if plyrs['status'] == False:
            await self.status(context)
        else:
            total_players = plyrs['total']

        name = "Playrs Online: " + str(total_players)
        embed = embedder(0xFF0099, name)
        player_names = "```\n"

        for plyr in plyrs['players']:
            player_names += plyr + "\n"

        player_names += '```'

        embed.add_field(name="Players", value=player_names, inline=False)
        await context.send(embed=embed)


    @commands.command()
    async def rpstat(self, context):
        players = get_players(self.tbot)

        if players['status'] == False:
            await status(context)
        else:
            embed = embedder(0x0dd5fc, "Player/Department Breakdown")

            for dept in players['departments']:
                player_names = players['departments'][dept]

                if len(player_names) == 0:
                    p = "(none)"
                else:
                    p = '\n'.join(player_names)

                p = '```' + p + '```'

                name = dept + ": " + str(len(player_names))
                embed.add_field(name=name, value=p, inline=False)

            await context.send(embed=embed)


    @commands.command()
    async def status(self, context):
        plyrs = get_players(self.tbot)

        if plyrs['status'] == False:
            embed = discord.Embed(description="Server Status 🌡️", color=0xff1439)
            embed.add_field(name="Status", value="Server is down.", inline=False)
        else:
            embed = discord.Embed(description="Server Status 🌡️", color=0x39ff14)
            embed.add_field(name="Status", value="Server is up & running.", inline=False)

        await context.send(embed=embed)

def setup(bot):
    bot.add_cog(ServerInfo(bot))
