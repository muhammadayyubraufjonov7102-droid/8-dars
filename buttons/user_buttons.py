from aiogram.types import (
    KeyboardButton, ReplyKeyboardMarkup,
    InlineKeyboardButton, InlineKeyboardMarkup)

GENDER_BUTTON=InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text="👨 Male", callback_data="menu_gender_male")],
        [InlineKeyboardButton(text="👩 Female", callback_data="menu_gender_female")],
        [InlineKeyboardButton(text="🧒 Child", callback_data="menu_gender_child")],
        [InlineKeyboardButton(text="🔙 Cancel ", callback_data="menu_gender_back")]
    ]
)

CATEGORY_BUTTONS=InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton(text="👕 Shirt", callback_data="cat_shirt"),
        InlineKeyboardButton(text="👟 Shoes", callback_data="cat_shoes"),
        InlineKeyboardButton(text="🧢 Cap", callback_data="cat_cap"),
    ],
    [
        InlineKeyboardButton(text="🧥 Jacket", callback_data="cat_jacket"),
        InlineKeyboardButton(text="👖 Trousers", callback_data="cat_trousers"),
        InlineKeyboardButton(text="🧩 Accessory", callback_data="cat_accessory"),
    ],
    [
        InlineKeyboardButton(text="🤵 Suit", callback_data="cat_suit"),
        InlineKeyboardButton(text="👜 Bag", callback_data="cat_bag"),
        InlineKeyboardButton(text="🔙 Back", callback_data="cat_back"),
    ],
])

SEASON_BUTTONS = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton(text="☀️ Yozgi", callback_data="season_summer"),
        InlineKeyboardButton(text="🍂 Kuzgi", callback_data="season_autumn")
    ],
    [
        InlineKeyboardButton(text="❄️ Qishki", callback_data="season_winter"),
        InlineKeyboardButton(text="🌸 Bahorgi", callback_data="season_spring"),
        InlineKeyboardButton(text="🔙 Back", callback_data="season_back")
    ]
])