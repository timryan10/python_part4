n = [37, 25, 60]

def num_within(n):
    true = "true"
    false = "false"
    if n[0] < n[1]:
        return false
    if n[0] > n[2]:
        return false
    else:
        return true
print(num_within(n)) 

