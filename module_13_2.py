#t.me/PervyUr_bot
from aiogram import Bot, Dispatcher, types
import asyncio
from aiogram.filters import CommandStart

api = "111"
bot = Bot(token=api)

dp = Dispatcher()


@dp.message(CommandStart())
async def start(message: types.Message):
    await message.answer('Привет! Я бот, помогающий твоему здоровью.')
    print('Привет! Я бот, помогающий твоему здоровью.')

@dp.message()
async def all_massages(message: types.Message):
    text = message.text
    if text in ['Привет', 'привет', 'hi', 'hello']:
        await message.answer('Введите команду /start, чтобы начать общение.')
        print('Введите команду /start, чтобы начать общение.')
    else:
        await message.answer(message.text)


async def main():
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
