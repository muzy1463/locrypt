import string
import random


def random_encryption(message):
    message = message.lower()
    message_list = list(set(message.lower()))
    character_codes = []
    characters = string.printable[:-4]
    key = {}

    while len(character_codes) != len(message_list):
        x = random.randint(0, len(characters)-1)
        if characters[x] not in character_codes:
            character_codes.append(characters[x])

    for i in range(0, len(message_list)):
        key[message_list[i]] = character_codes[i]

    output_text = "".join(key[i] for i in message)
    key = {v: k for k, v in key.items()}

    output_dictionary = {"input_text": message,
                         "output_text": output_text,
                         "key": key}

    return output_dictionary
