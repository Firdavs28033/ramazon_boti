from aiogram import  types
from aiogram.dispatcher.filters import Regexp

from loader import dp

EMAIL_REG = R'[^@ \t\r\n]+@[^@ \t\r\n]+\.[^@ \t\r\n]+'
@dp.message_handler(Regexp(EMAIL_REG))
async def email_menu(msg: types.Message):
    await msg.answer("Email shart emas bu bot uchun !")



