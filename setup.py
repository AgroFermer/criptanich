import contextlib
import asyncio 
from aiogram.types import ChatJoinRequest, InlineKeyboardButton, InlineKeyboardMarkup
from aiogram import Bot, Dispatcher, F
import logging
from aiogram.utils.markdown import hlink

# Bot 1 configuration
BOT1_TOKEN = '6650193766:AAEwpV6IxUDbd2EM9bt7_YnwW9RQwrtRnnw'
CHANNEL1_ID = -1001517472508
ADMIN1_ID = 430692329

# Bot 2 configuration
BOT2_TOKEN = '6350360716:AAEczkv6PbrUijqGGXRO80S-kQrQUeXngkU'
CHANNEL2_ID = -1001913564875
ADMIN2_ID = 402152266

# Bot 1 logic
async def approve_request_bot1(chat_join: ChatJoinRequest, bot: Bot):
    msg = f"Ваша запит одобрений!\n\nВступити в канал: https://t.me/+4uMnS-VXsvg3M2Yy"
    button = InlineKeyboardButton(text='ВСТУПИТИ', url='https://t.me/+4uMnS-VXsvg3M2Yy', disable_web_page_preview=True)
    markup = InlineKeyboardMarkup(inline_keyboard=[[button]])

    await bot.send_message(chat_id=chat_join.from_user.id, text=msg, reply_markup=markup, disable_web_page_preview=True)

# Bot 2 logic
async def approve_request_bot2(chat_join: ChatJoinRequest, bot: Bot):
    msg = f"Ваша запит одобрений!\n\nВступити в канал: https://t.me/+4uMnS-VXsvg3M2Yy"
    button = InlineKeyboardButton(text='ВСТУПИТИ', url='https://t.me/+4uMnS-VXsvg3M2Yy', disable_web_page_preview=True)
    markup = InlineKeyboardMarkup(inline_keyboard=[[button]])

    await bot.send_message(chat_id=chat_join.from_user.id, text=msg, reply_markup=markup, disable_web_page_preview=True)


async def start():
    logging.basicConfig(level=logging.DEBUG,
                           format="%(asctime)s - [%(levelname)s] - %(name)s -"
                           "(%(filename)s.%(funcName)s(%(lineno)d) - %(message)s"
                        )
    bot1 = Bot(token=BOT1_TOKEN)
    bot2 = Bot(token=BOT2_TOKEN)
    
    dp1 = Dispatcher()
    dp2 = Dispatcher()

    dp1.chat_join_request.register(approve_request_bot1, F.chat.id == CHANNEL1_ID)
    dp2.chat_join_request.register(approve_request_bot2, F.chat.id == CHANNEL2_ID)

    try:
        await asyncio.gather(
            dp1.start_polling(bot1, allowed_updates=dp1.resolve_used_update_types()),
            dp2.start_polling(bot2, allowed_updates=dp2.resolve_used_update_types())
        )
    except Exception as ex:
        logging.error(exc_info=True)
    finally:
        await asyncio.gather(
            bot1.session.close(),
            bot2.session.close()
        )

if __name__ == '__main__':
    with contextlib.suppress(KeyboardInterrupt, SystemExit):
        asyncio.run(start())

  

