# reseller-tools
Simple discord bot for reselling tools. (Currency converter, size converter and payout / fee calculator)

Custom emojis needed to be added to your discord server for this bot to work, here is how to:
  1. Visit https://drive.google.com/drive/folders/1gLyn1ax64WaFieJDbm4q6pED3pMpeEuy?usp=sharing and download these images
  2. Go to the discord app or web client, and right click on your server and press server settings
  3. Press the "Emoji tab" in the Overview category on the left hand side
  4. Click upload image that is in the purple button and upload all of the files downloaded (do not change the names of the emojis)

Right now money and size converter are US, EU, and UK, may add more later.

If you do not have a developer discord account: https://www.digitaltrends.com/gaming/how-to-make-a-discord-bot/

How to obtain a token:
1. Visit https://discordapp.com/developers/applications/ and sign into to your account. If it doesnt redirect you back after logging in, visit the link again
2. Press create an application and name it
3. Press the "Bot" category on the left and press "Add Bot" in purple.
4. Under the username it will say "Token" and click the blue text to reveal it. Then put this in the token variable in line 19 of the script.

**Remember to use the OAUTH link in the developer site to add the bot to your server**

How to run:
1. Open the script in a text editor and put your token in the token variable and save
2. Open a Command Prompt window and navigate to the folder
3. Run python tools.py

Requirements:
Python 3.6.5 or greater
discord.py v0.16.12

P.S Some of this code (especially the calculations) are messy. This was an old script I had made a little bit back. Just trying to give a basic example of what a discord bot using the api wrapper looks like. Enjoy!
