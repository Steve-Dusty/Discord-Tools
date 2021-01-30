import discord  
import asyncio
import datetime
import json
import requests


client = discord.Client()
client.sniped_messages = {}

with open("config.json") as foo:
    info = json.load(foo)

@client.event
async def on_ready():
    print(f"[INFO]====> Logged in as {client.user}")
    print("--------------------------------------")
    print(f"[LOADED]====> Loaded user identification {info['user_id']}")
    print(f"[LOADED]====> Loaded logging channel identification {info['logging_id']}")
    print(f"[LOADED]====> Loaded user token {info['token']}")


# Snipes messaging tester
@client.event
async def on_message_delete(message):
    # Filters commands

    if not message.content.startswith("/snipe"):
        client.sniped_messages[message.channel.id] = (message.content, message.author)

    for ids in info["logging_id"]:
        if message.channel.id == ids:
            with open("messages.txt", "a") as msgs:
                msgs.write(f"===={message.author.name}, {datetime.datetime.now().strftime('%x')}, {datetime.datetime.now().strftime('%X')}====\n{message.content}\n")


@client.event
async def on_message(message):
    if message.author.id == info["user_id"]:
        # This piece of code tests if bot works
        if message.content.startswith('/test'):
            await message.channel.send("**This is a test.**")

        # The announce function
        if message.content.startswith('/announce'):
            # Gets the announcement message
            x = message.content.split()[1:]
            announcement = " ".join(x)
            # Deletes command immediately after started process.
            await message.delete()
            d = datetime.datetime.now().strftime("%B %d, %Y")
            t = datetime.datetime.now().strftime("%-I:%M %p")
            await message.channel.send(f":mega: **__Announcement__** :mega: ({d}) ({t})\n```{announcement}```")
            
        # The poll function
        if message.content.startswith('/poll'):
            # Gets the poll message
            y = message.content.split()[1:]
            vote = " ".join(y)
            # Deletes command immediately after started process.
            await message.delete()
            d = datetime.datetime.now().strftime("%B %d, %Y")
            t = datetime.datetime.now().strftime("%-I:%M %p")
            poll = await message.channel.send(f":ballot_box: **__Poll__** :ballot_box: ({d}) ({t})\n```{vote}```")
            await poll.add_reaction("👍")
            await poll.add_reaction("👎")
        
        # The question command
        if message.content.startswith('/question'):
            # Gets the poll message
            z = message.content.split()[1:]
            question = " ".join(z)
            # Deletes command immediately after started process.
            await message.delete()
            d = datetime.datetime.now().strftime("%B %d, %Y")
            t = datetime.datetime.now().strftime("%-I:%M %p")
            await message.channel.send(f":grey_question: **__Question__** :grey_question: ({d}) ({t})\n```{question}```")

        # The avatar function
        if message.content.startswith('/avatar'):
            # Gets content after prefix and command
            f = message.content.split()[1:]
            #Strips the returned value in list to string
            identification = " ".join(f)
            # stripped it from discord identifiers <>@!
            stringID = identification.strip("<>@!")
            # Turns them into integers, IDs are integers
            integerID = int(stringID)
            # Gets user using ID
            user = client.get_user(integerID)
            # Deletes the message
            await message.delete()
            # Sends the avatar_url of the user.
            await message.channel.send(user.avatar_url)

        # Gets the last deleted message
        if message.content.startswith('/snipe'):
            contents, author = client.sniped_messages[message.channel.id]
            await message.channel.send(f"**Message was deleted by:** {author.name}#{author.discriminator}\n**The message content is:** ```{contents}```")
            await message.delete()

        if message.content.startswith("/essay"):
            await message.delete()
            running = True
            while running:
                async with message.channel.typing():
                    # Do nothing
                    pass
                
            

client.run(info["token"],bot=False)
