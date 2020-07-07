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

@bot.event
async def on_ready():
    guild = discord.utils.get(bot.guilds, name=GUILD)
    print(f'{bot.user} has connected to {guild.name}.')
    
    
@bot.command(name='info')
async def bot_info(ctx):
    await ctx.send('I\'m the Tricky Tipster. Whenever you join General, I\'ll give you a useful tip.')
    await ctx.send('Use command \'+ignore\' to stop receiving tips. Use command \'+receive\' to start receiving tips again.')
    
    
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
    
@bot.event
async def on_voice_state_update(member, before=None, after=369006447910191119):
    
    if before is not after and after.channel.id == 369006447910191119:
    
        if member.id in ignore_list:
            return
    
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
        'Trolls regenerate health when wounded, but are susceptible to fire.'
        ]
    
    
        daily_tip = random.choice(tips_list)
    
        to_channel = bot.get_channel(369006447910191117)
        await to_channel.send('-' * 100 + f'Welcome back, {member.name}. Here\'s a tip: \n\n{daily_tip}\n' + '-' * 100, delete_after=120)

bot.run(TOKEN)