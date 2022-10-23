class Student:

def main():
    student = get_student()
    print (f"{student.name} is from {student.house}")

def get_student():
    student = Student()
    student.name = input ("Name: ")
    student.house = input ("House: ")
    return student

if __name__ == "__main__":
    main()

'''
def main():
    student = get_student()
    if student ["name"] == "Sultan":
        student ["house"] = "Sargodha"
    print (f"{student['name']} is from {student['house']}")

def get_student():
    student =
    name = input("Name: ")
    house = input("House: ")
    return {"name": name, "house": house}

if __name__ == "__main__":
    main()
'''