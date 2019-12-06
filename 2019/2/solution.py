input = [1,0,0,3,1,1,2,3,1,3,4,3,1,5,0,3,2,1,13,19,1,9,19,23,2,13,23,27,2,27,13,31,2,31,10,35,1,6,35,39,1,5,39,43,1,10,43,47,1,5,47,51,1,13,51,55,2,55,9,59,1,6,59,63,1,13,63,67,1,6,67,71,1,71,10,75,2,13,75,79,1,5,79,83,2,83,6,87,1,6,87,91,1,91,13,95,1,95,13,99,2,99,13,103,1,103,5,107,2,107,10,111,1,5,111,115,1,2,115,119,1,119,6,0,99,2,0,14,0]

def main():
  #print(part_one(12,2,input))
  print(part_two())

def part_one(a, b, input):
  input[1] = a
  input[2] = b

  cur = 0
  while cur < len(input):
    if (input[cur + 1] > len(input) - 1 or input[cur + 2] > len(input) - 1 or input[cur + 3] > len(input) - 1):
      return
    if input[cur] == 1:
      input[input[cur + 3]] = input[input[cur + 1]] + input[input[cur + 2]]
    elif input[cur] == 2:
      input[input[cur + 3]] = input[input[cur + 1]] * input[input[cur + 2]]
    elif input[cur] == 99:
      return input[0]
    cur += 4
  return input[0]

def part_two():
  for a in range(100):
    for b in range(100):
      copy = input.copy()
      c = part_one(a, b, copy)
      if c == 19690720:
        return 100 * a + b


if __name__ == '__main__':
  main()