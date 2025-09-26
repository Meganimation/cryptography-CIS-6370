from Crypto.Cipher import AES
from Crypto.Util.Padding import pad
from Crypto.Util.Padding import unpad
from Crypto.Random import get_random_bytes
from Crypto.Protocol.KDF import PBKDF2
import os
import base64


key = get_random_bytes(32)  # AES-256

def aes_encrypt(plain_text: str, key: bytes) -> dict:
    cipher = AES.new(key, AES.MODE_CBC)
    ct_bytes = cipher.encrypt(pad(plain_text.encode('utf-8'), AES.block_size))
    iv = base64.b64encode(cipher.iv).decode('utf-8')
    ct = base64.b64encode(ct_bytes).decode('utf-8')
    return {'iv': iv, 'ciphertext': ct}

def aes_decrypt(iv:str, ciphertext:str, key:bytes):
    iv = base64.b64decode(iv)
    ct = base64.b64decode(ciphertext)
    cipher = AES.new(key, AES.MODE_CBC, iv)
    pt = unpad(cipher.decrypt(ct), AES.block_size)
    return pt.decode('utf-8')

# result = aes_encrypt("thisistemp", key)
# print("Encrypted:", result)
# decrypted = aes_decrypt(result['iv'], result['ciphertext'], key)
# print("Decrypted:", decrypted)


# def user_input_encrypt():
#     user_input = input("Enter text to encrypt: ")
#     encrypted = aes_encrypt(user_input, key)
#     print("Encrypted:", encrypted)
#     user_input_decrypt = input("Enter text to decrypt: ")
#     decrypted = aes_decrypt(encrypted['iv'], user_input_decrypt, key)
#     print("Decrypted:", decrypted)

def derive_key_from_password(password: str, salt: bytes) -> bytes:
    # Derive a 256-bit AES key from the password and salt
    return PBKDF2(password, salt, dkLen=32, count=100_000)

def send_encrypted_message():
    message = input("Enter the message you want to encrypt: ")
    password = input("Set a password to protect this message: ")
    salt = os.urandom(16)
    key = derive_key_from_password(password, salt)
    encrypted = aes_encrypt(message, key)
    encrypted['salt'] = base64.b64encode(salt).decode('utf-8')
    print("\nShare these values with the recipient:")
    print(encrypted)
    return encrypted

def receive_and_decrypt_message(iv=None, ciphertext=None, salt=None):
    if not iv:
        iv = input("Enter the IV: ")
    if not ciphertext:
        ciphertext = input("Enter the ciphertext: ")
    if not salt:
        salt = input("Enter the salt: ")
    password = input("Enter the password to decrypt the message: ")
    salt_bytes = base64.b64decode(salt)
    key = derive_key_from_password(password, salt_bytes)
    try:
        decrypted = aes_decrypt(iv, ciphertext, key)
        print("Decrypted message:", decrypted)
    except Exception as e:
        print("Decryption failed!", str(e))

def main():
    print("1. Send an encrypted message")
    print("2. Decrypt a received message")
    print("3. Read a message I left for you! (Use password FAU)")
    choice = input("Choose an option (1, 2, or 3): ")
    if choice == '1':
        send_encrypted_message()
    elif choice == '2':
        receive_and_decrypt_message()
    elif choice == '3':
        # These are the predefined values for the hidden message :)
        iv = "JZhmXSZO2C8GDP8v576y1g=="
        ciphertext = "DMCJmQzzuXTS8ySsMFXN0faLwqPCHfMp/zFAq+gs4U/kCJIZYHLLC1/xuKe7ni+sn2V4cFsaXUX/WtTFIBtoJFWRIBUoWv2B4d+ML8IIbjE="
        salt = "9alj0v3EVR7xZ8xkvgbezw=="
        receive_and_decrypt_message(iv, ciphertext, salt)
    else:
        print("Invalid choice.")

main()
