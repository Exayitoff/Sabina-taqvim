

import logging
import datetime

from aiogram import Bot, Dispatcher, executor, types
from tugma import keyboard , ramadan 
from aiogram.types import CallbackQuery

API_TOKEN = "6247711078:AAGM9C93e2ag72gbXuzp1HoGdwoJPs7K09s"

# Configure logging
logging.basicConfig(level=logging.INFO)

# Initialize bot and dispatcher
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(commands=['start', 'help'])
async def send_welcome(message: types.Message):
    """
    This handler will be called when user sends `/start` or `/help` command
    """
    await bot.send_photo(chat_id=message.from_user.id ,photo= "https://avatars.mds.yandex.net/i?id=55eaf45269d26968ed42703415fa047d91c44561-2431862-images-thumbs&n=13&exp=1", caption="Assalomu aleykum,botga xush kelibsiz Ramazon Muborak", reply_markup=keyboard)

@dp.callback_query_handler(lambda c: c.data == "kecha")
async def kecha_taqvim(callback: CallbackQuery):
    x = datetime.datetime.now()
    day = x.strftime("%d")
    last_day = int(day)-1
    for i in ramadan :
        if int(i["kun"]) == last_day:
            await bot.send_photo(chat_id=callback.from_user.id, photo="https://www.google.co.uz/imgres?imgurl=https%3A%2F%2Fiqra.lambeth.sch.uk%2Fwp-content%2Fuploads%2F2021%2F04%2FRamadan-Mubarak.png&tbnid=EnN4fIltjzJtUM&vet=12ahUKEwiVqubK_6P-AhVLzioKHeEkDaMQMygTegUIARDkAQ..i&imgrefurl=https%3A%2F%2Fiqra.lambeth.sch.uk%2F2021%2F04%2Ffun-things-during-ramadan-in-year-1%2F&docid=MrzyuQygyEIF5M&w=2000&h=2000&q=ramadan%20photo&ved=2ahUKEwiVqubK_6P-AhVLzioKHeEkDaMQMygTegUIARDkAQ", caption=f"<b>kechagi taqvim</b>\nSaharlik vaqti : {i['Saharlik']}\nIftorlik vaqti:{i['Iftorlik']}", reply_markup=keyboard,parse_mode="HTML")
    
    
@dp.callback_query_handler(lambda c: c.data == "bugun")
async def kecha_taqvim(callback: CallbackQuery):
    x = datetime.datetime.now()
    day = x.strftime("%d")
    last_day = int(day)
    for i in ramadan :
        if int(i["kun"]) == last_day:
            await bot.send_photo(chat_id=callback.from_user.id, photo="https://www.google.co.uz/imgres?imgurl=https%3A%2F%2Fiqra.lambeth.sch.uk%2Fwp-content%2Fuploads%2F2021%2F04%2FRamadan-Mubarak.png&tbnid=EnN4fIltjzJtUM&vet=12ahUKEwiVqubK_6P-AhVLzioKHeEkDaMQMygTegUIARDkAQ..i&imgrefurl=https%3A%2F%2Fiqra.lambeth.sch.uk%2F2021%2F04%2Ffun-things-during-ramadan-in-year-1%2F&docid=MrzyuQygyEIF5M&w=2000&h=2000&q=ramadan%20photo&ved=2ahUKEwiVqubK_6P-AhVLzioKHeEkDaMQMygTegUIARDkAQ", caption=f"<b>bugungi taqvim</b>\nSaharlik vaqti : {i['Saharlik']}\nIftorlik vaqti:{i['Iftorlik']}", reply_markup=keyboard,parse_mode="HTML")
    
    
@dp.callback_query_handler(lambda c: c.data == "ertaga")
async def kecha_taqvim(callback: CallbackQuery):
    x = datetime.datetime.now()
    day = x.strftime("%d")
    last_day = int(day)+1
    for i in ramadan :
        if int(i["kun"]) == last_day:
            await bot.send_photo(chat_id=callback.from_user.id, photo="https://www.google.co.uz/imgres?imgurl=https%3A%2F%2Fiqra.lambeth.sch.uk%2Fwp-content%2Fuploads%2F2021%2F04%2FRamadan-Mubarak.png&tbnid=EnN4fIltjzJtUM&vet=12ahUKEwiVqubK_6P-AhVLzioKHeEkDaMQMygTegUIARDkAQ..i&imgrefurl=https%3A%2F%2Fiqra.lambeth.sch.uk%2F2021%2F04%2Ffun-things-during-ramadan-in-year-1%2F&docid=MrzyuQygyEIF5M&w=2000&h=2000&q=ramadan%20photo&ved=2ahUKEwiVqubK_6P-AhVLzioKHeEkDaMQMygTegUIARDkAQ", caption=f"<b>ertangi taqvim</b>\nSaharlik vaqti : {i['Saharlik']}\nIftorlik vaqti:{i['Iftorlik']}", reply_markup=keyboard,parse_mode="HTML")
    
    
if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)