a = float(input("input a number:"))
b = float(input("input another number:"))

choice = input("choose an operation (+, -, *, /): ")

if choice == "+":
    result = a + b
elif choice == "-":
    result = a - b
elif choice == "*":
    result = a * b
elif choice == "/":
    result = a / b

print("The result is:", result)
