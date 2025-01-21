import os
from datetime import datetime
from twitchio.ext import commands
from commands.hello import HelloCommand
from commands.help import HelpCommand
from commands.random import RandomCommand
from commands.roulette import RouletteCommand
from commands.slots import SlotsCommand
from commands.rps import RPSCommand
from commands.iq import IQCommand
from commands.love import LoveCommand
from commands.guess import GuessCommand
from commands.ttt import TTTCommand
from commands.dice import DiceCommand
from commands.lottery import LotteryCommand

# Настройки бота
BOT_NICK = 'name'  # Имя вашего бота
BOT_PREFIX = '!'              # Префикс для команд бота
CHANNEL = 'channel'         # Название канала
OAUTH_TOKEN = 'oauth:token'        # OAuth-токен из переменных окружения

# Создаем директорию для сохранения сообщений, если она не существует
if not os.path.exists('messages'):
    os.makedirs('messages')

class Bot(commands.Bot):

    def __init__(self):
        super().__init__(token=OAUTH_TOKEN, prefix=BOT_PREFIX, initial_channels=[CHANNEL])
        self.user_balances = {}  # Балансы пользователей
        # Подключаем команды
        self.add_cog(HelloCommand(self))
        self.add_cog(HelpCommand(self))
        self.add_cog(RandomCommand(self))
        self.add_cog(RouletteCommand(self))
        #self.add_cog(SlotsCommand(self))
        self.add_cog(RPSCommand(self))
        self.add_cog(IQCommand(self))
        self.add_cog(LoveCommand(self))
        #self.add_cog(GuessCommand(self))
        #self.add_cog(TTTCommand(self))
        self.add_cog(DiceCommand(self))
        self.add_cog(LotteryCommand(self))

    async def event_ready(self):
        print(f'Logged in as | {self.nick}')
        print(f'User id is | {self.user_id}')

    async def event_message(self, message):
        if message.author is None:
            return
        await self.handle_commands(message)

    async def event_command_error(self, ctx, error):
        if isinstance(error, commands.CommandOnCooldown):
            await ctx.send(f"{ctx.author.name}, команда {ctx.command.name if ctx.command else 'unknown'} доступна через {int(error.retry_after)} секунд.")
        else:
            command_name = ctx.command.name if ctx.command else 'unknown'
            error_message = f"Ошибка в команде {command_name}: {error}"
            print(error_message)
            self.log_error(error_message)

    def log_command(self, username, command, result):
        current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        with open('messages/command_logs.txt', 'a', encoding='utf-8') as f:
            f.write(f"[{current_time}] {username} использовал команду {command}: {result}\n")

    def log_error(self, error_message):
        current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        with open('messages/error_logs.txt', 'a', encoding='utf-8') as f:
            f.write(f"[{current_time}] {error_message}\n")

if __name__ == '__main__':
    bot = Bot()
    bot.run()