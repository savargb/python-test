def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    return x / y 
         
while True:
    print("\n--- simple calculator ---")
    print("1. add")
    print("2. subtract")
    print("3. multiply")
    print("4. divide")
    print("5. stop")

    choice = input("Enter choice(1/2/3/4/5): ")

    if choice == "5":
        print("bye")
        break
        
    elif choice in ("1", "2", "3", "4"):
        
        try:
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter the second number: "))
            
            if choice == "1":
                print(num1, "+", num2, "=", add(num1, num2))
            elif choice == "2":
                print(num1, "-", num2, "=", subtract(num1, num2))
            elif choice == "3":
                print(num1, "*", num2, "=", multiply(num1, num2))
            elif choice == "4":
                print(num1, "/", num2, "=", divide(num1, num2))
                
        except ValueError:
            print("Error: Invalid input! Please enter numbers only.")
        except ZeroDivisionError:
            print("Error: Cannot divide by zero!")
            
    else:
        print("Invalid Choice. Please enter a number from 1 to 5.")
