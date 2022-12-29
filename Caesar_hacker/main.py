import string

def main():
    ciphered_txt_msg= input("What's the encrypted message you want to hack:\n > ")
    decrypt(ciphered_txt_msg)

def decrypt(msg):
    msg = msg.lower()
    alphabet= string.ascii_lowercase
    deciphered_txt_msg =""

    for key in range(1,len(alphabet)+1):
        for letter in msg:
            if letter.isalpha():
                shifted_letter= alphabet.find(letter) + key
                if shifted_letter >=26:
                    shifted_letter = shifted_letter % 26
                if shifted_letter <0:
                    shifted_letter += 26
                deciphered_txt_msg += alphabet[shifted_letter]
            else:
                deciphered_txt_msg += letter
        print(f"For a key of {key}, the message is:\n{deciphered_txt_msg.upper()}\n")
        deciphered_txt_msg= ""

main()
