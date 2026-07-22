import random

def get_numbers_ticket(min, max, quantity):
    if min < 1 or max > 1000 or quantity > (max - min + 1):
        return []

    lottery_numbers = set()
    while len(lottery_numbers) < quantity:
        number = random.randint(min, max)
        lottery_numbers.add(number)

    return sorted(lottery_numbers)
