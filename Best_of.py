#part 1
def score(total, correct, wrong):
  return ((correct * 2) + wrong)/(total * 2) * 100

#part 2
def score75(total, correct, wrong):
  return ((min(correct, .75*total) * 2) + min(wrong, max(.75*total - correct, 0)))/(.75 * total * 2) * 100

print(score75(20,20,0))
print(score75(20,15,0))
print(score75(20,15,5))
print(score75(20,10,5))
print(score75(20,0,20))