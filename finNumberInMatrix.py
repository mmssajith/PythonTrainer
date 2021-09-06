"""
Find element in the matrix
"""

def find_matrix(matrix, value):
  for row in matrix:
    for element in row:
      if element == value:
        return True
  return False


matrix = [[1,2,3,4],
          [2,4,6,8]]
          
print(find_matrix(matrix, 4))
