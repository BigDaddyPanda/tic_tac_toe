import geometrix as go
from math import sqrt
WC3=go.winning_condition_3(go.init_map(3))
WC4=go.winning_condition_3(go.init_map(4))
WC5=go.winning_condition_4(go.init_map(5))

def Move(s, i):
    return {"score": s, "index": i}


def rl(a):
    return range(len(a))


def empty_indices(board):
    return [x for x in rl(board) if board[x] ==0]


def win_check(sign, board, win):
    b = len(board)
    a=int(sqrt(b))
    if win == 3:
        winning_condition = WC3 if a == 3 else WC4
    else:
        winning_condition = WC5
        
    player = [i for i in rl(board) if board[i] == sign]
    for w in winning_condition:
        if set(w).issubset(set(player)):
            return True,sign,w
    return False

def extract_win_condition(board,win) :
    b = len(board)
    a=int(sqrt(b))
    if win == 3:
        winning_condition = WC3 if a == 3 else WC4
    else:
        winning_condition = WC5
    
    player1 = set([i for i in rl(board) if board[i] == 1])
    player2 = set([i for i in rl(board) if board[i] == -1])
    for w in winning_condition:
        if set(w).issubset(player1) or set(w).issubset(player2):
            return w

memo={}
# memo[(sign, board, is_max_sign, depth, win)]=minimax()
def minimax(sign, board, is_max_sign=True, depth=0, win=3):
    print(depth,board)
    depth += 1
    new_board = board.copy()
    empty_spots = empty_indices(new_board)
    # print(empty_spots)
    if is_max_sign:
        max_sign = sign
        min_sign = -(sign)
    else:
        max_sign = -(sign)
        min_sign = sign

    # Check for base case
    if win_check(max_sign, new_board, win):
        score = Move(100 - depth, None)
        return score
    elif win_check(min_sign, new_board, win):
        score = Move(depth - 100, None)
        return score
    elif len(empty_spots) == 0:
        score = Move(0, None)
        return score

    moves = []
    for i in empty_spots:
        move = Move(None, i)
        new_board[i] = sign
        if is_max_sign:
            # result=memo.get((min_sign, new_board, False, depth, win),minimax(min_sign, new_board, False, depth,win))
## no memorisation
          result = minimax(min_sign, new_board, False, depth,win)
        else:
            # result=memo.get((max_sign, new_board, True, depth, win),minimax(max_sign, new_board, True, depth,win))
## no memorisation
            result = minimax(max_sign, new_board, True, depth,win)
        move["score"] = result["score"]
        new_board[i] = 0   # Revert changes made to board
        moves.append(move)

    if is_max_sign:
        best_score = -1000
        for i in range(len(moves)):
            if moves[i]["score"] > best_score:
                best_move = i
                best_score = moves[i]["score"]
    else:
        best_score = 1000
        for i in range(len(moves)):
            if moves[i]["score"] < best_score:
                best_move = i
                best_score = moves[i]["score"]

    return moves[best_move]   # Return index of best move for passed board

# g=[0 for i in range(9)]
# g[4]=1
# print(minimax(-1, g,True,0,3))
