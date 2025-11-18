

# ============================================================================
# 1. CAESAR CIPHER (Shift Cipher)
# ============================================================================
# Libraries needed: None (uses built-in Python functions)
# Description: Shifts each letter by a fixed number of positions in the alphabet

def caesar_encrypt(text, shift):
    """Encrypt text using Caesar cipher"""
    result = ""
    for ch in text:
        if ch.isalpha():  # only letters
            # Handle both uppercase and lowercase
            base = ord('A') if ch.isupper() else ord('a')
            new_pos = (ord(ch) - base + shift) % 26
            result += chr(new_pos + base)
        else:
            result += ch  # keep non-alphabetic characters same
    return result

def caesar_decrypt(text, shift):
    """Decrypt text using Caesar cipher"""
    result = ""
    for ch in text:
        if ch.isalpha():
            base = ord('A') if ch.isupper() else ord('a')
            new_pos = (ord(ch) - base - shift) % 26
            result += chr(new_pos + base)
        else:
            result += ch
    return result

# Example usage for Caesar Cipher
print("=" * 60)
print("CAESAR CIPHER EXAMPLE")
print("=" * 60)
msg = "Hello Pakistan"
shift = 3
enc = caesar_encrypt(msg, shift)
print(f"Original: {msg}")
print(f"Encrypted: {enc}")
dec = caesar_decrypt(enc, shift)
print(f"Decrypted: {dec}")
print()


# ============================================================================
# 2. VIGENÈRE CIPHER
# ============================================================================
# Libraries needed: None (uses built-in Python functions)
# Description: Uses a keyword to shift letters by different amounts

def vigenere_encrypt(text, key):
    """Encrypt text using Vigenère cipher"""
    result = ""
    key = key.lower()
    klen = len(key)
    key_index = 0  # Track position in key (skip non-alphabetic chars)
    
    for ch in text:
        if ch.isalpha():
            base = ord('A') if ch.isupper() else ord('a')
            shift = ord(key[key_index % klen]) - ord('a')
            new_pos = (ord(ch) - base + shift) % 26
            result += chr(new_pos + base)
            key_index += 1
        else:
            result += ch
    return result

def vigenere_decrypt(text, key):
    """Decrypt text using Vigenère cipher"""
    result = ""
    key = key.lower()
    klen = len(key)
    key_index = 0
    
    for ch in text:
        if ch.isalpha():
            base = ord('A') if ch.isupper() else ord('a')
            shift = ord(key[key_index % klen]) - ord('a')
            new_pos = (ord(ch) - base - shift) % 26
            result += chr(new_pos + base)
            key_index += 1
        else:
            result += ch
    return result

# Example usage for Vigenère Cipher
print("=" * 60)
print("VIGENÈRE CIPHER EXAMPLE")
print("=" * 60)
msg = "Hello Pakistan"
key = "key"
enc = vigenere_encrypt(msg, key)
print(f"Original: {msg}")
print(f"Key: {key}")
print(f"Encrypted: {enc}")
dec = vigenere_decrypt(enc, key)
print(f"Decrypted: {dec}")
print()


# ============================================================================
# 3. TRANSPOSITION CIPHER (Simple Reversal)
# ============================================================================
# Libraries needed: None (uses built-in Python functions)
# Description: Reverses the order of characters in the message

def transposition_encrypt(text):
    """Encrypt text by reversing it"""
    return text[::-1]

def transposition_decrypt(text):
    """Decrypt text by reversing it again"""
    return text[::-1]

# Example usage for Transposition Cipher
print("=" * 60)
print("TRANSPOSITION CIPHER EXAMPLE")
print("=" * 60)
msg = "Hello Pakistan"
enc = transposition_encrypt(msg)
print(f"Original: {msg}")
print(f"Encrypted: {enc}")
dec = transposition_decrypt(enc)
print(f"Decrypted: {dec}")
print()


# ============================================================================
# 4. ONE-TIME PAD (OTP) - Version 1 (Numeric Key)
# ============================================================================
# Libraries needed: random (built-in)
# Description: Uses a random key of numbers for XOR encryption (most secure when used correctly)

import random

def otp_generate_key(length):
    """Generate a random key for OTP cipher"""
    return [random.randint(0, 255) for _ in range(length)]

def otp_encrypt(text, key):
    """Encrypt text using OTP with numeric key"""
    cipher = []
    for i, ch in enumerate(text):
        cipher_num = ord(ch) ^ key[i]  # XOR operation
        cipher.append(cipher_num)
    return cipher  # returns list of numbers

def otp_decrypt(cipher, key):
    """Decrypt OTP cipher text"""
    result = ""
    for i, num in enumerate(cipher):
        ch = chr(num ^ key[i])  # XOR again to decrypt
        result += ch
    return result

# Example usage for OTP (Version 1)
print("=" * 60)
print("ONE-TIME PAD (OTP) - NUMERIC KEY EXAMPLE")
print("=" * 60)
msg = "Hello"
key = otp_generate_key(len(msg))
print(f"Original: {msg}")
print(f"Key: {key}")
enc = otp_encrypt(msg, key)
print(f"Encrypted (numbers): {enc}")
dec = otp_decrypt(enc, key)
print(f"Decrypted: {dec}")
print()


# ============================================================================
# 5. ONE-TIME PAD (OTP) - Version 2 (String Key - Interactive)
# ============================================================================
# Libraries needed: None (uses built-in Python functions)
# Description: Uses a string key of same length for XOR encryption

def otp_string_encrypt(message, key):
    """Encrypt message using string-based OTP"""
    if len(message) != len(key):
        raise ValueError("Message and key must be the same length!")
    
    cipher_text = ""
    for i in range(len(message)):
        m_char = message[i]
        k_char = key[i]
        c_char = chr(ord(m_char) ^ ord(k_char))
        cipher_text += c_char
    return cipher_text

def otp_string_decrypt(cipher_text, key):
    """Decrypt OTP cipher text with string key"""
    if len(cipher_text) != len(key):
        raise ValueError("Cipher text and key must be the same length!")
    
    decrypted_text = ""
    for i in range(len(cipher_text)):
        c_char = cipher_text[i]
        k_char = key[i]
        d_char = chr(ord(c_char) ^ ord(k_char))
        decrypted_text += d_char
    return decrypted_text

# Example usage for OTP (Version 2)
print("=" * 60)
print("ONE-TIME PAD (OTP) - STRING KEY EXAMPLE")
print("=" * 60)
message = "HELLO"
key = "abcde"
print(f"Original: {message}")
print(f"Key: {key}")
enc = otp_string_encrypt(message, key)
print(f"Encrypted: {repr(enc)}")  # Using repr to show special characters
dec = otp_string_decrypt(enc, key)
print(f"Decrypted: {dec}")
print()


# ============================================================================
# 6. FERNET ENCRYPTION (Symmetric Encryption)
# ============================================================================
# Libraries needed: cryptography (install with: pip install cryptography)
# Description: Modern symmetric encryption using Fernet (based on AES)

try:
    from cryptography.fernet import Fernet

    def fernet_demo():
        """Demonstrate Fernet encryption"""
        # Generate a secret key
        key = Fernet.generate_key()
        print(f"Generated Key: {key}")
        
        # Create a Fernet objecth
        cipher_suite = Fernet(key)
        
        # Define the message
        message = "Hello, World we are here to learn IS!".encode()
        
        # Encrypt the message
        encrypted_message = cipher_suite.encrypt(message)
        print(f"Encrypted Message: {encrypted_message}")
        
        # Decrypt the message
        decrypted_message = cipher_suite.decrypt(encrypted_message)
        print(f"Decrypted Message: {decrypted_message.decode()}")

    # Example usage for Fernet
    print("=" * 60)
    print("FERNET ENCRYPTION EXAMPLE")
    print("=" * 60)
    fernet_demo()
    print()

except ImportError:
    print("=" * 60)
    print("FERNET ENCRYPTION - LIBRARY NOT INSTALLED")
    print("=" * 60)
    print("To use Fernet encryption, install: pip install cryptography")
    print()


# ============================================================================
# 7. MD5 HASH
# ============================================================================
# Libraries needed: hashlib (built-in)
# Description: Creates a 128-bit hash value (NOT recommended for security - use SHA-256 instead)

import hashlib

def md5_hash(input_string):
    """Create MD5 hash of input string"""
    md5 = hashlib.md5()
    md5.update(input_string.encode('utf-8'))
    hash_value = md5.hexdigest()
    return hash_value

# Example usage for MD5
print("=" * 60)
print("MD5 HASH EXAMPLE")
print("=" * 60)
input_string = "Hello, World!"
hash_result = md5_hash(input_string)
print(f"Input: {input_string}")
print(f"MD5 Hash: {hash_result}")
print("Note: MD5 is deprecated for security purposes. Use SHA-256 instead.")
print()


# ============================================================================
# 8. SHA-256 HASH
# ============================================================================
# Libraries needed: hashlib (built-in)
# Description: Creates a 256-bit hash value (recommended for security)

def sha256_hash(input_string):
    """Create SHA-256 hash of input string"""
    sha256 = hashlib.sha256()
    sha256.update(input_string.encode('utf-8'))
    hash_value = sha256.hexdigest()
    return hash_value

# Example usage for SHA-256
print("=" * 60)
print("SHA-256 HASH EXAMPLE")
print("=" * 60)
input_string = "Hello, World!"
hash_result = sha256_hash(input_string)
print(f"Input: {input_string}")
print(f"SHA-256 Hash: {hash_result}")
print()


# ============================================================================
# 9. HMAC (Hash-based Message Authentication Code)
# ============================================================================
# Libraries needed: hmac, hashlib (both built-in)
# Description: Creates a hash with a secret key for message authentication

import hmac

def create_hmac(key, message):
    """Create HMAC digest for message authentication"""
    hmac_object = hmac.new(key, message, hashlib.sha256)
    digest = hmac_object.hexdigest()
    return digest

# Example usage for HMAC
print("=" * 60)
print("HMAC EXAMPLE")
print("=" * 60)
key = b"my_secret_key"
message = b"Hello, World!"
digest = create_hmac(key, message)
print(f"Key: {key}")
print(f"Message: {message}")
print(f"HMAC Digest: {digest}")
print()


# ============================================================================
# SUMMARY
# ============================================================================
print("=" * 60)
print("SUMMARY OF AVAILABLE CIPHERS")
print("=" * 60)
print("""
1. Caesar Cipher - Simple letter shift cipher
2. Vigenère Cipher - Polyalphabetic substitution cipher
3. Transposition Cipher - Reverses message order
4. One-Time Pad (Numeric) - XOR with random numbers
5. One-Time Pad (String) - XOR with string key
6. Fernet - Modern symmetric encryption (requires: pip install cryptography)
7. MD5 Hash - Creates hash (deprecated for security)
8. SHA-256 Hash - Secure hashing algorithm
9. HMAC - Message authentication with secret key

Note: All examples above run automatically when you execute this file.
You can also import and use individual functions in your own code.
""")
