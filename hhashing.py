# Example usage
input_string = "Hello, World!"
hash_result = md5_hash(input_string)
import hashlib

def md5_hash(input_string):
    # Create an MD5 hash object
    md5 = hashlib.md5()

    # Update the hash object with the input string
    md5.update(input_string.encode('utf-8'))

    # Get the hexadecimal representation of the hash
    hash_value = md5.hexdigest()

    return hash_value

print(f"Input: {input_string}")
print(f"MD5 Hash: {hash_result}")