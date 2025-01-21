from twitchio.ext import commands

class HelpCommand(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.cooldown(rate=1, per=15, bucket=commands.Bucket.user)
    @commands.command(name='help')
    async def help(self, ctx):
        help_messages = [
            "Доступные команды:\n"
            "!hello - Бот поздоровается с вами.\n"
            "!help - Показывает этот список команд.\n"
            "!random - Генерирует случайное число от 1 до 100.\n"
            "!roulette - Сыграть в русскую рулетку (1 шанс из 6 проиграть).\n"
            "!rps [камень|ножницы|бумага] - Сыграй в камень, ножницы, бумагу! (Кулдаун: 15 секунд).",
            "!iq - Проверь свой IQ (от 8 до 160).\n"
            "!love <никнейм> - Попытайся потрахаться с кем-то из чата.\n"
            "!dice - Брось кости.\n"
            "!lottery - Участвуй в лотерее."
        ]

        for message in help_messages:
            await ctx.send(message)
            await asyncio.sleep(1)  # Пауза между сообщениями, чтобы не спамить

        self.bot.log_command(ctx.author.name, 'help', "Показан список команд")