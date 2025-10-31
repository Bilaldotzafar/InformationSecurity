# ===============================================================
# MULTIPLICATIVE CIPHER - ENCRYPTION & DECRYPTION
# ===============================================================
# This cipher multiplies each letter's position by a key number
# Only works with keys that are coprime with 26 (share no common factors)
# Valid keys: 1, 3, 5, 7, 9, 11, 15, 17, 19, 21, 23, 25
# ===============================================================

def mod_inverse(a, m):
    """
    Find multiplicative inverse of 'a' under modulo 'm'.
    
    The multiplicative inverse is a number 'x' such that:
    (a * x) % m = 1
    
    Example: For a=7 and m=26, the inverse is 15 because:
    (7 * 15) % 26 = 105 % 26 = 1
    
    Args:
        a: The number to find the inverse of
        m: The modulo value (26 for alphabet)
    
    Returns:
        The multiplicative inverse, or None if it doesn't exist
    """
    # Try all possible values from 1 to m-1
    for x in range(1, m):
        # Check if this value is the multiplicative inverse
        if (a * x) % m == 1:
            return x  # Found it! Return the inverse
    
    # No inverse exists (happens when a and m share common factors)
    return None


def encrypt(plaintext, key):
    """
    Encrypt plaintext using multiplicative cipher.
    
    Formula: C = (P * key) % 26
    Where P is the position of the letter (A=0, B=1, ..., Z=25)
    
    Args:
        plaintext: The message to encrypt
        key: The multiplication key (must be coprime with 26)
    
    Returns:
        Encrypted message in uppercase
    """
    ciphertext = ""  # Empty string to store encrypted message
    
    # Process each character in the message
    for char in plaintext.upper():  # Convert to uppercase first
        
        # Check if character is a letter (A-Z)
        if char.isalpha():
            # Step 1: Convert letter to number (A=0, B=1, ..., Z=25)
            p = ord(char) - 65  # ord('A') = 65, so A becomes 0
            
            # Step 2: Apply encryption formula: multiply by key and mod 26
            c = (p * key) % 26
            
            # Step 3: Convert number back to letter and add to ciphertext
            ciphertext += chr(c + 65)  # Add 65 to get back to ASCII range
        
        else:
            # If not a letter (space, punctuation), keep it unchanged
            ciphertext += char
    
    return ciphertext


def decrypt(ciphertext, key):
    """
    Decrypt ciphertext using multiplicative cipher.
    
    Formula: P = (C * inv_key) % 26
    Where inv_key is the multiplicative inverse of the key
    
    Args:
        ciphertext: The encrypted message
        key: The original encryption key
    
    Returns:
        Decrypted original message
    """
    # Step 1: Find the multiplicative inverse of the key
    inv_key = mod_inverse(key, 26)
    
    # Step 2: Check if inverse exists
    if inv_key is None:
        raise ValueError("No multiplicative inverse exists for this key!")
    
    plaintext = ""  # Empty string to store decrypted message
    
    # Process each character in the encrypted message
    for char in ciphertext.upper():
        
        # Check if character is a letter
        if char.isalpha():
            # Step 1: Convert letter to number (0-25)
            c = ord(char) - 65
            
            # Step 2: Apply decryption formula: multiply by inverse key
            p = (c * inv_key) % 26
            
            # Step 3: Convert number back to letter
            plaintext += chr(p + 65)
        
        else:
            # Keep non-letters unchanged
            plaintext += char
    
    return plaintext


def brute_force_attack(ciphertext):
    """
    Demonstrate brute force attack by trying all possible keys.
    
    Since there are only 12 valid keys, an attacker can easily
    try all of them and find which one produces readable text.
    
    Args:
        ciphertext: The encrypted message to crack
    """
    # Create list of all valid keys (those that have a multiplicative inverse)
    # List comprehension: includes k only if mod_inverse(k, 26) exists
    possible_keys = [k for k in range(1, 26) if mod_inverse(k, 26)]
    
    print("\n🔍 Brute Force Attack Results:")
    print("=" * 60)
    
    # Try decrypting with each possible key
    for k in possible_keys:
        try:
            # Decrypt with this key and display result
            decrypted = decrypt(ciphertext, k)
            print(f"Key={k:2d} → {decrypted}")
        except:
            # If any error occurs, skip this key
            pass
    
    print("=" * 60)
    print("👆 One of these is the original message!")


# ===============================================================
# MAIN PROGRAM - Run encryption, decryption, and attack demo
# ===============================================================
if __name__ == "__main__":
    
    # Get message from user
    message = input("Enter plaintext message: ")
    
    # Set the encryption key (must be coprime with 26)
    key = 7
    print(f"\nUsing key: {key}")
    print("=" * 60)
    
    # STEP 1: ENCRYPT the message
    encrypted = encrypt(message, key)
    print(f"🔒 Encrypted Message: {encrypted}")
    
    # STEP 2: DECRYPT the message (to verify it works)
    decrypted = decrypt(encrypted, key)
    print(f"🔓 Decrypted Message: {decrypted}")
    
    # STEP 3: Show how easy it is to crack with brute force
    brute_force_attack(encrypted)
    
    print("\n⚠️  SECURITY NOTE: This cipher is NOT secure!")
    print("   Only 12 possible keys make it trivial to break.")