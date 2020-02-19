
# Challenge What is the runtime complexity of this function

def power_r(a, b):
    try:
        _ = int(b) # O(1)
    except ValueError:
        print("Exponent (b) must be and integer") # O(1)
        return
    if b == 0:
        return 1 # O(1)
    elif b > 0: 
        return a * power_r(a, b - 1) # O(n)
    else:
        return 1 / (a * power_r(a, -b - 1)) #O(n)