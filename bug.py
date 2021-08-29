import discord
class MyClient(discord.Client):
    async def on_ready(self):
        print('Logged on as', self.user)
 
    async def on_message(self, message):
        # don't respond to ourselves
        if message.author == self.user:
            return
 
        if message.content == '.':
            await message.channel.send('你是一个一个机器人')
        if message.content == 'File':
            await message.channel.send(file=discord.File(r'bug.py'))
client = MyClient()
client.run('i am key')
