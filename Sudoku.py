
board = [ [5, 3, 0, 0, 7, 0, 0, 0, 0],
          [6, 0, 0, 1, 9, 5, 0, 0, 0],
          [0, 9, 8, 0, 0, 0, 0, 6, 0],
          [8, 0, 0, 0, 6, 0, 0, 0, 3],
          [4, 0, 0, 8, 0, 3, 0, 0, 1],
          [7, 0, 0, 0, 2, 0, 0, 0, 6],
          [0, 6, 0, 0, 0, 0, 2, 8, 0],
          [0, 0, 0, 4, 1, 9, 0, 0, 5],
          [0, 0, 0, 0, 8, 0, 0, 7, 9]]

def print_board(board):
  for row in board:
    output = ""
    for value in row:
      output += str(value) + " "
    print(output)

def find_zero(board):
  for row in range(len(board)):
    for col in range(len(board[row])):
      if board[row][col] == 0:
        return [row, col]
  return []

def is_valid(board, row, col, value):
  for i in range(len(board)):
    if board[i][col] == value:
      return False
  for i in range(len(board[row])):
    if board[row][i] == value:
      return False
  for i in range((row//3)*3,(((row//3)*3) + 3)):
    for j in range((col//3)*3,(((col//3)*3) + 3)):
      if board[i][j] == value:
        return False
  return True

def solve(board):
  if find_zero(board) == []:
    return board
  new_board = board
  row, col = find_zero(new_board)
  for i in range(1,10):
    if is_valid(new_board, row, col, i):
      new_board[row][col] = i
      if solve(new_board) == None:
        new_board[row][col] = 0
      else:
        return solve(new_board)
  return None


#result = solve(board)
#print_board(result)
#print(is_valid(board, 0, 2, 1))
#print(is_valid(board, 0, 2, 7))
#print(is_valid(board, 0, 2, 6))
#print(is_valid(board, 8, 7, 1))
#print(find_zero(board))
#print_board(board)