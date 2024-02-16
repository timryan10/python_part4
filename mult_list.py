n = [2, 3, 4, 5, 2]

def mult_list(n):
    prod = 1
    for x in n:
        prod = prod * x
    return prod
print(mult_list(n))