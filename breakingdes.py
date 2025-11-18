import base64
from Crypto.Cipher import DES
from Crypto.Util.Padding import unpad
import itertools
import string

# Your encrypted data
encrypted_data = "QPmYtnxcXR7w3LgmlsAUIE6INgvEGts"
print(f"Attempting to decrypt: {encrypted_data}")

# Fix base64 padding
def fix_base64_padding(b64_string):
    # Add padding if needed
    missing_padding = len(b64_string) % 4
    if missing_padding:
        b64_string += '=' * (4 - missing_padding)
    return b64_string

# Try to decode with fixed padding
try:
    fixed_b64 = fix_base64_padding(encrypted_data)
    ciphertext = base64.b64decode(fixed_b64)
    print(f"Successfully decoded {len(ciphertext)} bytes")
except Exception as e:
    print(f"Base64 decode error: {e}")
    # Let's also try decoding as raw bytes
    try:
        ciphertext = bytes.fromhex(encrypted_data)
        print(f"Interpreted as hex, got {len(ciphertext)} bytes")
    except:
        print("Cannot decode as base64 or hex")
        exit()

# Confirm this looks like DES (8 bytes) or AES (16 bytes)
if len(ciphertext) % 8 != 0:
    print(f"Warning: Length {len(ciphertext)} is not a multiple of 8")
else:
    print(f"Ciphertext length: {len(ciphertext)} bytes (likely {'DES' if len(ciphertext) <= 8 else 'DES/AES'})")

def try_decrypt_des(key_candidate):
    """Attempt DES decryption with padding validation"""
    try:
        # Ensure 8-byte key
        key_bytes = key_candidate.encode('utf-8')[:8].ljust(8, b'\x00')
        cipher = DES.new(key_bytes, DES.MODE_ECB)
        decrypted = cipher.decrypt(ciphertext)
        # Try to unpad
        plaintext = unpad(decrypted, DES.block_size)
        # Validate as readable text
        if all(32 <= c <= 126 or c in [10, 13] for c in plaintext):
            return plaintext.decode('utf-8', errors='ignore')
    except Exception as e:
        pass
    return None

# Method 1: Check for ECB pattern (duplicate blocks)
def analyze_ecb_pattern():
    print("Analyzing for ECB pattern...")
    block_size = 8  # DES block size
    blocks = [ciphertext[i:i+block_size] for i in range(0, len(ciphertext), block_size)]
    unique_blocks = set(blocks)
    
    print(f"Blocks: {len(blocks)}, Unique: {len(unique_blocks)}")
    if len(unique_blocks) < len(blocks):
        print("Duplicate blocks detected - confirms ECB mode")
        return True
    return False

# Method 2: Dictionary attack with common keys
def dictionary_attack():
    print("Trying dictionary attack...")
    # Common short keys/passwords
    common_keys = [
        "password", "123456", "admin", "root", "guest", "default",
        "qwerty", "abc123", "letmein", "welcome", "monkey", "dragon",
        "1234", "12345", "123456", "1234567", "12345678",
        "PASSWORD", "ADMIN", "ROOT", "GUEST",
        # Default keys sometimes used in implementations
        "01234567", "abcdefgh", "DEADBEEF", "CAFEBABE"
    ]
    
    for i, key in enumerate(common_keys):
        if i % 10 == 0:
            print(f"Tried {i}/{len(common_keys)} keys...")
            
        result = try_decrypt_des(key)
        if result and len(result.strip()) > 0:
            print(f"SUCCESS! Key: '{key}'")
            print(f"Plaintext: {result}")
            return key, result
    return None, None

# Method 3: Brute force very short keys
def brute_force_short():
    print("Brute forcing short keys...")
    charset = string.ascii_lowercase + string.digits
    
    # Try 1-6 character keys
    for length in range(1, 7):
        print(f"Trying {length}-character keys...")
        total = len(charset) ** length
        count = 0
        
        for attempt in itertools.product(charset, repeat=length):
            count += 1
            if count % 10000 == 0:
                print(f"  Progress: {count}/{total} ({100*count/total:.1f}%)")
                
            key = ''.join(attempt)
            result = try_decrypt_des(key)
            if result and len(result.strip()) > 0:
                # Additional validation to filter false positives
                if any(word in result.lower() for word in 
                      ['the', 'and', 'for', 'are', 'but', 'not', 'you', 'all', 'can', 'had', 'her', 'was', 'one', 'our', 'out', 'day', 'get', 'has', 'him', 'his', 'how', 'its', 'may', 'new', 'now', 'old', 'see', 'two', 'who', 'boy', 'did', 'man', 'men', 'put', 'too', 'use']):
                    print(f"\nLIKELY MATCH! Key: '{key}'")
                    print(f"Plaintext: {result}")
                    return key, result
    return None, None

# Execute the attack
print("=== ECB DES BREAKER (AUTHORIZED PENETRATION TEST) ===")

# Analyze ECB pattern
analyze_ecb_pattern()

# Try dictionary attack first
print("\n[1] Dictionary attack...")
key, plaintext = dictionary_attack()

if not key:
    print("\n[2] Brute force short keys...")
    key, plaintext = brute_force_short()

if not key:
    print("\nNo simple keys found.")
    print("\nConsider:")
    print("- A longer or more complex key")
    print("- Different encryption algorithm")
    print("- Using specialized tools like hashcat")
    print("- Creating a targeted wordlist")
else:
    print("\n=== DECRYPTION SUCCESSFUL ===")
    print(f"Found key: {key}")
    print(f"Decrypted text: {plaintext}")

# Show first few bytes as hex for manual inspection
print(f"\nRaw ciphertext (first 32 bytes): {ciphertext[:32].hex()}")