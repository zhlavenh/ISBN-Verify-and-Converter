# Importing sys moule to use later in a function to convert print display to a file
import sys

def main():
# Setting varibales for menu choices
    main_selection = 0
    verify_ISBN_10 = 1
    verify_ISBN_13 = 2
    convert_10_to_13 = 3
    convert_13_to_10 = 4
    exit_program = 5
# Need some varibale to use for entering and exiting loops
    counter = None
    file = 0
    main_menu = False
# Home page for main function
    while main_selection != exit_program:
        display_menu()
        main_selection = int(input('What would you like to do? '))
# Option 1: Verfiying check digit of an ISBN 10.
        while main_selection == verify_ISBN_10:
            file_or_input()
            file = int(input('What would you like to do? '))
            while file != 0:
# individual input
                if file == 1:
                    user_ISBN10 = input("Please enter your 10 digit ISBN without dashes.: ")
                    main_menu_option_1(user_ISBN10)
                    counter = go_back_menu("Verify the check digit of an ISBN-10", main_menu)
                    break
# file input
                elif file == 2:
                    print("Ensure ISBNs in your text file have no dashes and are on seperated lines")
                    save_or_nah()
                    save_display = int(input("What would you like to do? "))
# save diplay
                    if save_display == 1:
                        file_name = input("Insert text file name ending in .txt:")
                        new_file_name = input("Name of new text file: ")
                        read_from_file(file_name, main_menu_option_1)
                        save_output(new_file_name, file_name, main_menu_option_1)
                        print(f"Your file named {new_file_name}.txt has been created")
# Display only
                    elif save_display == 2:
                        file_name = input("Insert text file name ending in .txt:")
                        new_file_name = None
                        read_from_file(file_name, main_menu_option_1)
                    counter = go_back_menu("Verify the check digit of an ISBN-10", main_menu)
                    break
            if counter == 1:
                break
# Option 2: Verfiying check digit of an ISBN 13.
        while main_selection == verify_ISBN_13:
            file_or_input()
            file = int(input('What would you like to do? '))
            while file != 0:
                if file == 1:
                    user_ISBN13 = input("Please enter your 13 digit ISBN without dashes.: ")
                    main_menu_option_2(user_ISBN13)
                    counter = go_back_menu("Verify the check digit of an ISBN-13", main_menu)
                    break
                elif file == 2:
                    print("Ensure ISBNs in your text file have no dashes and are on seperated lines")
                    save_or_nah()
                    save_display = int(input("What would you like to do? "))
                    if save_display == 1:
                        file_name = input("Insert text file name ending in .txt:")
                        new_file_name = input("Name of new text file: ")
                        read_from_file(file_name, main_menu_option_2)
                        save_output(new_file_name, file_name, main_menu_option_2)
                        print(f"Your file named {new_file_name}.txt has been created")
                    elif save_display == 2:
                        file_name = input("Insert text file name ending in .txt:")
                        new_file_name = None
                        read_from_file(file_name, main_menu_option_2)
                    counter = int(go_back_menu("Verify the check digit of an ISBN-13", main_menu))
                    break
            if counter == 1:
                break
# Option 3: Converting ISBN 10 to ISBN 13.
        while main_selection == convert_10_to_13:
            file_or_input()
            file = int(input('What would you like to do? '))
            while file != 0:
                if file == 1:
                    user_ISBN10 = input("Please enter your 10 digit ISBN without dashes.: ")
                    main_menu_option_3(user_ISBN10)
                    counter = go_back_menu("Convert and ISBN-10 to an ISBN-13", main_menu)
                    break
                elif file == 2:
                    print("Ensure ISBNs in your text file have no dashes and are on seperated lines")
                    save_or_nah()
                    save_display = int(input("What would you like to do? "))
                    if save_display == 1:
                        file_name = input("Insert text file name ending in .txt:")
                        new_file_name = input("Name of new text file: ")
                        read_from_file(file_name, main_menu_option_3)
                        save_output(new_file_name, file_name, main_menu_option_3)
                        print(f"Your file named {new_file_name}.txt has been created")
                    elif save_display == 2:
                        file_name = input("Insert text file name ending in .txt:")
                        new_file_name = None
                        read_from_file(file_name, main_menu_option_3)
                    counter = go_back_menu("Convert and ISBN-10 to an ISBN-13", main_menu)
                    break
            if counter == 1:
                break
# Option 4: Converting ISBN 13 to ISBN 10.
        while main_selection == convert_13_to_10:
            file_or_input()
            file = int(input('What would you like to do? '))
            while file != 0:
                if file == 1:
                    user_ISBN13 = input("Please enter your 13 digit ISBN withou dashes.: ")
                    main_menu_option_4(user_ISBN13)
                    counter = go_back_menu("Convert an ISBN-13 to an ISBN-10", main_menu)
                    break
                elif file == 2:
                    print("Ensure ISBNs in your text file have no dashes and are on seperated lines")
                    save_or_nah()
                    save_display = int(input("What would you like to do? "))
                    if save_display == 1:
                        file_name = input("Insert text file name ending in .txt:")
                        new_file_name = input("Name of new text file: ")
                        read_from_file(file_name, main_menu_option_4)
                        save_output(new_file_name, file_name, main_menu_option_4)
                        print(f"Your file named {new_file_name}.txt has been created")
                    elif save_display == 2:
                        file_name = input("Insert text file name ending in .txt:")
                        new_file_name = None
                        read_from_file(file_name, main_menu_option_4)
                    counter = go_back_menu("Convert an ISBN-13 to an ISBN-10", main_menu)
                    break
            if counter == 1:
                break
# Exiting program from main menu
        if main_selection == exit_program:
            print('\nGoodbye')
            break
# Need to add a pass to exit directly from go back menu loop
        if counter == 1:
            pass
# User validation prompt
        else:
            print('Invalid entry. Please select from the menu options.****exit kickback')

# Defining Functions for program
# Display Menu
def display_menu():
    print('''
                .-~~~~~~~~~-._       _.-~~~~~~~~~-.
            __.'              ~.   .~              `.__
          .'//                  \./                  \\`.
        .'//                     |                     \\`.
      .'// .-~"""""""~~~~-._     |     _,-~~~~"""""""~-. \\`.
    .'//.-"                 `-.  |  .-'                 "-.\\`.
  .'//______.============-..   \ | /   ..-============.______\\`.
.'______________________________\|/______________________________`.
    ''')
    print('Welcome To The Python ISBN Conversion Menu \n')
    print('1. Verify the check digit of an ISBN-10')
    print('2. Verify the check digit of an ISBN-13')
    print('3. Convert an ISBN-10 to an ISBN-13')
    print('4. Convert and ISBN-13 to an ISBN-10')
    print('5. Exit \n')

def main_menu_option_1(user_ISBN10):
    multiplier = 0
    index_of_ISBN = -1
    sum_of_ISBN = 0
    if len(user_ISBN10) < 10 or len(user_ISBN10) > 10:
        user_ISBN10 = input("Invlaid number of digits. Please enter your 10 digit ISBN without dashes: ")
    while multiplier <= 9:
        while len(user_ISBN10) == 10:
            user_ISBN10_ncs = list(user_ISBN10)
            user_ISBN10_ncs.pop(-1)
            break
        sum_of_ISBN += int(user_ISBN10_ncs[index_of_ISBN]) * multiplier
        index_of_ISBN += 1
        multiplier += 1
    ISBN10_check_digit = sum_of_ISBN % 11
    if  ISBN10_check_digit == 10:
        print (f"The ISBN: {user_ISBN10} should have a check digit of X" )
    elif ISBN10_check_digit < 10 or ISBN10_check_digit >= 0:
        print(f"The ISBN: {user_ISBN10} should have a check digit of {ISBN10_check_digit}")
    else:
        print("There was an error processing you request. Please try again")

def main_menu_option_2(user_ISBN13):
    multiplier = [1, 3, 1, 3, 1, 3, 1, 3, 1, 3, 1, 3]
    sum_of_ISBN = 0
    index_of_ISBN = 0
    if len(user_ISBN13) < 13 or len(user_ISBN13) > 13:
        user_ISBN13 = input("Invlaid number of digits. Please enter your 10 digit ISBN without dashes: ")
    elif "978" not in user_ISBN13:
        user_ISBN13 = input("Your ISBN-13 does not contain 978. Please enter a valid ISBN 13.: ")
    while len(user_ISBN13) == 13:
        user_ISBN13_ncs = list(user_ISBN13)
        user_ISBN13_ncs.pop(-1)
        break
    for i in multiplier:
        sum_of_ISBN += int(user_ISBN13_ncs[index_of_ISBN]) * i
        index_of_ISBN += 1
    ISBN13_check_digit = sum_of_ISBN % 10
    if ISBN13_check_digit != 0 and ISBN13_check_digit != 1:
        ISBN13_check_digit = 10 - ISBN13_check_digit
        print(f"The ISBN: {user_ISBN13} should have a check digit of {ISBN13_check_digit}")
    elif ISBN13_check_digit == 0:
        print (f"The ISBN: {user_ISBN13} should have a check digit of X" )
    else:
        print("There was an error processing you request. Please try again")

def main_menu_option_3(user_ISBN10):
    ISBN13_ncs = ["9", "7", "8"]
    multiplier = [1, 3, 1, 3, 1, 3, 1, 3, 1, 3, 1, 3]
    sum_of_ISBN = 0
    index_of_ISBN = 0
    if len(user_ISBN10) < 10 or len(user_ISBN10) > 10:
        user_ISBN10 = input("Invlaid number of digits. Please enter your 10 digit ISBN without dashes: ")
    else:
        user_ISBN10_ncs = list(user_ISBN10)
        user_ISBN10_ncs.pop(-1)
        ISBN13_ncs.extend(user_ISBN10_ncs)
    for i in multiplier:
        sum_of_ISBN += int(ISBN13_ncs[index_of_ISBN]) * i
        index_of_ISBN += 1
    ISBN13_check_digit = sum_of_ISBN % 10
    if ISBN13_check_digit != 0 and ISBN13_check_digit != 1:
        ISBN13_check_digit = 10 - ISBN13_check_digit
        ISBN13_ncs.append(str(ISBN13_check_digit))
        ISBN13_wcs = ISBN13_ncs
        ISBN13_wcs.insert (3, "-")
        ISBN13_wcs.insert (5, "-")
        ISBN13_wcs.insert (8, "-")
        ISBN13_wcs.insert (-1, "-")
        ISBN13_wcs = "".join(ISBN13_wcs)
        print(f"Your ISBN 13 is {ISBN13_wcs}")
    elif ISBN13_check_digit == 0:
        ISBN13_ncs.append("X")
        ISBN13_wcs = ISBN13_ncs
        ISBN13_wcs.insert (3, "-")
        ISBN13_wcs.insert (5, "-")
        ISBN13_wcs.insert (8, "-")
        ISBN13_wcs.insert (-1, "-")
        ISBN13_wcs = "".join(ISBN13_wcs)
        print (f"Your ISBN 13 is{ISBN13_wcs}")
    else:
        print("There was an error processing you request. Please try again")

def main_menu_option_4(user_ISBN13):
    multiplier = 0
    index_of_ISBN = -1
    sum_of_ISBN = 0
    if len(user_ISBN13) < 13 or len(user_ISBN13) > 13:
        user_ISBN13 = input("Invlaid number of digits. Please enter your 13 digit ISBN withou dashes: ")
    elif len(user_ISBN13) == 13:
        if "978" not in user_ISBN13:
            user_ISBN13 = input("Your ISBN-13 does not contain 978. Please enter a valid ISBN 13.: ")
    user_ISBN13 = list(user_ISBN13)
    del user_ISBN13[0:3]
    user_ISBN13.pop(-1)
    ISBN10_ncs = user_ISBN13
    while multiplier <= 9:
        sum_of_ISBN += int(ISBN10_ncs[index_of_ISBN]) * multiplier
        index_of_ISBN += 1
        multiplier += 1
    ISBN10_check_digit = sum_of_ISBN % 11
    if  ISBN10_check_digit == 10:
        ISBN10_ncs.append("X")
        ISBN10_ncs.insert (1, "-")
        ISBN10_ncs.insert (4, "-")
        ISBN10_ncs.insert (-1, "-")
        ISBN10_wcs = "".join(ISBN10_ncs)
        print (f"Your ISBN 10 is {ISBN10_wcs}" )
    elif ISBN10_check_digit < 10 or ISBN10_check_digit >= 0:
        ISBN10_ncs.append(str(ISBN10_check_digit))
        ISBN10_ncs.insert (1, "-")
        ISBN10_ncs.insert (4, "-")
        ISBN10_ncs.insert (-1, "-")
        ISBN10_wcs = "".join(ISBN10_ncs)
        print(f"Your ISBN 10 is {ISBN10_wcs}")
    else:
        print("There was an error processing you request. Please try again")

def go_back_menu(c_method, var):
    secondary_selection = 0
    print (f"\nCurrent Method: {c_method}")
    print("1. Another ISBN using same method")
    print("2. Main menu")
    secondary_selection = int(input('What would you like to do? '))

    while var == False:
        if secondary_selection == 1:
            break
        elif secondary_selection == 2:
            var = True
            break
        else:
            print("You've entered an invlaid option please selction fomr the menu below.")
            go_back_menu()

    if var == True:
        return 1

def file_or_input():
    print('Would you like to type an ISBN or read from text file?')
    print('1. Type ISBN')
    print('2. Read from file')

def save_or_nah():
    print('Save to new file or just display on screen?')
    print("1. Display and save")
    print("2. Just Display")

def read_from_file(fileName, methodToRun):
    with open(f'{fileName}', 'r') as main_file:
        file_contents = main_file.readlines()
        for line in file_contents:
            user_ISBN10 = line.rstrip('\n')
            methodToRun(user_ISBN10)
    main_file.close()

def save_output(newfile, file_name, methodToRun):
    original_stdout = sys.stdout
    with open(f"{newfile}.txt", "w") as f:
        sys.stdout = f
        read_from_file(file_name, methodToRun)
        sys.stdout = original_stdout
    f.close()

#Calling main function
main()
