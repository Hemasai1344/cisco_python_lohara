import json
#1. class Patient {id, name}
class Patient:
    def __init__(self, id, name):
        self.id = id 
        self.name = name 
    def __str__(self):
        return f'[id={self.id}, name={self.name}]'
    def __repr__(self):
        return self.__str__()
#2. patients[]
patients = []

#3. patient_add(id, name)
def patient_add(id, name):
    global patients
    patient = Patient(id, name)
    patients.append(patient)
    print('Patient created successfully')
#4. patient_remove(id)
def patient_remove(id):
    global patients
    for patient in patients:
        if patient.id == id:
            print(patient)
            if input('Are you sure to delete(yes/no)?').lower() == 'yes':
                patients.remove(patient)
                print('Patient deleted successfully')
            return 
        #end if 
    #end for 
    print(f'No such id {id}')
#5. patient_display()
def patient_display():
    global patients
    for patient in patients:
        print(patient)
#patient_display_byid(id)
def patient_display_byid(id):
    global patients
    for patient in patients:
        if patient.id == id:
            print(patient)
            return 
        #endif
    #endfor 
    print('Invalid id')
#patient_update(id)
def patient_update(id):
    global patients
    for patient in patients:
        if patient.id == id:
            print(patient)
            name = input(f'Enter new name({patient.name}):')
            patient.name = name 
            print('Patient updated successfully')
            return 
        #end if 
    #end for 
    print(f'No such id {id}')
def write_patients_to_json_list(filename='patients_list.json'):
    global patients
    data = [{'id': patient.id, 'name': patient.name}for patient in patients]
    print(data)
    with open(filename,'w') as file:
        json.dump(data, file, indent=4)
    print(f'Data written to {filename}')       

#6. menu 
def menu():
    choice = int(input('''1-add patient
2-delete patient by id
3-display all patients
4-read patient by id 
5-update patient by id
6-save list to JSON
7-end                       
your choice:'''))
    if choice == 1:
        id = int(input('Enter patient id:'))
        name = input('Enter patient name:')
        patient_add(id, name)
    elif choice == 2:
        id = int(input('Enter patient id to delete:'))
        patient_remove(id)
    elif choice == 3:
        patient_display()
    elif choice == 4:
        id = int(input('Enter patient id:'))
        patient_display_byid(id)
    elif choice == 5:
        id = int(input('Enter patient id:'))
        patient_update(id)
    elif choice == 6:
        write_patients_to_json_list()    
    elif choice == 7:
        pass 
    else:
        print('Invalid menu')
    return choice
#7. menus 
def menus():
    choice = menu()
    while choice != 7:
        choice = menu()
    print('Thank you for using the app')
#8. driver program
menus()
