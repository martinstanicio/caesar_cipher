from sys import argv


DEFAULT_SHIFT: int = 1
DEFAULT_CHARSETS: list = ["abcdefghijklmnopqrstuvwxyz", "ABCDEFGHIJKLMNOPQRSTUVWXYZ"]


def caesar_cipher(
    chars_to_convert: str,
    shift: int = DEFAULT_SHIFT,
    charsets: list = DEFAULT_CHARSETS,
) -> str:
    if not isinstance(chars_to_convert, str):
        raise TypeError("chars_to_convert must be of type str")

    ciphered: str = ""
    for char in chars_to_convert:
        for charset in charsets:
            if char in charset:
                new_char_index = charset.index(char) + shift
                while new_char_index + 1 > len(charset):
                    new_char_index -= len(charset)
                ciphered += charset[new_char_index]
                break
        else:
            ciphered += char
    return ciphered


if __name__ == "__main__":
    chars_to_convert: str = ""
    shift: int = None
    try:
        _, *to_convert, shift = argv

        for item in to_convert:
            chars_to_convert += f"{item} "
        chars_to_convert.strip()

        shift = int(shift)
    except ValueError:
        if len(argv) != 1:
            print("invalid args, please input manually")
        chars_to_convert = input("str to convert:\n> ")
        shift = int(input(f"key (defaults to {DEFAULT_SHIFT}):\n> ") or DEFAULT_SHIFT)

    print(caesar_cipher(chars_to_convert, shift))
