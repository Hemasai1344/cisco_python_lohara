
lst = list(map(str,input().split())) # [hema, sai, thaninki, cisco]
#or lst = input().split()
#lst = input("Enter words separeted by spaces ").split()

tup = tuple(lst) # (hema, sai, thaninki, cisco)

print(f'List : {lst}')
print(f'Tuple: {tup}')
#write both list and tuple to a text file, each on a new line

with open("names.txt", "w") as file:
    file.write(f'List : {lst}\n')
    file.write(f'Tuple: {tup}\n')

print("Data written to file ")
#reads the content of the file and prints them out
"""
with open('names.txt', 'r') as file:
    line1 = file.readline()
    line2 = file.readline()
    print(line1)
    print(line2)
"""
#or 
with open('names.txt', 'r') as file:
    for i in range(2):
        print(file.readline())