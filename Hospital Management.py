from array import *
patients = []
diseases = set()
rooms = array ('i',[101,102,103,104,105])

def add_patient():
    print("/n-----Add Patients-----")
    patient_id = int(input("Enter Patient ID:"))
    name = input("Enter Name:")
    disease = input("Enter Disease:")
    age = int(input("Enter Age:"))
    doctor = input("Enter Doctor Name:")
    
    patient = {
        "id": patient_id,
        "name": name,
        "disease": disease,
        "age": age,
        "doctor": doctor
    }
    patients.append(patient)
    diseases.add(disease)
    print("\nPatient Added Successfully!")

def view_patients():
    print("/n-----View Patients-----")
    if len (patients)== 0:
        print("No patients found.")
    else:
        for patient in patients:
            print("\nPatient ID:",patient["id"])
            print("Name:",patient["name"])
            print("Disease:",patient["disease"])
            print("Age:",patient["age"])
            print("Doctor:",patient["doctor"])

def search_patient():
    print("/n-----Search Patients-----")
    search_id = int(input("Enter Patient ID to search:"))
    found = False
    for patient in patients:
        if patient["id"] == search_id:
            print("\nPatient Found!:")
            print("Name:",patient["name"])
            print("Age",patient["age"])
            print("Disease:",patient["disease"])
            print("Doctor:",patient["doctor"])
            found = True
            break
    if not found:
        print("Patient not found!")
        
def genrate_bill():
    print("/n-----Generate Bill-----")
    patient_name = input("Enter Patient Name:")
    days = int(input("Enter Number of Days Stayed:"))
    room_charge = 2000
    medicine_charge = 1500
    total = (days * medicine_charge) + medicine_charge
    print("\n-----Bill-----")
    print("Patient Name:",patient_name)
    print("Days Stayed:",days)
    print("Room Charge:",room_charge)
    print("Medicine Charge:",medicine_charge)
    print("Total Bill:",total)
    
def view_diseases():
    print("/n-----View Diseases-----")
    for disease in diseases:
        print(disease)

while True :
    print("\n----------")
    print("Hospital Management System")
    print("----------")
    print("1. Add Patient")
    print("2. View Patients")
    print("3. Search Patient")
    print("4. Generate Bill")
    print("5. View Diseases")
    print("6. View Rooms")
    print("7. Exit")
    choice = int(input("Enter your choice:"))
    if choice == 1:
        add_patient()
    elif choice == 2:
        view_patients()
    elif choice == 3:
        search_patient()
    elif choice == 4:
        genrate_bill()
    elif choice == 5:
        view_diseases()
    elif choice == 6:
        print("\n-----Room Num-----")
        for room in rooms:
            print(room)
    elif choice == 7:
        print("\nThankyou")
        break
    else:
        print("Invalid choice. Please try again.")