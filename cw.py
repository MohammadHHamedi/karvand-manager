
#names = ["mamad", "ali", "reza", "javad"]
#name = input("enter the name:").strip()
#if name in names:
#    print("found")
#else:
#    print("not found")

############# % 10 % ###############
# contacts = {"Ali": "09120000000", "Sara": "09130000000", "Reza": "09140000000"}
# name = input("Enter name: ").strip()
# print(contacts.get(name, "not found"))
# if name in contacts:
#    print("Phone number:", contacts[name])
# else:
#    print("Contact not found")
##############15################

# with open("names.txt", "w") as file:
#     while True:
#         name = input("Enter a name: ")
#         if name == "exit":
#             break
#         file.write(name + "\n")
# print ("Names saved successfully.")

################%% 16 %% ##########################

# with open("names.txt", "r") as file:
#     lines = file.readlines()

# print("Number of lines:", len(lines))

# for line in lines:
#     print(line.strip())

###############%% 17 %%################

# with open("names.txt", "a") as file:
#     while True:
#         name = input("Enter name: ").strip()
#         if name == "exit":
#             break
#         age = input("Enter age: ").strip()
#         file.write(f"{name} - {age}\n")

# print("Data saved successfully")
#################%% 18 %%###################
# with open("names.txt", "r") as file:
#     for line in file:
#         name, age = line.split("-")
#         name = name.strip()
#         age = age.strip()

#         print("Name:", name)
#         print("Age:", age)
#############%% 19 %%######################
# with open("names.txt", "r") as file:
#     total_age = 0
#     count = 0

#     for line in file:
#         name, age = line.split("-")
#         age = int(age.strip())

#         total_age += age
#         count += 1

# average = total_age / count

# print("Average age:", average)

####################%% 20 %%####################

# students = {}

# while True:
#     print("<||Command Info||>\n", 
#           "|To add a student, type: add|\n", 
#           "|To save your data, type: save|\n", 
#           "|To View your data, type: show|\n", 
#           "|To find your data, type: search|\n", 
#           "|To quit program, type: exit|")
#     command = input("Enter command: ")

#     if command == "add":
#         name = input("Enter student name: ")
#         grade = float(input("Enter grade: "))
#         students[name] = grade

#     elif command == "save":
#         with open("students.txt", "w") as file:
#             for name, grade in students.items():
#                 file.write(f"{name} - {grade}\n")

#         print("Data saved successfully.")

#     elif command == "show":
#         for name, grade in students.items():
#             print("Name:", name, " Grade:", grade)

#     elif command == "search":
#         name = input("Enter student name: ")

#         if name in students:
#             print("Grade:", students[name])
#         else:
#             print("Student not found.")

#     elif command == "exit":
#         break

#     else:
#         print("Invalid command.")


