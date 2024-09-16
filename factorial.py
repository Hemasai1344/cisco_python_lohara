def fact(num):
    ans=1
    for i in range(2,num+1):
        ans*=i
    return ans
s=fact(20)
print(s)