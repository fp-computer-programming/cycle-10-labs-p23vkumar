#1. Create a Python file named lab_10-2.py
#2. Using the same approach as lab 1, write a program that prints all
#the numbers that are multiples of 3 in a list. Be sure your program
#uses a continue statement


#Using the same approach as lab 1, write a program that prints all
#the numbers that are multiples of 3 in a list. Be sure your program


#created function multiples of three
def multiplesofthree():


    #list is equal to parenthesses
    List = []


    while True:
        #ask user to input a multiple of three
        inputednumber = int(input("Hello. Please Enter a Number that is only a multiple of three: "))
        #if inputed value is a multiple of three
        if inputednumber%3:
            print(List) #print(list)
            break
        #if user enters -1
        #official list
        elif inputednumber == -1:
            print(List)
            break #break the statement once done
        #append each value of a multiple of three to the list aside from -1
        else:
            List.append(inputednumber)


#close function
multiplesofthree()


