class Doctor:  # ID, Name, Specialization, Working Time, Qualification, Room Number
    def __init__(self):
        self.id = []
        self.name = []
        self.specialization = []
        self.working_time = []
        self.qualification = []
        self.room_number = []
        self.dlist = []
        self.readDoctorsFile()
        self.formatDrInfo()

    def formatDrInfo(self):  # Formats each doctor’s information (properties)
        #  firstly, determines the width of each category
        max_id_length = max(len(id_no) for id_no in self.id) * 2
        max_name_length = max(len(name) for name in self.name) * 2
        max_specialist_length = max(len(specialist) for specialist in self.specialization) * 2
        max_timing_length = max(len(timing) for timing in self.working_time) * 2
        max_qualification_length = max(len(qualification) for qualification in self.qualification) * 2
        max_room_length = max(len(room) for room in self.room_number) * 2

        self.dlist = []  # empties the list for new information

        # Formats the data to be aligned
        for i in range(len(self.id)):
            self.dlist.append(f"{self.id[i]:<{max_id_length}} {self.name[i]:<{max_name_length}} "
                              f"{self.specialization[i]:<{max_specialist_length}} "
                              f"{self.working_time[i]:<{max_timing_length}} "
                              f"{self.qualification[i]:<{max_qualification_length}} "
                              f"{self.room_number[i]:<{max_room_length}}")

    def enterDrInfo(self):  # Asks the user to enter doctor properties (listed in the Properties point)
        print("Enter the doctor’s ID:")
        self.id.append(input())
        print("Enter the doctor’s name:")
        self.name.append(input())
        print("Enter the doctor’s specialty:")
        self.specialization.append(input())
        print("Enter the doctor’s timing (e.g., 7am-10pm):")
        self.working_time.append(input())
        print("Enter the doctor’s qualification:")
        self.qualification.append(input())
        print("Enter the doctor’s room number:")
        self.room_number.append(input())
        self.addDrToFile(len(self.id) - 1)

    def readDoctorsFile(self):  # Reads from “doctors.txt” file and fills the doctor objects in a list
        with open('files/doctors.txt', 'r') as doctors_file:
            doctors_data = doctors_file.readlines()
            for line in doctors_data:
                parts = line.strip().split('_')  # this strips and splits the line of strings
                # stores the split strings by index into their respective categories
                self.id.append(parts[0])
                self.name.append(parts[1])
                self.specialization.append(parts[2])
                self.working_time.append(parts[3])
                self.qualification.append(parts[4])
                self.room_number.append(parts[5])
            doctors_file.close()

    def searchDoctorById(self):  # Searches whether the doctor is in the list of doctors/file using the
        # doctor ID that the user enters
        print("Enter the doctor Id:")
        search_id = input()
        try:
            index = self.id.index(search_id)
            self.displayDoctorInfo(index)

        except ValueError:
            print("\nCan't find the doctor with the same ID on the system\n")

    def searchDoctorByName(self):  # Searches whether the doctor is in the list of doctors/file using the
        # doctor name that the user enters
        print("Enter the doctor Name:")
        search_name = input()
        try:
            index = self.name.index(search_name)
            self.displayDoctorInfo(index)
        except ValueError:
            print("\nCan't find the doctor with the same name on the system\n")

    def displayDoctorInfo(self, index):  # Displays doctor information on different lines, as a list
        print(self.dlist[0])
        print(self.dlist[index])

    def editDoctorInfo(self):  # Asks the user to enter the ID of the doctor to change their information,
        # and then the user can enter the new doctor information
        print("Please enter the id of the doctor that you want to edit their information: ")
        search_id = input()
        try:
            index = self.id.index(search_id)
            print("Enter new Name")
            self.name[index] = input()
            print("Enter the doctor’s specialty:")
            self.specialization[index] = input()
            print("Enter the doctor’s timing (e.g., 7am-10pm):")
            self.working_time[index] = input()
            print("Enter the doctor’s qualification:")
            self.qualification[index] = input()
            print("Enter the doctor’s room number:")
            self.room_number[index] = input()
            self.writeListOfDoctorsToFile()
        except ValueError:
            print("\nCan't find the doctor with the same ID on the system\n")

    def displayDoctorsList(self):  # Displays all the doctors’ information, read from the file, as a report/table
        for i in range(len(self.dlist)):
            print(self.dlist[i])

    def writeListOfDoctorsToFile(self):	 # Writes the list of doctors to the doctors.txt file after
        # formatting it correctly
        self.formatDrInfo()
        with open('files/doctors.txt', 'w') as doctors_file:
            for line in self.dlist:
                line = line.split()
                line = '_'.join(line)
                doctors_file.write(line + "\n")
            doctors_file.close()

    def addDrToFile(self, index):  # Writes doctors to the doctors.txt file after formatting it correctly
        self.formatDrInfo()
        with open('files/doctors.txt', 'a') as doctors_file:
            line = self.dlist[index]
            line = line.split()
            line = '_'.join(line)
            doctors_file.write(line)
            doctors_file.close()


class Facility:  # Properties and Facility name
    def __init__(self):
        self.facilities_list = []
        with open('files/facilities.txt', 'r') as facilities_file:
            for line in facilities_file:
                self.facilities_list.append(line.strip())
            facilities_file.close()

    def addFacility(self): 	# Adds and writes the facility name to the file
        print("Enter Facility name:")
        self.facilities_list.append(input())
        self.writeListOfFacilitiesToFile()

    def displayFacilities(self):  # Displays the list of facilities
        print("The Hospital  Facilities are:")
        for item in self.facilities_list:
            print(item)

    def writeListOfFacilitiesToFile(self):  # Writes the facilities list to facilities.txt
        # though I wonder why not append?
        with open('files/facilities.txt', 'w') as facilities_file:
            for item in self.facilities_list:
                facilities_file.write(item + "\n")
            facilities_file.close()


class Laboratory:  # Properties, Lab name, cost
    def __init__(self):
        self.laboratory_list = []
        self.cost_list = []
        self.lab_and_cost_list = []
        self.readLaboratoriesFile()
        self.formatLaboratoryInfo()

    def addLabToFile(self, index):  # Adds and writes the lab name to the file
        # in the format of the data that is in the file
        self.formatLaboratoryInfo()
        with open('files/laboratories.txt', 'a') as laboratories_file:
            line = self.lab_and_cost_list[index]
            line = line.split()
            line = '_'.join(line)
            laboratories_file.write(line)
            laboratories_file.close()

    def writeListOfLabsToFile(self):  # Writes the list of labs into the file laboratories.txt
        self.formatLaboratoryInfo()
        with open('files/laboratories.txt', 'w') as laboratories_file:
            for line in self.lab_and_cost_list:
                line = line.split()
                line = '_'.join(line)
                laboratories_file.write(line + "\n")
            laboratories_file.close()

    def displayLabsList(self):  # Displays the list of laboratories
        for i in range(len(self.lab_and_cost_list)):
            print(self.lab_and_cost_list[i])

    def formatLaboratoryInfo(self):	 # Formats the Laboratory object similar to the laboratories.txt file
        max_lab_length = max(len(lab) for lab in self.laboratory_list) * 2
        max_cost_length = max(len(cost) for cost in self.cost_list) * 2

        self.lab_and_cost_list = []

        for i in range(len(self.laboratory_list)):
            self.lab_and_cost_list.append(f"{self.laboratory_list[i]:<{max_lab_length}}"
                                          f"{self.cost_list[i]:<{max_cost_length}}")

    def enterLaboratoryInfo(self):  # Asks the user to enter lab name and cost and forms a Laboratory object
        print("Enter Laboratory facility:")
        self.laboratory_list.append(input())
        print("Enter Laboratory cost:")
        self.cost_list.append(input())
        self.addLabToFile(len(self.laboratory_list) - 1)

    def readLaboratoriesFile(self):	 # Reads the laboratories.txt file and
        # fills its contents in a list of Laboratory objects
        with open('files/laboratories.txt', 'r') as laboratories_file:
            laboratories_data = laboratories_file.readlines()
            for line in laboratories_data:
                parts = line.strip().split('_')
                self.laboratory_list.append(parts[0])
                self.cost_list.append(parts[1])
            laboratories_file.close()


class Patient:  # Properties, pid, name, disease, gender, age
    def __init__(self):
        self.pid_list = []
        self.name_list = []
        self.disease_list = []
        self.gender_list = []
        self.age_list = []
        self.plist = []
        self.readPatientsFile()
        self.formatPatientInfo()

    def formatPatientInfo(self):  # Formats patient information to be added to the file
        max_pid_length = max(len(pid) for pid in self.pid_list) * 2
        max_name_length = max(len(name) for name in self.name_list) * 2
        max_disease_length = max(len(disease) for disease in self.disease_list) * 2
        max_gender_length = max(len(gender) for gender in self.gender_list) * 2
        max_age_length = max(len(age) for age in self.age_list) * 2

        self.plist = []  # empties current patient list for new information

        for i in range(len(self.pid_list)):  # this formats each line and appends it to the patient list
            self.plist.append(f"{self.pid_list[i]:<{max_pid_length}} {self.name_list[i]:<{max_name_length}}"
                              f"{self.disease_list[i]:<{max_disease_length}} {self.gender_list[i]:<{max_gender_length}}"
                              f"{self.age_list[i]:<{max_age_length}}")

    def enterPatientInfo(self):  # Asks the user to enter the patient info
        print("Enter Patient id:")
        self.pid_list.append(input())
        print("Enter Patient name:")
        self.name_list.append(input())
        print("Enter Patient disease:")
        self.disease_list.append(input())
        print("Enter Patient gender:")
        self.gender_list.append(input())
        print("Enter Patient age:")
        self.age_list.append(input())
        self.addPatientToFile(len(self.pid_list)-1)

    def readPatientsFile(self):  # Reads from file patients.txt
        with open('files/patients.txt', 'r') as patients_file:
            patients_data = patients_file.readlines()
            for line in patients_data:
                parts = line.strip().split('_')  # this strips and splits the line of strings
                # stores the split strings by index into their respective categories
                self.pid_list.append(parts[0])
                self.name_list.append(parts[1])
                self.disease_list.append(parts[2])
                self.gender_list.append(parts[3])
                self.age_list.append(parts[4])
                patients_file.close()

    def searchPatientById(self):  # Searches for a patient using their ID
        print("Enter the patient Id:")
        search_id = input()
        try:
            index = self.pid_list.index(search_id)
            self.displayPatientInfo(index)

        except ValueError:
            print("Can't find the patient with the same ID on the system")

    def displayPatientInfo(self, index):  # Displays patient info
        print(self.plist[0])
        print(self.plist[index])

    def editPatientInfo(self):  # Asks the user to edit patient information
        print("Please enter the id of the Patient that you want to edit their information: ")
        search_id = input()
        try:
            index = self.pid_list.index(search_id)
            print("Enter new Name")
            self.name_list[index] = input()
            print("Enter new disease:")
            self.disease_list[index] = input()
            print("Enter new gender:")
            self.gender_list[index] = input()
            print("Enter new age:")
            self.age_list[index] = input()
            self.writeListOfPatientsToFile()
        except ValueError:
            print("Can't find the doctor with the same ID on the system")

    def displayPatientsList(self):  # Displays the list of patients
        for i in range(len(self.plist)):
            print(self.plist[i])

    def writeListOfPatientsToFile(self):  # Writes a list of patients into the patients.txt file
        self.formatPatientInfo()
        with open('files/patients.txt', 'w') as patients_file:
            for line in self.plist:
                line = line.split()
                line = '_'.join(line)
                patients_file.write(line + "\n")
            patients_file.close()

    def addPatientToFile(self, index):  # Adds a new patient to the file
        self.formatPatientInfo()
        with open('files/patients.txt', 'a') as patients_file:
            line = self.plist[index]
            line = line.split()
            line = '_'.join(line)
            patients_file.write(line)
            patients_file.close()


class Management:
    def displayMenu(self):  # to display the menu shown in the Sample Run section.
        while True:
            print("Welcome to Alberta Hospital (AH) Management system")
            print("Select from the following options, or select 0 to stop: ")
            print("1 - 	Doctors")
            print("2 - 	Facilities")
            print("3 - 	Laboratories")
            print("4 - 	Patients")
            try:
                option = int(input())
            except ValueError:
                print("invalid option, please try again")
                continue

            if option == 1:
                self.doctorMenu()
            elif option == 2:
                self.facilitiesMenu()
            elif option == 3:
                self.laboratoriesMenu()
            elif option == 4:
                self.patientsMenu()
            elif option == 0:
                break

    def doctorMenu(self):
        while True:  # Doctors menu
            print("Doctors Menu:")
            print("1 - Display Doctors list")
            print("2 - Search for doctor by ID")
            print("3 - Search for doctor by name")
            print("4 - Add doctor")
            print("5 - Edit doctor info")
            print("6 - Back to the Main Menu\n")

            try:
                option = int(input())
            except ValueError:
                print("invalid option, please try again")
                continue

            if option == 1:
                doctor.displayDoctorsList()
                print("\nBack to the previous menu\n")
            elif option == 2:
                doctor.searchDoctorById()
                print("\nBack to the previous menu\n")
            elif option == 3:
                doctor.searchDoctorByName()
                print("\nBack to the previous menu\n")
            elif option == 4:
                doctor.enterDrInfo()
                print("\nBack to the previous menu\n")
            elif option == 5:
                doctor.editDoctorInfo()
                print("\nBack to the previous menu\n")
            elif option == 6:
                print("\nBack to the previous menu\n")
                break

    def facilitiesMenu(self):
        while True:  # Facilities menu
            print("Facilities Menu:")
            print("1 - Display Facilities list")
            print("2 - Add Facility")
            print("3 - Back to the Main Menu\n")
            try:
                option = int(input())
            except ValueError:
                print("invalid option, please try again")
                continue
            if option == 1:
                facility.displayFacilities()
                print("\nBack to the previous menu\n")
            elif option == 2:
                facility.addFacility()
                print("\nBack to the previous menu\n")
            elif option == 3:
                print("\nBack to the previous menu\n")
                break

    def laboratoriesMenu(self):
        while True:  # Laboratories menu
            print("Laboratories Menu:")
            print("1 - Display laboratories list")
            print("2 - Add laboratory")
            print("3 - Back to the Main Menu\n")
            try:
                option = int(input())
            except ValueError:
                print("\ninvalid option, please try again\n")
                continue
            if option == 1:
                laboratory.displayLabsList()
                print("\nBack to the previous menu\n")
            elif option == 2:
                laboratory.enterLaboratoryInfo()
                print("\nBack to the previous menu\n")
            elif option == 3:
                print("\nBack to the previous menu\n")
                break

    def patientsMenu(self):
        while True:  # Patients menu
            print("Patients Menu:")
            print("1 - Display patients list")
            print("2 - Search for patient by ID")
            print("3 - Add patient")
            print("4 - Edit patient info")
            print("5 - Back to the Main Menu\n")
            try:
                option = int(input())
            except ValueError:
                print("invalid option, please try again")
                continue

            if option == 1:
                patient.displayPatientsList()
                print("\nBack to previous menu\n")
            elif option == 2:
                patient.searchPatientById()
                print("\nBack to previous menu\n")
            elif option == 3:
                patient.enterPatientInfo()
                print("\nBack to previous menu\n")
            elif option == 4:
                patient.editPatientInfo()
                print("\nBack to previous menu\n")
            elif option == 5:
                print("\nBack to previous menu\n")
                break


#  initialize instances
doctor = Doctor()
facility = Facility()
laboratory = Laboratory()
patient = Patient()
management = Management()
management.displayMenu()
