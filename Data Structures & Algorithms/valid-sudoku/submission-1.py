class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for row in board:
            lst = []
            for cell in row:
                if cell != ".":
                    lst.append(cell)
            if len(set(lst)) != len(lst):
                return False

        for col in range(9):
            lst = []
            for r in range(9):
                cell = board[r][col]
                if cell != ".":
                    lst.append(cell)
            if len(set(lst)) != len(lst):
                return False

        for i in range(0, 9, 3):
            for j in range(0, 9, 3):
                values = []
                for r in range(i, i + 3):
                    for c in range(j, j + 3):
                        cell = board[r][c]
                        if cell != ".":
                            values.append(cell)
                if len(set(values)) != len(values):
                    return False

        return True