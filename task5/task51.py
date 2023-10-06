import random

def generate_random_string(length):
    random_string = ""
    for _ in range(length):
        random_char = chr(random.randint(0x0000, 0xFFFF))
        random_string += random_char
    return random_string

random_string = generate_random_string(1000)

with open("random_string.txt", "w", encoding="utf-8", errors='ignore') as file:
    file.write(random_string)