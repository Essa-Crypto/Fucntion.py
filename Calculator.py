def add (P, Q):
    return P + Q
def subtract (P, Q):
    return P - Q
def multiply (P, Q):
    return P * Q
def divide (P, Q):
    return P / Q

choice = input("Please enter your choice (Addition/ Subtraction/ Multiply/ Division): ")

num_1 = int (input ("Please enter the first number: "))
num_2 = int (input ("Please enter the second number: "))

if choice == 'Addition':
    print (num_1, " + ", num_2, " = ", add(num_1, num_2))

elif choice == 'Subtraction':
    print (num_1, " - ", num_2, " = ", subtract(num_1, num_2))

elif choice == 'Multiply':
    print (num_1, " * ", num_2, " = ", multiply(num_1, num_2))

elif choice == 'Division':
    print (num_1, " / ", num_2, " = ", divide(num_1, num_2))

else:
    print ("This is an invalid input")

