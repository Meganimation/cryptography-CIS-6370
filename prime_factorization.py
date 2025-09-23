#get the prime factors of a number
def get_prime_factors(n):
    i = 2
    factors = []
    while i * i <= n:
        if n % i:
            i += 1
        else:
            n //= i
            factors.append(i)
    if n > 1:
        factors.append(n)
    return factors
print(3**50)
# Example usage:
print(get_prime_factors(48))
print(get_prime_factors(60))