board = ["  " for x in range(9)]


def print_board():
    row1 = "| {} | {} | {} |".format(board[0], board[1], board[2])
    row2 = "| {} | {} | {} |".format(board[3], board[4], board[5])
    row3 = "| {} | {} | {} |".format(board[6], board[7], board[8])

    print()
    print(row1)
    print(row2)
    print(row3)
    print()

choice = 0


def player_move(icon):
    print("Your turn, player {}".format(icon))
    choice = int(input("Your move [1-9] ? ").strip())
    if board[choice - 1] == "  ":
        board[choice - 1] = icon
    else:
        print()
        print("That space is taken!")


def is_victory(icon):
    if (board[0] == icon and board[1] == icon and board[2] == icon) or \
        (board[3] == icon and board[4] == icon and board[5] == icon) or \
        (board[6] == icon and board[7] == icon and board[8] == icon) or \
        (board[0] == icon and board[3] == icon and board[6] == icon) or \
        (board[1] == icon and board[4] == icon and board[7] == icon) or \
        (board[2] == icon and board[5] == icon and board[8] == icon) or \
        (board[0] == icon and board[4] == icon and board[8] == icon) or \
        (board[2] == icon and board[4] == icon and board[6] == icon):
        return True;
    else:
        return False;


while choice < 10:
    print_board()
    player_move("X")
    print_board()
    if is_victory("X"):
        print("X Wins!")
        break
    player_move("O")
    if is_victory("O"):
        print_board()
        print("O Wins!")
        break