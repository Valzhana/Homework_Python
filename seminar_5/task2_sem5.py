# Task2

board = [int(i) for i in range(1, 10)]


def draw_board(board):
    print("-------------")
    for i in range(3):
        print("|", board[0 + i * 3], "|", board[1 + i * 3], "|", board[2 + i * 3], "|")
        print("-------------")


def take_cell(icon):
    valid = False
    while not valid:
        player = int(input(f'Where do you want to put "{icon}"?: '))
        if 1 <= player <= 9:
            if str(board[player - 1]) not in "XO":
                board[player - 1] = icon
                valid = True
            else:
                print('This cell is already taken!')
        else:
            print("You've entered an invalid number. Try again: ")


def check_win(board):
    win_position = ((0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6), (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6))
    for each in win_position:
        if board[each[0]] == board[each[1]] == board[each[2]]:
            return board[each[0]]
    return False


def main(board):
    win = False
    counter = 0
    while not win:
        draw_board(board)
        if counter % 2 == 0:
            take_cell('X')
        else:
            take_cell('O')
        counter += 1
        if counter > 4:
            tmp = check_win(board)
            if tmp:
                win = True
                print(f'"{tmp}", is the winner!')
                break
        if counter == 9:
            print('Friendship just won!')
            break
    draw_board(board)


main(board)
