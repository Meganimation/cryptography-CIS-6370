def fermat_little_theorem(a, p):
    # a^(p-1) ≡ 1 (mod p) for a prime p
    if p <= 1:
        return False
    return pow(a, p - 1, p) == 1