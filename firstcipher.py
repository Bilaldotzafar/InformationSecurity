
msg = "Bilal Zafar"
shift = 3

def encrypt(text, shift):
    result = ""
    for ch in text:
        if ch.isalpha():  # only letters
            # shift the letter
            new_pos = (ord(ch) - ord('a') + shift) % 26
            result += chr(new_pos + ord('a'))
        else:
            result += ch  # keep space same
    return result

def decrypt(text, shift):
    result = ""
    for ch in text:
        if ch.isalpha():
            new_pos = (ord(ch) - ord('a') - shift) % 26
            result += chr(new_pos + ord('a'))
        else:
            result += ch
    return result



enc = encrypt(msg, shift)
print("Encrypted:", enc)

dec = decrypt(enc, shift)
print("Decrypted:", dec)