import math

def print_pyramid():
    height_input = input("Enter the height of the pyramid: ")

    if not height_input.isdigit():
        print("Please enter a valid integer for the height.")
        return

    height = int(height_input)

    if height <= 0:
        print("Please enter a positive integer for the height.")
        return

    pi_option = input("Choose the value of pi (enter '22/7' or '3.14'): ").lower()

    if pi_option == '22/7':
        pi_value = 22 / 7
    elif pi_option == '3.14':
        pi_value = 3.14
    else:
        print("Invalid option for pi. Using the default value 3.14.")
        pi_value = 3.14

    for i in range(1, height + 1):
        spaces = " " * (height - i)
        stars = "*" * (2 * i - 1)
        print(spaces + stars)

    print(f"Using the value of pi: {pi_value}")

# Call the function to print the pyramid
print_pyramid()