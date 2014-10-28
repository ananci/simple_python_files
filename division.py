############################################################
## DIVISION PROGRAM                                       ##
# This program will:
#   -ask a user for 2 numbers
#   -divide the 2 numbers
#   -give the user a value and a remainder


print "Welcome to the division program!"
print "This program will take two numbers, divide them and tell you the answer!"

inp_numerator = raw_input("What's the first number? ")
try:
    numerator = int(inp_numerator)
    # what happens if the user puts in a number like 1.2?
    # try using float(inp_numerator) instead of int(numerator)
    # what happens?
except:
    print "That wasn't a number!"
    exit()
    # exit() tell the program to stop and not do anything else

inp_denominator = raw_input("What do you want to divide that number by? " )
try:
    denominator = int(inp_denominator)
except:
    print "That wasn't a number!"
    exit()

if denominator == 0:
    print "You can't divide by 0!"
    exit()

answer = numerator / denominator
# in programming / is the math operator for division

remainder = numerator % denominator
# % is a math operator that gives you a remainder

print str(numerator) + " / " + str(denominator) + " = " + str(answer) + " with a remainder of " + str(remainder)
