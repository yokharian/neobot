## Requirements
- Python 3.6 and up - https://www.python.org/downloads/
- git - https://git-scm.com/download/

## Useful to always have
Keep [this](https://discordpy.readthedocs.io/en/latest/) saved somewhere, as this is the docs to [discord.py]().
All you need to know about the library is defined inside here, even code that I don't use in this example is here.

## How to setup
1. Make a bot [here](https://discordapp.com/developers/applications/me) and grab the token
![Image_Example1](https://i.alexflipnote.dev/f9668b.png)
<!-- thank you alex flip note, i learned a lot-->

2. **config.json** fill in the required spots

3. To install what you need, do **pip install -r requirements.txt**<br>
(If that doesn't work, do **python -m pip install -r requirements.txt**)<br>
`NOTE: Use pip install with Administrator/sudo`

4. Start the bot by having the cmd/terminal inside the bot folder and type **python index.py**

5. You're done

## FAQ
Q: I don't see my bot on my server!<br>
A: Invite it by using this URL: https://drapaiton.github.io/DiscordTemplateBot/<br>you need the bot client id, go backwards


## Technology Stack
 - [Heroku](https://www.heroku.com) as a Hosting Platform
 


# Optional tools
### Flake8
Flake8 is a tool that helps you keep your code clean. Most coding softwares will have a plugin that supports this Python module so it can be integrated with your IDE. To install it, simply do `pip install flake8`. If you're using python 3.7, install by doing `pip install -e git+https://gitlab.com/pycqa/flake8#egg=flake8`


# Deployment

### heroku.com
You can host it on [Heroku](https://www.heroku.com) for free ([account verification required](https://devcenter.heroku.com/articles/account-verification)).

[![Deploy](https://www.herokucdn.com/deploy/button.svg)](https://heroku.com/deploy)


### Repl.it
You can run this on Repl.it!
[![Run on Repl.it](https://repl.it/badge/github/AlexFlipnote/discord_bot.py)](https://repl.it/github/AlexFlipnote/discord_bot.py)
Make sure to setup **config.json** in the way stated above.
