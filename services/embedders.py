import discord
from datetime import datetime

def embedder(colour, name):
    embed = discord.Embed(
        title="Visit our website for more information.",
        colour=discord.Colour(colour),
        url="http://www.texasstaterp.com/",
        description="Support us by donating at [payapl](https://www.paypal.com/cgi-bin/webscr?cmd=_s-xclick&hosted_button_id=HX5L5L5N5UESQ&source=url)",
        timestamp=datetime.utcfromtimestamp(1589809343)
    )
    embed.set_author(
        name=name,
        url="http://texasstaterp.com/",
        icon_url="http://www.texasstaterp.com/wp-content/uploads/2020/03/websidte-logo.png"
    )
    embed.set_thumbnail(url="http://www.texasstaterp.com/wp-content/uploads/2020/03/websidte-logo.png")
    embed.set_footer(text="Created at")

    return embed
