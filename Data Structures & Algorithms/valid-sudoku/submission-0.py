class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # мы идем по матрице и для каждого элемента i j определяем 
        # 3 словаря, в котором это число находится
        i_dict = dict() 
        j_dict = dict()
        cell_dict = dict()
        for i in range(9):
            for j in range(9):
                if board[i][j] != '.':
                    i_dict[i] = i_dict.get(i, set())
                    j_dict[j] = j_dict.get(j, set())
                    cell = i // 3 * 3 + j // 3 + 1
                    cell_dict[cell] = cell_dict.get(cell, set())
                    if (board[i][j] in i_dict[i]
                        or board[i][j] in j_dict[j]
                        or board[i][j] in cell_dict[cell]
                        ):
                        return False
                    i_dict[i].add(board[i][j])
                    j_dict[j].add(board[i][j])
                    cell_dict[cell].add(board[i][j])
        return True
                