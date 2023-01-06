
# VoiceCraft
A silly program that listens for certain words you speak while playing Minecraft, and blows you up or runs commands in your game to punish you for saying them. And insults you. Integrates with Google Sheets for crowdsourced insults. Inspired by DougDoug on Twitch (https://youtu.be/JsWK398Vvd8)

Note that this currently only works on standard US/English keyboards because it automatically presses the "/" key to run commands. It also may not work while you're in menus since you can't run commands in menus, so... honor system.

**RUN AS ADMIN!**

_____

HOWTO:
You can use the source code if you like, but please download the program precompiled from the releases page. Its a single easy executable. 

Run the executable and you'll see the following files generated with the following uses: 
*Note that all files are separated by NEWLINES. Each new entry should be its own line.*

**badwords.txt** - List of all the "bad words" you can't say while playing, one per line. If you say any of these words, the bot will run one of the configured *commands* and insult you with one of the configured *insults.*  
Pre-made list of all Minecraft Blocks to replicate DougDoug's "If I say a block I explode" idea: - [**DOWNLOAD**](https://cdn.discordapp.com/attachments/390339521473937419/1050574129184645230/badwords.txt)

**cmds.txt** - List of all the Minecraft commands the bot will pick from to run when you say a bad word. By default, it spawns an exploding fireball that will kill you unless you're wearing blast protection enchanted armor. One command per line, no preceding slash needed.

**insults.txt** - List of all the insults the program will call you for saying a bad word. When you say a bad word it says aloud "You said (badword), (insult)" like "You said stone, dumbass." One per line. 
*ALTERNATELY* rather than adding any insults, you can add the "Share" URL of a Google Sheets document. Note that it must be set to "Anyone with the link can view." The program will read the sheet and use everything in Column A as insults, so you and all your friends can crowdsource insults.


USE / TROUBLESHOOTING:

 - The program needs to be run as admin, or it can't briefly block your input when running the command so you may get typos. 
 - If it doesn't work at first, wait 5 seconds then restart it. It usually works the second time.
 - It should use your default Windows microphone. Shouldn't need any requirements.
 - It works using [IntRX](https://github.com/gcfrxbots/IntRX)'s Minecraft engine, which utilizes Autohotkey to very quickly open the game's console, paste in a command, run it, and close the console. This does have a few limitations, namely that if you're in a pause menu or an inventory you cannot open chat so the command cannot run. 
 - A new version is coming soon that will utilize webhooks and integrate all users with a central server, that can run commands from a server to circumvent the inventory issue as well as run multiple commands (Such as exploding then /killing the user). 
 - Datapacks can be super useful for this, the program can trigger `/function`. We've actually made one for the default fireball command that also does `/kill` on the player, just in case you want to guarantee death along with the explosion. If you use this, change cmds.txt to `/function voicecraft:rxvc/badword` - [**DOWNLOAD**](https://cdn.discordapp.com/attachments/380586341366366220/1060810875973423124/VoiceCraft.zip)
 - If using commands that kill you, we find it more fun to set the Minecraft game rule `doImmediateRespawn` to true. It saves you from having to manually click "Respawn" every time, while also not giving you time to check your death coordinates to make it more punishing.

Thanks to Tigeri102 and iCeParadox64 for assistance with the blocklist, commands, and ideas. And insults.
