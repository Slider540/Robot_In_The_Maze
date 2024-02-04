import pandas

url = 'https://drive.google.com/uc?id=1-crPzL6qMinByPzsrEHhGn1EJ1MfD3GX'
df = pandas.read_csv(url, names=list(range(0, 100, 1)))
city_map_list = df.values.tolist()
# courier_location = (10, 10)  # стартовая позиция курьера
# orders_location = [(1, 1), (92, 13), (46, 33)]  # координаты для доставки трех товаров
courier_location = (84, 17)
orders_location = [(66, 32), (39, 75), (90, 10), (89, 60), (79, 77), (65, 38), (9, 5)]

# city_map_list = [
#     [1, 1, 0, 0, 1],
#     [1, 1, 0, 0, 1],
#     [1, 1, 1, 1, 1],
#     [0, 0, 0, 0, 1],
#     [0, 0, 0, 0, 1]
# ]
# courier_location = (2, 2)  # стартовая позиция курьера
# orders_location = [(4, 0), (0, 2), (4, 3)]  # координаты для доставки трех товаров

route = []
x_move = 0
y_move = 0
move_right_flag = True
move_left_flag = True
move_up_flag = True
move_down_flag = True


def move_courier(curr_location, direction, hor_move, ver_move):
    global x_move, y_move
    global move_right_flag, move_left_flag, move_up_flag, move_down_flag

    if direction == 'right':
        new_location = (curr_location[0] + 1, curr_location[1])
    elif direction == 'left':
        new_location = (curr_location[0] - 1, curr_location[1])
    elif direction == 'up':
        new_location = (curr_location[0], curr_location[1] - 1)
    else:
        new_location = (curr_location[0], curr_location[1] + 1)

    if direction == 'right' or direction == 'left':
        x_move += hor_move
        move_up_flag = True
        move_down_flag = True
    else:
        y_move += ver_move
        move_right_flag = True
        move_left_flag = True
    route.append(new_location)

    return new_location


def check_move_availability(curr_location):
    global move_right_flag, move_left_flag, move_up_flag, move_down_flag
    move_directions = {'right': False, 'left': False, 'up': False, 'down': False}

    if curr_location[0] + 1 < len(city_map_list[0]) and city_map_list[curr_location[1]][curr_location[0] + 1] == 1:
        move_directions['right'] = True
    else:
        move_right_flag = False

    if curr_location[0] - 1 >= 0 and city_map_list[curr_location[1]][curr_location[0] - 1] == 1:
        move_directions['left'] = True
    else:
        move_left_flag = False

    if curr_location[1] - 1 >= 0 and city_map_list[curr_location[1] - 1][curr_location[0]] == 1:
        move_directions['up'] = True
    else:
        move_up_flag = False

    if curr_location[1] + 1 < len(city_map_list) and city_map_list[curr_location[1] + 1][curr_location[0]] == 1:
        move_directions['down'] = True
    else:
        move_down_flag = False

    print('Allowed moves: ', move_directions)
    return move_directions


order = 1
for order_location in orders_location:
    print(f'Order №{order}')
    print('Order destination: ', order_location)
    x_move = order_location[0] - courier_location[0]
    y_move = order_location[1] - courier_location[1]
    print('X move on start of step: ', x_move)
    print('Y move on start of step: ', y_move)

    while courier_location != order_location:
        allowed_move_directions = check_move_availability(courier_location)
        print('Old courier location: ', courier_location)
        if abs(x_move) >= abs(y_move):
            if x_move < 0:
                if allowed_move_directions['left'] and move_left_flag:
                    courier_location = move_courier(courier_location, 'left', 1, 0)
                elif y_move < 0 and allowed_move_directions['up'] and move_up_flag:
                    courier_location = move_courier(courier_location, 'up', 0, 1)
                elif y_move < 0 and allowed_move_directions['down'] and move_down_flag:
                    courier_location = move_courier(courier_location, 'down', 0, -1)
                elif y_move > 0 and allowed_move_directions['down'] and move_down_flag:
                    courier_location = move_courier(courier_location, 'down', 0, -1)
                elif y_move > 0 and allowed_move_directions['up'] and move_up_flag:
                    courier_location = move_courier(courier_location, 'up', 0, 1)
                elif y_move == 0 and allowed_move_directions['right'] and move_right_flag:
                    courier_location = move_courier(courier_location, 'right', -1, 0)
                elif y_move == 0 and allowed_move_directions['down'] and move_down_flag:
                    courier_location = move_courier(courier_location, 'down', 0, 1)
                elif y_move == 0 and allowed_move_directions['up'] and move_up_flag:
                    courier_location = move_courier(courier_location, 'up', 0, -1)
            else:
                if allowed_move_directions['right'] and move_right_flag:
                    courier_location = move_courier(courier_location, 'right', -1, 0)
                elif y_move < 0 and allowed_move_directions['up'] and move_up_flag:
                    courier_location = move_courier(courier_location, 'up', 0, 1)
                elif y_move < 0 and allowed_move_directions['down'] and move_down_flag:
                    courier_location = move_courier(courier_location, 'down', 0, -1)
                elif y_move > 0 and allowed_move_directions['down'] and move_down_flag:
                    courier_location = move_courier(courier_location, 'down', 0, -1)
                elif y_move > 0 and allowed_move_directions['up'] and move_up_flag:
                    courier_location = move_courier(courier_location, 'up', 0, 1)
                else:
                    courier_location = move_courier(courier_location, 'left', 1, 0)
        else:
            if y_move < 0:
                if allowed_move_directions['up'] and move_up_flag:
                    courier_location = move_courier(courier_location, 'up', 0, 1)
                elif x_move < 0 and allowed_move_directions['left'] and move_left_flag:
                    courier_location = move_courier(courier_location, 'left', 1, 0)
                elif x_move < 0 and allowed_move_directions['right'] and move_right_flag:
                    courier_location = move_courier(courier_location, 'right', -1, 0)
                elif x_move > 0 and allowed_move_directions['right'] and move_right_flag:
                    courier_location = move_courier(courier_location, 'right', -1, 0)
                elif x_move > 0 and allowed_move_directions['left'] and move_left_flag:
                    courier_location = move_courier(courier_location, 'left', 1, 0)
                else:
                    courier_location = move_courier(courier_location, 'down', 0, -1)
            else:
                if allowed_move_directions['down'] and move_down_flag:
                    courier_location = move_courier(courier_location, 'down', 0, -1)
                elif x_move < 0 and allowed_move_directions['left'] and move_left_flag:
                    courier_location = move_courier(courier_location, 'left', 1, 0)
                elif x_move < 0 and allowed_move_directions['right'] and move_right_flag:
                    courier_location = move_courier(courier_location, 'right', -1, 0)
                elif x_move > 0 and allowed_move_directions['right'] and move_right_flag:
                    courier_location = move_courier(courier_location, 'right', -1, 0)
                elif x_move > 0 and allowed_move_directions['left'] and move_left_flag:
                    courier_location = move_courier(courier_location, 'left', 1, 0)
                else:
                    courier_location = move_courier(courier_location, 'up', 0, 1)
        print('New courier location: ', courier_location)
        print('Route: ', route)
        print('X move after move: ', x_move)
        print('Y move after move: ', y_move)

    print(f"Order №{order} completed! ✅")
    order += 1

print("\nAll orders completed! 🎉🎉🎉")