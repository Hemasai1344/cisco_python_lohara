
lst = list(map(str,input().split())) # [hema, sai, thaninki, cisco]
tup = tuple(lst) # (hema, sai, thaninki, cisco)

#write both list and tuple to a text file, each on a new line

with open("names.txt", "w") as file:
    file.write("List: " + str(lst) + "\n")
    file.write("Tuple: " + str(tup) + "\n")

#reads the content of the file and prints them out

with open('names.txt', 'r') as file:
    line1 = file.readline()
    line2 = file.readline()
    print(line1)
    print(line2)