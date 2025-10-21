

GENDER_TEXT = (
    "<b>Iltimos, jinsingizni tanlang 👇</b>\n"
    "👨 Erkak\n"
    "👩 Ayol\n"
    "🧒 Bola"
)



CATEGORY_TEXT=""""👕✨ Ajoyib! Jinsingiz tanlandi.
Endi iltimos, quyidagi toifalardan birini tanlang 👇"""

SEASON_TEXT=""""🌤 Ajoyib tanlov!
Endi iltimos, quyidagi mavsumlardan birini tanlang — mahsulotlar shunga qarab moslashtiriladi 👇

🩵 Qaysi mavsum uchun kiyim izlayapsiz?
☀️ Yozgi
🍂 Kuzgi
❄️ Qishki
🌸 Bahorgi"""

def select_filter(gender, category, season):
    return f"""
    "🛍 <b>Sizning tanlovlaringiz:</b>\n\n"
    f"👤 <b>Jins:</b> {gender}\n"
    f"📂 <b>Toifa:</b> {category}\n"
    f"🌤 <b>Mavsum:</b> {season}\n\n"
    "💫 Ajoyib tanlov! Endi quyidagi bosqichni davom ettiring 👇"
)
await message.answer(text, parse_mode="HTML")
"""