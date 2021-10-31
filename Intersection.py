def is_in_list(n, lst):
  for i in lst:
    if n == i:
      return True
  return False

def intersection(lst1, lst2):
  result = []
  for i in lst1:
    if i in result:
      continue
    for b in lst2:
      if i == b:
        result.append(i)
        break
  return result
