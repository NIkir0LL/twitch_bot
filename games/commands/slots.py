import random
from twitchio.ext import commands

class SlotsCommand(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.cooldown(rate=1, per=40, bucket=commands.Bucket.user)
    @commands.command(name='slots')
    async def slots(self, ctx):
        symbols = ["🍒", "🍋", "🍊", "🍇", "🔔", "💎"]
        result = [random.choice(symbols) for _ in range(3)]
        await ctx.send(f"{ctx.author.name}, крутим слоты... {' '.join(result)}")

        if result[0] == result[1] == result[2]:
            result_message = f"{ctx.author.name}, ДЖЕКПОТ! 🎉"
        elif result[0] == result[1] or result[1] == result[2]:
            result_message = f"{ctx.author.name}, почти! Попробуй ещё раз."
        else:
            result_message = f"{ctx.author.name}, повезёт в следующий раз!"

        await ctx.send(result_message)
        log_message = f"Символы: {' '.join(result)}. {result_message}"
        self.bot.log_command(ctx.author.name, 'slots', log_message)