#!/usr/bin/python3.5
#Woot woot

import discord

client = discord.Client()

@client.event
async def on_member_join(member):
    server = member.server
	#We need to hard code the channel that the message is sent to
    await client.send_message(discord.Object(id='CHANNEL'), '{0.name} joined Pegasus Blend. Timestamp: {0.joined_at}'.format(member))


@client.event
async def on_message(message):
    # we do not want the bot to reply to itself
    if message.author == client.user:
        return
    if message.content.startswith('!hello'):
        msg = 'Hello {0.author.mention}'.format(message)
        await client.send_message(message.channel, msg)
    if message.content.startswith('season pass'):
        msg = 'https://media.giphy.com/media/ToMjGpx9F5ktZw8qPUQ/giphy.gif'.format(message)
        await client.send_message(message.channel, msg)

@client.event
async def on_member_update(before, after):
    if before.nick != after.nick:      
        await client.send_message(discord.Object(id='CHANNEL'), 'Nickname change. Before: {} After: {}'.format(before.nick, after.nick))
    else:
        return

@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')

client.run('APIKEY')
