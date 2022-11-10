import studentController
print("\n\n")
print("1. enter student menu...")
print("2. enter courses menu...")
print("3. enter Registration menu...")
print("4. enter grades menu...")
print("5. Exit program")

while True:
    cmd = int(input())
    
    if (cmd == 1):
        print("\n\n")
        print("1. add student:")
        print("2. delete student:")
        print("3. update student:")
        print("4. list all students:")
        print("5. list student by id:")
        print("6. exit student menu")
        if (input() == 1):
            print("??")
        elif (input() == 2):
            print("??")
        elif (input() == 3):
            print("??")
        elif (input() == 4):
            print("??")
        elif (input() == 5):
            print("??")
        elif (input() == 6):
            break
        else:
            print("??")
    elif (cmd == 2):
        print("\n\n")
        print("1. add course:")
        print("2. delete course:")
        print("3. update course:")
        print("4. list all courses:")
        print("5. list course by id:")
        print("6. exit courses menu")
        if (input() == 1):
            print("??")
        elif (input() == 2):
            print("??")
        elif (input() == 3):
            print("??")
        elif (input() == 4):
            print("??")
        elif (input() == 5):
            print("??")
        elif (input() == 6):
            break
        else:
            print("??")
    elif (cmd== 3):
        print("1. Show the registered courses for a student")
        print("2. Show the registered student for a course")
        print("3. Add courses for students")
        print("4. Drop courses for students")
        print("5. exit Registration menu")
        if (input() == 1):
            print("??")
        elif (input() == 2):
            print("??")
        elif (input() == 3):
            print("??")
        elif (input() == 4):
            print("??")
        elif (input() == 5):
            break
        else:
            print("??")
    elif (cmd == 4):
        print("1. Show the registered courses for a student")
        print("1. add grade to a student:")
        print("2. delete grade to a student:")
        print("3. update grade to a student for one course:")
        print("4. list all grades to a student for all courses:")
        print("5. list grade to a student for a course:")
        print("6. exit grades menu")
        if (input() == 1):
            print("??")
        elif (input() == 2):
            print("??")
        elif (input() == 3):
            print("??")
        elif (input() == 4):
            print("??")
        elif (input() == 5):
            print("??")
        elif (input() == 6):
            break
        else:
            print("??")

    elif(cmd==5):
        break
    else:
        print("wrong command")
        continue