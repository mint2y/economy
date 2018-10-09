import discord
from discord.ext import commands
import asyncio
import time
import json
import random
import operator
import os

class money():
    def __init__(self, bot):
        self.bot = bot



        @bot.command(pass_context=True)
        async def gems(ctx, user: discord.User = None):



            with open('economy_bot.json', 'r+') as f:
                data = json.load(f)

                if ctx.message.channel.id != "485307812046569503":



                    if not user:
                        user_id = ctx.message.author.id
                        await bot.say("{} has {} Gems".format(ctx.message.author.mention, data[user_id]['money']))


                    if user:
                        await bot.say("**{}** has {} Gems".format(user.mention, data[user.id]['money']))



                with open('economy_bot.json', 'w') as f:
                    json.dump(data, f, indent=4)

        @gems.error
        async def gems_error(ctx, error):
            if isinstance(error, commands.BadArgument):
                await ctx.send("Invalid Command")



        @bot.command(pass_context=True)
        async def give(ctx, user: discord.User, amount):
            with open('economy_bot.json', 'r+') as f:
                data = json.load(f)
            amount = (int(amount))
            user_id = ctx.message.author.id

            if ctx.message.channel.id != "485307812046569503":
                if data[user_id]['money'] <= 0:
                    await bot.say("{} You do not have enough Gems".format(ctx.message.author.mention))
                elif user == ctx.message.author:
                    await bot.say("{} You can't give yourself money".format(ctx.message.author.mention))

                elif amount <= 0:
                    await bot.say("{} You can't to that silly".format(ctx.message.author.mention))

                elif data[user_id]['money'] > 0:
                    data[user_id]['money'] = data[user_id]['money'] - amount
                    data[user.id]['money'] = data[user.id]['money'] + amount
                    await bot.say("{} has received {} Gems".format(user.mention, amount))

            with open('economy_bot.json', 'w') as f:
                json.dump(data, f, indent=4)

        @give.error
        async def give_error(ctx, error):
            if isinstance(error, commands.BadArgument):
                await ctx.send("Invalid Command")





        @bot.command(pass_context=True)
        async def gamble(ctx, amount):
            with open('economy_bot.json', 'r+') as f:
                data = json.load(f)
            user_id = ctx.message.author.id
            random_number = random.randint(0, 100)

            amount = (int(amount))
            if ctx.message.channel.id != "485307812046569503":
                if amount > 200:
                    await bot.say("{} You can't gamble higher than 200".format(ctx.message.author.mention))

                elif data[user_id]['money'] <= 0:
                    await bot.say("{} You do not have enough Gems".format(ctx.message.author.mention))

                elif amount > data[user_id]['money']:
                    await bot.say("{} You do not have enough Gems".format(ctx.message.author.mention))

                elif amount <= 0:
                    await bot.say("You can't gamble less than 1")

                elif data[user_id]['money'] + amount < 0:
                    await bot.say("{} You cannot do this")


                elif random_number > 50:
                    data[user_id]['money'] = data[user_id]['money'] + amount
                    await bot.say("{} You have been rewarded {} **Gems**".format(ctx.message.author.mention, amount))

                elif random_number < 50:
                    data[user_id]['money'] = data[user_id]['money'] - amount
                    await bot.say("{} You lost {} Gems".format(ctx.message.author.mention, amount))



            with open('economy_bot.json', 'w') as f:
                json.dump(data, f, indent=4)


        @gamble.error
        async def gamble_error(ctx, error):
            if isinstance(error, commands.BadArgument):
                await ctx.send("Invalid Command")



        @bot.event
        async def on_message(message):
            user_id = message.author.id


            with open('messages.json', 'r+') as f:
                msg = json.load(f)

            with open('economy_bot.json', 'r+') as f:
                data = json.load(f)
            await bot.process_commands(message)

            if not user_id in msg:
                msg[user_id] = {}
                msg[user_id]['messages'] = 1

            else:
                msg[user_id]['messages'] += 1


            if not user_id in data:
                data[user_id] = {}
                data[user_id]['money'] = 0


            else:
                random_money = random.randint(1, 5)
                data[user_id]['money'] = data[user_id]['money'] + random_money
                await asyncio.sleep(120)



            with open('economy_bot.json', 'w') as f:
                json.dump(data, f, indent=4)

            with open('messages.json', 'w') as f:
                json.dump(msg, f, indent=4)



















def setup(bot):
    bot.add_cog(money(bot))