import os
import sys
import time
import random
import shutil

# Terminal control helpers
def clear():
    print("\033[2J", end="")

def goto(x, y):
    print(f"\033[{y};{x}H", end="")

def hide_cursor():
    print("\033[?25l", end="")

def show_cursor():
    print("\033[?25h", end="")

def set_color(color):
    COLORS = {
        'red': 31, 'green': 32, 'yellow': 33, 'blue': 34,
        'magenta': 35, 'cyan': 36, 'white': 37
    }
    print(f"\033[{COLORS[color]}m", end="")

# Get terminal size safely
def get_size():
    size = shutil.get_terminal_size((80, 24))
    return size.columns, size.lines

# Directions
UP_RIGHT = 'ur'
UP_LEFT = 'ul'
DOWN_RIGHT = 'dr'
DOWN_LEFT = 'dl'
DIRS = [UP_RIGHT, UP_LEFT, DOWN_RIGHT, DOWN_LEFT]

# logo keys
X = 'x'
Y = 'y'
DIR = 'dir'
COLOR = 'color'

def main():
    clear()
    hide_cursor()

    width, height = get_size()
    width -= 4

    NUMBER_OF = int(input("HOW MANY DVD LOGOS? "))
    PAUSE = float(input("PAUSE AMOUNT? (seconds): "))

    COLORS = ['red', 'green', 'blue', 'yellow', 'magenta', 'cyan', 'white']

    logos = []
    for i in range(NUMBER_OF):
        logos.append({
            X: random.randint(1, width),
            Y: random.randint(1, height - 1),
            DIR: random.choice(DIRS),
            COLOR: random.choice(COLORS)
        })

        if logos[-1][X] % 2 == 1:
            logos[-1][X] -= 1

    corner_bounces = 0

    try:
        while True:
            # Erase previous frames
            for logo in logos:
                goto(logo[X], logo[Y])
                print("   ", end="")

            # Update each logo
            for logo in logos:
                ox, oy = logo[X], logo[Y]
                d = logo[DIR]

                at_left = logo[X] <= 1
                at_right = logo[X] >= width
                at_top = logo[Y] <= 1
                at_bottom = logo[Y] >= height

                # CORNER BOUNCES
                if at_left and at_top:
                    logo[DIR] = DOWN_RIGHT
                    corner_bounces += 1
                elif at_left and at_bottom:
                    logo[DIR] = UP_RIGHT
                    corner_bounces += 1
                elif at_right and at_top:
                    logo[DIR] = DOWN_LEFT
                    corner_bounces += 1
                elif at_right and at_bottom:
                    logo[DIR] = UP_LEFT
                    corner_bounces += 1

                else:
                    # WALL BOUNCES
                    if at_left and d in [UP_LEFT, DOWN_LEFT]:
                        logo[DIR] = UP_RIGHT if d == UP_LEFT else DOWN_RIGHT
                    if at_right and d in [UP_RIGHT, DOWN_RIGHT]:
                        logo[DIR] = UP_LEFT if d == UP_RIGHT else DOWN_LEFT
                    if at_top and d in [UP_LEFT, UP_RIGHT]:
                        logo[DIR] = DOWN_LEFT if d == UP_LEFT else DOWN_RIGHT
                    if at_bottom and d in [DOWN_LEFT, DOWN_RIGHT]:
                        logo[DIR] = UP_LEFT if d == DOWN_LEFT else UP_RIGHT

                # Color change on bounce
                if logo[DIR] != d:
                    logo[COLOR] = random.choice(COLORS)

                # Move
                if logo[DIR] == UP_RIGHT:
                    logo[X] += 2; logo[Y] -= 1
                elif logo[DIR] == UP_LEFT:
                    logo[X] -= 2; logo[Y] -= 1
                elif logo[DIR] == DOWN_RIGHT:
                    logo[X] += 2; logo[Y] += 1
                elif logo[DIR] == DOWN_LEFT:
                    logo[X] -= 2; logo[Y] += 1

            # Draw corner bounce counter
            goto(1, 1)
            set_color('white')
            print(f"Corner bounces: {corner_bounces}    ", end="")

            # Draw logos
            for logo in logos:
                goto(logo[X], logo[Y])
                set_color(logo[COLOR])
                print("DVD", end="")

            sys.stdout.flush()
            time.sleep(PAUSE)

    except KeyboardInterrupt:
        show_cursor()
        print("\nBye!")
        sys.exit()

if __name__ == "__main__":
    main()
