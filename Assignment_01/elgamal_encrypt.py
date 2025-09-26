from Crypto.Random import random
from Crypto.Util.number import getPrime, inverse

# ElGamal key generation
def elgamal_keygen(bits=256):
    p = getPrime(bits)
    g = random.randint(2, p - 2)
    x = random.randint(2, p - 2)  # Private key
    y = pow(g, x, p)              # Public key
    return {'p': p, 'g': g, 'x': x, 'y': y}

# ElGamal encryption
def elgamal_encrypt(m, public_key):
    p, g, y = public_key['p'], public_key['g'], public_key['y']
    k = random.randint(2, p - 2)
    a = pow(g, k, p)
    b = (m * pow(y, k, p)) % p
    return {'a': a, 'b': b}

# ElGamal decryption
def elgamal_decrypt(ciphertext, private_key, public_key):
    p, x = public_key['p'], private_key['x']
    a, b = ciphertext['a'], ciphertext['b']
    s = pow(a, x, p)
    m = (b * inverse(s, p)) % p
    return m

# Example usage:
if __name__ == "__main__":
    # Key generation
    keys = elgamal_keygen(256)
    public_key = {'p': keys['p'], 'g': keys['g'], 'y': keys['y']}
    private_key = {'x': keys['x']}

    # Message to encrypt (as integer)
    message = 12345
    print("Original message:", message)

    # Encrypt
    ciphertext = elgamal_encrypt(message, public_key)
    print("Ciphertext:", ciphertext)

    # Decrypt
    decrypted = elgamal_decrypt(ciphertext, private_key, public_key)
    print("Decrypted message:", decrypted)
