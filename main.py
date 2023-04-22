N = 3

def board(m):
    """
    Set of marked (x,y) coordinates given by integer m
    as expressed in binary.
    """
    b = set()
    for x in range(N):
        for y in range(N):
            n = x+N*y
            # stackoverflow.com/questions/49079440
            if ((m & (1 << n)) >> n)==1:
                b.add( (x,y) )
    return frozenset(b)

boards = [board(n) for n in range(2**(N**2))]

def adjacent(tupl,board):
    if (tupl[0]-1,tupl[1]) in board:
        return True
    if (tupl[0]+1,tupl[1]) in board:
        return True
    if (tupl[0],tupl[1]-1) in board:
        return True
    if (tupl[0],tupl[1]+1) in board:
        return True
    return False

def left_to_right(board):
    """
    True if there is a path from left to right
    """
    traveled = set(t for t in board if t[0]==0)
    while True:
        reachable = set(t for t in board if t in traveled or adjacent(t,traveled))
        if reachable == traveled:
            break
        traveled = reachable
    return len([t for t in traveled if t[0]==N-1]) > 0

def top_to_bottom(board):
    transpose = set((t[1],t[0]) for t in board)
    return left_to_right(transpose)

def finished(board):
    return left_to_right(board) or top_to_bottom(board)

value = {}

def evaluate(board):
    if board in value:
        return value[board]
    if finished(board):
        value[board] = 0
        return 0
    move_values = set()
    for x in range(N):
        for y in range(N):
            if (x,y) not in board:
                move_values.add(evaluate(board|set([(x,y)])))
    # return mex
    mex = 0
    while True:
        if mex not in move_values:
            value[board] = mex
            return mex
        mex += 1

def board_to_string(board):
    """
    Print out representation of board
    """
    output = ""
    for y in range(N):
        for x in range(N):
            if (x,y) in board:
                output += "X"
            else:
                output += "."
        output += "\n"
    output += f"{evaluate(board)}\n"
    return output


# Writing to file
with open("3x3.txt", "w") as f:
    for n in range(2**(N**2)):
        f.write(board_to_string(boards[n]))
        f.write("\n")
