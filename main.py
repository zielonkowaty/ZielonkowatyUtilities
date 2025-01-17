"""
This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <https://www.gnu.org/licenses/>.
"""

# ZIELONKOWATYUTILITIES - STABLE BRANCH
# By saying "client" I'm referring to it's bot instance.
# © 2025, mail@zielonkowaty.pl



# Dependencies import

import discord
from discord.ext import commands
from discord import app_commands

# Bot Settings
intents = discord.Intents.default()
intents.presences = True
intents.members = True
intents.messages = True
intents.message_content = True

# Command Prefix
bot = commands.Bot(command_prefix='!', intents=intents)

# Slash commands sync
@bot.event
async def on_ready():
    try:
        synced = await bot.tree.sync()
        print(f"Synced {len(synced)} slash command(s).")
    except Exception as e:
        print(f"Error syncing commands: {e}")
    print(f"Bot is ready! Logged in as {bot.user}")

# Slash command: /poll
@bot.tree.command(name="poll", description="Create a poll with a question.")
async def poll(interaction: discord.Interaction, question: str):
    embed = discord.Embed(
        title="🗳️ Poll",
        description=question,
        color=discord.Color.blue()
    )
    embed.set_footer(text=f"Poll created by: {interaction.user.display_name}")

    # Sending embed
    poll_message = await interaction.channel.send(embed=embed)

    # Adding reactions
    await poll_message.add_reaction("👍")
    await poll_message.add_reaction("👎")
    await poll_message.add_reaction("🤷")

    # Confirmation of successfully created poll
    await interaction.response.send_message("Poll has been created!", ephemeral=True)


# Slash command: /help
@bot.tree.command(name="help", description="Show the help menu.")
async def help_command(interaction: discord.Interaction):
    embed = discord.Embed(
        title="Help",
        description="List of available commands and their actions.",
        color=discord.Color.blue()
    )
    embed.add_field(
        name="Poll creation",
        value="/poll <question>\n"
              "Everything after `/poll` will become a poll question.",
        inline=False
    )
    embed.add_field(
        name="Other commands",
        value="/help - shows help dialog box\n"
              "/author - shows info about author\n"
              "/invite - sends a link to invite the bot to your server",
        inline=False
    )
    embed.add_field(
        name="Support",
        value="COMING SOON! Official support server.",
        inline=False
    )
    embed.set_footer(text="ZielonkowatyUtilities - by Zielonkowaty")
    await interaction.response.send_message(embed=embed, ephemeral=True)


# Slash command: /author
@bot.tree.command(name="author", description="Show information about the author.")
async def author_command(interaction: discord.Interaction):
    embed = discord.Embed(
        title="Author info",
        description="This bot has been created by Zielonkowaty.",
        color=discord.Color.purple()
    )
    await interaction.response.send_message(embed=embed, ephemeral=True)


# Slash command: /invite
@bot.tree.command(name="invite", description="Get an invite link for the bot.")
async def invite_command(interaction: discord.Interaction):
    invite_link = "https://discord.com/oauth2/authorize?client_id=1327465372718469171&permissions=8&scope=bot%20applications.commands"
    embed = discord.Embed(
        title="Invite ZielonkowatyUtilities",
        description=f"Click [here]({invite_link}) to invite ZielonkowatyUtilities to your server!",
        color=discord.Color.gold()
    )
    await interaction.response.send_message(embed=embed, ephemeral=True)


# Slash command: /discord
@bot.tree.command(name="discord", description="Get support information.")
async def discord_command(interaction: discord.Interaction):
    embed = discord.Embed(
        title="Support",
        description="COMING SOON! Official support server for ZielonkowatyUtilities.",
        color=discord.Color.red()
    )
    embed.set_footer(text="Contact me on Discord: Zielonkowaty")
    await interaction.response.send_message(embed=embed, ephemeral=True)


# Bot token
TOKEN = "REPLACE WITH YOUR TOKEN"
bot.run(TOKEN)
