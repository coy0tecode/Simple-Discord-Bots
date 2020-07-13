import os
import discord
import random
from dotenv import load_dotenv
from discord.ext import commands

load_dotenv(r'C:\PythonStuff\Projects\discord-bot\.env')
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('DISCORD_GUILD')

bot = commands.Bot(command_prefix='+')

# Ignores Rythm and Rythm2 by default
ignore_list = [235088799074484224, 252128902418268161]

# Tips list
tips_list = [
    'Watch out for the clouds.',
    'Never set spikes.',
    'Lay those bricks down.',
    'Do not burn the candle at both ends, as it leads to the life of a hairdresser.',
    'Never underestimate the power of the scout\'s code.',
    'Don\'t make me angry, you won\'t like me when I\'m angry.',
    'Vote early, and often.',
    'Try not. Do - or do not. There is no try.',
    'Get busy livin\' or get busy dyin\'.',
    'Fish are friends, not food.',
    'The grass is always greener on the side that\'s using Scotts® Turf Builder. Scotts® Turf Builder: Your lawn is hungry. Feed it!',
    'No journey is too great when one finds what he seeks.',
    'Secrets are like herpes; if you got \'em, might as well spread \'em around.',
    'The right man in the wrong place can make all the difference in the world.',
    'One should always play fairly when one has the winning cards.',
    'You can\'t hide from the Grim Reaper. Especially when he\'s got a gun.',
    'Shorts are comfy and easy to wear.',
    'Never pet a burning dog.',
    'First rule of politics, kiddo: Never let the truth get in the way of a good story.',
    'Clear alcohols are for rich women on diets.',
    'If you don\'t teach your children that Paris Hilton should be despised, how will they know?',
    'Only kiss me if you mean it.',
    'Wait 30 minutes after eating before you swim. Or don\'t. You\'re an adult, you decide.',
    'Don\'t eat that sandwich, it\'s not yours.',
    'Trolls regenerate health when wounded, but are susceptible to fire.',
    'Always wash your berries before you eat them.'
    ]
    
    
# Phrase lists for creating()
first = [
    'Always ',
    'Never ',
    'Don\'t ',
    'Remember to ',
    'You must ',
    'Please ',
    'If you value your life, '
]

second = [
    'wash ',
    'run ',
    'anger ',
    'caress ',
    'validate ',
    'fight ',
    'refurbish ',
    'acquire ',
    'obliterate ',
    'reconstitute ',
    'devour ',
    'destroy ',
    'bully ',
    'create ',
    'encourage ',
    'assimilate ',
    'paint ',
    'draw ',
    'operate on ',
    'kiss ',
    'work out with ',
    'make music with ',
    'remember ',
    'forget ',
    'restructure your company because of ',
    'file for bankruptcy due to ',
    'purchase a lottery ticket from ',
    'trust ',
    'build a house with ',
    'marry and start a life with ',
    'elope with ',
    'steal from ',
    'go to a jazz club with ',
    'eat tacos with ',
    'take advice from ',
    'get into an argument with ',
    'blow up the Deathstar with '
]

third = [
    '4 grapes ',
    'an emaciated orphan ',
    'Batman ',
    'the drummer from Led Zeppelin ',
    'Chris Tucker ',
    'a pelican ',
    '3 French hens ',
    'the Partridge family ',
    'Lewis Black ',
    'Meatwad ',
    'the TrickyTipster ',
    'an angry accountant ',
    'all past and present members of SNL ',
    'Master Chief ',
    'Ice Cube ',
    'a bowl of oatmeal ',
    'a wild stallion ',
    'hundreds of Eastern gray squirrels ',
    'Van Halen\'s tour bus ',
    'Eric Cartman ',
    'the Teletubbies ',
    'Jesus Christ ',
    'an alpaca ',
    'Walt Disney ',
    'Rihanna ',
    'Jackie Chan ',
    'Owen Wilson ',
    'an abandoned shack ',
    'the owl from Warcraft ',
    'Peter Griffin ',
    'an erupting volcano ',
    'a large, unidentified fish ',
    'a bic boi '
]

fourth = [
    'on a Tuesday.',
    'on a Sunday.',
    'on a Monday.',
    'indoors.',
    'outside.',
    'aboard Air Force One.',
    'without gloves.',
    'unless you are fully prepared.',
    'inside an aquarium.',
    'aboard a train.',
    'during a pandemic.',
    'in the middle of a war.',
    'during a funeral.',
    'on the toilet.',
    'while assembling a jigsaw puzzle.',
    'while getting a massage.',
    'at the doctor\'s.',
    'at your inlaws\' house.',
    'with anger in your heart.',
    'under duress.',
    'during an economic crisis.',
    'at the movie theatre.',
    'while strapped.',
    'at the wheat processing plant.',
    'during halftime at the SuperBowl.',
    'on your day off.',
    'without proper guidance.',
    'unless you really want to.',
    'in a magical forest.'
]
    

@bot.event
async def on_ready():
    guild = discord.utils.get(bot.guilds, name=GUILD)
    print(f'{bot.user} has connected to {guild.name}.')
    
    
@bot.command(name='info')
async def bot_info(ctx):
    await ctx.send('I\'m the Tricky Tipster. Whenever you join General, I\'ll give you a useful tip. ')
    await ctx.send('Use command \'+ignore\' to stop receiving tips. ' + 
                   'Use command \'+receive\' to start receiving tips again. ' +
                   'Use command \'+create\' to generate a randomized tip.')
    
    
@bot.command(name='ignore')
async def ignoring(ctx):

    global ignore_list

    if ctx.author.id not in ignore_list:
        ignore_list.append(ctx.author.id)
        await ctx.send(f'I am now ignoring {ctx.author}. No tip for you!', delete_after=10.0)
    else:
        await ctx.send(f'I was already ignoring {ctx.author}, and I still am.', delete_after=10.0)
        
        
@bot.command(name='receive')
async def receiving(ctx):

    global ignore_list
    
    if ctx.author.id in ignore_list:
        ignore_list.remove(ctx.author.id)
        await ctx.send(f'{ctx.author} will now receive tips when joining General voice chat.', delete_after=10.0)
    else:
        await ctx.send(f'{ctx.author}, you are already receiving tips.', delete_after=10.0)
        
@bot.command(name='create')
async def creating(ctx):

    line1 = random.choice(first)
    line2 = random.choice(second)
    line3 = random.choice(third)
    line4 = random.choice(fourth)
    
    await ctx.send('-' * 100 + '\nHere\'s your custom tip:\n\n' + line1 + line2 + line3 + line4 + '\n' + '-' * 100, delete_after=120)
    
@bot.event
async def on_voice_state_update(member, before, after):
    
    try:
        test_id = after.channel.id
    except:
        pass
    else:
        if after.channel.id == 369006447910191119:
    
            if member.id in ignore_list:
                return
    
            daily_tip = random.choice(tips_list)
    
            to_channel = bot.get_channel(369006447910191117)
            await to_channel.send('-' * 100 + f'Welcome back, {member.name}. Here\'s a tip: \n\n{daily_tip}\n' + '-' * 100, delete_after=120)

bot.run(TOKEN)