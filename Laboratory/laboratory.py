# Assignment: Classes (Group)
# Edward Magtoto 000816021

# Assignment
# Alberta Rural Patient Care (ARPC) is a new healthcare provider in Alberta. To complement the existing large-scale hospitals located in urban settings, ARPC is building a network of smaller scale mini-hospitals which target underserved rural populations. ARPC has hired your company to create a management system which is customized to meet their unique operational needs. (laboratory section)


### IMPORTS
import lab

### LISTS
l_list = []


### READ FILE
def readLaboratoriesFile():
    l_list = []
    with open("laboratories.txt", "r") as i:
        file = i
        l = 1
        for line in file:
            if l == 1:
                l += 1
                continue
            items = line.split("_")
            place = lab.Lab(items[0], int(items[1]))
            l_list.append(str(place))
        file.close
        return l_list

### ADD LAB      
def addLabToList():
    addLab = enterLaboratoryInfo()
    writeList = open("laboratories.txt", "a")
    writeList.write(addLab)
    writeList.close()

### ADD LAB (INFO)
def enterLaboratoryInfo():
    name = str(input("\nEnter Lab Name: "))
    cost = int(input("Enter Lab Cost: "))
    place = lab.Lab(name, cost)
    newPlace = place.formatLabInfo()
    return newPlace


### DISPLAY LIST
def displayLabsList():
    labs = readLaboratoriesFile()
    print("\n")
    print('{:<10s} {:>17s}'.format("Lab Name", "Cost"))
    print('\n'.join(labs))
    # print("\n")

### OPTIONS
def option1():
    displayLabsList()
    laboratoriesMenu()
def option2():
    addLabToList()
    laboratoriesMenu()

### lABORATORIES MENU
def laboratoriesMenu():
    print("\nLaboratory Menu\n0 - Return to Main Menu\n1 - Display Laboratories List\n2 - Add Laboratories")
    option = int(input("Please Enter Option: "))
    if option == 1:
        option1()
    if option == 2:
        option2()
    if option == 0:
        return


if __name__ == "__main__":
    laboratoriesMenu()