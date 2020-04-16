try:
    import os
    import time
    import discord
    from discord.ext import commands
except ImportError:
    import os
    import time
    os.system("py -m pip install discord.py")
    time.sleep(10)
    import discord
    from discord.ext import commands


token = 'NzAwMjg5NjA3MzkyMTY1OTU5.XpgxoA.8s7RkRoRLbZ8VZo3Genw3WaZPYI'

client = commands.Bot(command_prefix = '-')

@client.event
async def on_startup():
    pass

@client.event
async def on_message(message):
    if message.content == "Hey":
        await message.channel.send("Hey " + str(message.author))


client.run(token)
