import random
from twitchio.ext import commands

class LoveCommand(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.cooldown(rate=1, per=15, bucket=commands.Bucket.user)
    @commands.command(name='love')
    async def love(self, ctx):
        if len(ctx.message.content.split()) < 2:
            result_message = f"{ctx.author.name}, используй команду так: !love <никнейм>"
            await ctx.send(result_message)
            self.bot.log_command(ctx.author.name, 'love', result_message)
            return

        target_user = ctx.message.content.split()[1].lower()
        responses = [
            f"{ctx.author.name} и {target_user} провели время вместе! 🎉",
            f"{ctx.author.name} пытался провести время с {target_user}, но не получилось... 😅",
            f"{ctx.author.name} и {target_user} устроили веселую вечеринку! 🎈🎂",
            f"{ctx.author.name} предложил {target_user} провести время вместе, но получил отказ. 😢",
            f"{ctx.author.name} и {target_user} ушли в закат, держась за руки. 🌅",
            f"{ctx.author.name} и {target_user} решили, что дружба важнее всего. 🤝",
            f"{ctx.author.name} и {target_user} устроили романтический ужин при свечах. 🕯️🍷",
            f"{ctx.author.name} и {target_user} решили, что лучше просто обняться. 🤗",
            f"{ctx.author.name} и {target_user} устроили битву подушками вместо вечеринки. 🛏️💥",
            f"{ctx.author.name} и {target_user} решили, что Netflix и chill — это лучшее. 🍿📺",
            f"{ctx.author.name} и {target_user} пошли на прогулку в парк. 🌳🌷",
            f"{ctx.author.name} и {target_user} решили поиграть в настольные игры. 🎲🃏",
            f"{ctx.author.name} и {target_user} устроили пикник на природе. 🧺🌞",
            f"{ctx.author.name} и {target_user} пошли в кино на новый фильм. 🎟️🍿",
            f"{ctx.author.name} и {target_user} решили вместе почитать книгу. 📚📖",
            f"{ctx.author.name} и {target_user} устроили вечер караоке. 🎤🎵",
            f"{ctx.author.name} и {target_user} пошли на концерт любимой группы. 🎸🎶",
            f"{ctx.author.name} и {target_user} решили вместе заняться спортом. 🏃‍♂️🏋️‍♀️",
            f"{ctx.author.name} и {target_user} устроили вечер игр на приставке. 🎮🕹️",
            f"{ctx.author.name} и {target_user} пошли на выставку в музей. 🖼️🏛️"
        ]

        result_message = random.choice(responses)
        await ctx.send(result_message)
        self.bot.log_command(ctx.author.name, 'love', result_message)
