import sys
from __init__ import *

if __name__ == "__main__":
    N = int(sys.argv[1])
    values = {}
    boards = [board(m,N) for m in range(2**(N**2))]
    if len(sys.argv)<3:
        with open(f"{N}x{N}.txt", "w") as f:
            for n in range(2**(N**2)):
                f.write(board_to_string(boards[n],N))
                f.write("\n")
    else:
        tokens = int(sys.argv[2])
        with open(f"{N}x{N}-with-{tokens}-tokens-value-zero.txt","w") as f:
            for board in boards:
                if len(board)==tokens:
                    if evaluate(board,N,values) == 0 and not finished(board,N):
                        for y in range(N):
                            output = ""
                            for x in range(N):
                                if (x,y) in board:
                                    output += "X"
                                else:
                                    output += "."
                            print(output, file=f)
                        print(file=f)
