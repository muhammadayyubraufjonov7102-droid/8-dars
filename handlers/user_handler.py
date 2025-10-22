from aiogram import F,Router
from aiogram.types import Message, CallbackQuery,ReplyKeyboardRemove
from aiogram.fsm.context import FSMContext
from aiogram.types.input_file import FSInputFile
from texts import GENDER_TEXT, CATEGORY_TEXT, REGISTERED_TEXT, SEASON_TEXT, select_filter
from buttons import GENDER_BUTTON,REGISTER_SUCCESS_BUTTONS, SEASON_BUTTONS, category_button
from states import MenuOption
from database import get_filter_products, get_category_by_id


user_router=Router()


@user_router.message(F.text=="Menu")
async def start_mahsulotlar(m:Message, st:FSMContext):
    
    # await st.set_state(MenuOption.gender)
    image_path="media/image/main.jpg"
    
    await m.answer(text="menu tanlandi!",reply_markup=ReplyKeyboardRemove())
    await m.answer_photo(photo=FSInputFile(path=image_path), caption=GENDER_TEXT, reply_markup=GENDER_BUTTON, parse_mode="HTML"),
    
    
@user_router.callback_query(F.data.startswith("menu_gender_"))
async def get_gender_router(call:CallbackQuery, st:FSMContext):
    gender=call.data.split("_")[-1]
    
    if gender=='cancel':
        await st.clear()
        await call.message.edit_reply_markup(reply_markup=None)
        await call.m.answer(REGISTERED_TEXT, reply_markup=REGISTER_SUCCESS_BUTTONS)
        await call.answer("Cancel")
    else:
        await st.update_data(gender=gender)
        await st.set_state(MenuOption.category)
        
        await call.message.edit_caption(caption=CATEGORY_TEXT)
        await call.message.edit_reply_markup(reply_markup=category_button())

        
@user_router.callback_query(F.data.startswith("category_"))
async def get_category_menu(call:CallbackQuery, st:FSMContext):
    category=call.data.split("_")[-1] 
    
    
    if category =="back":
        await call.message.edit_caption(caption=GENDER_TEXT,parse_mode="HTML"),
        await call.message.edit_reply_markup(reply_markup=GENDER_BUTTON)
    else:
        await st.update_data(category=category)
        await st.set_state(MenuOption.season),
        
        
        await call.message.edit_caption(text=SEASON_TEXT)
        await call.message.edit_reply_markup(reply_markup=SEASON_BUTTONS)
 
 
@user_router.callback_query(F.data.startswith("season_"))
async def send_product_by_filter(call:CallbackQuery, st:FSMContext):
    season=call.date.split("_")[-1].capitalize()
    
    if season=="Back":
        await call.message.edit_caption(caption=CATEGORY_TEXT)
        await call.message.edit_reply_markup(reply_markup=category_id)
    else:
        data= await st.get_data()
        gender=data.get("gender").capitalize()
        category_id=data.get("category").capitalize()
        await st.clear()
        
        await call.message.edit_reply_markup(reply_markup=None)
        
        category_name=get_category_by_id(category_id)[0]
        
        
        await call.message.answer(text=select_filter(gender,category_name, season)) 
        data=get_filter_products(category_id, season, gender)