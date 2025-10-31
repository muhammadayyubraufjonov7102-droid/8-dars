from aiogram.types import (
    KeyboardButton, ReplyKeyboardMarkup,
    InlineKeyboardButton, InlineKeyboardMarkup)


from database import get_category




GENDER_BUTTON=InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text="👨 Male", callback_data="menu_gender_male")],
        [InlineKeyboardButton(text="👩 Female", callback_data="menu_gender_female")],
        [InlineKeyboardButton(text="🧒 Child", callback_data="menu_gender_child")],
        [InlineKeyboardButton(text="🔙 Cancel ", callback_data="menu_gender_back")]
    ]
)


def category_button():
    inline_keyboard=[]
    button=[]
    data=get_category()
    
    for i in range(1,len(data)+1):
        button.append(InlineKeyboardButton(text=data[i-1][1], callback_data=f"category_{data[i-1][0]}"))
        if i%2==0:
            inline_keyboard.append(button)
            button=[]
            
    if button:
        inline_keyboard.append(button)
    inline_keyboard.append([InlineKeyboardButton(text="🔙 Back", callback_data="cat_back")])
    
    return InlineKeyboardMarkup(
        inline_keyboard=inline_keyboard
    )  
        

SEASON_BUTTONS = InlineKeyboardMarkup(inline_keyboard=[
    
    [ InlineKeyboardButton(text="🌦️ All", callback_data="season_all")
    ],
    [
        InlineKeyboardButton(text="☀️ Yozgi", callback_data="season_summer"),
        InlineKeyboardButton(text="🍂 Kuzgi", callback_data="season_autumn")
    ],
    
    [
        InlineKeyboardButton(text="❄️ Qishki", callback_data="season_winter"),
        InlineKeyboardButton(text="🌸 Bahorgi", callback_data="season_spring")],
    
       
    [ InlineKeyboardButton(text="🔙 Back", callback_data="season_back")
    ]
])