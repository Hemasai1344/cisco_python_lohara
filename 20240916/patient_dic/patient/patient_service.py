# patients 
from Patient import Patient
patients = {}

#adding a patient

def patient_add(id,name):
    global patients
    patient = Patient(id,name)
    patients[patient.id]=patient
    print("patient is admitted in the hospital")
    print(patients[id])

#removing patient
def patient_remove(id):
    global patients
    patient = patients.get(id)
    if patient == None:
        print(f'No such id {id}')
        return
    print(patient)
    if input('Are you sure to delete (yes/no)?').lower() == "yes":
        del patients[id] #id is the key and name is the value
        print("patient deleted successfully")
    #end if

def patient_read_by_id(id):
    global patients
    patient = patients.get(id)
    if patient == None:
        print(f'No such id {id}')
        return
    print(patient)
    
def update_name_by_id(id):
    global patients
    patient = patients.get(id)
    if patient == None:
        print(f'No such id {id}')
        return
    print(patient)
    name = input(f'Enter new name({patient.name}) : ')
    patient.name = name 
    print("Patient updated succesfully")


#display the patient details

def patient_display():
    global patients
    """
    for list:
    for patient in patients:
        print(patient)
    """
    if len(patients)==0:
        print("No patient data found try to update the data ")
    for id in patients:
        print(patients[id])