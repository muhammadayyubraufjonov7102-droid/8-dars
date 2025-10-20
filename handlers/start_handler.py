from aiogram import F,Router
from aiogram.types import Message, CallbackQuery,ReplyKeyboardRemove
from aiogram.filters import CommandStart
from aiogram.fsm.context import FSMContext


from states import Register
from texts import START_TEXT, REGISTER_SUCCESS_TEXT, REGISTERED_TEXT
from buttons import (START_BUTTON, PHONE_BUTTON,
 GENDER_BUTTON, LOCATION_BUTTON, REGISTER_SUCCESS_BUTTONS)
from filters import is_valid_name

from database import is_register_by_id, insert_user


start_router=Router()

@start_router.message(CommandStart())
async def sart_handler(m:Message):
    if is_register_by_id(m.from_user.id):
        await m.answer(REGISTERED_TEXT, reply_markup=REGISTER_SUCCESS_BUTTONS)
    else:
        await m.answer(START_TEXT, reply_markup=START_BUTTON)

@start_router.message(F.text=="Register")
async def register_handler(m:Message, state:FSMContext):
    text="""Ro'yxatdan o'tish uchun Iltimos to'liq ismingizni kiriting\n
    masalan: Ali Valiyev"""
    await state.set_state(Register.name)
    await m.answer( text ,reply_markup=ReplyKeyboardRemove())

@start_router.message(Register.name)
async def get_name(m:Message,state:FSMContext):
    full_name=m.text
    
    if is_valid_name(full_name):
        await state.update_data(name=m.text)
        await state.set_state(Register.phone)

        await m.answer("""Ism qabul qilindi! 📞 Endi iltimos telefon raqamingizni kiriting.\n\n
    'Masalan: +998901234567\n\n':""",
                       reply_markup=PHONE_BUTTON)
    else:
        await m.answer("iltimos, to'liq formatda kiriting!")

@start_router.message(Register.phone)
async def get_phone(m: Message, state:FSMContext):
    
    if m.contact:
        phone=m.contact.phone_number
    else:
        phone=m.text
    await state.update_data(phone=phone)
    await state.set_state(Register.gender)
    await m.answer(f"Telefon raqam{phone} saqlandi!",reply_markup=ReplyKeyboardRemove())
    await m.answer(f" Jins Tanlang:",reply_markup=GENDER_BUTTON)


@start_router.callback_query(F.data.startswith("gender_"))
async def get_gender(call:CallbackQuery, state:FSMContext):

    gender=call.data.split("_")[-1]

    await state.update_data(gender=gender)
    await state.set_state(Register.address)
    await call.answer(f"siz {gender} tanladingiz!")
    await call.message.edit_reply_markup(reply_markup=None)
    await call.message.edit_text(f"siz {gender} tanladingiz! endi address yuboring: ")
    await call.message.answer("address yuboring:", reply_markup=LOCATION_BUTTON)



@start_router.message(Register.address)
async def get_address(m: Message, state: FSMContext):
    print("Keldi:", m)
    print("Location:", m.location)

    if not m.location:
        await m.answer("⚠️ Lokatsiya topilmadi. Iltimos, 📍 tugmasini bosib joylashuvingizni qayta yuboring.")
        return

        
        fullname=data.get("name")
        phone=data.get("phone")
        gender=data.get("gender")
        address= f"lon: {lon}, lat: {lat}"
        if insert_user(fullname, phone, gender, address,m.from_user.id):
            
            await m.answer(REGISTER_SUCCESS_TEXT,reply_markup=REGISTER_SUCCESS_BUTTONS)
        else:
            await m.answer("registratsiyada muammo bor qayta ro'yxatdan o'ting!", reply_markup=ReplyKeyboardRemove())
        
    else:
        await m.answer("Iltimos qaytadan yuboring:")