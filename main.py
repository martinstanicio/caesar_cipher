from string import ascii_lowercase, ascii_uppercase

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
    message = input("message to cipher:\n> ")
    print()

    if not len(message):
        print("message cannot be empty")
        exit()

    try:
        shift = int(
            input(f"cipher shift (defaults to {DEFAULT_SHIFT}):\n> ") or DEFAULT_SHIFT
        )
        print()
    except ValueError:
        print()
        print("shift must be an integer")
        exit()

    ciphered_message = caesar_cipher(message, shift)

    print(f"{ciphered_message =}")
