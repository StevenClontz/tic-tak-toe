def board(m,N):
    """
    Set of marked (x,y) coordinates given by integer m<N^2
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

def left_to_right(board,N):
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

def top_to_bottom(board,N):
    transpose = set((t[1],t[0]) for t in board)
    return left_to_right(transpose,N)

def finished(board,N):
    return left_to_right(board,N) or top_to_bottom(board,N)

def evaluate(board,N,values):
    if board in values:
        return values[board]
    if finished(board,N):
        values[board] = 0
        return 0
    move_values = set()
    for x in range(N):
        for y in range(N):
            if (x,y) not in board:
                move_values.add(evaluate(board|set([(x,y)]),N,values))
    # return mex
    mex = 0
    while True:
        if mex not in move_values:
            values[board] = mex
            return mex
        mex += 1

def board_to_string(board,N,values):
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
    output += f"{evaluate(board,N,values)}\n"
    return output
