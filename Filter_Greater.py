def is_increasing(lst):
  if len(lst) == 0:
    return False
  elif len(lst) == 1:
    return True
  else:
    return lst[0] < lst[1] and is_increasing(lst[1:])
"""
print(is_increasing([1,2,3,4]))
print(is_increasing([1,3,2,4]))
print(is_increasing([]))
"""

def filter_gt_n(lst, n):
  if len(lst) < 1:
    return []
  elif lst[0] > n:
    return [lst[0]] + filter_gt_n(lst[1:], n)
  else:
    return filter_gt_n(lst[1:], n)
"""
print(filter_gt_n([1,2,3,4],2))
print(filter_gt_n([2,2,3,3],1))
print(filter_gt_n([2,2,3,3],4))
"""