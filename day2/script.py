index = {
  "A": 1,
  "X": 1,
  "B": 2,
  "Y": 2,
  "C": 3,
  "Z": 3
}

"""
             LOSE      WIN
1rock      -> scissors  paper
2paper     -> rock      scissors
3scissors  -> paper     rock

1 -> 3 2 -> +2 +1 -> 
2 -> 1 3 -> -1 +1 -> 
3 -> 2 1 -> -1 -2 -> 
"""

def play(a, b):
  p = index[a] - index[b]
  if p == -1 or p == 2:
    return 6
  elif p == 1 or p == -2:
    return 0
  else:
    return 3

def how_to_end(a, b):
  if b == "X":
    return lose(a)
  elif b == "Y":
    return index[a] + 3
  elif b == "Z":
    return win(a)

def lose(a):
  if a == "A":
    return 3
  elif a == "B":
    return 1
  elif a == "C":
    return 2

def win(a):
  if a == "A":
    return 2 + 6
  elif a == "B":
    return 3 + 6
  elif a == "C":
    return 1 + 6

def part1():
  score = 0

  with open("input.txt", "r") as f:
    data = f.readlines()
  
  for i in data:
    other, me = i.split()
    score += play(other, me)
    score += index[me]
  
  print(score)

def part2():
  score = 0
  with open("input.txt", "r") as f:
    data = f.readlines()
  for i in data:
    a, b = i.split()
    score += how_to_end(a, b)
  print(score)

if __name__ == "__main__":
  part1()
  part2()