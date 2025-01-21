import random
import asyncio
from twitchio.ext import commands

class LotteryCommand(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.lottery_active = False
        self.participants = []

    @commands.cooldown(rate=1, per=300, bucket=commands.Bucket.user)
    @commands.command(name='lottery')
    async def lottery(self, ctx):
        if ctx.author.name.lower() != 'quasari1337':  # Замените 'gwinglade' на ваш никнейм
            await ctx.send(f"@{ctx.author.name}, эта команда доступна только для gwinglade.")
            return

        if self.lottery_active:
            await ctx.send("Лотерея уже запущена! Дождитесь её завершения.")
            return

        self.lottery_active = True
        self.participants = []
        await ctx.send(f"{ctx.author.name} запустил лотерею! Напишите 'join', чтобы участвовать. У вас есть 5 минут! Победа = БАН")

        # Ждем 5 минут (300 секунд)
        await asyncio.sleep(300)

        # Завершаем лотерею
        self.lottery_active = False

        if not self.participants:
            await ctx.send("Никто не участвовал в лотерее. 😢")
            return

        # Выбираем победителя
        winner = random.choice(self.participants)
        await ctx.send(f"Победитель лотереи: {winner}! 🎉")
        self.bot.log_command(ctx.author.name, 'lottery', f"Победитель: {winner}")

    @commands.Cog.event()
    async def event_message(self, message):
        if not self.lottery_active:
            return

        if message.author is None:
            return

        # Если сообщение "join" и автор еще не участвует
        if message.content.lower() == "join" and message.author.name not in self.participants:
            self.participants.append(message.author.name)
            await message.channel.send(f"{message.author.name} присоединился к лотерее!")