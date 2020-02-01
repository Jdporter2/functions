'''
@author: amayamunoz
'''

'''
For this assignment you should read the task, then below the task do what it asks you to do.
For tasks with return statements, you can test out if you are correct by 
calling the function and printing what is returned
EXAMPLE TASK:
'''
#EX) Define a function that adds two numbers and returns the result
#def add_two_numbers(num1, num2):
#    sumOfTwoNumbers = num1 + num2
#    return sumOfTwoNumbers

'''
END OF EXAMPLE
'''

'''
START HERE
'''


#1) Define a function that subtracts the second number from the first number. Return the result.
def subtract(num1, num2):
    differenceOfTwoNumbers = num1 - num2
    return differenceOfTwoNumbers

#2) Define a function that divides a number by 2, multiplies it by 77, and then adds 10000. Return the result.
def divide(num1):
    division = num1/2 * 77 + 10000
    return division
#3) Define a function that checks if two numbers are equal. If they are equal, return true. If they are not equal, return false.
def equivalent(num1,num2):
    check_if_equal = num1 == num2
    return check_if_equal
#4) Define a function that takes in two numbers and returns the larger number. If they are the same, it should just return that number.
def larger(num1, num2):
    if num1 >= num2:
        larger_number = num1
        return larger_number
    else:
        larger_number = num2
        return larger_number
    
#5) Define a function that takes in two words and returns a string that contains both words combined.
def twoWords(word1,word2):
    words_combined = word1 + word2
    return words_combined
#6) Define a function that takes in three numbers. If the first number is equal to the second OR the third number, return true. Else, return false.
def threeNumbers(num1,num2,num3):
    if num1 == num2 or num1 == num3:
        three_numbers = True
        return three_numbers
    else:
        three_numbers = False
        return three_numbers
#7) Define a function that prints your name.
def myName(name):
    my_name = name
    return my_name

my_name = myName("Josh")
print(my_name)
#8) Define a function that takes in a string that is the name of a color. If that string is equal to your favorite color, it prints "That's my favorite color!" If it is not, it prints "That is not my favorite color. Try again."
color = "Orange"
def favoriteColor(color):
    if color == "Purple":
        favoriteColor = True
    else:
        favoriteColor = False
if favoriteColor == True:
    print("That's my favorite color!")
else:
    print("That is not my favorite color. Try again.")
#9) Define a function that takes in a number. If the number is not equal to zero, the function runs a loop until the number reaches 0. HINT: Within the loop, keep subtracting 1 from the number.
def givenNumber(number):
    usernum = number
    return usernum
usernum = givenNumber(8)
while (usernum == 0) == False:
    usernum -= 1
    print(usernum)
    
'''YOUR OWN FUNCTION'''

#10) Define a function that takes in a string, if that string is my name, it will print "Correct"
name = "NotJosh"
def personalizedName(name):
    if name == "Josh":
        personalizedName = True
    else:
        personalizedName = False
if personalizedName == True:
    print("Correct!")
else:
    print("That is not my name. Try again.")
