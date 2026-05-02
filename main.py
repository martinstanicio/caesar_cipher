from string import ascii_lowercase, ascii_uppercase
from sys import argv

DEFAULT_SHIFT = 1
DEFAULT_CHARACTER_SETS = [ascii_lowercase, ascii_uppercase]


def caesar_cipher(
    message: str,
    shift: int = DEFAULT_SHIFT,
    character_sets: list[str] = DEFAULT_CHARACTER_SETS,
) -> str:
    ciphered_message = ""

    for character in message:
        for character_set in character_sets:
            try:
                current_index = character_set.index(character)
            except ValueError:
                continue

            new_index = (current_index + shift) % len(character_set)

            ciphered_message += character_set[new_index]
            break
        else:
            ciphered_message += character

    return ciphered_message


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
