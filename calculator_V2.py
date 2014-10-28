############################################################
## CALCULATOR PROGRAM                                     ##
# This program will:
#   -ask a user for a number
#   -ask a user for a math function
#   -ask a user for another number
#   -calculate the result
#   -ask the user if they would like to continue
# V2 is slightly more sophisticated than V1

import operator
import sys

#make a dictionary of possible operators
available_operations = {"+":operator.add,
                        "plus":operator.add,
                        "add":operator.add,
                        "-":operator.sub,
                        "minus":operator.sub,
                        "subtract":operator.sub,
                        "x":operator.mul,
                        "*":operator.mul,
                        "times":operator.mul,
                        "multiply":operator.mul,
                        "/":operator.div,
                        "divided by":operator.div,
                        "divide":operator.div}

# we want to program to run until the user is done

# set a variable we'll check every time. When it becomes 
# 'False' we will stop running the program
repeat = True

while repeat is True:

    #Ask the user for the first number
    first_number_input = raw_input("Please enter the first number: ")
    #Then make sure it's really a number!
    try:
        first_number = float(first_number_input)
    except:
        print first_number_input + " is not a number!"
        exit()
    #Ask the user for the operation
    #They can chose from:
    # plus, minus, times, divided by

    operation = raw_input("Please enter the mathematic operation: ")
    #Make sure the program understands the input
    while operation.lower() not in available_operations.keys():
        print "I don't know how to do that!"
        print "available options are: "
        for op in available_operations.keys():
            print op 
        operation = raw_input("Please enter the mathematic operation: ")
        
    #Ask the user for the first number
    second_number_input = raw_input("Please enter the second number: ")
    #Then make sure it's really a number!
    try:
        second_number = float(second_number_input)
    except:
        print second_number_input + " is not a number!"
        exit()

    # Try to do the math. if there's a problem 
    try:
        answer = available_operations[operation](first_number, second_number)
    except ZeroDivisionError:
        print "Can't divide by 0!"
        break
    except:
        # if we got here something went really wrong.
        print "Something went wrong!"
        print "Got exception ", sys.exc_info()[0]
        break

    # Show the user the answer
    print first_number_input + " " + operation + " " + second_number_input + " = " + str(answer)
    
    # see if the user wants to continue
    print "\nWould you like to continue?"
    repeat_input = raw_input("Y / N:  ")
    if repeat_input.lower() == "y":
        repeat = True
    else:
        # anything that is not 'y' or 'Y' will cause the program to exit
        repeat = False
        
print "Goodbye"