import math

def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "Error! Division by zero."
    else:
        return x / y
    
def exponentiate(x, y):
    return x ** y

def square_root(x):
    if x < 0:
        return "Error! Cannot compute square root of a negative number"
    else:
        return math.sqrt(x)
    
def main():

    while True:
        print("================Welcome to Calculator!================")
        print("Select operation:")
        print("1.add")
        print("2.subtract")
        print("3.multiply")
        print("4.divide")
        print("5.exponentiate")
        print("6.square_root")
        choice = input("Enter choice (1/2/3/4/5/6): ")

        if choice in ('1', '2', '3', '4', '5', '6'):
            if choice in ('1', '2', '3', '4', '5'):
                num1 = float(input("Enter first number: "))
                num2 = float(input("Enter second number: "))

            else:
                num1 = float(input("Enter a number: "))

            if choice == '1':
                print("Result:", add(num1, num2))
            elif choice == '2':
                print("Result:", subtract(num1, num2))
            elif choice == '3':
                print("Result:", multiply(num1, num2))
            elif choice == '4':
                print("Result:", divide(num1, num2))
            elif choice == '5':
                print("Result:", exponentiate(num1, num2))
            elif choice == '6':
                print("Result:", square_root(num1))

            another_calculation = input("Do you want to perform anther calculation? (yes/no): ")
            if another_calculation.lower() != "yes":
                print("Thank you for using Calculator")
                break
        else:
            print("Invalid input. Please enter a valid number.")

if __name__ == "__main__":
    main()