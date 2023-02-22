import aiogram as ai
from settings import setti


bot = ai.Bot(setti.BotToken)
dp = ai.Dispatcher(bot)


@dp.message_handler(commands=["start"])
async def on_message(message: ai.types.Message):
    await bot.send_message(message.from_user.id, "Hi")

@dp.message_handler()
async def repeat(message: ai.types.Message):
    await bot.send_message(message.from_user.id, f"{message.text}")


if __name__ == "__main__":
    ai.executor.start_polling(dp)
