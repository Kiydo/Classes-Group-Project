# Assignment: Classes (Group)
# Edward Magtoto 000816021
# GROUP: Edward Magtoto, Bryan Jake Columbres, Rolan Ho

# Assignment
# Alberta Rural Patient Care (ARPC) is a new healthcare provider in Alberta. To complement the existing large-scale hospitals located in urban settings, ARPC is building a network of smaller scale mini-hospitals which target underserved rural populations. ARPC has hired your company to create a management system which is customized to meet their unique operational needs. (Main menu section)

# TABLE OF CONTENTS
#   IMPORTS
#   DOCTOR
#   FACILITIES
#   LABORATORIES
#   PATIENTSMENU
#   OPTIONS
#   MAIN MENU

### IMPORTS
from doctor_folder import doctor
from lab_folder import laboratory
from patient_folder import patient_program
from facilities_folder import facility

### DOCTOR
def doctorsMenu():
    doctor.Doctor.doctorsMenu()

### FACILITIES
def facilitiesMenu():
    facility. menuFacilities()

### LABORATORIES
def laboratoriesMenu():
    laboratory.laboratoriesMenu()

### PATIENTSMENU
def patientsMenu():
    patient_program.menuPatient()




### OPTIONS
def option1():
    doctorsMenu()
    mainMenu()
def option2():
    facilitiesMenu()
def option3():
    laboratoriesMenu()
    mainMenu()
def option4():
    patientsMenu()
    mainMenu()


### MAIN MENU
def mainMenu():
    print("\nWelcome to the Alberta Rural Patient Care Management System")
    print("\nMain Menu\n0 - Close Application\n1 - Doctors\n2 - Facilities\n3 - Laboratories\n4 - Patients")
    option = int(input("Enter option: "))
    if option == 1:
        option1()
    if option == 2:
        option2()
    if option == 3:
        option3()
    if option == 4:
        option4()
    if option == 0:
        return



if __name__ == "__main__":
    mainMenu()