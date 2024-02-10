import pandas
from tkinter import *

# def check_possible_directions(robot_location):
#     allowed_directions = {'right': False, 'left': False, 'up': False, 'down': False}
#
#     if (robot_location[0] + 1 < len(city_map[0])
#             and city_map[robot_location[1]][robot_location[0] + 1] == 1):
#         allowed_directions['right'] = True
#     else:
#         move_right_flag = False
#
#     if robot_location[0] - 1 >= 0 and city_map[robot_location[1]][robot_location[0] - 1] == 1:
#         allowed_directions['left'] = True
#     else:
#         move_left_flag = False
#
#     if robot_location[1] - 1 >= 0 and city_map[robot_location[1] - 1][robot_location[0]] == 1:
#         allowed_directions['up'] = True
#     else:
#         move_up_flag = False
#
#     if robot_location[1] + 1 < len(city_map) and city_map[robot_location[1] + 1][
#         robot_location[0]] == 1:
#         allowed_directions['down'] = True
#     else:
#         move_down_flag = False
#
#     return allowed_directions
#
#
# def move_robot(current_location, direction, hor_move, ver_move):
#     if direction == 'right':
#         new_location = (current_location[0] + 1, current_location[1])
#     elif direction == 'left':
#         new_location = (current_location[0] - 1, current_location[1])
#     elif direction == 'up':
#         new_location = (current_location[0], current_location[1] - 1)
#     else:
#         new_location = (current_location[0], current_location[1] + 1)
#
#     if direction == 'right' or direction == 'left':
#         x_move += hor_move
#         move_up_flag = True
#         move_down_flag = True
#     else:
#         y_move += ver_move
#         move_right_flag = True
#         move_left_flag = True
#     route.append(new_location)
#
#     return new_location


if __name__ == '__main__':
    url = 'https://drive.google.com/uc?id=1-crPzL6qMinByPzsrEHhGn1EJ1MfD3GX'
    df = pandas.read_csv(url, names=list(range(0, 100, 1)))
    city_map = df.values.tolist()

    robot_location = (84, 17)
    orders_location = [(66, 32), (39, 75), (90, 10), (89, 60), (79, 77), (65, 38), (9, 5)]

    tk = Tk()
    tk.title('Robot in the maze')
    width = (tk.winfo_screenwidth() - 640) // 2
    height = (tk.winfo_screenheight() - 640) // 2
    tk.geometry(f'640x640+{width}+{height}')
    canvas = Canvas(tk, width=600, height=600, bg='white')
    canvas.pack(anchor=CENTER, expand=1)

    for i in range(len(city_map)):
        for j in range(len(city_map[0])):
            if city_map[i][j] == 0:
                canvas.create_rectangle(j * 6 + 1, i * 6 + 1, j * 6 + 7, i * 6 + 7, fill='#3B14AF', outline='#3B14AF')

    for order_location in orders_location:
        canvas.create_rectangle(order_location[0] * 6 + 1, order_location[1] * 6 + 1, order_location[0] * 6 + 7,
                                order_location[1] * 6 + 7, fill='#DC0156')

    robot = canvas.create_rectangle(robot_location[0] * 6 + 1, robot_location[1] * 6 + 1, robot_location[0] * 6 + 7,
                                    robot_location[1] * 6 + 7, fill='#1DD201')
    # route = []
    # distance = {'x': 0, 'y': 0}
    # opened_directions = {'right': True, 'left': True, 'up': True, 'down': True}
    # last_move_direction = ''
    #
    # order = 1
    # for order_location in orders_location:
    #     distance['x'] = order_location[0] - robot_location[0]
    #     distance['y'] = order_location[1] - robot_location[1]
    #
    #     while robot_location != order_location:
    #         allowed_directions = check_possible_directions(robot_location)
    #
    #         if abs(distance['x']) >= abs(distance['y']):
    #             if distance['x'] < 0:
    #                 if allowed_directions['left'] and opened_directions['left']:
    #                     robot_location = move_robot(robot_location, 'left', 1, 0)
    #                 elif y_move < 0 and allowed_directions['up'] and move_up_flag:
    #                     robot_location = move_robot(robot_location, 'up', 0, 1)
    #                 elif y_move < 0 and allowed_directions['down'] and move_down_flag:
    #                     robot_location = move_robot(robot_location, 'down', 0, -1)
    #                 elif y_move > 0 and allowed_directions['down'] and move_down_flag:
    #                     robot_location = move_robot(robot_location, 'down', 0, -1)
    #                 elif y_move > 0 and allowed_directions['up'] and move_up_flag:
    #                     robot_location = move_robot(robot_location, 'up', 0, 1)
    #                 elif y_move == 0 and allowed_directions['right'] and move_right_flag:
    #                     robot_location = move_robot(robot_location, 'right', -1, 0)
    #                 elif y_move == 0 and allowed_directions['down'] and move_down_flag:
    #                     robot_location = move_robot(robot_location, 'down', 0, 1)
    #                 elif y_move == 0 and allowed_directions['up'] and move_up_flag:
    #                     robot_location = move_robot(robot_location, 'up', 0, -1)
    #             else:
    #                 if allowed_directions['right'] and move_right_flag:
    #                     robot_location = move_robot(robot_location, 'right', -1, 0)
    #                 elif y_move < 0 and allowed_directions['up'] and move_up_flag:
    #                     robot_location = move_robot(robot_location, 'up', 0, 1)
    #                 elif y_move < 0 and allowed_directions['down'] and move_down_flag:
    #                     robot_location = move_robot(robot_location, 'down', 0, -1)
    #                 elif y_move > 0 and allowed_directions['down'] and move_down_flag:
    #                     robot_location = move_robot(robot_location, 'down', 0, -1)
    #                 elif y_move > 0 and allowed_directions['up'] and move_up_flag:
    #                     robot_location = move_robot(robot_location, 'up', 0, 1)
    #                 else:
    #                     robot_location = move_robot(robot_location, 'left', 1, 0)
    #         else:
    #             if y_move < 0:
    #                 if allowed_directions['up'] and move_up_flag:
    #                     robot_location = move_robot(robot_location, 'up', 0, 1)
    #                 elif x_move < 0 and allowed_directions['left'] and move_left_flag:
    #                     robot_location = move_robot(robot_location, 'left', 1, 0)
    #                 elif x_move < 0 and allowed_directions['right'] and move_right_flag:
    #                     robot_location = move_robot(robot_location, 'right', -1, 0)
    #                 elif x_move > 0 and allowed_directions['right'] and move_right_flag:
    #                     robot_location = move_robot(robot_location, 'right', -1, 0)
    #                 elif x_move > 0 and allowed_directions['left'] and move_left_flag:
    #                     robot_location = move_robot(robot_location, 'left', 1, 0)
    #                 else:
    #                     robot_location = move_robot(robot_location, 'down', 0, -1)
    #             else:
    #                 if allowed_directions['down'] and move_down_flag:
    #                     robot_location = move_robot(robot_location, 'down', 0, -1)
    #                 elif x_move < 0 and allowed_directions['left'] and move_left_flag:
    #                     robot_location = move_robot(robot_location, 'left', 1, 0)
    #                 elif x_move < 0 and allowed_directions['right'] and move_right_flag:
    #                     robot_location = move_robot(robot_location, 'right', -1, 0)
    #                 elif x_move > 0 and allowed_directions['right'] and move_right_flag:
    #                     robot_location = move_robot(robot_location, 'right', -1, 0)
    #                 elif x_move > 0 and allowed_directions['left'] and move_left_flag:
    #                     robot_location = move_robot(robot_location, 'left', 1, 0)
    #                 else:
    #                     robot_location = move_robot(robot_location, 'up', 0, 1)

    tk.mainloop()
