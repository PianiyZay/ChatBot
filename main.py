from random import randint
from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor

from config import TOKEN


bot = Bot(token='1756397257:AAGjqG33JvOhj6AgIsrrp7KzE2cLFRyioSM')
dp = Dispatcher(bot)


@dp.message_handler(commands=['start'])
async def process_start_command(message: types.Message):
    await message.reply("Привет!\nНапиши мне что-нибудь!")


@dp.message_handler(commands=['help'])
async def process_help_command(message: types.Message):
    await message.reply("Напиши мне что-нибудь, и я отпрпавлю этот текст тебе в ответ!")


@dp.message_handler()
async def echo_message(msg: types.Message):
    await bot.send_message(msg.from_user.id, msg.text)

def rand_recipe():
    a = randint(0, len(db_first) - 1)
    rand_some = str(db_first[a]['name'] + '\n' + db_first[a]['recipe'])
    return rand_some


db_first = [
    dict(name='Борщ', recipe='Какой-то рецепт'),
    dict(name='Солянка', recipe='Какой-то рецепт'),
    dict(name='Гороховый суп', recipe='Какой-то рецепт')
]


bot.polling(none_stop=True)
