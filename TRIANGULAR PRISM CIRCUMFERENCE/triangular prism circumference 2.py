import math

def triangular_prism_properties(a, b, c, h):
    perimeter = a + b + c + 2 * h
    area_base = herons_formula(a, b, c)
    surface_area = area_base * 2 + perimeter * h
    return perimeter, surface_area

def herons_formula(a, b, c):
    s = (a + b + c) / 2
    area = math.sqrt(s * (s - a) * (s - b) * (s - c))
    return area

# User input with error handling
try:
    side_a = float(input("Enter the length of side a: "))
    side_b = float(input("Enter the length of side b: "))
    side_c = float(input("Enter the length of side c: "))
    height = float(input("Enter the height of the triangular prism: "))
    
    if side_a <= 0 or side_b <= 0 or side_c <= 0 or height <= 0:
        raise ValueError("All side lengths and height must be positive.")
    
    perimeter, surface_area = triangular_prism_properties(side_a, side_b, side_c, height)
    
    print("Perimeter:", perimeter)
    print("Surface Area:", surface_area)

except ValueError as e:
    print(f"Error: {e}. Please enter valid positive numerical values.")
except Exception as e:
    print(f"An unexpected error occurred: {e}")