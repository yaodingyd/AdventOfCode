import math

def main():
  l = []
  with open('input.txt') as file:
    for line in file:
      l = line.split(',')
  l = list(map(int, l))
  print(complete_intcode_computer(l, 5))


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

def complete_intcode_computer(l, input):
  cur = 0
  output = 0
  while cur < len(l):
    opcode = l[cur] % 100

    param1, param2, param3 = get_params(l[cur], cur, l)

    if opcode == 1:
      l[param3] = l[param1] + l[param2]
      cur += 4
    elif opcode == 2:
      l[param3] = l[param1] * l[param2]
      cur += 4
    elif opcode == 3:
      l[param1] = input
      cur += 2
    elif opcode == 4:
      output = l[param1]
      cur += 2
    elif opcode == 5:
      if l[param1] != 0:
        cur = l[param2]
      else:
        cur += 3
    elif opcode == 6:
      if l[param1] == 0:
        cur = l[param2]
      else:
        cur += 3
    elif opcode == 7:
      if l[param1] < l[param2]:
        l[param3] = 1
      else:
        l[param3] = 0
      cur += 4
    elif opcode == 8:
      if l[param1] == l[param2]:
        l[param3] = 1
      else:
        l[param3] = 0
      cur += 4
    elif l[cur] == 99:
      return output

def check_param_mode(mode, index, l):
  if index >= len(l):
    return 0
  if mode == 0:
    return l[index]
  if mode == 1:
    return index

def get_params(instruction, index, l):
  param_mode_one = (instruction // 100) % 10
  param_mode_two = (instruction // 1000) % 10
  param_mode_three = (instruction // 10000) % 10

  param1 = check_param_mode(param_mode_one, index + 1, l)
  param2 = check_param_mode(param_mode_two, index + 2, l)
  param3 = check_param_mode(param_mode_three, index + 3, l)

  return param1, param2, param3


if __name__ == '__main__':
  main()