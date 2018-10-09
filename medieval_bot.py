import discord
from discord.ext import commands
import asyncio
import time
import json
import random
import operator
import os

bot = commands.Bot(command_prefix='-')
bot.remove_command('help')

startup_commands = ["money", "mod", "Shop"]


@bot.event
async def on_ready():
    print("Bot is ready")





########MATH COMMAND###################

@bot.command(pass_context=True)
async def math(ctx):

    with open('economy_bot.json', 'r+') as f:
        data = json.load(f)
    role_names = [role.name for role in ctx.message.author.roles]
    number1 = random.randint(0, 12)
    number2 = random.randint(0, 12)

    eq = {'+':operator.add,
          '-':operator.sub,
          '*':operator.mul}
    op = random.choice(list(eq.keys()))
    answer = eq.get(op)(number1, number2)        #answer

    if ctx.message.channel.id != "485307812046569503":
        await bot.say("**{}** answer the equation: {} {} {}".format(ctx.message.author.mention, number1, op, number2))



        guess = await bot.wait_for_message(author=ctx.message.author, timeout=4)
        try:
            input = (float(guess.content))
            if input == answer:


                if input == answer and 'Citizen' in role_names: #PEASANT
                    money_earnt = random.randint(1, 15)

                    author = ctx.message.author.id
                    if not author in data:
                        data[author] = {}
                        data[author]['money'] = money_earnt
                        await bot.say("You earnt {} **Gems**".format(money_earnt))
                    else:
                        data[author]['money'] = data[author]['money'] + money_earnt
                        await bot.say("You earnt {} **Gems**".format(money_earnt))

                elif input == answer and 'Lower Class' in role_names: #LOWER CLASS
                    money_earnt = random.randint(1, 20)

                    author = ctx.message.author.id
                    if not author in data:
                        data[author] = {}
                        data[author]['money'] = money_earnt
                        await bot.say("You earnt {} **Gems**".format(money_earnt))
                    else:
                        data[author]['money'] = data[author]['money'] + money_earnt
                        await bot.say("You earnt {} **Gems**".format(money_earnt))

                elif input == answer and 'Middle Class' in role_names: #MIDDLE CLASS
                    money_earnt = random.randint(1, 25)

                    author = ctx.message.author.id
                    if not author in data:
                        data[author] = {}
                        data[author]['money'] = money_earnt
                        await bot.say("You earnt {} **Gems**".format(money_earnt))
                    else:
                        data[author]['money'] = data[author]['money'] + money_earnt
                        await bot.say("You earnt {} **Gems**".format(money_earnt))

                elif input == answer and 'Upper Class' in role_names: #UPPER CLASS
                    money_earnt = random.randint(1, 30)

                    author = ctx.message.author.id
                    if not author in data:
                        data[author] = {}
                        data[author]['money'] = money_earnt
                        await bot.say("You earnt {} **Gems**".format(money_earnt))
                    else:
                        data[author]['money'] = data[author]['money'] + money_earnt
                        await bot.say("You earnt {} **Gems**".format(money_earnt))

                elif input == answer and 'Lords' in role_names: #LORDS
                    money_earnt = random.randint(1, 40)

                    author = ctx.message.author.id
                    if not author in data:
                        data[author] = {}
                        data[author]['money'] = money_earnt
                        await bot.say("You earnt {} **Gems**".format(money_earnt))
                    else:
                        data[author]['money'] = data[author]['money'] + money_earnt
                        await bot.say("You earnt {} **Gems**".format(money_earnt))


                else:
                    money_earnt = random.randint(1, 10)

                    author = ctx.message.author.id
                    if not author in data:
                        data[author] = {}
                        data[author]['money'] = money_earnt
                        await bot.say("You earnt {} **Gems**".format(money_earnt))
                    else:
                        data[author]['money'] = data[author]['money'] + money_earnt
                        await bot.say("You earnt {} **Gems**".format(money_earnt))


            elif input != answer:
                await bot.say("{} You answered incorrectly".format(ctx.message.author.mention))

            elif guess != int:
                await bot.say("{} Invalid response".format(ctx.message.author))

            else:
                await bot.say("Invalid Command")


        except AttributeError:
            await bot.say("{} You did not answer in time".format(ctx.message.author))


    with open('economy_bot.json', 'w') as f:
        json.dump(data, f, indent=4)


@math.error
async def math_error(ctx, error):
    if isinstance(error, commands.BadArgument):
        await ctx.send("Invalid Command")






@bot.event
async def on_member_join(member):



    embed = discord.Embed(
        title='**Welcome {}**'.format(member),
        description="Be sure to read #│rules and #│faq",
        colour=discord.Colour.blue()
    )
    embed.set_thumbnail(url="https://cdn.discordapp.com/avatars/{0.id}/{0.avatar}.png?size=1024".format(member))



    channel = member.server.get_channel("485307812046569503")

    await bot.send_message(channel, embed=embed)

    with open('economy_bot.json', 'r+') as f:
        data = json.load(f)

    user_id = member.id
    if not user_id in data:
        data[user_id] = {}
        data[user_id]['money'] = 0


    with open('economy_bot.json', 'w') as f:
        json.dump(data, f, indent=4)




@bot.command(pass_context=True)
async def leaderboard(ctx):

    if ctx.message.author.server_permissions.administrator:

        if 'gems' in ctx.message.content:
            with open('economy_bot.json', 'r+') as f:
                users = json.load(f)

            high_score_list = sorted(users, key=lambda x: users[x].get('money', 0), reverse=True)
            message = ''

            for number, user in enumerate(high_score_list):

                message += '{0}. {1} has {2} Gems\n'.format(number + 1,'<@!{}>'.format(user), users[user].get('money', 0))

                if number == 9:
                    break
                else: number += 1
            await bot.say(message)

            with open('economy_bot.json', 'w') as f:
                json.dump(users, f, indent=4)



        elif 'messages' in ctx.message.content:

            with open('messages.json', 'r+') as f:
                msg = json.load(f)

            message_score = sorted(msg, key=lambda x: msg[x].get('messages', 0),reverse=True)
            message = ''
            for number, user in enumerate(message_score):
                message += '{0}. {1} has sent {2} Messages\n'.format(number + 1,'<@!{}>'.format(user), msg[user].get('messages', 0))
                if number == 9:
                    break
                else: number += 1
            await bot.say(message)

            with open('messages.json', 'w') as f:
                json.dump(msg, f, indent=4)
    else:
        await bot.say("You do not have permission")


@leaderboard.error
async def leaderboard_error(ctx, error):
    if isinstance(error, commands.BadArgument):
        await ctx.send("Invalid Command")




@bot.command(pass_context=True)
async def help(ctx):


    if ctx.message.channel.id != "485307812046569503":
        embed = discord.Embed(
            title='Help',

            colour=discord.Colour.blue())

        embed.add_field(name='Math', value='-math (To earn gems)', inline=False)
        embed.add_field(name='Economy', value='-gems\n-give\n-gamble\n', inline=False)
        embed.add_field(name='Shop', value='-buy citizen\n-buy lower class\n-buy middle class\n-buy upper class\n-buy lords', inline=False)


        await bot.say(embed=embed)



@bot.command(pass_context=True)
async def helpmod(ctx):

    if ctx.message.channel.id != "485307812046569503" and ctx.message.author.server_permissions.mute_members == True:
        embed = discord.Embed(
            title='Modding Help',
            description='Do not use the [] it is just for example.',

            colour=discord.Colour.blue())

        embed.add_field(name='Mute', value='-mute [User] [s/ m/ h/ d] [Reason]', inline=False)
        embed.add_field(name='Unmute', value='-unmute [User]', inline=False)
        embed.add_field(name='Ban', value='-ban [User] [Reason]', inline=False)
        embed.add_field(name='Kick', value='-kick [User] [Reason]', inline=False)
        embed.add_field(name='Warn', value='-warn [User] [Reason]', inline=False)
        embed.add_field(name='Warns(Show Warnings)', value='-warns [User]', inline=False)

        await bot.say(embed=embed)

@bot.command(pass_context=True)
async def helpadmin(ctx):

    if ctx.message.channel.id != "485307812046569503" and ctx.message.author.server_permissions.administrator:
        embed = discord.Embed(
            title='Admin Help',
            colour=discord.Colour.blue())

        embed.add_field(name='Add Gems', value='-gems_add', inline=False)
        embed.add_field(name='Remove Gems', value='-gems_remove', inline=False)
        embed.add_field(name='Reset Gems', value='-gems_reset', inline=False)
        embed.add_field(name='Remove Warning', value='-remove_warn', inline=False)
        embed.add_field(name='Leaderboard', value='-leaderboard gems/-leaderboard messages. (Do not use as it pings. It is only used weekly', inline=False)
        embed.add_field(name='Reset Messages', value='-message_reset (Do not use this. It is used weekly with Leaderboard)', inline=False)





        await bot.say(embed=embed)



if __name__ == "__main__":
    for extension in startup_commands:
        try:
            bot.load_extension(extension)
        except Exception as e:
            exc = '{}: {}'.format(type(e).__name__, e)
            print('Failed to load extension {}\n{}'.format(extension, exc))








bot.run(os.getenv('TOKEN'))