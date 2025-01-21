import random
from twitchio.ext import commands

class RPSCommand(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.cooldown(rate=1, per=15, bucket=commands.Bucket.user)
    @commands.command(name='rps')
    async def rps(self, ctx):
        if len(ctx.message.content.split()) > 1:
            user_choice = ctx.message.content.split()[1].lower()
            if user_choice not in ['камень', 'ножницы', 'бумага']:
                result_message = f"{ctx.author.name}, нужно выбрать: камень, ножницы или бумага!"
                await ctx.send(result_message)
                self.bot.log_command(ctx.author.name, 'rps', result_message)
                return

            bot_choice = random.choice(['камень', 'ножницы', 'бумага'])
            if user_choice == bot_choice:
                result_message = "Ничья!"
            elif (user_choice == 'камень' and bot_choice == 'ножницы') or \
                 (user_choice == 'ножницы' and bot_choice == 'бумага') or \
                 (user_choice == 'бумага' and bot_choice == 'камень'):
                result_message = f"{ctx.author.name} выиграл!"
            else:
                result_message = f"{ctx.author.name} проиграл!"

            await ctx.send(f"{ctx.author.name}, я выбрал {bot_choice}. {result_message}")
            log_message = f"Пользователь: {user_choice}, Бот: {bot_choice}. {result_message}"
            self.bot.log_command(ctx.author.name, 'rps', log_message)
        else:
            result_message = f"{ctx.author.name}, используй команду так: !rps [камень|ножницы|бумага]"
            await ctx.send(result_message)
            self.bot.log_command(ctx.author.name, 'rps', result_message)