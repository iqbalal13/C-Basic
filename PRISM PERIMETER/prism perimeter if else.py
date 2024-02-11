def prism_perimeter(length, width, height, base_shape):
    if base_shape == "rectangle":
        base_perimeter = 2 * (length + width)
        prism_perimeter = base_perimeter * 4  # Assuming a rectangular prism with 4 sides
        return prism_perimeter
    else:
        # Add conditions for other base shapes if needed
        print("Base shape not supported")
        return None

# Example usage
base_shape = input("Enter the base shape of the prism (rectangle, triangle, etc.): ")

if base_shape == "rectangle":
    length = float(input("Enter the length of the rectangular base: "))
    width = float(input("Enter the width of the rectangular base: "))
    height = float(input("Enter the height of the prism: "))
    
    perimeter = prism_perimeter(length, width, height, base_shape)
    if perimeter is not None:
        print(f"The perimeter of the rectangular prism is: {perimeter}")
else:
    print("Base shape not supported")