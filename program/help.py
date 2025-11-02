import discord
from discord.ext import commands
from discord import app_commands

class Help(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @app_commands.command(name="help", description="ヘルプを表示します")
    async def help(self, interaction: discord.Interaction):
        embed = discord.Embed(
            title="ℹ️ヘルプ",
            color=discord.Color.green()
        )

        embed.add_field(
            name="未設定システム",
            value=(
                "/？？？ … いいよこいよ！\n"
            ),
            inline=False
        )

        embed.set_footer(text="HGHomeBot v0.1β対応")

        await interaction.response.send_message(embed=embed)

async def setup(bot):
    await bot.add_cog(Help(bot))
