import os
from os import getenv
from dotenv import load_dotenv
if os.path.exists("local.env"):
load_dotenv("local.env")
load_dotenv()
admins = {}
SESSION_NAME = getenv("SESSION_NAME","BABylIQXCwniaNCCK9N8Nw9HoX4eXDBoe_aHG_qkKirziipwmRpH_tVvoLHIr1IWashpA8m4hVc4PuskX4kyS9nlUxH0H6TjNv6kjHGPzJkdzNsLr1FVV7S0ANWmW8pa97Kiddfzi1Dj7QRFnVwCoJPkQy1lg6S5ExjiI6pmw5S0gXin-gIIwebG2tiPnx9sdPcIkeMnn9bu2wvizKZ84NfEpgc3hSMCooDXACTJUohA2yl8dh3W4flSV1tvoMyxMM1ddDet2CX2SSc3zNp4mUjy0T1k4ocCxnqei8qizjGu-JvIfPEN5xojZsoeySFpKaYUSAJn9Tvl6fZ-YkObJV-aAAAAAU8ApeoA")
BOT_TOKEN = getenv("BOT_TOKEN","5763646030:AAHFiugGAAQ2GZboD7vtq_Bl5umAefPza_U")
API_ID = int(getenv("API_ID","14195301"))
MONGODB_URL = getenv("MONGODB_URL")
API_HASH = getenv("API_HASH","abaa325214e54b6fc765a085de12a622")
OWNER_NAME = getenv("OWNER_NAME", "BK_Zt")
MONGODB_URL = getenv("MONGODB_URL")
UPDATES_CHANNEL = getenv("UPDATES_CHANNEL", "SR_TeleGod")
ALIVE_IMG = getenv("ALIVE_IMG", "https://telegra.ph/file/4c7636b9c50116387d9f6.jpg")
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "240"))
UPSTREAM_REPO = getenv("UPSTREAM_REPO")
IMG_1 = getenv("IMG_1", "https://telegra.ph/file/d6f92c979ad96b2031cba.png")
IMG_2 = getenv("IMG_2", "https://telegra.ph/file/6213d2673486beca02967.png")
IMG_3 = getenv("IMG_3", "https://telegra.ph/file/f02efde766160d3ff52d6.png")
FORCE_SUBSCRIBE_TEXT = getenv("SUBSCRIBE_TEXT", f"عليك الاشتراك في قناة البوت لتتمكن من استخدامة \n- @{UPDATES_CHANNEL}")
SUBSCRIBE = getenv("SUBSCRIBE", "no")
SUDO_USERS = list(map(int, getenv("SUDO_USERS", "5372193406").split()))
