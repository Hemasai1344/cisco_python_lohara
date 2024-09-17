# creating patient class with id and name

class Patient:
    def __init__(self,id,name):
        self.id = id
        self.name = name

    def __str__(self):
        return f'[id={self.id}, name={self.name}]'
    
    def __repr__(self):
        return self.__str__()
    
# patients 

patients = []

#adding a patient

def patient_add(id,name):
    global patients
    patient = Patient(id,name)
    patients.append(patient)
    print("patient is admitted in the hospital")
    print(patients)

#removing patient
def patient_remove(id):
    global patients

    for patient in patients:
        if patient.id == id:
            print("Are you sure ?")
            s=input().lower()
            if s=="yes":
                patients.remove(patient)
                print(f'Patient with id {id} is discharged')
            return
                #break
            #return
        #end if
    #end for
    print(f'no such data for that patient id {id} ')

def patient_read_by_id(id):
    global patients
    for p in patients:
        if p.id==id:
            print(p)
            return

def update_name_by_id(id):
    global patients
    for patient in patients:
        if patient.id==id:
            name1=input(f'enter the updated name ({patient.name})')
            patient.name = name1
            print("patient data updated successfully")
            #return


#display the patient details

def patient_display():
    global patients
    for i in patients:
        print(i)

#menu

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
    while choice!=4:
        choice=menu()
    print("Thank you using our application")

menus()