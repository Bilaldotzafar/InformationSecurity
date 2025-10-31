
def mod_inverse(a, m):
    for i in range(1, m):
        if (a * i) % m == 1:
            return i
    return None

def encrypt(text, a, b):
    result = ""
    for char in text:
        if char.isalpha():
            if char.isupper():
                x = ord(char) - ord('A')
                encrypted = (a * x + b) % 26
                result += chr(encrypted + ord('A'))
            else:
                x = ord(char) - ord('a')
                encrypted = (a * x + b) % 26
                result += chr(encrypted + ord('a'))
        else:
            result += char
    return result

def decrypt(text, a, b):
    a_inv = mod_inverse(a, 26)
    result = ""
    for char in text:
        if char.isalpha():
            if char.isupper():
                y = ord(char) - ord('A')
                decrypted = (a_inv * (y - b)) % 26
                result += chr(decrypted + ord('A'))
            else:
                y = ord(char) - ord('a')
                decrypted = (a_inv * (y - b)) % 26
                result += chr(decrypted + ord('a'))
        else:
            result += char
    return result


a = 5  
b = 8
plaintext = "Hello"

encrypted = encrypt(plaintext, a, b)
print(f"Plaintext: {plaintext}")
print(f"Encrypted: {encrypted}")

decrypted = decrypt(encrypted, a, b)
print(f"Decrypted: {decrypted}")