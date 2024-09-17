#with automatically uses names_db.close() function
#without using 'with' class
"""
names_db = open('names.txt','r')
all_names = names_db.read()
print(all_names)
names_db.close()
"""
#using with function
"""
with open('names.txt','r') as names_db:
    all_names = names_db.read()
    print(all_names)
"""

#using 'with' + read lines
"""
with open('names.txt', 'r') as file:
    lines = file.readlines()
    print(lines)
"""
