def caesar_cipher(text: str, shift: int, alphabet: str) -> str:
    encrypted_text = ""
    alphabet_length = len(alphabet)

    for char in text:
        if char in alphabet:
            original_index = alphabet.index(char)
            new_index = (original_index + shift) % alphabet_length
            encrypted_text += alphabet[new_index]
        else:
            encrypted_text += char

    return encrypted_text
