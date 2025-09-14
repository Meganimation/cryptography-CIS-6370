def aes_encrypt(plain_text):
    from Crypto.Cipher import AES
    from Crypto.Util.Padding import pad
    from Crypto.Random import get_random_bytes
    import base64

    key = get_random_bytes(32)  # AES-256
    cipher = AES.new(key, AES.MODE_CBC)
    ct_bytes = cipher.encrypt(pad(plain_text.encode('utf-8'), AES.block_size))
    iv = base64.b64encode(cipher.iv).decode('utf-8')
    ct = base64.b64encode(ct_bytes).decode('utf-8')
    return {'iv': iv, 'ciphertext': ct, 'key': base64.b64encode(key).decode('utf-8')}