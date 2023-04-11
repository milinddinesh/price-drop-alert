#! /usr/bin/env python3

#Dicord Bot

import discord
from discord import app_commands
from discord.ext import commands
import os
from dotenv import load_dotenv
import botHelper

load_dotenv()

client = commands.Bot(command_prefix="!", intents=discord.Intents.default())

@client.tree.command(name="test")
async def hello(interaction: discord.Interaction):
    await interaction.response.send_message("Hello World")


@client.tree.command(name="track")
@app_commands.describe(item = "item name",url="amazon url")
async def track(interaction: discord.Interaction, item :str , url:str):
    await interaction.response.defer()
    async with interaction.channel.typing():
        price = botHelper.save(interaction.user.name,item,url)

    await interaction.followup.send("Current price : ", price , ". I'll let you know when the price drops" )

@client.event
async def on_ready():
    print("Logged in as {0.user}".format(client))
    try:
        synced = await client.tree.sync()
        print(f"synced {len(synced)} command(s)")

    except Exception  as e:
        print("An excption occured : ", e)

client.run(os.getenv('TOKEN')) 