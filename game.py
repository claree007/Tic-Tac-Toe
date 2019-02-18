import itertools
import ai


def create_game(game_size):
    # create a 3d list called game
    game = []
    for i in range(game_size):
        # create a list containing zeroes of length game_size
        row = ['*' for j in range(game_size)]
        game.append(row)
    return game

def show_game():
    # show game along with row and column numbers
    print()
    print("    " + "    ".join([str(i) for i in range(game_size)]))
    [print(index, row) for index, row in enumerate(game)]
    print()
        
def move(board, size, player, row, col):
    try:
        # check if position already occupied
        if board[row][col] != '*':
            print("This position has already been filled! Try again.")
            return board, False
        board[row][col] = 'X' if player=="You" else 'O'
        show_game()
        return board, True
    except IndexError as e:
        print("Trying to play on positions out of board? Check input", e)
        return board, False
    except Exception as e:
        print("Something went wrong.", e)
        return board, False

def check_win(current_game, size):
    def same_elements(arr):
        if arr.count(arr[0]) == len(arr) and arr[0] != '*':
            return True
        else:
            return False

    # horizontally
    for row in current_game:
        if same_elements(row):
            return True

    # vertically
    for index in range(size):
        elements = [row[index] for row in current_game]
        if same_elements(elements):
            return True

    # diagonally
    d1, d2 = [], []
    for index in range(size):
        d1.append(current_game[index][index])
        d2.append(current_game[index][size-1-index])
    if same_elements(d1):
        return True
    elif same_elements(d2):
        return True

    # if no win then
    return False


game_size = 4
play = True

while play:
    game = create_game(game_size)
    players = itertools.cycle(["You", "Computer"])
    won = False
    no_of_moves = 0

    # print game at the start
    show_game()
    # initialise computer
    ai.init_ai(game_size)

    choice = input("Do you want to play first? (y/n) ")
    if choice.lower() != 'y':
        next(players)
        current_player = next(players)
    else:
        current_player = next(players)

    while not won:
        played = False
        print("Current Player:", current_player)
        while not played:
            if current_player == "You":
                # input where the user wants to make a move
                row = int(input("Enter row: "))
                col = int(input("Enter column: "))
            else:
                try:
                    # computer's move
                    row, col = ai.run_ai(game)
                except:
                    print("Computer crashed!!!")
                    exit()

            game, played = move(game, game_size, current_player, row, col)

        no_of_moves += 1
        # give position of players to computer
        ai.positions(game, row, col)
        won = check_win(game, game_size)
        if won:
            print(current_player, "won the game!!!")
            break
        elif no_of_moves == (game_size * game_size):
            won = True
            print("Match draw!")
        else:
            # change player after turn
            current_player = next(players)

    again = input("Do you wish to play again? (y/n) ")
    if again.lower() != 'y':
        play = False
        print("Exited game. Bye.")
