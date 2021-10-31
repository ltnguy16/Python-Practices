def fizzbuzz(n):
  i = 0
  while i <= n:
    if (i%3 == 0 and i%5 == 0):
      print("fizzbuzz")
    elif i%3 == 0:
      print("fizz")
    elif i%5 == 0:
      print("buzz")
    else:
      print(i)
    i += 1
  return

def multiply(a, b):
  x = abs(a)
  index = 0
  total = 0
  while index < x:
    if a < 0:
      total -= b
    else:
      total += b
    index += 1
  print(total)
  return

def prime_numbers(n):
  count = 0
  index = 2
  values = []
  print("---------------------------------- begin ---------------------------------------")
  while count < n:
    for i in range(2, index+1):
      if index % i == 0 and i != index:
        break
      elif index % i == 0 and i == index:
        values.append(i)
        count += 1
    index += 1
  return values
      
print(prime_numbers(20))

      
      

