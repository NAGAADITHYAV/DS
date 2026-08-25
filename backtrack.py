'''
Backtracking implementation
for path of a knight on a chessboard to cover all 64 squares,
Start for with either of the knight's inital positons that (0,1) or (0,6) or (7,1) or (7,6)
'''
def KnightTour():
    # Implementation for knight's tour using backtracking
    start = (0, 1)  # or (0, 6), (7, 1), (7, 6) 
    board = [[0 for _ in range(8)] for _ in range(8)]
    board[start[0]][start[1]] = 1
    visited = set()
    visited.add(start)
    directions = [(-2, -1), (-2, 1), (-1, -2), (-1, 2), (1, -2), (1, 2), (2, -1), (2, 1)]
    def print_board():
        for row in reversed(board):
            print(" ".join(str(x) for x in row))
    def dfs(row, col, move):
        if move == 64:
            print_board()
            return True

        for drow, dcol in directions:
            nrow, ncol = row + drow, col + dcol
            if 0 <= nrow < 8 and 0 <= ncol < 8 and (nrow, ncol) not in visited:
                visited.add((nrow, ncol))
                board[nrow][ncol] = move + 1
                if dfs(nrow, ncol, move + 1):
                    return True
                visited.remove((nrow, ncol))
                board[nrow][ncol] = 0
    
    dfs(start[0],start[1], 1)

KnightTour()