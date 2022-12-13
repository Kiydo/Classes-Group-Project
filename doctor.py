#Group project code -Jake Columbres- 000896319

class Doctor:

    #Class variables
    doctorObjects =  []
    #Doctor methods
    def __init__(self, drId, drName, drSpecialty, drSchedule, drQualification, drRoomNumber):
        self.id = drId
        self.name = drName
        self.specialty = drSpecialty
        self.schedule = drSchedule
        self.qualification = drQualification
        self.roomNumber = drRoomNumber

    def formatDrInfo(self):
        return f"{self.id}_{self.name}_{self.specialty}_{self.schedule}_{self.qualification}_{self.roomNumber}"

    def __str__(self):
        return f"{self.id:3} {self.name:3} {self.specialty:3} {self.schedule:3} {self.qualification:3} {self.roomNumber:3}"


    #Doctor related methods
    def enterDrInfo():
        drId = input("\nEnter Dr Id: ")
        drName = input("Enter Dr name: ")
        drSpecialty = input("Enter Dr specialty: ")
        drSchedule = input("Enter Dr schedule: ")
        drQualifications = input("Enter Dr qualifications: ")
        drRoomNumber = input("Enter Dr room number: ")
     
        #Create new Doctor object
        doctor1 = Doctor(drId, drName, drSpecialty, drSchedule, drQualifications, drRoomNumber)
        
        return doctor1.formatDrInfo()

####Read Doctor file into a list of Doctor Objects####
    def readDoctorsFile():
        fileName = "doctors.txt"
        drFile = open(fileName, 'r')

        for line in drFile:
            doctorIndividual = line.rstrip().split('_')
            Doctor.doctorObjects.append(doctorIndividual)
        drFile.close()
        return Doctor.doctorObjects

####Search the list of doctor objects for a specified ID that the user enters####
    def searchDoctorById():
        validation = False
        #Refresh the list
        Doctor.doctorObjects.clear()
        Doctor.doctorObjects = Doctor.readDoctorsFile()
        #Set to global for the EditDoctorInfo
        searchId = input("\nEnter the doctor ID: ")

        for i in range(len(Doctor.doctorObjects)):

            if Doctor.doctorObjects[i][0] == searchId:
                #Display the Doctor's attributes
                for x in range(len(Doctor.doctorObjects[i])):
                    print(f'{Doctor.doctorObjects[i][x]} {" " :5}', end='')
                validation = True
        if validation == False:
            print(f'Doctor  with ID {searchId} not found in file\n')

            

####Search the list of doctor objects for a specified name that the user enters####
    def searchDoctorByName():
        validation = False
        #Refresh the list
        Doctor.doctorObjects.clear()
        Doctor.doctorObjects = Doctor.readDoctorsFile()
        #Set to global for the editDoctorInfo Method
        global searchName
        searchName = input("\nEnter the doctor name: ")

        for i in range(len(Doctor.doctorObjects)):

            if Doctor.doctorObjects[i][1] == searchName:
                #Display Doctor attributes
                for x in range(len(Doctor.doctorObjects[i])):
                    print(f'{Doctor.doctorObjects[i][x]} {" " :5}', end='')
                validation = True
        if validation == False:
            print(f'Doctor {searchName} not found in file\n')
     
    

#### Search for the ID (input from user), prompt new values and update the list of Doctors####       
    def editDoctorInfo():
        validation = True
        #Refresh the list
        Doctor.doctorObjects.clear()
        Doctor.doctorObjects = Doctor.readDoctorsFile()
        
        searchId = input("\nEnter the doctor ID: ")
        #Search the list by ID and printing the attributes
        for i in range(len(Doctor.doctorObjects)):

            if Doctor.doctorObjects[i][0] == searchId:
                #Display the Doctor's attributes
                for x in range(len(Doctor.doctorObjects[i])):
                    print(f'{Doctor.doctorObjects[i][x]} {" " :5}', end='')
                validation = True
        if validation == False:
            print(f'Doctor  with ID {searchId} not found in file\n')

        for i in range(len(Doctor.doctorObjects)):
            if Doctor.doctorObjects[i][0] == searchId:
                drName = input("\nEnter new name: ")
                drSpecialty = input("Enter new specialty in: ")
                drSchedule = input("Enter new schedule: ")
                drQualifications = input("Enter new qualifications: ")
                drRoomNumber = input("Enter new room number: ")
                doctorAttributes = f'{searchId}_{drName}_{drSpecialty}_{drSchedule}_{drQualifications}_{drRoomNumber}'

                #Insert the new user-entered attributes into a list temp
                temp  = doctorAttributes.split('_')

                #for loop to replace the old attribtes with new ones at location [x][x]
                for k in range(len(Doctor.doctorObjects[i])):
                    Doctor.doctorObjects[i][k] = temp[k]

                #Update the doctors.txt file  
                Doctor.WriteDoctorsListToFile()  

                break
               
####Print all the doctors information(attributes)###
    def displayDoctorsList():
        #Refresh the list
        Doctor.doctorObjects.clear()
        Doctor.doctorObjects = Doctor.readDoctorsFile()

        for i in range (len(Doctor.doctorObjects)):
            for j in range(len(Doctor.doctorObjects[i])):
                print(f'{Doctor.doctorObjects[i][j]:17}', end='')
            print()

####Writes into the "doctors.1txt" from the list of doctors####
    def WriteDoctorsListToFile():
        fileName = "doctors.txt"
        drFile = open(fileName, 'w')

        for i in range(len(Doctor.doctorObjects)):
            drFile.write(f'{"_".join(Doctor.doctorObjects[i])}\n')

####Gets new doctor object (With user-entered doctor information) and add it to the doctors list####    
    def addDrToList():
        #Refresh the list
        Doctor.doctorObjects.clear()
        Doctor.doctorObjects = Doctor.readDoctorsFile()
       
        doctor1 = Doctor.enterDrInfo()

        #Append new attributes to the end of the list of doctors
        Doctor.doctorObjects.append(doctor1.split('_'))

        #Update the "doctors.txt" file
        Doctor.WriteDoctorsListToFile()


