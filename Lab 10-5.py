#1. Create a Python file named lab_10-5.py
#2. Write a function called add_foods that will do the following using a try/except
#loop:
#1. Accept a list as an argument
#2. Add the sixth letter of each food to a new list variable, sixth_letter
#3. If the food is not a string, add the item to a new list variable, not_foods
#4. If the string does not have six letters, add the entire string to a new list variable,
#short_foods
#5. Print each output so the name of the list precedes the content of the list, separated by a
#colon.
#3. Use the following inputs to test your function:


#Write a function called add_foods that


def add_foods(FoodList):


    #variables to define empty lsit within paremeters
    sixth_letter = []    #variables to define empty lsit within paremeters


    not_foods = []    #variables to define empty lsit within paremeters


    short_foods = []    #variables to define empty lsit within paremeters


        #for items in the list or range
    for x in FoodList:


        #will do the following using a try/except
        #loop:      
        try:
            sixth_letter.append(x[5]) #Add the sixth letter of each food to a new list variable, sixth_letter
        except TypeError:
            not_foods.append(x) #. If the food is not a string, add the item to a new list variable, not_foods
        except IndexError:
            short_foods.append(x) #. If the string does not have six letters, add the entire string to a new list variable,
#short_foods


            #define variable to enclose formating
    x = f'The Sixth Letter Foods are:: {sixth_letter}'
    y = f'The Not foods are:: {not_foods}'
    z = f'The Short Foods are:: {short_foods}'
    #print the variables in order
    print(x)
    print(y)
    print(z)    


#close functions off
#create three test cases to try and produce
#accurate results


add_foods(['potatoes','salsa','cherries','banana','apple'])
add_foods(['naan','celery','buckwheat',7,'clementine'])
add_foods(['cheeseburger',True,'chicken','rice','radish'])
