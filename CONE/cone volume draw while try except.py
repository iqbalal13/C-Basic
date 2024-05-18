import turtle

def draw_cone(height, radius):
    # Set up the Turtle screen
    screen = turtle.Screen()
    screen.bgcolor("white")

    # Create a Turtle object
    cone_turtle = turtle.Turtle()
    cone_turtle.speed(2)

    try:
        # Draw the cone
        cone_turtle.penup()
        cone_turtle.goto(0, -height/2)
        cone_turtle.pendown()
        cone_turtle.circle(radius, 180)
        cone_turtle.goto(0, -height/2)
        cone_turtle.pendown()
        cone_turtle.forward(height)

        # Wait for the user to close the window
        turtle.done()

    except turtle.Terminator:
        # Handle if the user closes the window prematurely
        print("Window closed. Program terminated.")

def get_user_input():
    while True:
        height_input = input("Enter the height of the cone: ")
        radius_input = input("Enter the radius of the cone: ")

        try:
            height = float(height_input)
            radius = float(radius_input)
            return height, radius
        except ValueError:
            print("Invalid input. Please enter valid numeric values.")

def main():
    while True:
        height, radius = get_user_input()

        # Draw the cone
        draw_cone(height, radius)

        # Ask the user if they want to draw another cone
        draw_another = input("Do you want to draw another cone? (yes/no): ").lower()
        if draw_another != 'yes':
            break

if __name__ == "__main__":
    main()