from functions.hash_functions import md5, sha_1, sha_512, sha_256, sha_224, sha3_512, sha3_384, sha_224_3
from functions.random_functions import random_encryption
from functions.caesar_encryption import caesar_cipher

algorithm_list = ["Random", "Caesar", "MD5", "SHA1", "SHA224", "SHA3-224", "SHA256", "SHA3-384",
                  "SHA512", "SHA3-512"]


def encrypt(algorithm, text, caesar_step=None, caesar_direction=1, controller=None):
    if algorithm == algorithm_list[0]:
        output = random_encryption(text)
        controller.key = output["key"]
        return output["output_text"]

    elif algorithm == algorithm_list[1]:
        return caesar_cipher(caesar_direction, text, caesar_step, controller=controller)

    elif algorithm == algorithm_list[2]:
        return md5(text)

    elif algorithm == algorithm_list[3]:
        return sha_1(text)

    elif algorithm == algorithm_list[4]:
        return sha_224(text)

    elif algorithm == algorithm_list[5]:
        return sha_224_3(text)

    elif algorithm == algorithm_list[6]:
        return sha_256(text)

    elif algorithm == algorithm_list[7]:
        return sha3_384(text)

    elif algorithm == algorithm_list[8]:
        return sha_512(text)

    elif algorithm == algorithm_list[9]:
        return sha3_512(text)

    else:
        return None
