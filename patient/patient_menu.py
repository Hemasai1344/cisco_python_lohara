from patient_service import patient_add,patient_display,patient_read_by_id,patient_remove,update_name_by_id
def menu():
    choice=int(input('''
1-joining patient 
2-discharge patient 
3-patient_read_by_id
4-update_name_by_id
5-display all patients
6-end 
your choice..... '''))
    if choice==1:
        id = int(input("Enter the patient id- "))
        name = input("enter patient name: ")
        patient_add(id,name)
        #print(patients)
    elif choice==2:
        id = int(input("Enter the patient id to discharge- "))
        patient_remove(id)
        #print(patients)
    elif choice==3:
        id = int(input("Enter the patient id- "))
        patient_read_by_id(id)
    elif choice==4:
        id = int(input("enter patient id with wrong name details "))
        update_name_by_id(id)
    elif choice==5:
        patient_display()
    elif choice==6:
        pass
    else:
        print("Invalid choice. Please try again.")
    return choice


def menus():
    choice = menu()
    while choice!=7:
        choice=menu()
    print("Thank you using our application")