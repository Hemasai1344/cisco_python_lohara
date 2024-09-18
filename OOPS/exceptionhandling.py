def find_quotient(d,n):
    if n==0:
        raise ZeroDivisionError()
    return d/n
try:
    number=int(input("enter a number:"))
    result=find_quotient(10,number)
except ValueError:
    print("invalid input!,Enter a valid input:")
except ZeroDivisionError:
    print("you cannot divide with zero")
else:
    print (result)
finally:
    print('cleaning up')
print('end of program')
