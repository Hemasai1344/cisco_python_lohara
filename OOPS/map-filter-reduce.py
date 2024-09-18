"""
from functools import *
nums = [2,3,4]
#map syntax
#map(<func>,iterable)
nums_sqr = list(map(lambda num: num**2,nums))
print(nums_sqr)

#filter
nums_even = list(filter(lambda num:num%2==0, nums))
print(nums_even)

#reduce syntax
# reduce((function),list_name,0)
# 0 can change accoriding to our functionality

#sum and product of a list using reduce
nums = [10,20,30,40]
nums_sum = reduce(lambda s,i: s+i, nums, 0)
nums_product = reduce(lambda p,i: p*i, nums, 1)
print(nums_sum, nums_product)

#min and max values using reduce

nums_min = reduce(lambda a, b: a if a < b else b, nums) #10
nums_max = reduce(lambda a, b: a if a > b else b, nums) #40

print(nums_min,nums_max)

nums_min1 = reduce(min,nums) #10
nums_max1 = reduce(max,nums) #40

print(nums_min1,nums_max1)
"""