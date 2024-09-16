"""
def find_sum(first_num,second_num):
    return first_num+second_num

#first_num = int(input())
#second_num = int(input())

s=find_sum(10,20)
print(s)
"""

def cal(first:int, second:int)->int:
    sum = first+second
    diff = first-second
    product = first*second
    quotient = first//second
    return sum,diff,product,quotient

s,d,p,q = cal(20,6)
print(s,d,p,q)