############################################################
## CALCULATORROGRAM                                       ##
# This program will:
#   -ask a user for a number
#   -ask a user for a math function
#   -ask a user for another number
#   -calculate the result
#   -ask the user if they would like to continue

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
print "Available operations: "
available_operations = ["plus", "minus", "times", "divided by"]
for op in available_operations:
    print "\t" + op
    #'\t' put a tab in the line, it moves the text over to the right
operation = raw_input("Please enter the mathematic operation: ")
#Make sure the program understands the input
if operation.lower() not in available_operations:
    print "I don't know how to do that!"
    exit()
    
#Ask the user for the first number
second_number_input = raw_input("Please enter the second number: ")
#Then make sure it's really a number!
try:
    second_number = float(second_number_input)
except:
    print second_number_input + " is not a number!"
    exit()
    
if operation.lower() == "plus":
    answer = first_number + second_number
elif operation.lower() == "minus":
    #elif is a fancy was of saying "Else if"
    answer = first_number - second_number
elif operation.lower() == "times":
    answer = first_number * second_number
elif operation.lower() == "divided by":
    # better make sure the second number isn't zero!
    if second_number != 0:
        answer = first_number / second_number
    else:
        print "Cannot divide by 0!"
        exit()
else:
    # if we got here something went really wrong.
    print "Did not find the operator " + operation
    exit()

# Show the user the answer
print first_number_input + " " + operation + " " + second_number_input + " = " + str(answer)
  
