"""
def find_diff(first: int = 1, second: int = 2) -> int:
    return first - second

print(find_diff(20, 10))          # Output: 10
print(find_diff(second=10, first=20))  # Output: 10
print(find_diff(second=10))       # Output: -9 (since first defaults to 1)
print(find_diff())                # Output: -1 (since first defaults to 1 and second defaults to 2)
"""

"""
def change_name(names, index, name): #hema sai , 1, hemasai
    names[index] = name #hema sai[1] = hemasai so sai=)hemasai

names = ["Hema","Sai"]
print(names)
change_name(names,1,'Hemasai')
print(names)
"""

#list is the iteratable using list iterator

"""
def find_sum(first, second, *others):
    s = first+second
    if(len(others)>0):
        for i in others:
            s+=i
        #end for
    #end if
    #print(type(others)) #tuple
    return s
print(find_sum(10,20))
print(find_sum(10,20,30,40))
print(find_sum(10,20,30,40,50))
"""

"""
def find_sum(first, second, **others):
    s = first+second
    if(len(others)>0):
        for i in others:
            s+=i
        #end for
    #end if
    #print(type(others)) #dict
    return s
print(find_sum(first=10,second=20))
print(find_sum(first=10,second=20,third=30))
print(find_sum(first=10,second=20,third=30,fourth=40,fifth=50))
"""

#factorial using recursion
"""
def factorial(num):
    if num<0:
        return "Factorial is not applicable for negative numbers"
    elif num==0 or num==1:
        return 1
    return num*factorial(num-1)
num=int(input())
print(factorial(num))
"""

import math
def isprime(num):
    sqrt_num = int(math.sqrt(num))
    for i in range(2,sqrt_num+1):
        if num%i==0:
            return "Not a prime number"
        #end if
    #end for
    return "Prime Number"

num = int(input())
print(isprime(num))

#debugger to use debug by ys sharmila