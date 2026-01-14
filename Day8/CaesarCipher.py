def caesar_cipher():
    alphabet = 'abcdefghijklmnopqrstuvwxyz'

    word = input("Enter a word to encrypt: ").lower()
    shift = int(input("Enter shift number: "))

    encrypted_word = ""

    for letter in word:
        if letter in alphabet:
            current_position = alphabet.index(letter)
            new_position = (current_position + shift) % 26
            encrypted_word += alphabet[new_position]
        else:
            encrypted_word += letter

    print(f"Encrypted word: {encrypted_word}")


caesar_cipher()
