from aiogram.dispatcher.filters import Command, Text
from aiogram.types import Message, ReplyKeyboardRemove
from keyboards.default.taqvim_button import menuTaqvim
from loader import dp

@dp.message_handler(text='📆 Taqvim')
async def send_link(msg: Message):
    await msg.answer("Kerakli viloyatni yozing")
@dp.message_handler(text="🤲🏻 Og'iz yopish duosi")
async def send_link(msg: Message):
    await msg.answer(f" 🤲 Navaytu an asuvma sovma shahri ramazona minal fajri ilal magʻribi, xolisan lillahi taʼaalaa Allohu akbar.\n"
                     f" 🤲 Maʼnosi: «Ramazon oyining roʻzasini subhdan to kun botguncha tutmoqni niyat qildim. Xolis Alloh uchun Alloh buyukdir.")



@dp.message_handler(text="🤲🏻 Og'iz ochish duosi")
async def send_link(msg: Message):
    await msg.answer(f" 🤲 Allohumma laka sumtu va bika aamantu va aʼlayka tavakkaltu va aʼlaa rizqika aftartu, fagʻfirliy ma qoddamtu va maa axxortu birohmatika yaa arhamar roohimiyn\n"
                     f" 🤲 Maʼnosi: «Ey Alloh, ushbu Roʻzamni Sen uchun tutdim va Senga iymon keltirdim va Senga tavakkal qildim va bergan rizqing bilan iftor qildim. Ey mehribonlarning eng mehriboni, mening avvalgi va keyingi gunohlarimni magʻfirat qilgil»")

