from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandHelp, CommandSettings

from loader import dp


@dp.message_handler(CommandHelp())
async def bot_help(message: types.Message):
    text = ("Buyruqlar: ",
            "/start - Botni ishga tushirish",
            "/help - Yordam",

            )
    
    await message.answer("\n".join(text))

@dp.message_handler(CommandSettings())
async def bot_sozlamalar(message: types.Message):
    await message.answer("Ushbu bot bevosita 2024-yilgi ramazon taqvimi uchun chiqarilgan !")







