#1. Create a Python file named lab_10-1.py
#2. Using a while loop, write a program that prompts the user to input
#a number.
#3. If the user inputs a number, add that to the sum of the previous
#numbers entered.
#4. If the user enters -1, the program should end and display the sum of
#all the numbers entered.
#5. Be sure the program uses a break statement


totalsum = 0


#2. Using a while loop, write a program that prompts the user to input
#a number.


while True:
    #3. If the user inputs a number, add that to the sum of the previous
#numbers entered.
    inputednumber = int(input("Hello. Please Enter a Number: "))


    if inputednumber == -1:
        #4. If the user enters -1, the program should end and display the sum of
#all the numbers entered.
        print(totalsum) #print total sum with other values
        break #break when inputed value equals -1
    totalsum += inputednumber
    #condition to follow for adding of values
