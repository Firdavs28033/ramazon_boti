from aiogram import types
from aiogram.dispatcher import filters
from loader import dp

@dp.message_handler(content_types=types.ContentTypes.AUDIO)
async def audio_menu(msg: types.Message):
    await msg.answer("Biz ning botga faqat text yozishingiz mumkin")

@dp.message_handler(content_types=types.ContentTypes.DOCUMENT)
async def document_menu(msg: types.Message):
    await msg.answer("Document tashlamang !")

@dp.message_handler(content_types=types.ContentTypes.PHOTO)
async def photo_menu(msg: types.Message):
    await msg.answer("Rasm tashlamang foydalanuvchi")

@dp.message_handler(content_types=types.ContentTypes.STICKER)
async def sticer_menu(msg: types.Message):
    await msg.answer("❌ NOT Sticer")

