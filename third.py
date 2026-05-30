import re

def normalize_phone(phone_number):

    cleaned = re.sub(r'[^\d+]', '', phone_number)

    if cleaned.startswith('+380'):

        return cleaned
    
    elif cleaned.startswith('380'):

        return '+' + cleaned
    
    else:
        if cleaned.startswith('+'):
            cleaned = cleaned[1:]
        return '+38' + cleaned