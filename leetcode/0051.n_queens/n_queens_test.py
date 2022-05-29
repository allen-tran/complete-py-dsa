from n_queens import *


def test():
    print('---------------Leetcode Problem 51---------------')
    io = {
        1: [["Q"]],
        4: [[".Q..", "...Q", "Q...", "..Q."], ["..Q.", "Q...", "...Q", ".Q.."]]
    }

    for i in io.keys():
        if solveNQueens(i) == io[i]:
            print('PASS')
        else:
            print('FAIL')


if __name__ == "__main__":
    test()
