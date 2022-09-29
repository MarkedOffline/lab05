########################################################################
##
## CS 101 Lab
## Program # 5
## Name Gabe Gonzalez
## Email irvin.glz1995@gmail.com
##
## PROBLEM : Describe the problem
##
## ALGORITHM :
##      1. Write out the algorithm
##
## ERROR HANDLING:
##      Any Special Error handling to be noted.  Wager not less than 0. etc
##
## OTHER COMMENTS:
##      Any special comments
##
########################################################################


# import statements

# functions
def get_school(l_card):
    school = ''
    if (l_card[5] == '1'):
        school = 'School of Computing and Engineering SCE'
    elif (l_card[5] == '2'):
        school = 'School of Law'
    elif (l_card[5] == '3'):
        school = 'College of Arts and Sciences'
    else:
        school = 'Invalid School'
    return school


def get_grade(l_card):
    if (l_card[6] == '1'):
        grade = 'Freshman'
    elif (l_card[6] == '2'):
        grade = 'Sophomore'
    elif (l_card[6] == '3'):
        grade = 'Junior'
    elif (l_card[6] == '4'):
        grade = 'Senior'
    else:
        grade = 'Invalid Grade'
    return grade


def character_value(character):
    if ord(character) - 65 >= 0 or ord(character) < 25:
        character = abs(65 - ord(character))
    return character


def get_check_digit(l_card):
    check_digit = 0
    for i in range(len(l_card)):
        check_digit += int(character_value(l_card[i])) * int(i + 1)
    check_digit %= 10
    return check_digit


def find_bad_character(library_card, alpha_or_digit):
    if (alpha_or_digit == 1):
        for i in range(len(library_card)):
            if (library_card[i].isalpha() == False):
                return [i, library_card[i]]
    elif (alpha_or_digit == 2):
        for i in range(len(library_card)):
            if (library_card[i].isdigit() == False):
                return [i, library_card[i]]


def verify_check_digit(l_card):
    error = ''
    passed = False

    if (len(l_card) != 10):
        error = "The length of the number given must be 10"
        passed = False
    elif ((l_card[0:5]).isalpha() == False):
        passed = False
        error = f"The first 5 characters must be A-Z, the invalid character is at {find_bad_character(l_card, 1)[0]} is {find_bad_character(l_card, 1)[1]}"
    elif ((l_card[7:10]).isdigit() == False):
        passed = False
        error = f"The last 3 characters must be 0-9, the invalid character is at {find_bad_character(l_card, 2)[0]} is {find_bad_character(l_card, 2)[0]}"
    elif (get_school(l_card) == 'Invalid School'):
        passed = False
        error = "The sixth character must be 1 2 or 3"
    elif (get_grade(l_card) == 'Invalid Grade'):
        passed = False
        error = "The seventh character must be 1 2 3 or 4"
    elif (int(get_check_digit(l_card)) != int(l_card[9])):
        passed = False
        error = f"Check Digit {l_card[9]} does not match calculated value {get_check_digit(l_card)}."
    else:
        passed = True
        error = ''

    return (passed, error)


if __name__ == "__main__":
    # main program
    ''' print("Main Program")
    print('{:^50}'.format('Linda Hall'))
    print('{:^50}'.format('Library Card Check'))
    print('='*50)

    l_card = ('Enter Library Card. Hit Enter to Exit ==>')'''
