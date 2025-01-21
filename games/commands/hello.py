from twitchio.ext import commands

class HelloCommand(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.cooldown(rate=1, per=15, bucket=commands.Bucket.user)
    @commands.command(name='hello')
    async def hello(self, ctx):
        result = f"Hello {ctx.author.name}!"
        await ctx.send(result)
        self.bot.log_command(ctx.author.name, 'hello', result)