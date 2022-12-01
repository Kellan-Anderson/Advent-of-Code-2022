def main():
  with open("input.txt", "r") as f:
    data = f.readlines()

  current = 0
  arr = []
  for i in data:
    if i.strip() != '':
      current += int(i.strip())
    else:
      arr.append(current)
      current = 0
  arr.sort()
  print(arr[-1])
  print(sum(arr[-3:]))

if __name__ == "__main__":
    main()