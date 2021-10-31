def is_valid_matrix(matrix):
  for i in range(len(matrix) - 1):
    if len(matrix[i]) !=  len(matrix[i+1]):
      return False
  return True

"""
print(is_valid_matrix([[1,2,3],[4,5,6],[7,8,9]]))
print(is_valid_matrix([[1,2,3],[4,5],[7,8,9]]))
"""

matrix1 =  [[1,2,3],
            [4,5,6]]

matrix2 =  [[1,2],
            [3,4],
            [5,6]]

def matrix_multiply(m, n):
  if m == [] or n == []:
    return "None"
  num_rows = len(n)
  num_cols = len(n[0])
  result = [[0 for x in range(len(m))] for y in range(num_cols)]
  if len(m[0]) != len(n):
    return "None"
  else:
    for i in range(len(m)):
      for j in range(num_cols):
         for k in range(num_rows):
           result[i][j] += m[i][k] * n[k][j]
  return result
"""
print(matrix_multiply(matrix1, matrix2))
print(matrix_multiply(matrix1, [[]]))
print(matrix_multiply(matrix2, matrix2))
"""