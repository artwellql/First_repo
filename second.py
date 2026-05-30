import random

def get_numbers_ticket(min, max, quantity):
    if min >= 1 and max <= 1000 and min <= max and 1 <= quantity <= (max - min + 1):
        numbers = random.sample(range(min, max + 1), quantity)
        return sorted(numbers)
    else:
        return []