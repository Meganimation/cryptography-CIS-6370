def linear_congruential_generator(seed, a, c, m):
    while True:
        seed = ((a * seed) + c) % m
        yield seed
# Example usage:
# seed = 3
# a = 4
# c = 1
# m = 7
print("First 10 values from the Linear Congruential Generator:")
lcg = linear_congruential_generator(3, 4, 1, 7)
for _ in range(10):
    print(next(lcg))
