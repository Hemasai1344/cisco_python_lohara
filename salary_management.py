
salaries = []
"""

1. add salary
2. remove salary
3. find avg of salaries
4. find min of salaries1
5. find max of salaries

"""
def add_sal(salary):
    global salaries
    salaries.append(salary)

def rem_salary(salary):
    global salaries
    try:
        salaries.remove(salary)
    except ValueError as err:
        print("No such salary")

def sum_salaries():
    global salaries
    return sum(salaries)

def avg_salaries():
    global salaries
    return sum(salaries)//len(salaries)

def find_max():
    global salaries
    return max(salaries)

def find_min():
    global salaries
    return min(salaries)

def menu():
    choice = int(input('''
1-add
2-delete
3-sum
4-min
5-max
6-avg
7-exit
your choice...'''))
    
    if choice == 1:
        salary = float(input('enter the salary of a person '))
        add_sal(salary)
        print(salaries)
    elif choice ==2:
        salary = float(input('enter the remove salary of a person '))
        rem_salary(salary)
        print(salaries)
    elif choice==3:
        s = sum_salaries()
        print(s)
    elif choice == 4:
        min = find_min()
        print(min)
    elif choice == 5:
        max = find_max()
        print(max)
    elif choice == 6:
        avg = avg_salaries()
        print(avg)
    elif choice == 7:
        print("Exiting...")
        return choice
    else:
        print("Invalid choice. Please try again.")
    return choice

def menus():
    choice = menu()
    while choice !=7:
        choice = menu()
    print('your salary automation was finished ...:)')
menus()