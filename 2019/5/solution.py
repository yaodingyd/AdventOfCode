import math

def main():
  l = []
  with open('input.txt') as file:
    for line in file:
      l = line.split(',')
  l = list(map(int, l))
  print(process_two(l, 5))


def process(l, input):
  cur = 0
  output = 0
  while cur < len(l):
    opcode = l[cur] % 100

    param_mode_one = (l[cur] // 100) % 10
    param_mode_two = (l[cur] // 1000) % 10

    print(opcode, param_mode_one, param_mode_two)

    if opcode == 1:
      l[l[cur + 3]] = check_param(param_mode_one, cur+1, l) + check_param(param_mode_two, cur+2, l)
      cur += 4
    elif opcode == 2:
      l[l[cur + 3]] = check_param(param_mode_one, cur+1, l) * check_param(param_mode_two, cur+2, l)
      cur += 4
    elif opcode == 3:
      l[l[cur+1]] = input
      cur += 2
    elif opcode == 4:
      output = l[l[cur+1]]
      cur += 2
    elif l[cur] == 99:
      return output

def process_two(l, input):
  cur = 0
  output = 0
  while cur < len(l):
    opcode = l[cur] % 100

    param_mode_one = (l[cur] // 100) % 10
    param_mode_two = (l[cur] // 1000) % 10
    param_mode_three = (l[cur] // 10000) % 10


    if opcode == 1:
      l[l[cur + 3]] = check_param(param_mode_one, cur+1, l) + check_param(param_mode_two, cur+2, l)
      cur += 4
    elif opcode == 2:
      l[l[cur + 3]] = check_param(param_mode_one, cur+1, l) * check_param(param_mode_two, cur+2, l)
      cur += 4
    elif opcode == 3:
      l[l[cur+1]] = input
      cur += 2
    elif opcode == 4:
      output = l[l[cur+1]]
      cur += 2
    elif opcode == 5:
      if check_param(param_mode_one, cur+1, l) != 0:
        cur = check_param(param_mode_two, cur+2, l)
      else:
        cur += 3
    elif opcode == 6:
      if check_param(param_mode_one, cur+1, l) == 0:
        cur = check_param(param_mode_two, cur+2, l)
      else:
        cur += 3
    elif opcode == 7:
      if check_param(param_mode_one, cur+1, l) < check_param(param_mode_two, cur+2, l):
        l[check_param(param_mode_three, cur+3, l)] = 1
      else:
        l[check_param(param_mode_three, cur+3, l)] = 0
      cur += 4
    elif opcode == 8:
      if check_param(param_mode_one, cur+1, l) == check_param(param_mode_two, cur+2, l):
        l[check_param(param_mode_three, cur+3, l)] = 1
      else:
        l[check_param(param_mode_three, cur+3, l)] = 0
      cur += 4
    elif l[cur] == 99:
      return output

def check_param(mode, index, l):
  if mode == 0:
    return l[l[index]]
  if mode == 1:
    return l[index]

if __name__ == '__main__':
  main()