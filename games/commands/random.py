import random
from twitchio.ext import commands

class RandomCommand(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.cooldown(rate=1, per=15, bucket=commands.Bucket.user)
    @commands.command(name='random')
    async def random_number(self, ctx):
        num = random.randint(1, 100)
        result = f"Случайное число: {num}"
        await ctx.send(result)
        self.bot.log_command(ctx.author.name, 'random', result)