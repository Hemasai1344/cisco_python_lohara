# patients 
from Patient import Patient
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
            return
    print(f'invalid id {id}')

#display the patient details

def patient_display():
    global patients
    for i in patients:
        print(i)
