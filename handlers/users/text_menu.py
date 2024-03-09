from aiogram import types
from aiogram.dispatcher.filters import Text

from loader import dp
# @dp.message_handler()
# async  def default_text(msg: types.Message):
#     await msg.answer("ILtimos , to'gri buyruq kiriting")


@dp.message_handler(Text(equals="assalomu alaykum", ignore_case=True))
async def salom_menu(msg: types.Message):
    await msg.answer("Vaalaykum Assalom , botga xush kelibsiz, Botdan foydalanish uchun maxsus buyruqlarni kiriting !")


@dp.message_handler(Text(contains="assalom"))
@dp.message_handler(Text(contains="salom"))
@dp.message_handler(Text(contains="alik"))
async def salom1_menu(msg: types.Message):
    await msg.answer("Vaalaykum Assalom , botga xush kelibsiz, Botdan foydalanish uchun maxsus buyruqlarni kiriting !")

@dp.message_handler(Text(contains="Andijon"))
@dp.message_handler(Text(contains="andijon"))
@dp.message_handler(Text(contains="and"))
@dp.message_handler(Text(contains="ANDIJON"))
@dp.message_handler(Text(contains="андижон"))
@dp.message_handler(Text(contains="Aндижон"))
async def anjan(msg: types.Message):
    await msg.answer(f" 🕌 11-mart Dushanba Saxarlik-5:11 Iftorlik-18:15\n"
                     f" 🕌 12-mart Seshanba Saxarlik-5:09 Iftorlik-18:16\n"
                     f" 🕌 13-mart Chorshanba Saxarlik-5:08 Iftorlik-18:17\n"
                     f" 🕌 14-mart Payshanba Saxarlik-5:06 Iftorlik-18:19\n"
                     f" 🕌 15-mart Juma Saxarlik-5:04 Iftorlik-18:20\n"
                     f" 🕌 16-mart Shanba Saxarlik-5:02 Iftorlik-18:21\n"
                     f" 🕌 17-mart Yakshanba Saxarlik-5:01 Iftorlik-18:22\n"
                     f" 🕌 18-mart Dushanba Saxarlik-4:59 Iftorlik-18:23\n"
                     f" 🕌 19-mart Seshanba Saxarlik-4:57 Iftorlik-18:24\n"
                     f" 🕌 20-mart Chorshanba Saxarlik-4:56 Iftorlik-18:25\n"
                     f" 🕌 21-mart Payshanba Saxarlik-4:54 Iftorlik-18:26\n"
                     f" 🕌 22-mart Juma Saxarlik-4:53 Iftorlik-18:27\n"
                     f" 🕌 23-mart Shanba Saxarlik-4:51 Iftorlik-18:28\n"
                     f" 🕌 24-mart Yakshanba Saxarlik-4:49 Iftorlik-18:30\n"
                     f" 🕌 25-mart Dushanba Saxarlik-4:47 Iftorlik-18:31\n"
                     f" 🕌 26-mart Seshanba Saxarlik-4:46 Iftorlik-18:32\n"
                     f" 🕌 27-mart Chorshanba Saxarlik-4:44 Iftorlik-18:33\n"
                     f" 🕌 28-mart Payshanba Saxarlik-4:42 Iftorlik-18:34\n"
                     f" 🕌 29-mart Juma Saxarlik-4:40 Iftorlik-18:35\n"
                     f" 🕌 30-mart Shanba Saxarlik-4:38 Iftorlik-18:35\n"
                     f" 🕌 31-mart Yakshanba Saxarlik-4:37 Iftorlik-18:36\n"
                     f" 🕌 1-aprel Dushanba Saxarlik-4:35 Iftorlik-18:37\n"
                     f" 🕌 2-aprel Seshanba Saxarlik-4:33 Iftorlik-18:38\n"
                     f" 🕌 3-aprel Chorshanba Saxarlik-4:31 Iftorlik-18:39\n"
                     f" 🕌 4-aprel Payshanba Saxarlik-4:29 Iftorlik-18:40\n"
                     f" 🕌 5-aprel Juma Saxarlik-4:27 Iftorlik-18:41\n"
                     f" 🕌 6-aprel Shanba Saxarlik-4:25 Iftorlik-18:43\n"
                     f" 🕌 7-aprel Yakshanba Saxarlik-4:23 Iftorlik-18:44\n"
                     f" 🕌 8-aprel Dushanba Saxarlik-4:21 Iftorlik-18:45\n"
                     f" 🕌 9-aprel Seshanba Saxarlik-4:20 Iftorlik-18:46\n"
                     )

@dp.message_handler(Text(contains="Buxoro"))
@dp.message_handler(Text(contains="buxoro"))
@dp.message_handler(Text(contains="bux"))
async def buxoro_taqvim(msg: types.Message):
    await msg.answer(f" 🕌 11-mart Dushanba Saxarlik-5:23 Iftorlik-18:27\n"
                     f" 🕌 12-mart Seshanba Saxarlik-5:21 Iftorlik-18:28\n"
                     f" 🕌 13-mart Chorshanba Saxarlik-5:20 Iftorlik-18:29\n"
                     f" 🕌 14-mart Payshanba Saxarlik-5:18 Iftorlik-18:31\n"
                     f" 🕌 15-mart Juma Saxarlik-5:16 Iftorlik-18:32\n"
                     f" 🕌 16-mart Shanba Saxarlik-5:14 Iftorlik-18:33\n"
                     f" 🕌 17-mart Yakshanba Saxarlik-5:13 Iftorlik-18:34\n"
                     f" 🕌 18-mart Dushanba Saxarlik-5:11 Iftorlik-18:35\n"
                     f" 🕌 19-mart Seshanba Saxarlik-5:09 Iftorlik-18:36\n"
                     f" 🕌 20-mart Chorshanba Saxarlik-5:07 Iftorlik-18:37\n"
                     f" 🕌 21-mart Payshanba Saxarlik-5:05 Iftorlik-18:38\n"
                     f" 🕌 22-mart Juma Saxarlik-5:04 Iftorlik-18:39\n"
                     f" 🕌 23-mart Shanba Saxarlik-5:02 Iftorlik-18:40\n"
                     f" 🕌 24-mart Yakshanba Saxarlik-5:00 Iftorlik-18:42\n"
                     f" 🕌 25-mart Dushanba Saxarlik-4:58 Iftorlik-18:43\n"
                     f" 🕌 26-mart Seshanba Saxarlik-4:57 Iftorlik-18:44\n"
                     f" 🕌 27-mart Chorshanba Saxarlik-4:55 Iftorlik-18:45\n"
                     f" 🕌 28-mart Payshanba Saxarlik-4:53 Iftorlik-18:46\n"
                     f" 🕌 29-mart Juma Saxarlik-4:51 Iftorlik-18:47\n"
                     f" 🕌 30-mart Shanba Saxarlik-4:49 Iftorlik-18:48\n"
                     f" 🕌 31-mart Yakshanba Saxarlik-4:48 Iftorlik-18:49\n"
                     f" 🕌 1-aprel Dushanba Saxarlik-4:46 Iftorlik-18:50\n"
                     f" 🕌 2-aprel Seshanba Saxarlik-4:44 Iftorlik-18:51\n"
                     f" 🕌 3-aprel Chorshanba Saxarlik-4:42 Iftorlik-18:52\n"
                     f" 🕌 4-aprel Payshanba Saxarlik-4:40 Iftorlik-18:53\n"
                     f" 🕌 5-aprel Juma Saxarlik-4:38 Iftorlik-18:54\n"
                     f" 🕌 6-aprel Shanba Saxarlik-4:36 Iftorlik-18:56\n"
                     f" 🕌 7-aprel Yakshanba Saxarlik-4:34 Iftorlik-18:57\n"
                     f" 🕌 8-aprel Dushanba Saxarlik-4:32 Iftorlik-18:58\n"
                     f" 🕌 9-aprel Seshanba Saxarlik-4:31 Iftorlik-18:59\n")

@dp.message_handler(Text(contains="Toshkent"))
@dp.message_handler(Text(contains="toshkent"))
@dp.message_handler(Text(contains="tosh"))
@dp.message_handler(Text(contains='тошкент'))
@dp.message_handler(Text(contains='Тошкент'))
async def toshkent_taqvim(msg: types.Message):
    await msg.answer(f" 🕌 11-mart Dushanba Saxarlik-5:23 Iftorlik-18:27\n"
                         f" 🕌 12-mart Seshanba Saxarlik-5:21 Iftorlik-18:28\n"
                         f" 🕌 13-mart Chorshanba Saxarlik-5:20 Iftorlik-18:29\n"
                         f" 🕌 14-mart Payshanba Saxarlik-5:18 Iftorlik-18:31\n"
                         f" 🕌 15-mart Juma Saxarlik-5:16 Iftorlik-18:32\n"
                         f" 🕌 16-mart Shanba Saxarlik-5:14 Iftorlik-18:33\n"
                         f" 🕌 17-mart Yakshanba Saxarlik-5:13 Iftorlik-18:34\n"
                         f" 🕌 18-mart Dushanba Saxarlik-5:11 Iftorlik-18:35\n"
                         f" 🕌 19-mart Seshanba Saxarlik-5:09 Iftorlik-18:36\n"
                         f" 🕌 20-mart Chorshanba Saxarlik-5:07 Iftorlik-18:37\n"
                         f" 🕌 21-mart Payshanba Saxarlik-5:05 Iftorlik-18:38\n"
                         f" 🕌 22-mart Juma Saxarlik-5:04 Iftorlik-18:39\n"
                         f" 🕌 23-mart Shanba Saxarlik-5:02 Iftorlik-18:40\n"
                         f" 🕌 24-mart Yakshanba Saxarlik-5:00 Iftorlik-18:42\n"
                         f" 🕌 25-mart Dushanba Saxarlik-4:58 Iftorlik-18:43\n"
                         f" 🕌 26-mart Seshanba Saxarlik-4:57 Iftorlik-18:44\n"
                         f" 🕌 27-mart Chorshanba Saxarlik-4:55 Iftorlik-18:45\n"
                         f" 🕌 28-mart Payshanba Saxarlik-4:53 Iftorlik-18:46\n"
                         f" 🕌 29-mart Juma Saxarlik-4:51 Iftorlik-18:47\n"
                         f" 🕌 30-mart Shanba Saxarlik-4:49 Iftorlik-18:48\n"
                         f" 🕌 31-mart Yakshanba Saxarlik-4:48 Iftorlik-18:49\n"
                         f" 🕌 1-aprel Dushanba Saxarlik-4:46 Iftorlik-18:50\n"
                         f" 🕌 2-aprel Seshanba Saxarlik-4:44 Iftorlik-18:51\n"
                         f" 🕌 3-aprel Chorshanba Saxarlik-4:42 Iftorlik-18:52\n"
                         f" 🕌 4-aprel Payshanba Saxarlik-4:40 Iftorlik-18:53\n"
                         f" 🕌 5-aprel Juma Saxarlik-4:38 Iftorlik-18:54\n"
                         f" 🕌 6-aprel Shanba Saxarlik-4:36 Iftorlik-18:56\n"
                         f" 🕌 7-aprel Yakshanba Saxarlik-4:34 Iftorlik-18:57\n"
                         f" 🕌 8-aprel Dushanba Saxarlik-4:32 Iftorlik-18:58\n"
                         f" 🕌 9-aprel Seshanba Saxarlik-4:31 Iftorlik-18:59\n")

@dp.message_handler(Text(contains="Sirdaryo"))
@dp.message_handler(Text(contains="sirdaryo"))
@dp.message_handler(Text(contains="sir"))
@dp.message_handler(Text(contains='сирдарё'))
@dp.message_handler(Text(contains='Сирдарё'))
async def toshkent_taqvim(msg: types.Message):
        await msg.answer(f" 🕌 11-mart Dushanba Saxarlik-5:26 Iftorlik-18:29\n"
                         f" 🕌 12-mart Seshanba Saxarlik-5:24 Iftorlik-18:30\n"
                         f" 🕌 13-mart Chorshanba Saxarlik-5:23 Iftorlik-18:31\n"
                         f" 🕌 14-mart Payshanba Saxarlik-5:20 Iftorlik-18:33\n"
                         f" 🕌 15-mart Juma Saxarlik-5:19 Iftorlik-18:34\n"
                         f" 🕌 16-mart Shanba Saxarlik-5:17 Iftorlik-18:35\n"
                         f" 🕌 17-mart Yakshanba Saxarlik-5:16 Iftorlik-18:36\n"
                         f" 🕌 18-mart Dushanba Saxarlik-5:14 Iftorlik-18:37\n"
                         f" 🕌 19-mart Seshanba Saxarlik-5:12 Iftorlik-18:38\n"
                         f" 🕌 20-mart Chorshanba Saxarlik-5:11 Iftorlik-18:39\n"
                         f" 🕌 21-mart Payshanba Saxarlik-5:09 Iftorlik-18:40\n"
                         f" 🕌 22-mart Juma Saxarlik-5:08 Iftorlik-18:41\n"
                         f" 🕌 23-mart Shanba Saxarlik-5:06 Iftorlik-18:42\n"
                         f" 🕌 24-mart Yakshanba Saxarlik-5:04 Iftorlik-18:44\n"
                         f" 🕌 25-mart Dushanba Saxarlik-5:02 Iftorlik-18:45\n"
                         f" 🕌 26-mart Seshanba Saxarlik-5:01 Iftorlik-18:46\n"
                         f" 🕌 27-mart Chorshanba Saxarlik-4:59 Iftorlik-18:47\n"
                         f" 🕌 28-mart Payshanba Saxarlik-4:57 Iftorlik-18:48\n"
                         f" 🕌 29-mart Juma Saxarlik-4:55 Iftorlik-18:49\n"
                         f" 🕌 30-mart Shanba Saxarlik-4:53 Iftorlik-18:50\n"
                         f" 🕌 31-mart Yakshanba Saxarlik-4:52 Iftorlik-18:51\n"
                         f" 🕌 1-aprel Dushanba Saxarlik-4:50 Iftorlik-18:52\n"
                         f" 🕌 2-aprel Seshanba Saxarlik-4:48 Iftorlik-18:53\n"
                         f" 🕌 3-aprel Chorshanba Saxarlik-4:46 Iftorlik-18:54\n"
                         f" 🕌 4-aprel Payshanba Saxarlik-4:44 Iftorlik-18:55\n"
                         f" 🕌 5-aprel Juma Saxarlik-4:42 Iftorlik-18:56\n"
                         f" 🕌 6-aprel Shanba Saxarlik-4:40 Iftorlik-18:58\n"
                         f" 🕌 7-aprel Yakshanba Saxarlik-4:38 Iftorlik-18:59\n"
                         f" 🕌 8-aprel Dushanba Saxarlik-4:36 Iftorlik-19:00\n"
                         f" 🕌 9-aprel Seshanba Saxarlik-4:35 Iftorlik-19:01\n")

@dp.message_handler(Text(contains="Jizzax"))
@dp.message_handler(Text(contains="jizzah"))
@dp.message_handler(Text(contains="jiz"))
@dp.message_handler(Text(contains='жиззах'))
@dp.message_handler(Text(contains='Жиззах'))
async def toshkent_taqvim(msg: types.Message):
        await msg.answer(f" 🕌 11-mart Dushanba Saxarlik-5:29 Iftorlik-18:33\n"
                         f" 🕌 12-mart Seshanba Saxarlik-5:27 Iftorlik-18:34\n"
                         f" 🕌 13-mart Chorshanba Saxarlik-5:26 Iftorlik-18:35\n"
                         f" 🕌 14-mart Payshanba Saxarlik-5:24 Iftorlik-18:37\n"
                         f" 🕌 15-mart Juma Saxarlik-5:22 Iftorlik-18:38\n"
                         f" 🕌 16-mart Shanba Saxarlik-5:20 Iftorlik-18:39\n"
                         f" 🕌 17-mart Yakshanba Saxarlik-5:19 Iftorlik-18:40\n"
                         f" 🕌 18-mart Dushanba Saxarlik-5:17 Iftorlik-18:41\n"
                         f" 🕌 19-mart Seshanba Saxarlik-5:15 Iftorlik-18:42\n"
                         f" 🕌 20-mart Chorshanba Saxarlik-5:15 Iftorlik-18:43\n"
                         f" 🕌 21-mart Payshanba Saxarlik-5:13 Iftorlik-18:44\n"
                         f" 🕌 22-mart Juma Saxarlik-5:12 Iftorlik-18:45\n"
                         f" 🕌 23-mart Shanba Saxarlik-5:10 Iftorlik-18:46\n"
                         f" 🕌 24-mart Yakshanba Saxarlik-5:08 Iftorlik-18:48\n"
                         f" 🕌 25-mart Dushanba Saxarlik-5:06 Iftorlik-18:49\n"
                         f" 🕌 26-mart Seshanba Saxarlik-5:05 Iftorlik-18:50\n"
                         f" 🕌 27-mart Chorshanba Saxarlik-5:03 Iftorlik-18:51\n"
                         f" 🕌 28-mart Payshanba Saxarlik-5:01 Iftorlik-18:52\n"
                         f" 🕌 29-mart Juma Saxarlik-4:59 Iftorlik-18:53\n"
                         f" 🕌 30-mart Shanba Saxarlik-4:57 Iftorlik-18:53\n"
                         f" 🕌 31-mart Yakshanba Saxarlik-4:56 Iftorlik-18:54\n"
                         f" 🕌 1-aprel Dushanba Saxarlik-4:54 Iftorlik-18:55\n"
                         f" 🕌 2-aprel Seshanba Saxarlik-4:52 Iftorlik-18:56\n"
                         f" 🕌 3-aprel Chorshanba Saxarlik-4:50 Iftorlik-18:57\n"
                         f" 🕌 4-aprel Payshanba Saxarlik-4:48 Iftorlik-18:58\n"
                         f" 🕌 5-aprel Juma Saxarlik-4:46 Iftorlik-18:59\n"
                         f" 🕌 6-aprel Shanba Saxarlik-4:44 Iftorlik-19:01\n"
                         f" 🕌 7-aprel Yakshanba Saxarlik-4:42 Iftorlik-19:02\n"
                         f" 🕌 8-aprel Dushanba Saxarlik-4:40 Iftorlik-19:03\n"
                         f" 🕌 9-aprel Seshanba Saxarlik-4:39 Iftorlik-19:04\n")


@dp.message_handler(Text(contains="Navoiy"))
@dp.message_handler(Text(contains="navoiy"))
@dp.message_handler(Text(contains="nav"))
@dp.message_handler(Text(contains='Навоий'))
@dp.message_handler(Text(contains='навоий'))
@dp.message_handler(Text(contains="НAВОИЙ"))
async def navoiy_taqvim(msg: types.Message):
        await msg.answer(f" 🕌 11-mart Dushanba Saxarlik-5:39 Iftorlik-18:43\n"
                         f" 🕌 12-mart Seshanba Saxarlik-5:37 Iftorlik-18:44\n"
                         f" 🕌 13-mart Chorshanba Saxarlik-5:36 Iftorlik-18:45\n"
                         f" 🕌 14-mart Payshanba Saxarlik-5:34 Iftorlik-18:47\n"
                         f" 🕌 15-mart Juma Saxarlik-5:32 Iftorlik-18:48\n"
                         f" 🕌 16-mart Shanba Saxarlik-5:30 Iftorlik-18:49\n"
                         f" 🕌 17-mart Yakshanba Saxarlik-5:29 Iftorlik-18:50\n"
                         f" 🕌 18-mart Dushanba Saxarlik-5:27 Iftorlik-18:51\n"
                         f" 🕌 19-mart Seshanba Saxarlik-5:25 Iftorlik-18:52\n"
                         f" 🕌 20-mart Chorshanba Saxarlik-5:25 Iftorlik-18:53\n"
                         f" 🕌 21-mart Payshanba Saxarlik-5:23 Iftorlik-18:54\n"
                         f" 🕌 22-mart Juma Saxarlik-5:22 Iftorlik-18:55\n"
                         f" 🕌 23-mart Shanba Saxarlik-5:20 Iftorlik-18:56\n"
                         f" 🕌 24-mart Yakshanba Saxarlik-5:18 Iftorlik-18:58\n"
                         f" 🕌 25-mart Dushanba Saxarlik-5:16 Iftorlik-18:59\n"
                         f" 🕌 26-mart Seshanba Saxarlik-5:15 Iftorlik-19:00\n"
                         f" 🕌 27-mart Chorshanba Saxarlik-5:13 Iftorlik-19:01\n"
                         f" 🕌 28-mart Payshanba Saxarlik-5:11 Iftorlik-19:02\n"
                         f" 🕌 29-mart Juma Saxarlik-5:09 Iftorlik-19:03\n"
                         f" 🕌 30-mart Shanba Saxarlik-5:07 Iftorlik-19:03\n"
                         f" 🕌 31-mart Yakshanba Saxarlik-5:06 Iftorlik-19:04\n"
                         f" 🕌 1-aprel Dushanba Saxarlik-5:04 Iftorlik-19:05\n"
                         f" 🕌 2-aprel Seshanba Saxarlik-5:02 Iftorlik-19:06\n"
                         f" 🕌 3-aprel Chorshanba Saxarlik-5:00 Iftorlik-19:07\n"
                         f" 🕌 4-aprel Payshanba Saxarlik-4:58 Iftorlik-19:08\n"
                         f" 🕌 5-aprel Juma Saxarlik-4:56 Iftorlik-19:09\n"
                         f" 🕌 6-aprel Shanba Saxarlik-4:54 Iftorlik-19:11\n"
                         f" 🕌 7-aprel Yakshanba Saxarlik-4:52 Iftorlik-19:12\n"
                         f" 🕌 8-aprel Dushanba Saxarlik-4:50 Iftorlik-19:13\n"
                         f" 🕌 9-aprel Seshanba Saxarlik-4:49 Iftorlik-19:14\n")


@dp.message_handler(Text(contains="Namangan"))
@dp.message_handler(Text(contains="namangan"))
@dp.message_handler(Text(contains="nam"))
@dp.message_handler(Text(contains='наманган'))
@dp.message_handler(Text(contains='Наманган'))
@dp.message_handler(Text(contains="НAМAНГAН"))
async def navoiy_taqvim(msg: types.Message):
        await msg.answer(f" 🕌 11-mart Dushanba Saxarlik-5:14 Iftorlik-18:18\n"
                         f" 🕌 12-mart Seshanba Saxarlik-5:12 Iftorlik-18:19\n"
                         f" 🕌 13-mart Chorshanba Saxarlik-5:11 Iftorlik-18:20\n"
                         f" 🕌 14-mart Payshanba Saxarlik-5:09 Iftorlik-18:22\n"
                         f" 🕌 15-mart Juma Saxarlik-5:07 Iftorlik-18:23\n"
                         f" 🕌 16-mart Shanba Saxarlik-5:05 Iftorlik-18:24\n"
                         f" 🕌 17-mart Yakshanba Saxarlik-5:04 Iftorlik-18:25\n"
                         f" 🕌 18-mart Dushanba Saxarlik-5:02 Iftorlik-18:26\n"
                         f" 🕌 19-mart Seshanba Saxarlik-5:00 Iftorlik-18:27\n"
                         f" 🕌 20-mart Chorshanba Saxarlik-4:58 Iftorlik-18:28\n"
                         f" 🕌 21-mart Payshanba Saxarlik-4:56 Iftorlik-18:29\n"
                         f" 🕌 22-mart Juma Saxarlik-4:55 Iftorlik-18:30\n"
                         f" 🕌 23-mart Shanba Saxarlik-4:53 Iftorlik-18:31\n"
                         f" 🕌 24-mart Yakshanba Saxarlik-4:51 Iftorlik-18:33\n"
                         f" 🕌 25-mart Dushanba Saxarlik-4:49 Iftorlik-18:34\n"
                         f" 🕌 26-mart Seshanba Saxarlik-4:48 Iftorlik-18:35\n"
                         f" 🕌 27-mart Chorshanba Saxarlik-4:46 Iftorlik-18:36\n"
                         f" 🕌 28-mart Payshanba Saxarlik-4:44 Iftorlik-18:37\n"
                         f" 🕌 29-mart Juma Saxarlik-4:42 Iftorlik-18:38\n"
                         f" 🕌 30-mart Shanba Saxarlik-4:40 Iftorlik-18:38\n"
                         f" 🕌 31-mart Yakshanba Saxarlik-4:39 Iftorlik-18:39\n"
                         f" 🕌 1-aprel Dushanba Saxarlik-4:37 Iftorlik-18:40\n"
                         f" 🕌 2-aprel Seshanba Saxarlik-4:35 Iftorlik-18:41\n"
                         f" 🕌 3-aprel Chorshanba Saxarlik-4:33 Iftorlik-18:42\n"
                         f" 🕌 4-aprel Payshanba Saxarlik-4:31 Iftorlik-18:43\n"
                         f" 🕌 5-aprel Juma Saxarlik-4:29 Iftorlik-18:44\n"
                         f" 🕌 6-aprel Shanba Saxarlik-4:27 Iftorlik-18:46\n"
                         f" 🕌 7-aprel Yakshanba Saxarlik-4:25 Iftorlik-18:47\n"
                         f" 🕌 8-aprel Dushanba Saxarlik-4:23 Iftorlik-18:48\n"
                         f" 🕌 9-aprel Seshanba Saxarlik-4:22 Iftorlik-18:49\n")

@dp.message_handler(Text(contains="Qoraqalpog'iston Respublikasi"))
@dp.message_handler(Text(contains="qoraqalpog'iston"))
@dp.message_handler(Text(contains="qora"))
@dp.message_handler(Text(contains='қорақалпоғистон'))
@dp.message_handler(Text(contains='Қорақалпоғистон'))
@dp.message_handler(Text(contains="ҚОРAҚAЛПОҒИСТОН"))
@dp.message_handler(Text(contains="Qoraqalpog'iston"))
async def qoraqalpoq_taqvim(msg: types.Message):
        await msg.answer(f" 🕌 11-mart Dushanba Saxarlik-6:00 Iftorlik-19:05\n"
                         f" 🕌 12-mart Seshanba Saxarlik-5:58 Iftorlik-19:06\n"
                         f" 🕌 13-mart Chorshanba Saxarlik-5:57 Iftorlik-19:07\n"
                         f" 🕌 14-mart Payshanba Saxarlik-5:55 Iftorlik-19:09\n"
                         f" 🕌 15-mart Juma Saxarlik-5:53 Iftorlik-19:10\n"
                         f" 🕌 16-mart Shanba Saxarlik-5:51 Iftorlik-19:11\n"
                         f" 🕌 17-mart Yakshanba Saxarlik-5:50 Iftorlik-19:12\n"
                         f" 🕌 18-mart Dushanba Saxarlik-5:48 Iftorlik-19:13\n"
                         f" 🕌 19-mart Seshanba Saxarlik-5:46 Iftorlik-19:14\n"
                         f" 🕌 20-mart Chorshanba Saxarlik-5:44 Iftorlik-19:16\n"
                         f" 🕌 21-mart Payshanba Saxarlik-5:42 Iftorlik-19:17\n"
                         f" 🕌 22-mart Juma Saxarlik-5:41 Iftorlik-19:18\n"
                         f" 🕌 23-mart Shanba Saxarlik-5:39 Iftorlik-19:19\n"
                         f" 🕌 24-mart Yakshanba Saxarlik-5:37 Iftorlik-19:21\n"
                         f" 🕌 25-mart Dushanba Saxarlik-5:35 Iftorlik-19:22\n"
                         f" 🕌 26-mart Seshanba Saxarlik-5:34 Iftorlik-19:23\n"
                         f" 🕌 27-mart Chorshanba Saxarlik-5:32 Iftorlik-19:24\n"
                         f" 🕌 28-mart Payshanba Saxarlik-5:30 Iftorlik-19:25\n"
                         f" 🕌 29-mart Juma Saxarlik-5:28 Iftorlik-19:26\n"
                         f" 🕌 30-mart Shanba Saxarlik-5:26 Iftorlik-19:27\n"
                         f" 🕌 31-mart Yakshanba Saxarlik-5:25 Iftorlik-19:28\n"
                         f" 🕌 1-aprel Dushanba Saxarlik-5:23 Iftorlik-19:29\n"
                         f" 🕌 2-aprel Seshanba Saxarlik-5:21 Iftorlik-19:30\n"
                         f" 🕌 3-aprel Chorshanba Saxarlik-5:19 Iftorlik-19:31\n"
                         f" 🕌 4-aprel Payshanba Saxarlik-5:17 Iftorlik-19:32\n"
                         f" 🕌 5-aprel Juma Saxarlik-5:15 Iftorlik-19:33\n"
                         f" 🕌 6-aprel Shanba Saxarlik-5:13 Iftorlik-19:35\n"
                         f" 🕌 7-aprel Yakshanba Saxarlik-5:11 Iftorlik-19:36\n"
                         f" 🕌 8-aprel Dushanba Saxarlik-5:09 Iftorlik-19:37\n"
                         f" 🕌 9-aprel Seshanba Saxarlik-5:08 Iftorlik-19:38\n")

@dp.message_handler(Text(contains="Samarqand"))
@dp.message_handler(Text(contains="samarqand"))
@dp.message_handler(Text(contains="sam"))
@dp.message_handler(Text(contains='Самарқанд'))
@dp.message_handler(Text(contains='СAМAРҚAНД'))
@dp.message_handler(Text(contains="сам"))
@dp.message_handler(Text(contains="samar"))
@dp.message_handler(Text(contains="SAMARQAND"))
async def samarqand_taqvim(msg: types.Message):
        await msg.answer(f" 🕌 11-mart Dushanba Saxarlik-5:33 Iftorlik-18:37\n"
                         f" 🕌 12-mart Seshanba Saxarlik-5:31 Iftorlik-18:38\n"
                         f" 🕌 13-mart Chorshanba Saxarlik-5:30 Iftorlik-18:39\n"
                         f" 🕌 14-mart Payshanba Saxarlik-5:28 Iftorlik-18:41\n"
                         f" 🕌 15-mart Juma Saxarlik-5:26 Iftorlik-18:42\n"
                         f" 🕌 16-mart Shanba Saxarlik-5:24 Iftorlik-18:43\n"
                         f" 🕌 17-mart Yakshanba Saxarlik-5:23 Iftorlik-18:44\n"
                         f" 🕌 18-mart Dushanba Saxarlik-5:21 Iftorlik-18:45\n"
                         f" 🕌 19-mart Seshanba Saxarlik-5:19 Iftorlik-18:46\n"
                         f" 🕌 20-mart Chorshanba Saxarlik-5:19 Iftorlik-18:46\n"
                         f" 🕌 21-mart Payshanba Saxarlik-5:17 Iftorlik-18:47\n"
                         f" 🕌 22-mart Juma Saxarlik-5:16 Iftorlik-18:48\n"
                         f" 🕌 23-mart Shanba Saxarlik-5:14 Iftorlik-18:49\n"
                         f" 🕌 24-mart Yakshanba Saxarlik-5:12 Iftorlik-18:51\n"
                         f" 🕌 25-mart Dushanba Saxarlik-5:10 Iftorlik-18:52\n"
                         f" 🕌 26-mart Seshanba Saxarlik-5:09 Iftorlik-18:53\n"
                         f" 🕌 27-mart Chorshanba Saxarlik-5:07 Iftorlik-18:54\n"
                         f" 🕌 28-mart Payshanba Saxarlik-5:05 Iftorlik-18:55\n"
                         f" 🕌 29-mart Juma Saxarlik-5:03 Iftorlik-18:56\n"
                         f" 🕌 30-mart Shanba Saxarlik-5:01 Iftorlik-18:56\n"
                         f" 🕌 31-mart Yakshanba Saxarlik-5:00 Iftorlik-18:57\n"
                         f" 🕌 1-aprel Dushanba Saxarlik-4:58 Iftorlik-18:58\n"
                         f" 🕌 2-aprel Seshanba Saxarlik-4:56 Iftorlik-18:59\n"
                         f" 🕌 3-aprel Chorshanba Saxarlik-4:54 Iftorlik-19:00\n"
                         f" 🕌 4-aprel Payshanba Saxarlik-4:52 Iftorlik-19:01\n"
                         f" 🕌 5-aprel Juma Saxarlik-4:50 Iftorlik-19:02\n"
                         f" 🕌 6-aprel Shanba Saxarlik-4:48 Iftorlik-19:04\n"
                         f" 🕌 7-aprel Yakshanba Saxarlik-4:46 Iftorlik-19:05\n"
                         f" 🕌 8-aprel Dushanba Saxarlik-4:44 Iftorlik-19:06\n"
                         f" 🕌 9-aprel Seshanba Saxarlik-4:43 Iftorlik-19:07\n")



@dp.message_handler(Text(contains="Surxondaryo"))
@dp.message_handler(Text(contains="surxondaryo"))
@dp.message_handler(Text(contains="sur"))
@dp.message_handler(Text(contains='сурхондарё'))
@dp.message_handler(Text(contains='Сурхондарё'))
@dp.message_handler(Text(contains="сур"))
@dp.message_handler(Text(contains="surxon"))
async def surxon_taqvim(msg: types.Message):
        await msg.answer(f" 🕌 11-mart Dushanba Saxarlik-5:34 Iftorlik-18:37\n"
                         f" 🕌 12-mart Seshanba Saxarlik-5:32 Iftorlik-18:38\n"
                         f" 🕌 13-mart Chorshanba Saxarlik-5:31 Iftorlik-18:39\n"
                         f" 🕌 14-mart Payshanba Saxarlik-5:29 Iftorlik-18:41\n"
                         f" 🕌 15-mart Juma Saxarlik-5:27 Iftorlik-18:42\n"
                         f" 🕌 16-mart Shanba Saxarlik-5:25 Iftorlik-18:43\n"
                         f" 🕌 17-mart Yakshanba Saxarlik-5:24 Iftorlik-18:44\n"
                         f" 🕌 18-mart Dushanba Saxarlik-5:22 Iftorlik-18:45\n"
                         f" 🕌 19-mart Seshanba Saxarlik-5:20 Iftorlik-18:46\n"
                         f" 🕌 20-mart Chorshanba Saxarlik-5:20 Iftorlik-18:45\n"
                         f" 🕌 21-mart Payshanba Saxarlik-5:18 Iftorlik-18:46\n"
                         f" 🕌 22-mart Juma Saxarlik-5:17 Iftorlik-18:47\n"
                         f" 🕌 23-mart Shanba Saxarlik-5:15 Iftorlik-18:48\n"
                         f" 🕌 24-mart Yakshanba Saxarlik-5:13 Iftorlik-18:50\n"
                         f" 🕌 25-mart Dushanba Saxarlik-5:11 Iftorlik-18:51\n"
                         f" 🕌 26-mart Seshanba Saxarlik-5:10 Iftorlik-18:52\n"
                         f" 🕌 27-mart Chorshanba Saxarlik-5:08 Iftorlik-18:53\n"
                         f" 🕌 28-mart Payshanba Saxarlik-5:06 Iftorlik-18:54\n"
                         f" 🕌 29-mart Juma Saxarlik-5:04 Iftorlik-18:55\n"
                         f" 🕌 30-mart Shanba Saxarlik-5:04 Iftorlik-18:54\n"
                         f" 🕌 31-mart Yakshanba Saxarlik-5:03 Iftorlik-18:55\n"
                         f" 🕌 1-aprel Dushanba Saxarlik-5:01 Iftorlik-18:56\n"
                         f" 🕌 2-aprel Seshanba Saxarlik-4:59 Iftorlik-18:57\n"
                         f" 🕌 3-aprel Chorshanba Saxarlik-4:57 Iftorlik-18:58\n"
                         f" 🕌 4-aprel Payshanba Saxarlik-4:55 Iftorlik-18:59\n"
                         f" 🕌 5-aprel Juma Saxarlik-4:53 Iftorlik-19:00\n"
                         f" 🕌 6-aprel Shanba Saxarlik-4:51 Iftorlik-19:02\n"
                         f" 🕌 7-aprel Yakshanba Saxarlik-4:49 Iftorlik-19:03\n"
                         f" 🕌 8-aprel Dushanba Saxarlik-4:47 Iftorlik-19:04\n"
                         f" 🕌 9-aprel Seshanba Saxarlik-4:46 Iftorlik-19:05\n")


@dp.message_handler(Text(contains="Xorazm"))
@dp.message_handler(Text(contains="xorazm"))
@dp.message_handler(Text(contains="xor"))
@dp.message_handler(Text(contains='хоразм'))
@dp.message_handler(Text(contains='Хоразм'))
@dp.message_handler(Text(contains="ХОРAЗМ"))
@dp.message_handler(Text(contains="хор"))
async def xorazm_taqvim(msg: types.Message):
        await msg.answer(f" 🕌 11-mart Dushanba Saxarlik-5:56 Iftorlik-19:01\n"
                         f" 🕌 12-mart Seshanba Saxarlik-5:54 Iftorlik-19:02\n"
                         f" 🕌 13-mart Chorshanba Saxarlik-5:53 Iftorlik-19:03\n"
                         f" 🕌 14-mart Payshanba Saxarlik-5:51 Iftorlik-19:05\n"
                         f" 🕌 15-mart Juma Saxarlik-5:49 Iftorlik-19:06\n"
                         f" 🕌 16-mart Shanba Saxarlik-5:47 Iftorlik-19:07\n"
                         f" 🕌 17-mart Yakshanba Saxarlik-5:46 Iftorlik-19:08\n"
                         f" 🕌 18-mart Dushanba Saxarlik-5:44 Iftorlik-19:09\n"
                         f" 🕌 19-mart Seshanba Saxarlik-5:42 Iftorlik-19:10\n"
                         f" 🕌 20-mart Chorshanba Saxarlik-5:40 Iftorlik-19:12\n"
                         f" 🕌 21-mart Payshanba Saxarlik-5:38 Iftorlik-19:13\n"
                         f" 🕌 22-mart Juma Saxarlik-5:37 Iftorlik-19:14\n"
                         f" 🕌 23-mart Shanba Saxarlik-5:35 Iftorlik-19:15\n"
                         f" 🕌 24-mart Yakshanba Saxarlik-5:33 Iftorlik-19:17\n"
                         f" 🕌 25-mart Dushanba Saxarlik-5:31 Iftorlik-19:18\n"
                         f" 🕌 26-mart Seshanba Saxarlik-5:30 Iftorlik-19:19\n"
                         f" 🕌 27-mart Chorshanba Saxarlik-5:28 Iftorlik-19:20\n"
                         f" 🕌 28-mart Payshanba Saxarlik-5:26 Iftorlik-19:21\n"
                         f" 🕌 29-mart Juma Saxarlik-5:24 Iftorlik-19:22\n"
                         f" 🕌 30-mart Shanba Saxarlik-5:21 Iftorlik-19:24\n"
                         f" 🕌 31-mart Yakshanba Saxarlik-5:20 Iftorlik-19:25\n"
                         f" 🕌 1-aprel Dushanba Saxarlik-5:18 Iftorlik-19:26\n"
                         f" 🕌 2-aprel Seshanba Saxarlik-5:16 Iftorlik-19:27\n"
                         f" 🕌 3-aprel Chorshanba Saxarlik-5:14 Iftorlik-19:28\n"
                         f" 🕌 4-aprel Payshanba Saxarlik-5:12 Iftorlik-19:29\n"
                         f" 🕌 5-aprel Juma Saxarlik-5:10 Iftorlik-19:30\n"
                         f" 🕌 6-aprel Shanba Saxarlik-5:08 Iftorlik-19:32\n"
                         f" 🕌 7-aprel Yakshanba Saxarlik-5:06 Iftorlik-19:33\n"
                         f" 🕌 8-aprel Dushanba Saxarlik-5:04 Iftorlik-19:34\n"
                         f" 🕌 9-aprel Seshanba Saxarlik-5:03 Iftorlik-19:35\n")


@dp.message_handler(Text(contains="Farg'ona"))
@dp.message_handler(Text(contains="farg'ona"))
@dp.message_handler(Text(contains="far"))
@dp.message_handler(Text(contains="Farg'ona"))
@dp.message_handler(Text(contains="Фарғона"))
@dp.message_handler(Text(contains="фарғона"))
async def anjan(msg: types.Message):
    await msg.answer(f" 🕌 11-mart Dushanba Saxarlik-5:14 Iftorlik-18:17\n"
                     f" 🕌 12-mart Seshanba Saxarlik-5:012 Iftorlik-18:18\n"
                     f" 🕌 13-mart Chorshanba Saxarlik-5:11 Iftorlik-18:19\n"
                     f" 🕌 14-mart Payshanba Saxarlik-5:09 Iftorlik-18:21\n"
                     f" 🕌 15-mart Juma Saxarlik-5:07 Iftorlik-18:22\n"
                     f" 🕌 16-mart Shanba Saxarlik-5:05 Iftorlik-18:23\n"
                     f" 🕌 17-mart Yakshanba Saxarlik-5:04 Iftorlik-18:24\n"
                     f" 🕌 18-mart Dushanba Saxarlik-5:02 Iftorlik-18:25\n"
                     f" 🕌 19-mart Seshanba Saxarlik-5:00 Iftorlik-18:26\n"
                     f" 🕌 20-mart Chorshanba Saxarlik-4:59 Iftorlik-18:27\n"
                     f" 🕌 21-mart Payshanba Saxarlik-4:57 Iftorlik-18:28\n"
                     f" 🕌 22-mart Juma Saxarlik-4:56 Iftorlik-18:29\n"
                     f" 🕌 23-mart Shanba Saxarlik-4:54 Iftorlik-18:30\n"
                     f" 🕌 24-mart Yakshanba Saxarlik-4:52 Iftorlik-18:32\n"
                     f" 🕌 25-mart Dushanba Saxarlik-4:50 Iftorlik-18:33\n"
                     f" 🕌 26-mart Seshanba Saxarlik-4:49 Iftorlik-18:34\n"
                     f" 🕌 27-mart Chorshanba Saxarlik-4:47 Iftorlik-18:35\n"
                     f" 🕌 28-mart Payshanba Saxarlik-4:45 Iftorlik-18:36\n"
                     f" 🕌 29-mart Juma Saxarlik-4:43 Iftorlik-18:37\n"
                     f" 🕌 30-mart Shanba Saxarlik-4:41 Iftorlik-18:37\n"
                     f" 🕌 31-mart Yakshanba Saxarlik-4:40 Iftorlik-18:38\n"
                     f" 🕌 1-aprel Dushanba Saxarlik-4:38 Iftorlik-18:39\n"
                     f" 🕌 2-aprel Seshanba Saxarlik-4:36 Iftorlik-18:40\n"
                     f" 🕌 3-aprel Chorshanba Saxarlik-4:34 Iftorlik-18:41\n"
                     f" 🕌 4-aprel Payshanba Saxarlik-4:32 Iftorlik-18:42\n"
                     f" 🕌 5-aprel Juma Saxarlik-4:30 Iftorlik-18:43\n"
                     f" 🕌 6-aprel Shanba Saxarlik-4:28 Iftorlik-18:45\n"
                     f" 🕌 7-aprel Yakshanba Saxarlik-4:26 Iftorlik-18:46\n"
                     f" 🕌 8-aprel Dushanba Saxarlik-4:24 Iftorlik-18:47\n"
                     f" 🕌 9-aprel Seshanba Saxarlik-4:23 Iftorlik-18:48\n")


@dp.message_handler(Text(contains="Qashqadaryo"))
@dp.message_handler(Text(contains="qashqadaryo"))
@dp.message_handler(Text(contains="qash"))
@dp.message_handler(Text(contains='qashqa'))
@dp.message_handler(Text(contains='қашқадарё'))
@dp.message_handler(Text(contains="Қашқадарё"))
@dp.message_handler(Text(contains="qashqadar"))
async def surxon_taqvim(msg: types.Message):
        await msg.answer(f" 🕌 11-mart Dushanba Saxarlik-5:38 Iftorlik-18:42\n"
                         f" 🕌 12-mart Seshanba Saxarlik-5:36 Iftorlik-18:43\n"
                         f" 🕌 13-mart Chorshanba Saxarlik-5:35 Iftorlik-18:44\n"
                         f" 🕌 14-mart Payshanba Saxarlik-5:33 Iftorlik-18:46\n"
                         f" 🕌 15-mart Juma Saxarlik-5:31 Iftorlik-18:47\n"
                         f" 🕌 16-mart Shanba Saxarlik-5:29 Iftorlik-18:48\n"
                         f" 🕌 17-mart Yakshanba Saxarlik-5:28 Iftorlik-18:49\n"
                         f" 🕌 18-mart Dushanba Saxarlik-5:26 Iftorlik-18:50\n"
                         f" 🕌 19-mart Seshanba Saxarlik-5:24 Iftorlik-18:51\n"
                         f" 🕌 20-mart Chorshanba Saxarlik-5:24 Iftorlik-18:51\n"
                         f" 🕌 21-mart Payshanba Saxarlik-5:22 Iftorlik-18:52\n"
                         f" 🕌 22-mart Juma Saxarlik-5:21 Iftorlik-18:53\n"
                         f" 🕌 23-mart Shanba Saxarlik-5:19 Iftorlik-18:54\n"
                         f" 🕌 24-mart Yakshanba Saxarlik-5:17 Iftorlik-18:56\n"
                         f" 🕌 25-mart Dushanba Saxarlik-5:15 Iftorlik-18:57\n"
                         f" 🕌 26-mart Seshanba Saxarlik-5:14 Iftorlik-18:58\n"
                         f" 🕌 27-mart Chorshanba Saxarlik-5:12 Iftorlik-18:59\n"
                         f" 🕌 28-mart Payshanba Saxarlik-5:10 Iftorlik-19:00\n"
                         f" 🕌 29-mart Juma Saxarlik-5:08 Iftorlik-19:01\n"
                         f" 🕌 30-mart Shanba Saxarlik-5:08 Iftorlik-19:01\n"
                         f" 🕌 31-mart Yakshanba Saxarlik-5:07 Iftorlik-19:02\n"
                         f" 🕌 1-aprel Dushanba Saxarlik-5:05 Iftorlik-19:03\n"
                         f" 🕌 2-aprel Seshanba Saxarlik-5:03 Iftorlik-19:04\n"
                         f" 🕌 3-aprel Chorshanba Saxarlik-5:01 Iftorlik-19:05\n"
                         f" 🕌 4-aprel Payshanba Saxarlik-4:59 Iftorlik-19:06\n"
                         f" 🕌 5-aprel Juma Saxarlik-4:57 Iftorlik-19:07\n"
                         f" 🕌 6-aprel Shanba Saxarlik-4:55 Iftorlik-19:09\n"
                         f" 🕌 7-aprel Yakshanba Saxarlik-4:53 Iftorlik-19:10\n"
                         f" 🕌 8-aprel Dushanba Saxarlik-4:51 Iftorlik-19:11\n"
                         f" 🕌 9-aprel Seshanba Saxarlik-4:50 Iftorlik-19:12\n")






