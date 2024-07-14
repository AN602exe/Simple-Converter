# Let's try to make a number base converter (Decimal, Hexadecimal, Binary)
print("Welcome to the number converter, type 1 for hexadecimal or 2 for binary: ")
# Declaration of the function for the converter with the relative parameter
def converter(choice):
# First condition for the function choice
    if choice == '1':
        print("You have chosen the decimal to hexadecimal converter, enter your number: ")
        num = input()
        print("Your number in hexadecimal is: " + hex(int(num)))
# Second condition for the function choice, using elif to consider another possibility
    elif choice == '2':
        print("You have chosen the decimal to binary converter, enter your number: ")
        num = input()
        print("Your number converted to binary is: " + bin(int(num)))
# Function call
converter(input())
