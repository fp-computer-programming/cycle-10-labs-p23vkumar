#1. Create a Python file named lab_10-4.py
#2. Write a program that contains a function called indexed_names.
#The function should take a list of names as its only parameter.
#3. When a list is passed as an argument to the function, the function
#should return a new list where each value is replaced by the index,
#followed by a color, space, and the original value
#i.e. passing through ["John", "Jane", "Bob"]
##would return ["0: John", "1: Jane", "2: Bob"]
#4. Write 2 test cases to confirm that your function works when passed
#a list that:


def indexed_names(ListOfNames):
#function called indexed_names.
#The function should take a list of names as its only parameter.
    numberedlist = []
    # for index in range enumerate the new list of names
    for i, v in enumerate(ListOfNames):
        #append the list with a number with the name
        numberedlist.append(f'{i}: {v}')
    #print a new list
    print(numberedlist)


        # list is passed as an argument to the function,


print(indexed_names(['Batman Begins (2005)', 'The Dark Knight (2008)', "The Dark Knight Rises (2012)"]))
# function should return a new list where each value is replaced by the index,
#followed by a color, space, and the original value
print(indexed_names(['Man of Steel (2013)', 'Batman vs Superman: Dawn of Justice (2016)', "Zack Synder's Justice League (2021)"]))
print(indexed_names(['Lord of the Rings: Fellowship of the Ring (2001)', 'Lord of the Rings: The Two Towers (2002)', "Lord of the Rings: Return of the King (2003)"]))


