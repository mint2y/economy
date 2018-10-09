import discord
from discord.ext import commands
import asyncio
import time
import json
import random
import operator
import os
from discord.ext.commands import bot


class mod():
    def __init__(self, bot):
        self.bot = bot

        @bot.command(pass_context=True)
        async def gems_add(ctx, user: discord.User, amount):

            with open('economy_bot.json', 'r+') as f:
                data = json.load(f)

            if ctx.message.author.server_permissions.administrator:
                amount = (int(amount))

                data[user.id]['money'] = data[user.id]['money'] + amount
                await bot.say("{} has been given {} Gems".format(user.mention, data[user.id]['money']))
            else:
                await bot.say("You do not have permission")

            with open('economy_bot.json', 'w') as f:
                json.dump(data, f, )

        @gems_add.error
        async def gems_add_error(ctx, error):
            if isinstance(error, commands.BadArgument):
                await ctx.send("Invalid Command")








        @bot.command(pass_context=True)
        async def gems_remove(ctx, user: discord.User, amount):

            with open('economy_bot.json', 'r+') as f:
                data = json.load(f)

            if ctx.message.author.server_permissions.administrator:
                amount = (int(amount))

                data[user.id]['money'] = data[user.id]['money'] - amount
                await bot.say("{} Gems have been removed from {}".format(amount, user.mention))
            else:
                await bot.say("You do not have permission")

            with open('economy_bot.json', 'w') as f:
                json.dump(data, f, )

        @gems_remove.error
        async def gems_remove_error(ctx, error):
            if isinstance(error, commands.BadArgument):
                await ctx.send("Invalid Command")








        @bot.command(pass_context=True)
        async def gems_reset(ctx, user: discord.User):
            if ctx.message.author.server_permissions.administrator:
                with open('economy_bot.json', 'r+') as f:
                    data = json.load(f)

                    data[user.id]['money'] = 0
                    await bot.say("{}'s Gems has been reset".format(user.mention))

                with open('economy_bot.json', 'w') as f:
                    json.dump(data, f, )

            else:
                await bot.say("You do not have permission")

        @gems_reset.error
        async def gems_reset_error(ctx, error):
            if isinstance(error, commands.BadArgument):
                await ctx.send("Invalid Command")








        @bot.command(pass_context=True)
        async def ban(ctx, user: discord.User, *, reason="No Reason given"):
            role_names = [role.name for role in ctx.message.author.roles]

            if user == ctx.message.author:
                await bot.say("You cannot ban yourself")


            elif ctx.message.author.server_permissions.ban_members == True:
                embed = discord.Embed(
                    title='{} Was banned'.format(user),
                    colour=discord.Colour.blue()
                )

                embed.set_image(
                    url="https://cdn.discordapp.com/attachments/485332048144236545/497765231066349569/White-Walker-in-Game-of-Thrones.jpg")
                embed.add_field(name='Banned: ', value='{}'.format(user), inline=False)
                embed.add_field(name='Reason', value='{}'.format(reason), inline=False)
                await bot.say(embed=embed)
                await bot.send_message(bot.get_channel('485517816573984778'), embed=embed)

                await bot.ban(user)
            else:
                await bot.say("You do not have permission")

        @ban.error
        async def ban_error(ctx, error):
            if isinstance(error, commands.BadArgument):
                await ctx.send("Invalid Command")







        @bot.command(pass_context=True)
        async def kick(ctx, user: discord.User, *, reason="No Reason given"):


            if user == ctx.message.author:
                await bot.say("You cannot ban yourself")

            elif ctx.message.author.server_permissions.kick_members == True:

                embed = discord.Embed(
                    title='{} Was kicked'.format(user),

                    colour=discord.Colour.blue()
                )

                embed.set_image(
                    url="https://cdn.discordapp.com/attachments/485332048144236545/497765231066349569/White-Walker-in-Game-of-Thrones.jpg")
                embed.add_field(name='Kicked: ', value='{}'.format(user), inline=False)
                embed.add_field(name='Reason', value='{}'.format(reason), inline=False)
                await bot.say(embed=embed)
                await bot.send_message(bot.get_channel('485517816573984778'), embed=embed)

                await bot.kick(user)
            else:
                await bot.say("{} You do not have permission".format(ctx.message))


        @kick.error
        async def kick_error(ctx, error):
            if isinstance(error, commands.BadArgument):
                await ctx.send("Invalid Command")









        @bot.command(pass_context=True)
        async def warn(ctx, user: discord.User, *, reason="No reason given"):



            user_id = user.id


            if ctx.message.author.server_permissions.mute_members == True:
                with open('warnings.json', 'r+') as f:
                    data = json.load(f)

                embed = discord.Embed(
                    title='User Warned',
                    Description="User Warned",
                    colour=discord.Colour.blue())

                embed.set_thumbnail(url="https://cdn.discordapp.com/avatars/{0.id}/{0.avatar}.png?size=1024".format(user))
                embed.add_field(name='Warned: ', value='{}'.format(user), inline=False)
                embed.add_field(name='Reason', value='{}'.format(reason), inline=False)
                await bot.say(embed=embed)
                await bot.send_message(bot.get_channel('485517816573984778'), embed=embed)

                if not user_id in data:
                    data[user_id] = {}
                    data[user_id]['reason'] = [reason]


                else:
                    data[user_id]['reason'].append(reason)

                with open('warnings.json', 'w') as f:
                    json.dump(data, f, indent=4)


            else:
                await bot.say("You do noy have permission")


        @warn.error
        async def warn_error(ctx, error):
            if isinstance(error, commands.BadArgument):
                await ctx.send("Invalid Command")








        @bot.command(pass_context=True)
        async def warns(ctx, user: discord.User):
            role_names = [role.name for role in ctx.message.author.roles]

            with open('warnings.json', 'r+') as f:
                warns = json.load(f)

            if ctx.message.author.server_permissions.mute_members == True:

                embed = discord.Embed(
                    title="showing warns for {}".format(user),

                    colour=discord.Colour.blue()
                )
                embed.set_thumbnail(url=user.avatar_url)
                for i in range(0, len(warns[user.id]['reason'])):
                    embed.add_field(name="Reason:", value='{}'.format(warns[user.id]['reason'][i]), inline=False)

                await bot.say(embed=embed)

            elif not user in warns:
                await bot.say("They have no warns")

            else:
                await bot.say("You do not have permission")

            with open('warnings.json', 'w') as f:
                json.dump(warns, f, indent=4)


        @warns.error
        async def warns_error(ctx, error):
            if isinstance(error, commands.BadArgument):
                await ctx.send("Invalid Command")







        @bot.command(pass_context=True)
        async def remove_warn(ctx, user: discord.User, warning):

            with open('warnings.json', 'r+') as f:
                warns = json.load(f)

            if ctx.message.author.server_permissions.administrator:

                warns[user.id]['reason'].remove(warning)

            else:
                bot.say("You do not have permission")

            with open('warnings.json', 'w') as f:
                json.dump(warns, f, indent=4)


        @remove_warn.error
        async def remove_warn_error(ctx, error):
            if isinstance(error, commands.BadArgument):
                await ctx.send("Invalid Command")








        @bot.command(pass_context=True)
        async def unmute(ctx, user: discord.User):
            if ctx.message.author.server_permissions.mute_members == True:

                embed = discord.Embed(
                    title='{} has been unmuted'.format(user),
                    colour=discord.Colour.blue())


                await bot.say(embed=embed)
                await bot.send_message(bot.get_channel('485517816573984778'), embed=embed)

                role = discord.utils.get(user.server.roles, name="Muted")
                await bot.remove_roles(user, role)


            else:
                await bot.say("You do not have permission")




        @bot.command(pass_context=True)
        async def mute(ctx, user: discord.User, time=None, length=None, *, reason="No reason chosen"):


            if not length:
                if ctx.message.author.server_permissions.mute_members == True:  # Mute in seconds
                    embed = discord.Embed(
                        title='{} has been muted'.format(user),
                        colour=discord.Colour.blue())

                    embed.set_thumbnail(
                        url="https://cdn.discordapp.com/avatars/{0.id}/{0.avatar}.png?size=1024".format(user))
                    embed.add_field(name='Reason', value='{}'.format(reason), inline=False)
                    await bot.say(embed=embed)
                    await bot.send_message(bot.get_channel('485517816573984778'), embed=embed)

                    role = discord.utils.get(user.server.roles, name="Muted")
                    await bot.add_roles(user, role)


                else:
                    await bot.say("You do not have permission")

            if length == 's' in ctx.message.content:

                if ctx.message.author.server_permissions.mute_members == True: #Mute in seconds
                    embed = discord.Embed(
                        title='{} has been muted'.format(user),
                        colour=discord.Colour.blue())

                    embed.set_thumbnail(url="https://cdn.discordapp.com/avatars/{0.id}/{0.avatar}.png?size=1024".format(user))
                    embed.add_field(name='Length: ', value=("{} Second(s)".format(time)), inline=False)
                    await bot.say(embed=embed)
                    await bot.send_message(bot.get_channel('485517816573984778'), embed=embed)

                    role = discord.utils.get(user.server.roles, name="Muted")
                    await bot.add_roles(user, role)

                    time = (int(time))
                    await asyncio.sleep(time)

                    await bot.remove_roles(user, role)

                else:
                    await bot.say("You do not have permission")


            elif length == 'm' in ctx.message.content:

                if ctx.message.author.server_permissions.mute_members == True: #Mute in mins
                    embed = discord.Embed(
                        title='{} has been muted'.format(user),
                        colour=discord.Colour.blue())

                    embed.set_thumbnail(url="https://cdn.discordapp.com/avatars/{0.id}/{0.avatar}.png?size=1024".format(user))
                    embed.add_field(name='Length: ', value=("{} Minute(s)".format(time)), inline=False)
                    embed.add_field(name='Reason', value='{}'.format(reason), inline=False)
                    await bot.say(embed=embed)
                    await bot.send_message(bot.get_channel('485517816573984778'), embed=embed)

                    role = discord.utils.get(user.server.roles, name="Muted")
                    await bot.add_roles(user, role)

                    time = (int(time))
                    await asyncio.sleep(time) * 60

                    await bot.remove_roles(user, role)
                else:
                    await bot.say("You do not have permission")



            elif length == 'h' in ctx.message.content:

                if ctx.message.author.server_permissions.mute_members == True: #Mute in hours
                    embed = discord.Embed(
                        title='{} has been muted'.format(user),
                        colour=discord.Colour.blue())

                    embed.set_thumbnail(url="https://cdn.discordapp.com/avatars/{0.id}/{0.avatar}.png?size=1024".format(user))
                    embed.add_field(name='Length: ', value=("{} Hour(s)".format(time)), inline=False)
                    embed.add_field(name='Reason', value='{}'.format(reason), inline=False)
                    await bot.say(embed=embed)
                    await bot.send_message(bot.get_channel('485517816573984778'), embed=embed)

                    role = discord.utils.get(user.server.roles, name="Muted")
                    await bot.add_roles(user, role)

                    time = (int(time))
                    await asyncio.sleep(time) * 3600

                    await bot.remove_roles(user, role)
                else:
                    await bot.say("You do not have permission")



            elif length == 'd' in ctx.message.content:

                if ctx.message.author.server_permissions.mute_members == True: #Mute in days
                    embed = discord.Embed(
                        title='{} has been muted'.format(user),
                        colour=discord.Colour.blue())

                    embed.set_thumbnail(url="https://cdn.discordapp.com/avatars/{0.id}/{0.avatar}.png?size=1024".format(user))
                    embed.add_field(name='Length: ', value=("{} Day(s)".format(time)), inline=False)
                    embed.add_field(name='Reason', value='{}'.format(reason), inline=False)
                    await bot.say(embed=embed)
                    await bot.send_message(bot.get_channel('485517816573984778'), embed=embed)

                    role = discord.utils.get(user.server.roles, name="Muted")
                    await bot.add_roles(user, role)

                    time = (int(time))
                    await asyncio.sleep(time) * 86400

                    await bot.remove_roles(user, role)
                else:
                    await bot.say("You do not have permission")




        @mute.error
        async def mute_error(ctx, error):
            if isinstance(error, commands.BadArgument):
                await ctx.send("Invalid Command")










        @bot.command(pass_context=True)
        async def message_reset(ctx):
            with open('messages.json', 'r+') as f:
                msg = json.load(f)

            if ctx.message.author.server_permissions.administrator:

                for i in msg:
                    del msg[i]
                    break
                await bot.say("Message count has been reset")
            else:
                bot.say("You do not have permission")

            with open('messages.json', 'w') as f:
                json.dump(msg, f, indent=4)

        @message_reset.error
        async def message_reset_error(ctx, error):
            if isinstance(error, commands.BadArgument):
                await ctx.send("Invalid Command")















def setup(bot):
    bot.add_cog(mod(bot))
