def check_similar_elements(arr1, arr2):
  for i in arr1:
    if i in arr2:
      return i

def find_all_occurances(l1, l2, l3):
  for i in l1:
    if i in l2 and i in l3:
      return i

def get_value(num: str):
  if num.isupper():
    return ord(num) - 38
  else:
    return ord(num) - 96

def part1():
  with open("input.txt", "r") as f:
    data = f.readlines()

  total = 0
  for i in data:
    length = len(i)
    list1 = i[:-length//2]
    list2 = i[-length//2:]
    element = check_similar_elements(list1, list2)
    num = get_value(element)
    print(element, num)
    total += num
  
  print(total)

def part2():
  with open("input.txt", "r") as f:
    data = f.readlines()
  
  total = 0
  for i in range(len(data)//3):
    index = 3 * i
    l1, l2, l3 = data[index: index + 3]
    total += get_value(find_all_occurances(l1,l2,l3))
  print(total)

if __name__ == "__main__":
  part1()
  part2()