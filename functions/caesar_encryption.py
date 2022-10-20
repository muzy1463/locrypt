def caesar_cipher(direction=1, message="", step=3, controller=None) -> str:
    """A function to encrypt a message with Caesar Encryption Method."""
    key = {}
    message = message.lower()
    character_codes = []

    if step is None:
        step = 3

    if direction == 1:
        character_codes = [chr(ord(i)+step) for i in message]
        for i in range(0, len(character_codes)):
            key[character_codes[i]] = message[i]

        controller.key = key

        return ''.join(chr(ord(i) + step) for i in message)

    elif direction == -1:
        x = [chr(ord(i) - step) for i in message]
        for i in range(0, len(character_codes)):
            key[character_codes[i]] = x[i]
        controller.key = key
        return "".join(x)

    else:
        raise ValueError("The direction should be either 1, for encryption, or -1 , for decryption.")
