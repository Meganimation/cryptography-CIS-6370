def get_primative_num(num):
    for i in range(2, num):
        seen = set()
        for j in range(1, num):
            val = pow(i, j, num)
            if val in seen:
                break
            seen.add(val)
        if len(seen) == num - 1:
            return i
    return None

print(get_primative_num(11)) 
