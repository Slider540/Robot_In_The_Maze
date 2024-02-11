import pandas
from tkinter import *
from time import *


def check_possible_directions(current_location):
    allowed_directions = {'right': False, 'left': False, 'up': False, 'down': False}

    if current_location[0] + 1 < len(city_map[0]) and city_map[current_location[1]][current_location[0] + 1] == 1:
        allowed_directions['right'] = True
    else:
        opened_directions['right'] = False

    if current_location[0] - 1 >= 0 and city_map[current_location[1]][current_location[0] - 1] == 1:
        allowed_directions['left'] = True
    else:
        opened_directions['left'] = False

    if current_location[1] - 1 >= 0 and city_map[current_location[1] - 1][current_location[0]] == 1:
        allowed_directions['up'] = True
    else:
        opened_directions['up'] = False

    if current_location[1] + 1 < len(city_map) and city_map[current_location[1] + 1][current_location[0]] == 1:
        allowed_directions['down'] = True
    else:
        opened_directions['down'] = False

    return allowed_directions


def move_robot(current_location, direction):
    def move_robot_on_map(x, y):
        for dot in range(0, 6):
            canvas.move(robot, x, y)
            tk.update()
            sleep(0.015)

    new_location = tuple()

    if direction == 'right':
        new_location = (current_location[0] + 1, current_location[1])
        distance['x'] += 1
        move_robot_on_map(1, 0)
    elif direction == 'left':
        new_location = (current_location[0] - 1, current_location[1])
        distance['x'] -= 1
        move_robot_on_map(-1, 0)
    elif direction == 'up':
        new_location = (current_location[0], current_location[1] - 1)
        distance['y'] -= 1
        move_robot_on_map(0, -1)
    elif direction == 'down':
        new_location = (current_location[0], current_location[1] + 1)
        distance['y'] += 1
        move_robot_on_map(0, 1)

    if direction == 'right' or direction == 'left':
        opened_directions['up'] = True
        opened_directions['down'] = True
    else:
        opened_directions['right'] = True
        opened_directions['left'] = True

    route.append(new_location)
    return new_location


if __name__ == '__main__':

    # load the map, the position of the robot and orders
    url = 'https://drive.google.com/uc?id=1-crPzL6qMinByPzsrEHhGn1EJ1MfD3GX'
    df = pandas.read_csv(url, names=list(range(0, 100, 1)))
    city_map = df.values.tolist()
    robot_location = (20, 20)
    orders_location = [(2, 2), (70, 3)]
    # robot_location = (84, 17)
    # orders_location = [(66, 32), (39, 75), (90, 10), (89, 60), (79, 77), (65, 38), (9, 5)]

    # initiate the canvas
    tk = Tk()
    tk.title('Robot in the maze')
    width = (tk.winfo_screenwidth() - 640) // 2
    height = (tk.winfo_screenheight() - 640) // 2
    tk.geometry(f'640x640+{width}+{height}')
    canvas = Canvas(tk, width=600, height=600, bg='#C1DED9')
    canvas.pack(anchor=CENTER, expand=1)

    # map the labyrinth, the position of the robot and orders
    for i in range(len(city_map)):
        for j in range(len(city_map[0])):
            if city_map[i][j] == 0:
                canvas.create_rectangle(j * 6 + 1, i * 6 + 1, j * 6 + 7, i * 6 + 7, fill='#406092', outline='#406092')
    for order_location in orders_location:
        canvas.create_rectangle(order_location[0] * 6 + 1, order_location[1] * 6 + 1, order_location[0] * 6 + 7,
                                order_location[1] * 6 + 7, fill='#DC0156')
    robot = canvas.create_rectangle(robot_location[0] * 6 + 1, robot_location[1] * 6 + 1, robot_location[0] * 6 + 7,
                                    robot_location[1] * 6 + 7, fill='#1DD201')

    # set the main variables
    route = []
    distance = {'x': 0, 'y': 0}
    opened_directions = {'right': True, 'left': True, 'up': True, 'down': True}

    # moving the robot according to orders
    for order_location in orders_location:
        distance['x'] = order_location[0] - robot_location[0]
        distance['y'] = order_location[1] - robot_location[1]

        while robot_location != order_location:
            possible_directions = check_possible_directions(robot_location)
            print(possible_directions)

            if abs(distance['x']) >= abs(distance['y']):
                if distance['x'] < 0:
                    if possible_directions['left'] and opened_directions['left']:
                        robot_location = move_robot(robot_location, 'left')
                    elif distance['y'] < 0 and possible_directions['up'] and opened_directions['up']:
                        robot_location = move_robot(robot_location, 'up')
                    elif distance['y'] < 0 and possible_directions['down'] and opened_directions['down']:
                        robot_location = move_robot(robot_location, 'down')
                    elif distance['y'] > 0 and possible_directions['down'] and opened_directions['down']:
                        robot_location = move_robot(robot_location, 'down')
                    elif distance['y'] > 0 and possible_directions['up'] and opened_directions['up']:
                        robot_location = move_robot(robot_location, 'up')
                    elif distance['y'] == 0 and possible_directions['right'] and opened_directions['right']:
                        robot_location = move_robot(robot_location, 'right')
                    elif distance['y'] == 0 and possible_directions['down'] and opened_directions['down']:
                        robot_location = move_robot(robot_location, 'down')
                    elif distance['y'] == 0 and possible_directions['up'] and opened_directions['up']:
                        robot_location = move_robot(robot_location, 'up')
                else:
                    if possible_directions['right'] and opened_directions['right']:
                        robot_location = move_robot(robot_location, 'right')
                    elif distance['y'] < 0 and possible_directions['up'] and opened_directions['up']:
                        robot_location = move_robot(robot_location, 'up')
                    elif distance['y'] < 0 and possible_directions['down'] and opened_directions['down']:
                        robot_location = move_robot(robot_location, 'down')
                    elif distance['y'] > 0 and possible_directions['down'] and opened_directions['down']:
                        robot_location = move_robot(robot_location, 'down')
                    elif distance['y'] > 0 and possible_directions['up'] and opened_directions['up']:
                        robot_location = move_robot(robot_location, 'up')
                    else:
                        robot_location = move_robot(robot_location, 'left')
            else:
                if distance['y'] < 0:
                    if possible_directions['up'] and opened_directions['up']:
                        robot_location = move_robot(robot_location, 'up')
                    elif distance['x'] < 0 and possible_directions['left'] and opened_directions['left']:
                        robot_location = move_robot(robot_location, 'left')
                    elif distance['x'] < 0 and possible_directions['right'] and opened_directions['right']:
                        robot_location = move_robot(robot_location, 'right')
                    elif distance['x'] > 0 and possible_directions['right'] and opened_directions['right']:
                        robot_location = move_robot(robot_location, 'right')
                    elif distance['x'] > 0 and possible_directions['left'] and opened_directions['left']:
                        robot_location = move_robot(robot_location, 'left')
                    else:
                        robot_location = move_robot(robot_location, 'down')
                else:
                    if possible_directions['down'] and opened_directions['down']:
                        robot_location = move_robot(robot_location, 'down')
                    elif distance['x'] < 0 and possible_directions['left'] and opened_directions['left']:
                        robot_location = move_robot(robot_location, 'left')
                    elif distance['x'] < 0 and possible_directions['right'] and opened_directions['right']:
                        robot_location = move_robot(robot_location, 'right')
                    elif distance['x'] > 0 and possible_directions['right'] and opened_directions['right']:
                        robot_location = move_robot(robot_location, 'right')
                    elif distance['x'] > 0 and possible_directions['left'] and opened_directions['left']:
                        robot_location = move_robot(robot_location, 'left')
                    else:
                        robot_location = move_robot(robot_location, 'up')

    tk.mainloop()
