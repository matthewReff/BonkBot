# Overview
Python discord bot for bonking users

Communicates with an AWS hosted HTTP API Gateway

# Personal Installation / Development Setup
[Python 3.9](https://www.python.org/downloads/release/python-3915/)

[Python Pip](https://pip.pypa.io/en/stable/installation/)

[Discord.py](https://discordpy.readthedocs.io/en/stable/intro.html#installing)

# Setting up the bot user
[Go to the discord app page](https://discord.com/developers/applications)

Create a new 

Go to `Settings` -> `Bot` -> `Build-A-Bot` -> `Add Bot` button. This will convert the application into a usable bot account.

Click the `Regenerate` button under `Token`. You might be prompted to confirm your account. Once this is done, copy the token.

Open the `bot.py` file, and add your copied token in quotes to the bot.run('') line.

Go back to the `Settings` -> `Bot` section in the discord app page

For this bot to work, it needs `Server Members Intent` to be allowed under `Privileged Gateway Intents`. Flip that toggle to on

Last step in the discord page, you'll need to go to the `Settings` -> `OAuth2` and copy your Client ID.

Add your Client ID to this link, and invite the bot to your server. https://discord.com/oauth2/authorize?client_id={Client ID Here}&scope=bot&permissions=274877975552