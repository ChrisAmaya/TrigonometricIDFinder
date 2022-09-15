# Addi Amaya
# Sept 13 2022

#----------------------Purpose-----------------------
# Given a trig type this program will return related Identities
#----------------------User Notes----------------------
# all trig input should be in the format of TRIG(x) or TRIG(-x)
# Anything else wont work, look at the if statements
#----------------------Program------------------------
# Can add more Identities!
# \n means "newline" I added it for readability
def Identifier(InputTrig):
    # cos(x)
    if InputTrig == "cos(x)":
        print('\nsin(pi/2 - x)\n')
        print('cos(-x)\n')
        print('sin(2x) / 2sin(x)\n')
    # cos^2(x)
    elif InputTrig == "cos^2(x)":
        print('\n1-sin^2(x)\n')
        print('cos(2x) + sin^2(x)\n')
        print('(1 + cos(2x)) / 2\n')
    # sin(x)
    elif InputTrig == "sin(x)":
        print('\nsin(2x) / 2cos(x)\n')
        print('sin(pi - x)\n')
    # sin^2(x)
    elif InputTrig == "sin^2(x)":
        print('\n1 - cos^2(x)\n')
        print('(1 - cos(2x)) / 2\n')
        print('cos^2(x) - cos(2x)\n')
    # sec^2(x)
    elif InputTrig == "sec^2(x)":
        print('\n1 + tan^2(x)\n')
    # csc^2(x)
    elif InputTrig == "csc^2(x)":
        print("\n1 + cot^2(x)\n")
    # sin(x +/- y)
    elif InputTrig == "sin(x +/- y)":
        print("\nsin(x)cos(y) +/- cos(x)sin(y)\n")
    # sin(2x)
    elif InputTrig == "sin(2x)":
        print("\n2sin(x)cos(x)\n")
    # cos(2x)
    elif InputTrig == "cos(2x)":
        print("\ncos^2(x) - sin^2(x)\n")
        print("2cos^2(x) - 1\n")
        print("1 - 2sin^2(x)\n")
    # sin(-x)
    elif InputTrig == "sin(-x)":
        print("\n-sin(x)\n")
    # cos(x +/- y)
    elif InputTrig == "cos(x +/- y)":
        print("\ncos(x)cos(y) +/- sin(x)sin(y)\n")
    # cos(-x)
    elif InputTrig == "cos(-x)":
        print("\ncos(x)\n")
    # -cos(x)"
    elif InputTrig == "-cos(x)":
        print("\ncos(pi - x)\n")
    # tan(x +/- y)
    elif InputTrig == "tan(x +/- y)":
        print("\n(tan(x) +/- tan(y)) / (1 +/- tan(x)tan(y))\n")
    else:
        print('\n--------------------------------Error------------------------------')
        print("\nThe Input was either Invalid or there are no Trigonometric Identities\n")
        print("Make sure that the input is in the form trig(argument)\n")
        print("Example: cos(2pix) should be typed as cos(x) for the sake of the program\n")
        print('-------------------------------------------------------------------')


# Where the indentifier function is called
def main():
    # An endless loop so you dont have to restart the program everytime
    while(1):
        GivenTrig = input("What is the Trig that You want to Find an ID For? ")
        Identifier(GivenTrig)
#--------------Where the Program Executes--------------
# A good habit to structure code like this
if __name__ == "__main__":
    main()
