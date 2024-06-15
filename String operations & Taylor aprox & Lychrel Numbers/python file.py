def question1_vowels():
    # Legal is define to be an element that belong to the letters (a-z or A-z) and aren't belong to lower case vowels
    vowel_string = input()
    lower_case_vowels_string = ['a', 'e', 'i', 'o', 'u', 'y']
    count_illegal_values = 0
    for index in range(0, len(vowel_string)):  # Run of the index of the string
        if vowel_string[index] in lower_case_vowels_string or not vowel_string[index].isalpha():
            # Check if the element at the vowel_string in the index position is legal
            count_illegal_values += 1
    print(len(vowel_string) - count_illegal_values)  # Print the number of legal elements


def calculate_taylor_approximation(x, n):
    # Auxiliary function to calculate the taylor approximation
    approximation_value = 0
    for i in range(1, n + 1):  # Calculate the taylor approximation of the expression ln(1 + x)
        approximation_value = approximation_value + ((-1) ** (i - 1)) * (x ** i) / i
    print(approximation_value)


def check_string_is_a_float(x):
    # Auxiliary function to check if string is a float
    flag = False
    if "." in x:  # Check for float numbers
        split_number = x.split('.')
        if len(split_number) == 2 and split_number[0].isdigit() and split_number[1].isdigit():
            flag = True
    return flag


def check_string_is_negative_number(x):
    # Check if the string is a negative number
    flag = False
    if "-" in x:
        split_number = x.split('-')  # List of element in position 0 before "-" and number after "-" in position 1
        if len(split_number) == 2 and split_number[0] == '':
            if split_number[1].isdigit() or check_string_is_a_float(split_number[1]):
                # Check the number after the minos is legal
                if float(split_number[1]) < 1:
                    flag = True
    return flag


def number_is_validity(x, n):
    flag = False
    if x.isdigit():  # Validity test for x
        flag = True
    elif check_string_is_negative_number(x):
        flag = True
    elif check_string_is_a_float(x):
        flag = True
    return flag


def question2_taylor_approximation():
    x = input()
    n = input()

    if n.isnumeric() or (check_string_is_a_float(n) and float(n) == int(float(n))):  # Validity test for n
        n = int(float(n))  # Change the legal string to int
        if number_is_validity(x, n):  # Validity test for x
            x = float(x)  # Change the legal string to float
            calculate_taylor_approximation(x, n)
        else:
            print("error")
    else:
        print("error")
    exit()


def question3_playing_with_strings():
    #   Program to make even words to upper case and odd words to lower case
    words = input()
    list_words = words.split(" ")
    even_list = []
    odd_list = []
    for index in range(0, len(list_words)):
        # Make every even word to upper case and every odd word to lower case
        if index % 2 == 0:
            even_list.append(list_words[index].upper())
        else:
            odd_list.append(list_words[index].lower())
    #   Sort the lists
    even_list.sort()
    odd_list.sort()
    #   Reverse the odd_list
    odd_list.reverse()
    #   Update the string and print it
    words = " ".join(even_list) + ' ' + " ".join(odd_list)
    print(words)
    exit()


def revers_number(number):  # Program return the value of the revers number
    #   Initiate value to null
    test_num = 0
    while number > 0:  # Initialize the test_num to be the revers number
        #   Define a variable that his value is the unity digit
        remainder = number % 10
        test_num = test_num * 10 + remainder
        number = number // 10
    return test_num


def question4_lychrel_numbers():
    # Program print True if the number is Lychrel number else print number of iterations to get palindrome
    number = int(input())
    backwards_num = revers_number(number)
    counter_iterations = 0
    while number != backwards_num:
        number += backwards_num
        backwards_num = revers_number(number)
        counter_iterations += 1
        if counter_iterations > 500:
            break
    if counter_iterations > 500:
        print("True")
    else:
        print(counter_iterations)


question_number = input()
if question_number == '1':
    question1_vowels()
elif question_number == '2':
    question2_taylor_approximation()
elif question_number == '3':
    question3_playing_with_strings()
elif question_number == '4':
    question4_lychrel_numbers()
else:
    print("error")
