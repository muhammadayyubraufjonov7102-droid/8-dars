import re

def is_valid_name(full_name: str) -> bool:

   
    full_name = full_name.strip()

   
    pattern = r"^[A-Za-zА-Яа-яЁё‘’ʻ`]+\s+[A-Za-zА-Яа-яЁё‘’ʻ`]+$"

    if not re.match(pattern, full_name):
        return False

    # Har bir so‘z kamida 2 harf bo‘lishi kerak
    parts = full_name.split()
    return all(len(p) >= 2 for p in parts)
