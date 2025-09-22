def isValidSudoku(board) -> bool:
    cols = {i: set() for i in range(9)}
    squares = {(i,j): set() for i in range(3) for j in range(3)}

    for row_index in range(len(board)):
        cur_row = set()
        for col_index in range(len(board[row_index])):
            cur_entry = board[row_index][col_index]
            
            # if the square is empty, continue
            if cur_entry == ".":
                continue
            
            # check if the current row is valid
            if cur_entry in cur_row:
                return False
            else:
                cur_row.add(cur_entry)
            
            # check if the current column is valid
            if cur_entry in cols[col_index]:
                return False
            else:
                cols[col_index].add(cur_entry)

            # check if the current square is valid
            if cur_entry in squares[(
                col_index // 3, row_index // 3
            )]:
                return False
            else:
                squares[(
                col_index // 3, row_index // 3
            )].add(cur_entry)

    return True

# Test cases
def test_isValidSudoku():
    # Valid sudoku
    valid_board = [
        ["5","3",".",".","7",".",".",".","."],
        ["6",".",".","1","9","5",".",".","."],
        [".","9","8",".",".",".",".","6","."],
        ["8",".",".",".","6",".",".",".","3"],
        ["4",".",".","8",".","3",".",".","1"],
        ["7",".",".",".","2",".",".",".","6"],
        [".","6",".",".",".",".","2","8","."],
        [".",".",".","4","1","9",".",".","5"],
        [".",".",".",".","8",".",".","7","9"]
    ]
    assert isValidSudoku(valid_board) == True
    
    # Invalid row
    invalid_row_board = [
        ["5","3","5",".","7",".",".",".","."],
        ["6",".",".","1","9","5",".",".","."],
        [".","9","8",".",".",".",".","6","."],
        ["8",".",".",".","6",".",".",".","3"],
        ["4",".",".","8",".","3",".",".","1"],
        ["7",".",".",".","2",".",".",".","6"],
        [".","6",".",".",".",".","2","8","."],
        [".",".",".","4","1","9",".",".","5"],
        [".",".",".",".","8",".",".","7","9"]
    ]
    assert isValidSudoku(invalid_row_board) == False
    
    # Invalid column
    invalid_col_board = [
        ["5","3",".",".","7",".",".",".","."],
        ["6",".",".","1","9","5",".",".","."],
        [".","9","8",".",".",".",".","6","."],
        ["8",".",".",".","6",".",".",".","3"],
        ["4",".",".","8",".","3",".",".","1"],
        ["7",".",".",".","2",".",".",".","6"],
        [".","6",".",".",".",".","2","8","."],
        [".",".",".","4","1","9",".",".","5"],
        ["5",".",".",".","8",".",".","7","9"]
    ]
    assert isValidSudoku(invalid_col_board) == False
    
    # Invalid 3x3 box
    invalid_box_board = [
        ["5","3",".",".","7",".",".",".","."],
        ["6",".",".","1","9","5",".",".","."],
        [".","9","8",".",".",".",".","6","."],
        ["8",".",".",".","6",".",".",".","3"],
        ["4",".",".","8",".","3",".",".","1"],
        ["7",".",".",".","2",".",".",".","6"],
        [".","6",".",".",".",".","2","8","."],
        [".",".",".","4","1","9",".",".","5"],
        [".",".",".",".","8",".",".","7","9"]
    ]
    # Manually create invalid box by placing duplicate in top-left 3x3
    invalid_box_board[0][0] = "6"  # This creates duplicate with board[1][0]
    assert isValidSudoku(invalid_box_board) == False
    
    # Empty board (all dots)
    empty_board = [["." for _ in range(9)] for _ in range(9)]
    assert isValidSudoku(empty_board) == True
    
    # Single cell board
    single_cell = [["5"] + ["." for _ in range(8)] for _ in range(9)]
    assert isValidSudoku(single_cell) == False
    
    print("All sudoku tests passed!")

test_isValidSudoku()
        