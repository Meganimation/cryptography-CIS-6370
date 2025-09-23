#this gets the greatest common divisor of two numbers
def euclidean_algorithm(a, b):
    while b:
        a, b = b, a % b
    return a


print(euclidean_algorithm(22, 120))

def extended_euclidean_algorithm(a, b):
    if a == 0:
        print('gcd aquired?', b,0,1)
        return b, 0, 1
    gcd, x1, y1 = extended_euclidean_algorithm(b % a, a)
    print('gcd', gcd, 'x1', x1, 'y1', y1)
    x = y1 - (b // a) * x1
    y = x1
    print('gcd', gcd, 'x', x, 'y', y)
    return gcd, x, y

print(extended_euclidean_algorithm(23, 120))
