#print the menu
print("1. Login")
print("2. Creat User")

#get the option the user selected
while True:
    user_option = input("Would you like to (1) login or (2) create account?")
    #Ensure the user entered a valid option (1 or 2)
    if user_option != 1 and user_option != 2:
        print("\nERROR: Enter a 1 or 2")
        continue
    else:
        print("Yay! Your not dumb!")
        break
    # -if not, ptomt user again
# is user shose 1 ask for user name and password and 
# - validate username and password combination in the user.txt file
# - if not valid combination repromt the user
# - if valid then move on to prompt for student data
#if user chose 2, ask for user name and password and 
# - validate username and passworf lenght. if valid, write to user.tx flie 
# - and move on
#if not valid re prompt user

# promt user to enter student name and number score