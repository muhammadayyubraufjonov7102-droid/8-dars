from aiogram import F,Router
from aiogram.types import Message, CallbackQuery,ReplyKeyboardRemove
from aiogram.fsm.context import FSMContext


user_router=Router()


@user_router.message(F.text=="mahsulotlar")
async def start_mahsulotlar(m:Message):
    await m.answer("siz mahsulotlar ro'yxatini tanladingiz!")
    