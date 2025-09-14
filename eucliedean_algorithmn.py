#this gets the greatest common divisor of two numbers
def euclidean_algorithm(a, b):
    while b:
        a, b = b, a % b
    return a

print(euclidean_algorithm(3**52, 11))

def extended_euclidean_algorithm(a, b):
    if a == 0:
        return b, 0, 1
    gcd, x1, y1 = extended_euclidean_algorithm(b % a, a)
    x = y1 - (b // a) * x1
    y = x1
    return gcd, x, y

# #solve 23x ≡ 3 (mod 120)
# print(extended_euclidean_algorithm(23, 120))
