print("Simple Calculator")
print("Enter first number")
a = float(input())
print("Enter second number")
b = float(input())
print("Choose operation")
print("1 Add")
print("2 Subtract")
print("3 Multiply")
print("4 Divide")
choice = input()
if choice == "1":
    print("Result:", a + b)
elif choice == "2":
    print("Result:", a - b)
elif choice == "3":
    print("Result:", a * b)
elif choice == "4":
    if b != 0:
        print("Result:", a / b)
    else:
        print("Cannot divide by zero")
else:
    print("Invalid choice")
