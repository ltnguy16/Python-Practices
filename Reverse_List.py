def generate_list(start, end, step):
  lst = []
  i = start
  if start < end:
    while i < end:
      lst.append(i)
      i += step
  else:
    while i > end:
      lst.append(i)
      i += step
  return lst
  
"""
print(generate_list(0,5,1))
print(generate_list(0,0,1))
print(generate_list(5,10,2))
print(generate_list(10,5,-2))
"""

def reverse_list(mylist):
  newlist = []
  i = len(mylist)
  while i > 0:
    newlist.append(mylist[i-1])
    i -= 1
  return newlist

"""
print(reverse_list([1,2,3,4,5]))
print(reverse_list([]))
"""
