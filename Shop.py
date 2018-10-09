import discord
from discord.ext import commands
import asyncio
import time
import json
import random
import operator
import os


class Shop():
    def __init__(self, bot):
        self.bot = bot


        @bot.command(pass_context=True)
        async def shop(ctx):
            if ctx.message.channel.id != "485307812046569503":
                embed = discord.Embed(
                    title='Shop',
                    description="This is the shop where you can buy roles using gems. You must purchase the items in order otherwise it will not work. To purchase something type -buy. "
                                "Roles will increase the amount of Gems you earn with -math. New rewards will be added in the future.",
                    colour=discord.Colour.blue())

                embed.add_field(name='Citizen', value='1000 Gems', inline=False)
                embed.add_field(name='Lower Class', value='10000 Gems', inline=False)
                embed.add_field(name='Middle Class', value='15000 Gems', inline=False)
                embed.add_field(name='Upper Class', value='30000 Gems', inline=False)
                embed.add_field(name='Lords', value='50000 Gems', inline=False)
                await bot.say(embed=embed)




        @bot.command(pass_context=True)
        async def buy(ctx, *,item):


            with open('economy_bot.json', 'r+') as f:
                data = json.load(f)

            user_id = ctx.message.author.id
            user = ctx.message.author

            mention = ctx.message.author.mention
            role_names = [role.name for role in ctx.message.author.roles]

            if ctx.message.channel.id != "485307812046569503":

                if item == 'citizen' in ctx.message.content:

                    if 'Peasant' not in role_names:
                        await bot.say("{} You cant do this".format(mention))

                    elif data[user_id]['money'] < 1000:
                        await bot.say("{} You do not have enough gems".format(mention))

                    elif "Citizen" in role_names:
                        await bot.say("{} You already have that role".format(mention))


                    elif data[user_id]['money'] >= 1000:
                        role = discord.utils.get(user.server.roles, name="Citizen")
                        await bot.add_roles(user, role)

                        role_remove = discord.utils.get(user.server.roles, name="Peasant") #remove role
                        await bot.remove_roles(user, role_remove)

                        data[user_id]['money'] = data[user_id]['money'] - 1000
                        await bot.say("{} You purchased Citizen".format(mention))
                    else:
                        await bot.say("Invalid")

                elif item == 'lower class' in ctx.message.content:

                    if "Citizen" not in role_names:
                        await bot.say("{} You cant do this".format(mention))

                    elif "Lower Class" in role_names:
                        await bot.say("{} You already have that role".format(mention))

                    elif data[user_id]['money'] < 10000:
                        await bot.say("{} You do not have enough Gems".format(mention))

                    elif data[user_id]['money'] >= 10000 and "Citizen" in role_names:
                        Peasant = discord.utils.get(user.server.roles, name="Lower Class") #add role
                        await bot.add_roles(user, Peasant)

                        role_remove = discord.utils.get(user.server.roles, name="Citizen") #remove role
                        await bot.remove_roles(user, role_remove)

                        data[user_id]['money'] = data[user_id]['money'] - 10000
                        await bot.say("{} You purchased Lower Class".format(mention))



                elif item == 'middle class' in ctx.message.content:

                    if 'Lower Class' not in role_names:
                        await bot.say("{} You cant do this".format(mention))

                    elif "Middle Class" in role_names:
                        await bot.say("{} You already have that role".format(mention))


                    elif data[user_id]['money'] < 15000:
                        await bot.say("{} You do not have enough gems".format(mention))

                    elif data[user_id]['money'] >= 15000 and 'Lower Class' in role_names:
                        middle_class = discord.utils.get(user.server.roles, name="Middle Class") #add role
                        await bot.add_roles(user, middle_class)

                        role_remove = discord.utils.get(user.server.roles, name="Lower Class") #remove role
                        await bot.remove_roles(user, role_remove)

                        data[user_id]['money'] = data[user_id]['money'] - 15000
                        await bot.say("{} You purchased Middle Class".format(mention))
                    else:
                        await bot.say("Invalid")

                elif item == 'upper class' in ctx.message.content:

                    if 'Middle Class' not in role_names:
                        await bot.say("{} You cant do this".format(mention))

                    elif "Upper Class" in role_names:
                        await bot.say("{} You already have the role".format(mention))

                    elif data[user_id]['money'] < 30000:
                        await bot.say("{} You do not have enough gems".format(mention))

                    elif data[user_id]['money'] >= 30000 and 'Middle Class' in role_names:
                        upper_class = discord.utils.get(user.server.roles, name="Upper Class") #add role
                        await bot.add_roles(user, upper_class)

                        role_remove = discord.utils.get(user.server.roles, name="Middle Class") #remove role
                        await bot.remove_roles(user, role_remove)

                        data[user_id]['money'] = data[user_id]['money'] - 30000
                        await bot.say("{} You purchased Upper Class".format(mention))
                    else:
                        bot.say("Invalid")

                elif item == 'lords' in ctx.message.content:

                    if "Lords" in role_names:
                        await bot.say("{} You already have this role".format(mention))

                    elif 'Upper Class' not in role_names:
                        await bot.say("{} you can't do this".format(mention))

                    elif data[user_id]['money'] < 50000:
                        await bot.say("{} You do not have enough gems".format(mention))

                    elif data[user_id]['money'] >= 50000 and 'Upper Class' in role_names:

                        Lords = discord.utils.get(user.server.roles, name="Lords") #add role
                        await bot.add_roles(user, Lords)

                        role_remove = discord.utils.get(user.server.roles, name="Upper Class") #remove role
                        await bot.remove_roles(user, role_remove)

                        data[user_id]['money'] = data[user_id]['money'] - 50000
                        await bot.say("{} You purchased Lords".format(mention))
                    else:
                        await bot.say("Invalid Command")




            with open('economy_bot.json', 'w') as f:
                json.dump(data, f, indent=4)



        @buy.error
        async def buy_errors(ctx, error):
            if isinstance(error, commands.BadArgument):
                await ctx.send("Invalid Command")











def setup(bot):
    bot.add_cog(Shop(bot))