def init_ai(game_size):
    global board, size, win_blocks, user, ai
    user = []
    ai = []
    size = game_size
    board = game_board(size)
    win_blocks = wins(size)

def game_board(size):
    board = []
    for i in range(size):
        row = [(i*size)+j for j in range(size)]
        board.append(row)
    return board

def wins(size):
    win_blocks = []
    # horizontal
    for i in range(size):
        win = [board[i][j] for j in range(size)]
        win_blocks.append(win)

    # vertical
    for i in range(size):
        win = [board[j][i] for j in range(size)]
        win_blocks.append(win)

    # diagonal
    d1, d2 = [], []
    for i in range(size):
        d1.append(board[i][i])
        d2.append(board[i][size-1-i])
    win_blocks.append(d1)
    win_blocks.append(d2)

    return win_blocks

def positions(game, row, col):
    if game[row][col] == 'X':
        user.append(board[row][col])
    elif game[row][col] == 'O':
        ai.append(board[row][col])

def move(win_blocks, user, ai):
    def add(possible_win):
        possible_wins.append(win_blocks.index(possible_win))

    def occupied(pos):
        if position in user or position in ai:
            return True

    possible_wins = []
    for win in win_blocks:
        # 0: empty, 1: go(bc enemy), 2: go(bc myself), 3:don't go
        go = 0
        go_buffer = []
        for position in win:
            if position in ai:
                if go == 0:
                    go = 2
                    go_buffer.append(go)
                elif go == 1:
                    go == 3
                    break
                elif go==2:
                    go_buffer.append(go)
            elif position in user:
                if go == 0:
                    go = 1
                    go_buffer.append(go)
                elif go==1:
                    go_buffer.append(go)
                elif go == 2:
                    go = 3
                    break
        if go == 0:
            add(win)
        elif go == 1 or go == 2:
            for iter in range(go_buffer.count(go)):
                add(win)

    moves = [element for index in possible_wins for element in win_blocks[index]]

    for position in moves:
        if occupied(position):
            moves = list(filter(lambda a: a != position, moves))
    try:
        return max(set(moves), key=moves.count)
    except:
        for position in range(size*size):
            if not occupied(position):
                return position    

def run_ai(game):
    try:
        position = move(win_blocks, user, ai)
    except Exception as e:
        print(e)
    return position//size, position%size


size = 0
board = []
win_blocks = []
user = []
ai = []