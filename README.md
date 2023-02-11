# discord_spotify
Simple discord bot to add spotify songs to a playlist whenever a spotify link is posted in the chat

There were several discord spotify bots available, but none of them were as simple as i wanted. I made this so the bot will 
monitor a server/channel, and when a spotify song link is posted, it will add that song to a collaborative playlist, and then 
send a small message that the song has been added. It's unobtrusive and simple, and allows people to share music easily.

Edit your .env file with you discord tokens and keys. Run with python3 main.py. You may need to install dependencies.

You will need to create a bot/application in discord, give it the following permissions:
- "bot"
- "application.commands"
- "Send messages"
- "Read messages/View Channels"
- "Embed Links"

Copy the invitation URL and invite the bot to your server.

I tried to daemonize this but it wasnt working correctly. Instead I just run it in a screen session.
