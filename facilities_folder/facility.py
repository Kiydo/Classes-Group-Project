import facilities

f_list = [] # List for facilities

#   ADD FACILITY
def addFacilityToList():
    facilityName = str(input("\nEnter Facility name: "))
    f = open("facilities.txt", "a")
    f.write(facilityName)
    f.close()

#   DISPLAY FACILITIES
def displayFacilities(): 
    f = open("facilities.txt", "r")
    print(f.read())
    f.close()

#   OPTIONS
def option1():
    displayFacilities()
    menuFacilities()
def option2():
    addFacilityToList()
    menuFacilities()

#   MENU
def menuFacilities():
    print("\nFacilities Menu:\n1 - Display Facilities list\n2 - Add Facility\n3 - Back to the Main Menu") # Facilities Menu
    option = int(input("Please Enter option: ")) # Option Selection
    if option == 1:
        option1()
    if option == 2:
        option2()
    if option == 3:
        return

if __name__ == "__main__":
    menuFacilities()