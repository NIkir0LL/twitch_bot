import random
from twitchio.ext import commands

class IQCommand(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.cooldown(rate=1, per=15, bucket=commands.Bucket.user)
    @commands.command(name='iq')
    async def iq_test(self, ctx):
        iq = random.randint(8, 160)
        if iq < 50:
            comment = "Ты гений... в чём-то другом! 😅"
        elif iq < 80:
            comment = "Ну, ты хотя бы стараешься! 😄"
        elif iq < 100:
            comment = "Неплохо, но есть куда расти! 🧠"
        elif iq < 120:
            comment = "Ты умнее среднего! 🎓"
        elif iq < 140:
            comment = "Вау, ты настоящий гений! 🤓"
        else:
            comment = "Эйнштейн нервно курит в сторонке! 🚀"

        result_message = f"{ctx.author.name}, твой IQ: {iq}. {comment}"
        await ctx.send(result_message)
        self.bot.log_command(ctx.author.name, 'iq', result_message)