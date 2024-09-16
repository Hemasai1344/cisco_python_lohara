patients = []

def join_patient(pid):
    global patients
    return patients.append(pid)

def discharge_patient(pid):
    global patients
    try:
        patients.remove(pid)
    except ValueError as err:
        print("No data regarding that patient id")


def menu():
    choice=int(input('''
1-joining patient
2-discharge patient'''))
    if choice==1:
        pid = int(input("Enter the patient id- "))
        join_patient(pid)
        print(patients)
    elif choice==2:
        pid = int(input("Enter the patient id to discharge- "))
        discharge_patient(pid)
        print(patients)
    else:
        print("Invalid choice. Please try again.")
    return choice
    
def display():
    choice = menu()
    while choice !=3:
        choice = menu()
    print('your hospital automation was finished ...:)')
display()