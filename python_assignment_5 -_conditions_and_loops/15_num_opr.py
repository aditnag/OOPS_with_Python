# 15. Take integer inputs from user until he/she presses q ( Ask to press q to quit after every integer input ). Print average and product of all numbers.

numbers = []
while True:
    user_input = input("Enter an integer or press 'q' to quit: ")
    if user_input == 'q':
        break
    else:
        try:
            number = int(user_input)
            numbers.append(number)
        except ValueError:
            print("Invalid input! Please enter an integer.")

if numbers:
    product = 1
    for number in numbers:
        product *= number
    average = sum(numbers) / len(numbers)
    print(f"Product of all the entered numbers: {product}")
    print(f"Average of all the entered numbers: {average}")
else:
    print("No numbers were entered.")
