from Crypto.Cipher import AES
from Crypto.Util.Padding import pad
from Crypto.Util.Padding import unpad
from Crypto.Random import get_random_bytes

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

result = aes_encrypt("thisistemp", key)
print("Encrypted:", result)
decrypted = aes_decrypt(result['iv'], result['ciphertext'], key)
print("Decrypted:", decrypted)


# def user_input_encrypt():
#     user_input = input("Enter text to encrypt: ")
#     encrypted = aes_encrypt(user_input, key)
#     print("Encrypted:", encrypted)
#     user_input_decrypt = input("Enter text to decrypt: ")
#     decrypted = aes_decrypt(encrypted['iv'], user_input_decrypt, key)
#     print("Decrypted:", decrypted)



def user_login_decrypt(encrypted_password):
    user_input = input("Enter your password to login: ")
    decrypted = aes_decrypt(encrypted_password['iv'], encrypted_password['ciphertext'], key)
    if user_input == decrypted:
        print("Login successful!")
    else:
        print("Login failed!")
        
def user_create_account_encrypt():
    user_input = input("Create your password: ")
    encrypted = aes_encrypt(user_input, key)
    print("Encrypted:", encrypted)
    user_login_decrypt(encrypted)
    return encrypted
        
user_create_account_encrypt()
