#In this file are functions for PassHelper
import string

def check_specials(password):
    specials = 0
    special_list = "! @ $ % ^ & * ( ) _ - + = { } [ ] |  , . > < / ? ~ ` ' : ;".split()
    for char in password:
        if char in special_list:
            specials += 1
    if specials > 0:
        return True
    else:
        return False


def check_big_letters(password):
    uppers = 0
    upper_list = "A B C D E F G H I J K L M N O P Q R S T U V W X Y Z".split()
    for char in password:
        if char in upper_list:
            uppers += 1
    if uppers > 0:
        return True
    else:
        return False


def check_small_letters(password):
    lowers = 0
    lower_list = "a b c d e f g h i j k l m n o p q r s t u v w x y z".split()
    for char in password:
        if char in lower_list:
            lowers += 1
    if lowers > 0:
        return True
    else:
        return False


def check_numbers(password):
    numbers = 0
    number_list = "1 2 3 4 5 6 7 8 9 0".split()
    for char in password:
        if char in number_list:
            numbers += 1
    if numbers > 0:
        return True
    else:
        return False


def check_len(password):
    if len(password) >= 8:
        return True
    else:
        return False


def validate_password(password):
    check_dict = {
        'upper': check_big_letters(password),
        'lower': check_small_letters(password),
        'number': check_numbers(password),
        'special': check_specials(password),
        'len': check_len(password)
    }
    if check_big_letters(password) & check_small_letters(password) & check_numbers(password) & check_specials(password) & check_len(password):
        return True
    else:
        print("Invalid password! Review below and change your password accordingly!")
        if check_dict['upper'] == False:
            print("Password needs at least one upper-case character.")
        if check_dict['lower'] == False:
            print("Password needs at least one lower-case character.")
        if check_dict['number'] == False:
            print("Password needs at least one number.")
        if check_dict['special'] == False:
            print("Password needs at least one special character.")
        if check_dict['len'] == False:
            print("Password needs to be at least 8 characters in length.")
