from driver.filters import command2
from pyrogram import filters
from pyrogram.types import ReplyKeyboardMarkup
from driver.decorators import sudo_users_only
from pyrogram.raw import functions, types
from requests import get
from config import BOT_TOKEN, SUDO_USERS
from driver.veez import user, bot
import speedtest
from datetime import datetime
from sys import version_info
from time import time
from driver.veez import user as USER
from info import ASSISTANT_NAME, BOT_USERNAME
from config import (
    ALIVE_IMG,
    OWNER_NAME,
    UPDATES_CHANNEL,
    FORCE_SUBSCRIBE_TEXT,
    SUBSCRIBE,
    SUDO_USERS,
)
from driver.decorators import sudo_users_only
from program import __version__
from driver.filters import command, other_filters
from pyrogram import Client, filters
from pyrogram import __version__ as pyrover
from pytgcalls import (__version__ as pytover)
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, Message, ReplyKeyboardMarkup
import speedtest
ahmedyad = [] 

@bot.on_message(command2(["تنصيب php البوت"]) & ~filters.edited & filters.private)
@sudo_users_only
async def install_php(ay, message):
   await message.reply_text("جاري تنصيب الphp علي البوت")
   
@bot.on_message(command2(["اختبار الحساب المساعد"]) & ~filters.edited & filters.private)
@sudo_users_only
async def test_ass(ay, message):
   await message.reply_text("جاري اختبار الحساب المساعد")
   try:
     msa3d = (await user.get_me())
     bot = (await ay.get_me())
   except Exception as e:
       await message.reply_text(f"خطأ : {e}")
       return
   try:
       await user.send_message(chat_id=bot.username,text="الحساب المساعد يعمل بنجاح ✅")
       ahmedyad.append(message.from_user.id)
   except Exception as e:
       await message.reply_text(f"خطأ : {e}")
       return




@bot.on_message(command(["السورس"]) & ~filters.edited & filters.private)
async def khalid(client: Client, message: Message):
    await message.reply_photo(
        photo="https://telegra.ph/file/c11147b8c614b2b647428.jpg",
        caption=f"""[⌁ 𝚆𝙴𝙻𝙲𝙾𝙼𝙴 𝙼𝚄𝚂𝙸𝙲 ✨](https://t.me/SR_TeleGod)\n\n[⌁ 𝙳𝙴𝚅 𝚂𝙾𝚄𝚁𝙲𝙴✨](https://t.me/BK_ZT)""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "SouRce TeleGod", url=f"https://t.me/sr_TeleGod"), 
                ],[
                    InlineKeyboardButton(
                        "･ Salah Hemdan.", url=f"https://t.me/BK_ZT"),
                ],[
                    InlineKeyboardButton(
                        "اضف البوت لمجموعتك ➕", url=f"https://t.me/Bot_JABWA_Bot?startgroup=true"),
                ],

            ]

        ),

    )




@bot.on_message(command2(["الحساب المساعد يعمل بنجاح ✅"]) & ~filters.edited & filters.private)
async def forward_ass(_, message):
   msa3d = (await user.get_me())
   if message.from_user.id == msa3d.id and ahmedyad[0] in SUDO_USERS:
      await message.forward(ahmedyad[0])
      ahmedyad.remove(ahmedyad[0])

@bot.on_message(command2(["قياس سرعة انترنت السيرفر","قياس سرعة السيرفر"]) & ~filters.edited & filters.private)
@sudo_users_only
async def speed_test(_, message):
    m = await message.reply_text("قايس سرعة السيرفر\nالحالة : جاري البدء")
    try:
        test = speedtest.Speedtest()
        m = await m.edit("قايس سرعة السيرفر\nالحالة : الاتصال بي سيرفر القياس")
        test.get_best_server()
        m = await m.edit("قايس سرعة السيرفر\nالحالة : قياس سرعة التحميل")
        test.download()
        m = await m.edit("قايس سرعة السيرفر\nالحالة : قياس سرعة الرفع")
        test.upload()
        m = await m.edit("قايس سرعة السيرفر\nالحالة : استخاج النتائج")
        test.results.share()
        result = test.results.dict()
        m = await m.edit("قايس سرعة السيرفر\nالحالة : حساب النتائج")
    except Exception as e:
        return await m.edit(f"خطأ : {e}")
    m = await m.edit("قايس سرعة السيرفر\nالحالة : التقاط صورة")

    output = f"""**__نتائج  قياس سرعة السيرفر__**
    
سرعة التحميل : `{result["download"]}`
سرعة الرفع : `{result["upload"]}`
البينج : `{result["ping"]}`
موقع اختبار السرعة : `speedtest.net`

__معلومات سيرفر القياس__
الاسم : `{result['server']['name']}`
الموقع : `{result['server']['country']}, {result['server']['cc']}`
الهوست : `{result['server']['host']}`

__معلومات سيرفر الاتصال__
الايبي : `{result['client']['ip']}`
مقدم الخدمة : `{result['client']['isp']}`
كود الدولة : `{result['client']['country']}`
"""
    m = await m.edit("قايس سرعة السيرفر\nالحالة : ارسال النتائج")
    await message.reply_photo(photo=result["share"], caption=output)
    m = await m.edit("قايس سرعة السيرفر\nالحالة : تم ارسال النتائج")
    await m.delete()
