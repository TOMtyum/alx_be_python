try:
   4
    number = int(input("Enter a number to see its multiplication table: "))

    # Generate and print the multiplication table using a for loop
    for i in range(1, 11):
        result = number * i
        print(f"{number} * {i} = {result}")

except ValueError:
    print("Invalid input. Please enter a valid integer.")
