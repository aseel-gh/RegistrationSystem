import requests
import json


class Student:
    id = 0  # class value.

    def __init__(self, full_name, age, level, mobile_number):
        self.id = Student.id
        self.full_name = full_name
        self.age = age
        self.level = level
        self.mobile_number = mobile_number
        Student.id += 1

# Register or create New Student function-------------
    def register_student(self):
        while True:
            full_name = input("full name:")

            age = int(input("age:"))
            if age > 0:
                pass
            else:
                print("Invalid Age")
                break

            level = input("level (A,B,C):")
            if level == 'a' or 'b' or 'c' or 'A' or 'B' or 'C':
                pass
            else:
                print("Invalid Level")
                break

            mobile_number = input("mobile number:")

            data = {
                "full_name": full_name,
                "age": age,
                "level": level,
                "mobile_number": mobile_number
            }
            result = requests.post(url="http://staging.bldt.ca/api/method/build_it.test.register_student", data=data)
            result = json.loads(result.text)
            # status code, if 200 print registered, else fail to registered.
            if result['code'] == 200:
                print("Student Registered Successfully")
            else:
                print("Failed to Register Student")
            e = input("exit? (y/n) \n")
            if e == "y" or "Y":
                break

# Edit Student Details function-------------
    def edit_student_details(self):
        while True:
            id = input("ID:")

            full_name = input("full name:")

            age = int(input("age:"))  # turn input into integer.
            if age <= 0:
                print("Invalid Age")
                break

            level = input("level (A,B,C):")
            if level == 'a' or 'b' or 'c' or 'A' or 'B' or 'C':
                pass
            else:
                print("Invalid Level")
                break

            mobile_number = input("mobile number:")

            data = {
                "id": id,
                "full_name": full_name,
                "age": age,
                "level": level,
                "mobile_number": mobile_number
            }

            result = requests.post(url="http://staging.bldt.ca/api/method/build_it.test.edit_student", data=data)
            result = json.loads(result.text)
            print(result)
            if result['code'] == 200:
                print("Student Updated Successfully ")
            else:
                print("Failed to edit student ")
            e = input("exit? (y/n) \n")
            if e == "y" or "Y":
                break

# Delete Student function-------------------
    def delete_student(self):
        id = input("ID:")

        data = {
            "id": id}

        result = requests.post(url="http://staging.bldt.ca/api/method/build_it.test.delete_student", data=data)
        result = json.loads(result.text)
        print(result)
        if result['code'] == 200:
            print("Student Deleted \n")
        else:
            print("Failed to delete student \n")

# Export Students to text file function-----
    def get_students(self):
        result = requests.get(url="http://staging.bldt.ca/api/method/build_it.test.get_students")
        result = json.loads(result.text)
        if result.get('code') != 200:
            print("Error Occurred")
            return
        my_file = open("Students.txt", "w")
        students = result.get('data')
        for student in students:
            student_details = str(student.get('id')) + " -- " \
                              + str(student.get('full_name')) + " -- " \
                              + str(student.get('mobile_number')) + " -- " \
                              + str(student.get('age')) + " -- " \
                              + str(student.get('level')) + "\n"
            my_file.write(student_details)
        my_file.close()
        print("Students Data Exported Successfully \n")

# Export Students details to text file function-----
    def get_student_details(self):
        id = input("ID:")

        data = {"id": id }

        result = requests.get(url="http://staging.bldt.ca/api/method/build_it.test.get_student_details", data=data)
        result = json.loads(result.text)
        print(result)
        if result['code'] == 200:
            student = result.get('data')
            my_file = open(str(data['id']) + ".txt", "w")
            student_details = str(student.get('id')) + " -- " \
                              + str(student.get('full_name')) + " -- " \
                              + str(student.get('mobile_number')) + " -- " \
                              + str(student.get('age')) + " -- " \
                              + str(student.get('level')) + "\n"
            my_file.write(student_details)
            my_file.close()
            print("Student Details Exported Successfully")
        else:
            print("Failed to export student details")


student1 = Student(full_name="", age="", level="", mobile_number="")  # create object from Student class.


class Home:
    # print the main menu
    while True:
        print("1.Register New Student\n"
              "2.Edit Student Details\n"
              "3.Delete Student\n"
              "4.Export Students to txt file\n"
              "5.Export Student Details to txt file\n"
              "6.Exit")

        num = int(input("choose from the menu:"))  # turn input into integer.

        if num == 1:
            student1.register_student()
        elif num == 2:
            student1.edit_student_details()
        elif num == 3:
            student1.delete_student()
        elif num == 4:
            student1.get_students()
        elif num == 5:
            student1.get_student_details()
        elif num == 6:
            exit()
        else:
            print("Insufficient entry!")

