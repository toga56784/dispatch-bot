import discord
from discord import app_commands
from discord.ext import commands
import os

intents = discord.Intents.default()
intents.message_content = True
intents.members = True

bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user.name}')

    try:
        synced = await bot.tree.sync(guild=discord.Object(id=1428777931395829822))
        print(f'Synced {len(synced)} command(s).')
    except Exception as e:
        print(e)

@bot.tree.command(name="panic", guild=discord.Object(id=1428777931395829822))
async def panic(interaction: discord.Interaction):
    await interaction.response.send_message(f'Panic Alert Successful.', ephemeral=True)
    alert_channel = bot.get_channel(1430294741567799567)

    await alert_channel.send(f'# 🚨 Panic Alert 🚨\n Panic alert sent by {interaction.user.mention}.\n React ✅ if you are responding. <@&1430602297804722226>')

bot.run(BOT_TOKEN)
