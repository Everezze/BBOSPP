import string

def main():
    action = input("Do you want to encrypt or decrypt?\n> ").strip().lower()

    while action not in ("e","enc","encrypt","d","dec","decrypt"):
        action =input("Please insert a valid option.\n> ").strip().lower()

    crypto_key= input("Enter a key to use: \n> ").strip()
    while not crypto_key.isdecimal():
        crypto_key = input("Please insert a valid key:\n> ")
    crypto_key = int(crypto_key)
    
    if action in ("enc", "e","encrypt"):
        msg = input("Enter the message to encrypt\n> ")
        encrypt_or_decrypt(msg,crypto_key, encrypt = True)
    else:
        msg = input("Enter the message to decrypt\n> ")
        encrypt_or_decrypt(msg,crypto_key, decrypt = True)

def encrypt_or_decrypt(message,key, encrypt = False, decrypt = False):
    message = message.lower()
    alphabet = string.ascii_lowercase
    cipheredtext_message = ""
    for letter in message:
        if letter.isalpha():
            shifted_letter= alphabet.find(letter) + key if encrypt else alphabet.find(letter) - key

            if shifted_letter >= 26:
                shifted_letter = shifted_letter % 26
            if shifted_letter < 0:
                shifted_letter += 26
            cipheredtext_message += alphabet[shifted_letter]
        else:
            cipheredtext_message += letter
    print(cipheredtext_message.upper())

# def decrypt(message):
    #...

main()
