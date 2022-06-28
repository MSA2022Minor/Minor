print the menu

def print_main_menu():
    print("Select option from Menu\n-----------------------")
    print("1. Login")
    print("2. Create User")
    return

def get_user_option():
    print_main_menu
    while True:
        user_option = input("Would you like to (1) login or (2)create account? ")
        #Ensure the user entered a valid option (1 or 2)
        if user_option != "1" and user_option != "2":
            # -if not, prompt user again
            print("\nERROR: Enter a 1 or 2")
            continue
        else:
            print("YaY! Good input")
            break     
    return user_option
#prompt and get the option the user selected
def main():
    print_main_menu()
    user_option = get_user_option()


    if user_option == "1":
        while True:
            #If user chose 1, ask for user name and password
            user_name = input("Please enter your user name: ")
            user_pass = input("Please enter your password: ")
            # - validate username and password combination in the users.txt file
            #open the users files
            user_file = open("users.txt", "r")
            user_found = False

            #read the lines from the file
            for line in user_file:
                credentials = line.split(", ")
                #compare username and password for a match
                if user_name == credentials[0] and user_pass == credentials[1].rstrip():
                    user_found = True
                    break

            if user_found:
                # - if valid then move on to prompt for student data
                print(f"User {user_name} successfully logged in!\n")
                break
            else:
                # - if not valid combination reprompt the user. 
                print(f"User {user_name} not found!\n")
            
        
            
            

#If user chose 2, ask for user name and password and
elif user_option == "2":
    while True:
        user_name = input("Please enter your user name (4 - 12 characters): ")
        user_pass = input("Please enter your password (6 - 16 characters): ")

        user_name_length = len(user_name)
        user_pass_length = len(user_pass)

        if (user_name_length >= 4 and user_name_length <= 12) and (user_pass_length >= 6 and user_pass_length <= 16):
            #write user and pass to file
            user_file = open("users.txt", "a")
            user_file.write(f"{user_name}, {user_pass}\n")
            user_file.close()
            break
        else:
            print("ERROR: Inncorrect Username and or Password Length.")

print("Ask user for student data.")
#create 3 empty lists
student_names = []
student_scores = []
student_letter_grades = []
#Ask user how many students to enter data for
number_of_students = int(input("Enter number of student to enter grades for: "))

for counter in range(number_of_students):
    #prompt user to enter student name and number score
    student_name = input("Enter student name: ")
    student_score = float(input("Enter student score: "))

    #store data somewhere
    student_names.append(student_name)
    student_scores.append(student_score)

    #convert the number score to a letter grade 
    if student_score >= 90:
        student_letter_grades.append("A")
    elif student_score >= 80:
        student_letter_grades.append("B")
    elif student_score >= 70:
        student_letter_grades.append("C")
    elif student_score >= 60:
        student_letter_grades.append("D")
    else:
        student_letter_grades.append("F")

#Print student data(name, score, grade)
for index in range(len(student_names)):
    print(f"{student_names[index]} : {int(student_scores[index])}% : {student_letter_grades[index]}")

#Calculate and print class average
average_list = []

total = 0
for index in range(len(student_scores)):
    total = total + student_scores[index]
average = total / len(student_scores)

if average >= 90:
        average_list.append("A")
elif average >= 80:
        average_list.append("B")
elif average >= 70:
        average_list.append("C")
elif average >= 60:
        average_list.append("D")
else:
        average_list.append("F")
        
print(f"Average: {int(round(average, 2))}% {average_list}")




    
