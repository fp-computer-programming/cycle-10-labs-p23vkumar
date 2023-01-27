#1. Create a Python file named lab_10-3.py
#2. Write a program that contains a function called double_stuff.
#The function should take a list as its only parameter.
##3. When a list is passed as an argument to the function, the function
##should double each value in the list, regardless of its type
#4. Write test cases to confirm that your function works when passed a
#list that:
#1. Contains only integers
#2. Contains integer and float values
#3. Contains a combination of integer, string, and float values


#function called double_stuff to take in double list as argument
def double_stuff(doublelist):
    #enumerate list
    #Allows the index and value of a sequence to be used
    for i, v in enumerate(doublelist):
        doublelist[i] = v * 2 #condition that each value in the list doubles
    print(doublelist) #print the list




#1. Contains only integers
print(double_stuff([8, 22, 54, 67, 90]))
#2. Contains integer and float values
print(double_stuff([7, 2, 9, 3.456, 3.141529]))
#3. Contains a combination of integer, string, and float values
print(double_stuff([6,'Music', 'Sports', 3.1]))
