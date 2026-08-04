# Traffic Light Assisstant
print("="*30)
print("Traffic Light Assistant")
print("="*30)

while True:
    print("\nPlease select the traffic light color:")
    print("1. Red")
    print("2. Yellow")
    print("3. Green")

    choice = input("Enter your choice (1-3): ")

    if choice == '1':
        print("\nRed Light: Stop!")
    elif choice == '2':
        print("\nYellow Light: Get Ready!")
    elif choice == '3':
        print("\nGreen Light: Go!")
        break
    else:
        print("\nChoose again")
