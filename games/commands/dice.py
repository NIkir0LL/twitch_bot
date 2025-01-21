import random
from twitchio.ext import commands

class DiceCommand(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.cooldown(rate=1, per=10, bucket=commands.Bucket.user)
    @commands.command(name='dice')
    async def dice(self, ctx):
        dice1 = random.randint(1, 6)
        dice2 = random.randint(1, 6)
        result = f"{ctx.author.name}, выпало: {dice1} и {dice2}. Сумма: {dice1 + dice2}"
        await ctx.send(result)
        self.bot.log_command(ctx.author.name, 'dice', result)