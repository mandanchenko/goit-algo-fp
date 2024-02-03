import turtle


def draw_pifagoras_tree(branch_length, t, recursion_level):
    if recursion_level == 0:
        return
    else:
        # Draw the main branch
        t.forward(branch_length)

        # Right subtree
        t.right(45)
        draw_pifagoras_tree(0.7 * branch_length, t, recursion_level - 1)

        # Return to original direction
        t.left(90)

        # Left subtree
        draw_pifagoras_tree(0.7 * branch_length, t, recursion_level - 1)

        # Return to original direction
        t.right(45)
        t.backward(branch_length)


def main():
    recursion_level = int(input("Введіть рівень рекурсії для дерева Піфагора: "))

    screen = turtle.Screen()
    screen.bgcolor("white")

    t = turtle.Turtle()
    t.speed(2)
    t.color("#000076")
    t.penup()
    t.goto(-200, 0)
    t.pendown()

    draw_pifagoras_tree(75, t, recursion_level)

    screen.exitonclick()


if __name__ == "__main__":
    main()
