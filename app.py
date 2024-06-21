#main.py module
import logging
from db import Database
from default_button import mahsulot_button, menu_keyboard

from aiogram import Bot, Dispatcher, executor, types

API_TOKEN = "7353490544:AAGK5NxtrU_XhYK0hb7IqZngAIzJrXNip9Y"

logging.basicConfig(level=logging.INFO)

bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

# @dp.message_handler(commands=['start'])
# async def send_welcome(message: types.Message):
#     full_name = message.from_user.full_name
#     user_id = message.from_user.id
#     username = message.from_user.username
#     query = f"INSERT INTO users_1(username, full_name, user_id) VALUES('{username}', '{full_name}', {user_id})"
#     if await Database.check_user_id(user_id):
#         await message.reply(f"Sizni yana ko'rganimdan xursandman @{username}", reply_markup=menu_keyboard)
#     else:
#         await Database.connect(query, "insert")
#         await message.reply(f"Welcome @{username}", reply_markup=menu_keyboard)


# @dp.message_handler(lambda message: message.text == "Bo'limlar")
# async def menu(message: types.Message):
#     await message.answer("Bo'limlar", reply_markup=addresses_keyboard)

#
# @dp.message_handler(lambda message: message.text == "Back")
# async def menu(message: types.Message):
#     await message.answer("Bo'limlar", reply_markup=menu_keyboard)


# @dp.message_handler()
# async def echo(message: types.Message):
#     # oldstyle:
#     # await bot.send_message(message.chat.id, message.text)
#
#     await message.answer(message.text)
# #     await message.reply(f"Mening botimga hush kelibsiz {full_name}")

#
# if __name__ == '__main__':
#     executor.start_polling(dp, skip_updates=True)


# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>


# import logging
# from db import Database
# from aiogram import Bot, Dispatcher, executor, types
from default_button import menu_keyboard
from inline_button import keyboard
# import asyncio
#
# API_TOKEN = "7450181024:AAHK4U9bJ5Pcbib3GoluxgHdo2uu87ieL08"
#
#
# # Configure logging
# logging.basicConfig(level=logging.INFO)
#
# # Initialize bot and dispatcher
# bot = Bot(token=API_TOKEN)
# dp = Dispatcher(bot)


@dp.message_handler(commands=["start"])
async def send_welcome(message: types.Message):
    ful_name = message.from_user.full_name
    user_id = message.from_user.id
    username = message.from_user.username
    query = f"INSERT INTO users_1 (username, full_name, user_id) VALUES ('{username}', '{ful_name}', {user_id})"
    if await Database.check_user_id(user_id):
        await message.reply(f"Assalomu aleykum sizni ko'rganimdan xursantman  {ful_name}", reply_markup=menu_keyboard)

    else:
        await Database.connect(query, "insert")
        await message.reply(f"Xushkelibsiz {ful_name}", reply_markup=menu_keyboard)


@dp.message_handler(lambda message: message.text == "Menyu 1")
async def show_menu(message: types.Message):
    # action = button_callback_menu.new(action=message.text)
    await message.answer("1 - bo'lim. Mahsulotlardan birini tanglang:", reply_markup=keyboard)


@dp.message_handler(lambda message: message.text == "Menyu 2")
async def show_menu(message: types.Message):
    # action = button_callback_menu.new(action=message.text)
    await message.answer("2 - bo'lim. Mahsulotlardan birini tanglang:", reply_markup=keyboard)


@dp.message_handler(lambda message: message.text == "Menyu 3")
async def show_menu(message: types.Message):
    # action = button_callback_menu.new(action=message.text)
    await message.answer("3 - bo'lim. Mahsulotlardan birini tanglang:", reply_markup=keyboard)



@dp.message_handler(lambda message: message.text == "Menyu 4")
async def show_menu(message: types.Message):
    # action = button_callback_menu.new(action=message.text)
    await message.answer("4 - bo'lim. Mahsulotlardan birini tanglang:", reply_markup=keyboard)


@dp.message_handler(lambda message: message.text == "Menyu 5")
async def show_menu(message: types.Message):
    # action = button_callback_menu.new(action=message.text)
    await message.answer("5 - bo'lim. Mahsulotlardan birini tanglang:", reply_markup=keyboard)


@dp.message_handler(lambda message: message.text == "Back")
async def show_menu(message: types.Message):
    # action = button_callback_menu.new(action=message.text)
    await message.answer("Menyulardan birini tanglang:", reply_markup=menu_keyboard)


@dp.message_handler(lambda message: message.text == "Mahsulot 1")
async def show_menu(message: types.Message):
    # action = button_callback_menu.new(action=message.text)
    await message.answer("2 - bo'lim. Mahsulotlardan birini tanglang:", reply_markup=mahsulot_button)


@dp.message_handler(commands=['image'])
async def send_image(message: types.Message):
    if message.from_user.id in [6103459824, 1001968950]:
        await message.reply("Salom admin")
        photo_path = "telegram_bot/img.png"
        await bot.send_photo(message.chat.id, photo=photo_path)
    else:
        await message.reply("Bunday buyruq turi mavjud emas")


if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)
