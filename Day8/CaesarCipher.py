
def caesar_cipher():
    alphabet = 'abcdefghijklmnopqrstuvwxyz'

    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt: ").lower()
    text = input("Enter your message: ").lower()
    shift = int(input("Enter shift number: "))

    result = ""

    for letter in text:
        if letter in alphabet:
            current_position = alphabet.index(letter)

            if direction == "encode":
                new_position = (current_position + shift) % 26
            elif direction == "decode":
                new_position = (current_position - shift) % 26
            else:
                print("Invalid direction!")
                return

            result += alphabet[new_position]
        else:
            result += letter

    print(f"Result: {result}")


caesar_cipher()