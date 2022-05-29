from curses.ascii import NL


def solveNQueens(n):
    col = set()
    pos_diag = set()
    neg_diag = set()

    board = [['.'] * n for _ in range(n)]
    res = []

    def backtrack(row):
        if row == n:
            copy = ["".join(row) for row in board]
            res.append(copy)

        for c in range(n):
            if c in col or row + c in pos_diag or row - c in neg_diag:
                continue
            col.add(c)
            pos_diag.add(row+c)
            neg_diag.add(row-c)
            board[row][c] = 'Q'
            backtrack(row+1)

            col.remove(c)
            pos_diag.remove(row+c)
            neg_diag.remove(row-c)
            board[row][c] = '.'
    backtrack(0)
    return res
