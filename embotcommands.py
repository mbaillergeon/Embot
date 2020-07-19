import discord
from discord.ext import commands


memberstrikes = {}

@commands.command()
async def hello(ctx):
    print("Command Triggered")
    await ctx.send(f"Hello, {ctx.author}")

@commands.command()
async def embot_help(ctx):
    response = 'I dont know how to do anything yet.'
    await ctx.send(response)

@commands.command()
@commands.has_role('Bee')
async def strikeclear(ctx):
    #change this to check the role
    strikechannel = discord.utils.get(ctx.guild.text_channels, name = 'strikes')
    strikemessage = await strikechannel.pins()
    await strikemessage[0].edit(content = 'Toes: 1')

@commands.command()
@commands.has_role('Whole')
async def destrike(ctx, striketarget, numberofstrikes = 1):
    await strikemod(ctx.guild, striketarget, numberofstrikes * -1)

@commands.command()
async def strike(ctx, striketarget, numberofstrikes = 1):
    await strikemod(ctx.guild, striketarget, numberofstrikes * 1)


async def strikemod(guild, striketarget, numberofstrikes = 1):
    #apply the strikes

    strikechannel = discord.utils.get(guild.text_channels, name = 'strikes')
    strikemessage = await strikechannel.pins()
    strikecontent = (strikemessage[0].system_content).split('\n')
    print(strikecontent)

    for member in strikecontent:
        memberstrikecount = member.split(': ')
        memberstrikes[memberstrikecount[0].lower()] = int(memberstrikecount[1])

    if striketarget not in memberstrikes:
        memberstrikes[striketarget] = numberofstrikes
    else:
        memberstrikes[striketarget] += numberofstrikes

    strikepost = ''

    for x in memberstrikes:
        strikepost += f'{x}: {memberstrikes[x]}\n'

    await strikemessage[0].edit(content = strikepost)
    print(memberstrikes)

def setup(bot):
    bot.add_command(hello)
    bot.add_command(embot_help)
    bot.add_command(strike)
    bot.add_command(destrike)
    bot.add_command(strikeclear)