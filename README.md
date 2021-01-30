# Discord-Tools

Discord-Tools is owned by Steve-Dusty. This Discord-Tool enhances your experience on Discord, the internet messenger.

# First steps
To start, clone this repository onto your local machine. `git clone https://github.com/Steve-Dusty/Discord-Tools` Remember the path to the program.<br> Install Python 3 if you do not already have it.<br>
Then, install discord.py 1.5.1 using pip3 by `pip3 install discord.py==1.5.1`. This will also work with reverting versions if you already have discord.py installed.<br>
**WARNING:** Some commands will only work discord.py 1.5.1 due to some bugs in version 1.6<br>

This is confusing, so to recap:<br>
Run `pip3 install discord.py==1.5.1` on the command line. <br>
`cd` into the folder where you want the bot files to be in.<br>
Run `git clone https://github.com/Steve-Dusty/Discord-Tools`<br>
You're all set!
One thing to remember is that you'll need fundamental filesystem skills. Although README.md is extremely thorough, my program is not meant for absolute tech-illiterates.<br>

# Configuration
You must first configurate the program to the correct settings of your Discord account in a few easy steps.

1. Open config.json file.
2. Go to `"token"` and input the token of your account inside the quotation marks `""`
3. Move down to the line under `"token"` and you'll see `"user_id`. Now, replace `"user_id"` with the identification of your account as is.
4. Lastly, on `"logging_id"`, put the ID of the channel you want to message log. Group chats work too!
Ta-da! You're officially finished with configuration.<br>

**Example**<br>
```json
{
  "token":"H5boY1GE3dNFiQJSM.IdkI.Dl0PQWEfYBI0Yv-NzKsNTEyNTQJdWQ0OSmOMjY0",
  "user_id":936212549914029121,
  "logging_id":[
    192806890395834216,
    776919872286097462,
    788082069698904104,
    757745285186453586,
    804431813962367029,
    506605752899731457
  ]
}
```
You can add as much channels as you desire, but beware, don't get carried off as logging may get slow or rate-limited.
Be sure to place a commma `,` in the end of every channel ID in the array (list) except the last one, as shown in the example above.

# Usage 
There are 6 commands available to you.

* `/announce [message]` This announces the message you want to send. Works anywhere.
* `/question [message]` Same as the last one but asks with the message.
* `/poll [message]` This command creates a poll based on your message.
* `/avatar [@user]` Fetches the avatar link of the identified user. Works with mention, ID, and whatnot.
* `/essay` Shows typing indicator on the channel you called the commmand on. Goes on forever until a message is sent to that channel.
* `/snipe` This gets the last deleted message in the current channel. 
All deleted messages in the channel configured in `config.json` will be logged inside `messages.txt` along with its author and the time deleted of your timezone. 

An addition command is added called `/test`, if a message is returned, the bot is working. 

<br>What to watch out for:
  When I refer to "message returned" or "message sent", I mean that it will always be sent to the channel using your account, not logged in the terminal.
  To clarify, every output will be sent inside the current channel with exceptions to `/essay` and the automatic message logging system.
  
**Running the main file**<br>
When you're finished with every step, run the file by `python utility.py` on Windows  or `python3 utility.py` if you're on Linux or Unix without command alias.<br>

# FAQ 
Answering frequently-asked-questions<br>

**Where can I find you?**<br>
You can reach me by opening an issue right here on Github, make a pull request, or contact my Discord alt account `guy3#5398`.<br>
**Is the program harmful in any way, shape or form?**<br>
You shouldn't be downloading hack scripts on Github if you don't understand them, that's for you to figure out.<br>
**How can I find my account token and IDs?**<br>
To find your token, go to [discord.com/robots.txt](https://discord.com/robots.txt), access console in developer tools and type `localStorage.getItem("token")`. Your token will be outputted below. Copy the token but ignore the quotes.<br>
Here is everything you need to find your ID [how to find IDs](https://support.discord.com/hc/en-us/articles/206346498-Where-can-I-find-my-User-Server-Message-ID-), including direct message IDs if you want to log DMs.<br>
**What can I do if the program isn't working properly and showing errors?**<br>
You can open an issue here on Github or contact me on Discord.<br>
**How do I contribute?**<br>
Contact me on Discord or make a pull request to fix bugs, optimize code, or add other necessary components.<br>
**Is this against Discord Terms of Service?**<br>
Yes, so don't get caught. You can delete messages so others cannot report your suspicious messages. Deleted messages are not saved in the Discord messaging database.

# Resources

Python documentation https://docs.python.org/3/<br>
Discord.py documentation https://discordpy.readthedocs.io/<br>
Discord.py pypi package https://pypi.org/project/discord.py/<br>

# What now?
Now that you have everything, run the bot and test out  Discord-Tools.<br>
You may not understand the purpose of every command by me just describing them.<br>
Go out and spread your wings, see how the commands look like and how they work!<br>



