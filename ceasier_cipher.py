def caesar_encrypt(plaintext, shift):
   
    encrypted_text = ""
    for char in plaintext:
        if char.isalpha():
            # Shift only alphabetical characters
            base = ord('a') if char.islower() else ord('A')
            shifted_char = chr((ord(char) - base + shift) % 26 + base)
            encrypted_text += shifted_char
        else:
            # Keep non-alphabetical characters unchanged
            encrypted_text += char
    return encrypted_text


def caesar_decrypt(ciphertext, shift):
    """
    Decrypts the given ciphertext using the Caesar Cipher.
    :param ciphertext: The encrypted message (string).
    :param shift: The shift value (integer).
    :return: The decrypted plaintext (string).
    """
    return caesar_encrypt(ciphertext, -shift)  # Decryption is just negative shift


def main():
    try:
        plaintext = input("Enter the message to encrypt: ")
        shift = int(input("Enter the shift value (positive integer): "))

        encrypted_message = caesar_encrypt(plaintext, shift)
        decrypted_message = caesar_decrypt(encrypted_message, shift)

        print(f"\nEncrypted message: {encrypted_message}")
        print(f"Decrypted message: {decrypted_message}")
    except ValueError:
        print("Invalid input. Please enter a valid shift value.")


if __name__ == "__main__":
    main()
