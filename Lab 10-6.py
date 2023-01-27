#1. Create a Python file named lab_10-6.py
#2. Write a function called add_nums that will do the following using a
#try/except loop:
#1. Accept a list of numbers as an argument
#2. Asks a user to input a number
#3. If the user enters a number on a keypad (i.e. ‘7’ and not ‘seven’), add the user
##input to every number in the list
#4. If user enters anything else (input cannot be converted to a number) print an
#error message explaining the problem and prompting to try again
#5. no matter what, the function should print the list passed as an argument and the
#user input, with display text identifying them.
##• ie “passed list: [1,2,3,4] ; user input: twelve”
#3. Write at least 3 test cases for your function, giving all possible outcomes:


#. Write a function called add_nums that will do the following using a
#try/except loop:
#. Accept a list of numbers as an argument


def add_nums(numberedlist):


    #. Asks a user to input a number


    inputednumber = input("Hello User. Please Enter Number: ")


    #print the inputed number
    print(inputednumber)
   
    #. If the user enters a number on a keypad (i.e. ‘7’ and not ‘seven’), add the user
##input to every number in the list
    try:
        for index, value in enumerate(numberedlist):
            numberedlist[index] += int(inputednumber)
    except TypeError:
        print('Hiii. Yeah its me again. Um. Please Try again cause uh your wrong.') #. If user enters anything else (input cannot be converted to a number) print an
#error message explaining the problem and prompting to try again
    finally:
        print(f'Well. You got it so yeah. Passed list: {numberedlist}; Your input was: {inputednumber}') #. no matter what, the function should print the list passed as an argument and the
#user input, with display text identifying them.




#at least 3 test cases for your function, giving all possible outcomes:
add_nums([1,2,3,4])
add_nums([11,12,13,124])
add_nums([21,22,23,24])
add_nums([31,32,33,34])
