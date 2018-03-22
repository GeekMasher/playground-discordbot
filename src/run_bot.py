#!/usr/bin/env python3

import os
import asyncio
import logging

import gmutils
from discord.ext import commands


logging.basicConfig(
    format='%(asctime)s - %(levelname)s - %(message)s',
    level=logging.INFO
)


class DiscordConfig(gmutils.Config):
    DISCORD_TOKEN = None
    description = None

    bot = commands.Bot(command_prefix='/', description=description)


@DiscordConfig.bot.command()
async def test():
    """Adds two numbers together."""
    await DiscordConfig.bot.say('Hello... Nik')

@DiscordConfig.bot.command()
async def add(left: int, right: int):
    """Adds two numbers together."""
    await DiscordConfig.bot.say(left + right)


config_file = './data/config.test.json'

if os.path.exists(config_file):
    DiscordConfig.loadFile(config_file)

DiscordConfig.bot.run(DiscordConfig.DISCORD_TOKEN)
