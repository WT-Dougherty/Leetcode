# Given a binary matrix (0s and 1s), find the area of the largest square of 1s
# Example matrix:
# 0 1 1 0 1
# 1 1 0 1 0
# 0 1 1 1 0
# 1 1 1 1 0
# 1 1 1 1 1
# 0 0 0 0 0
# 
# The largest square of 1s has area 9 (3x3 square)

def max_square_area(matrix: list[list[int]]) -> int:
    m = len(matrix)
    n = len(matrix[0])
    dp = [[0] * n for _ in range(m)]
    max_area = 0
    for i in range(m):
        for j in range(n):
            # if we have a 0, move on
            if matrix[i][j] == 0:
                continue
            else:
                dp[i][j] = 1

            # make sure we aren't on the borders
            if i != 0 and j != 0:
                # do our check of surrounding squares
                ss = min(dp[i-1][j], dp[i][j-1])
                if dp[i-1][j-1] != 0 and ss != 0:
                    dp[i][j] = max(dp[i][j], ss) + 1
            
            max_area = max(max_area, dp[i][j])
            
    return max_area ** 2
    

# Test cases
def test_max_square_area():
    # Example from problem description
    matrix1 = [
        [0, 1, 1, 0, 1],
        [1, 1, 0, 1, 0],
        [0, 1, 1, 1, 0],
        [1, 1, 1, 1, 0],
        [1, 1, 1, 1, 1],
        [0, 0, 0, 0, 0]
    ]
    assert max_square_area(matrix1) == 9
    
    # Single 1x1 square
    matrix2 = [
        [0, 0, 0],
        [0, 1, 0],
        [0, 0, 0]
    ]
    assert max_square_area(matrix2) == 1
    
    # All zeros
    matrix3 = [
        [0, 0, 0],
        [0, 0, 0],
        [0, 0, 0]
    ]
    assert max_square_area(matrix3) == 0
    
    # All ones
    matrix4 = [
        [1, 1, 1],
        [1, 1, 1],
        [1, 1, 1]
    ]
    assert max_square_area(matrix4) == 9
    
    # 2x2 square
    matrix5 = [
        [1, 1, 0],
        [1, 1, 0],
        [0, 0, 0]
    ]
    assert max_square_area(matrix5) == 4
    
    # Multiple squares, largest is 2x2
    matrix6 = [
        [1, 1, 0, 1],
        [1, 1, 0, 1],
        [0, 0, 1, 1],
        [1, 1, 1, 1]
    ]
    assert max_square_area(matrix6) == 4
    
    # Single row
    matrix7 = [
        [1, 1, 1, 0, 1]
    ]
    assert max_square_area(matrix7) == 1
    
    # Single column
    matrix8 = [
        [1],
        [1],
        [1],
        [0]
    ]
    assert max_square_area(matrix8) == 1
    
    print("All max square tests passed!")

test_max_square_area()
