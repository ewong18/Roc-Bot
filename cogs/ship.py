#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import discord
from discord.ext import commands
from ship_func import generic_ship_command_embed, affinity_search, random_ship_command_embed, all_ship_command_embed, ship_search, info_embed, find_number, detail_embed, customemoji, sanitise_input
from data import ShipData, CategoryLister, ShipLister

class ShipCog(commands.Cog, name="Ship Commands"):
    """ShipCog"""

    def __init__(self, bot):
        self.bot = bot

    @commands.group(aliases=['ships'])
    @commands.guild_only()
    async def ship(self, ctx):
        if ctx.invoked_subcommand is None:
            await ctx.send('Invalid ship command passed.')

    # Sub command to the @bot.group() decorator ship function.
    # Intended that for use in high traffic channels, the output size is 
    # intentialy small. 
    # A 5 line embed with basic info: name, weapon, dps, aura and zen.
    @ship.command(name='info')
    @commands.guild_only()
    async def info(self, ctx, *, arg1):
        await ctx.send(embed=ShipData(self, arg1).embed_info)

    # Returns the ship in game sequence number. For example Shinova is number 1.  
    @ship.command(name='number')
    @commands.guild_only()
    async def number(self, ctx, *, arg1):
        await ctx.send(ShipData(self, arg1).s_obj['number'])

    #Sub command to the @bot.group() decorator ship function.
    #Intended that for use in low traffic channels, the output size is large.
    #A 6+ line embed with detailed info: name, weapon, dps, aura and zen.
    @ship.command(name='detail')
    @commands.guild_only()
    async def detail(self, ctx, *, arg1):
        print(ctx.channel.id)
        if ctx.channel.id in [378546862627749908,596343881705062417]:
            await ctx.send(embed=ShipData(self, arg1).embed_detail)
        else:
            await ctx.send("Command limited to <#378546862627749908>.")

    @ship.command(name='dmg')
    @commands.guild_only()
    async def dmg(self, ctx, *, arg1=None):
        sub_command = ctx.subcommand_passed
        if arg1 == None:
            await ctx.send(embed=CategoryLister(self, sub_command).embed_list)
        else:
            await ShipLister(self, ctx, arg1, sub_command).create_emebed()

    @ship.command(name='aura')
    @commands.guild_only()
    async def aura(self, ctx, *, arg1=None):
        sub_command = ctx.subcommand_passed
        if arg1 == None:
            await ctx.send(embed=CategoryLister(self, sub_command).embed_list)
        else:
            await ShipLister(self, ctx, arg1, sub_command).create_emebed()


    @ship.command(name='zen')
    @commands.guild_only()
    async def zen(self, ctx, *, arg1=None):
        sub_command = ctx.subcommand_passed
        if arg1 == None:
            await ctx.send(embed=CategoryLister(self, sub_command).embed_list)
        else:
            await ShipLister(self, ctx, arg1, sub_command).create_emebed()

    @ship.command(name='rarity')
    @commands.guild_only()
    async def rarity(self, ctx, *, arg1=None):
        sub_command = ctx.subcommand_passed
        if ctx.channel.id == 378546862627749908:
            if arg1 == None:
                await ctx.send(embed=CategoryLister(self, sub_command).embed_list)
            else:
                await ShipLister(self, ctx, arg1, sub_command).create_emebed()
        else:
            await ctx.send("Command limited to <#378546862627749908>.")


    @ship.command(name='affinity')
    @commands.guild_only()
    async def affinity(self, ctx, *, arg1=None):
        sub_command = ctx.subcommand_passed
        if arg1 == None:
            await ctx.send(embed=CategoryLister(self, sub_command).embed_list)
        else:
            await ShipLister(self, ctx, arg1, sub_command).create_emebed()

    @ship.command(name='rand')
    @commands.guild_only()
    async def rand(self, ctx, *, arg1=None):
        if ctx.channel.id == 378546862627749908:
            if arg1 == None:
                arg1 = 10
                await random_ship_command_embed(self, ctx, arg1)
            else:
                await random_ship_command_embed(self, ctx, arg1)
        else:
            await ctx.send("Command limited to <#378546862627749908>.")

    @ship.command(name='all')
    @commands.guild_only()
    async def all(self, ctx, *, arg1=None):
        if ctx.channel.id == 378546862627749908:
            await all_ship_command_embed(self, ctx)
        else:
            await ctx.send("Command limited to <#378546862627749908>.")


# The setup fucntion below is neccesarry. Remember we give bot.add_cog() the 
# name of the class in this case ShipCog.
# When we load the cog, we use the name of the file.
def setup(bot):
    bot.add_cog(ShipCog(bot))
