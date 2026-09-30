board = [" " for _ in range(9)]


def display_board():
    print()
    print(" {} | {} | {} ".format(board[0], board[1], board[2]))
    print("---+---+---")
    print(" {} | {} | {} ".format(board[3], board[4], board[5]))
    print("---+---+---")
    print(" {} | {} | {} ".format(board[6], board[7], board[8]))
    print()


def check_winner(symbol):
    winning_positions = [
        (0, 1, 2),
        (3, 4, 5),
        (6, 7, 8),
        (0, 3, 6),
        (1, 4, 7),
        (2, 5, 8),
        (0, 4, 8),
        (2, 4, 6)
    ]

    for a, b, c in winning_positions:
        if board[a] == symbol and board[b] == symbol and board[c] == symbol:
            return True

    return False


def board_full():
    return " " not in board


def find_winning_move(symbol):
    # Check every empty position
    for i in range(9):
        if board[i] == " ":
            board[i] = symbol

            if check_winner(symbol):
                board[i] = " "
                return i

            board[i] = " "

    return None


def ai_move():
    # Rule 1: AI tries to win
    move = find_winning_move("O")

    if move is not None:
        board[move] = "O"
        print("AI chooses position:", move + 1)
        return

    # Rule 2: AI blocks the player
    move = find_winning_move("X")

    if move is not None:
        board[move] = "O"
        print("AI chooses position:", move + 1)
        return

    # Rule 3: Take the center
    if board[4] == " ":
        board[4] = "O"
        print("AI chooses position: 5")
        return

    # Rule 4: Take a corner
    corners = [0, 2, 6, 8]

    for position in corners:
        if board[position] == " ":
            board[position] = "O"
            print("AI chooses position:", position + 1)
            return

    # Rule 5: Take any remaining position
    for i in range(9):
        if board[i] == " ":
            board[i] = "O"
            print("AI chooses position:", i + 1)
            return


def main():
    print("TIC-TAC-TOE")
    print("You are X")
    print("AI is O")

    # Show position numbers
    print("\nPosition numbers:")
    print(" 1 | 2 | 3 ")
    print("---+---+---")
    print(" 4 | 5 | 6 ")
    print("---+---+---")
    print(" 7 | 8 | 9 ")

    while True:

        # Human turn
        display_board()

        while True:
            try:
                position = int(input("Enter your position (1-9): "))

                if position < 1 or position > 9:
                    print("Enter a number between 1 and 9.")
                elif board[position - 1] != " ":
                    print("Position already occupied.")
                else:
                    board[position - 1] = "X"
                    break

            except ValueError:
                print("Please enter a valid number.")

        # Check human win
        if check_winner("X"):
            display_board()
            print("You Win!")
            break

        # Check draw
        if board_full():
            display_board()
            print("It's a Draw!")
            break

        # AI turn
        ai_move()

        # Check AI win
        if check_winner("O"):
            display_board()
            print("AI Wins!")
            break

        # Check draw
        if board_full():
            display_board()
            print("It's a Draw!")
            break


main()