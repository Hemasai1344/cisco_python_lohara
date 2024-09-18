def is_odd(num):
    if num%2:
        return True

def is_even(num):
    if num%2==0:
        return True
import math  
def is_prime(num):
    sqrt_num = int(math.sqrt(num))
    for i in range(2,sqrt_num+1):
        if num%i==0:
            return False
    return True

