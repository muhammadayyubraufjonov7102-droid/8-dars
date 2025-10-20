@dp.message(Register.address) 
async def get_address(m:Message, state:FSMContext, call:CallbackQuery):
    if m.location:
       
        lon=m.location.longitude
        lat=m.location.latitude
        await m.answer(REGISTER_SUCCESS_TEXT,reply_markup=START_BUTONS)
    else:
        await m.answer("Iltimos qaytadan yuboring:")