import random
from twitchio.ext import commands

class RouletteCommand(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.cooldown(rate=1, per=15, bucket=commands.Bucket.user)
    @commands.command(name='roulette')
    async def roulette(self, ctx):
        result = random.randint(1, 6)
        if result <= 3:
            result_message = f"{ctx.author.name} проиграл в русской рулетке! 💥"
        else:
            result_message = f"{ctx.author.name} выжил в русской рулетке! 🎉"
        await ctx.send(result_message)
        self.bot.log_command(ctx.author.name, 'roulette', result_message)