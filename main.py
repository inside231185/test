field = [1, 2, 3, 4, 5, 6, 7, 8, 9]
victories = [[0, 1, 2], [3, 4, 5], [6, 7, 8], [0, 3, 6], [1, 4, 7], [2, 5, 8], [0, 4, 8], [2, 4, 6]]


def print_field():
    print(field[0], field[1], field[2])
    print(field[3], field[4], field[5])
    print(field[6], field[7], field[8])


def step_field(step_, symbol_):
    index_ = field.index(step_)
    field[index_] = symbol_


def get_result():
    win_ = ""
    for i in victories:
        if field[i[0]] == "X" and field[i[1]] == "X" and field[i[2]] == "X":
            win_ = "Крестик"
        if field[i[0]] == "O" and field[i[1]] == "O" and field[i[2]] == "O":
            win_ = "Нолик"

    return win_


game_ = False
player = True

while game_ == False:
    print_field()
    if player == True:
        symbol_ = "X"
        step_ = int(input("Первый игрок, ваш ход: "))
    else:
        symbol_ = "O"
        step_ = int(input("Второй игрок, ваш ход: "))

    step_field(step_, symbol_)
    win_ = get_result()
    if win_ != "":
        game_ = True
    else:
        game_ = False
        player = not player

print_field()
print("Победил", win_)
