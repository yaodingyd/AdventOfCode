import math

def main():
  l = []
  input = ''
  with open('input.txt') as file:
    for line in file:
      input = line
  
  part_two(input)

def part_one(line):
  width = 25
  height = 6

  size = width * height

  minimal_zero_counts = math.inf
  minimal_zero_layer = 0
  current_layer = 0

  while current_layer * size < len(line):
    zeros = count_zeros(line[current_layer * size : (current_layer+1) * size])
    if minimal_zero_counts > zeros:
      minimal_zero_layer = current_layer
      minimal_zero_counts = zeros
    current_layer += 1
  
  number_of_one = 0
  number_of_two = 0
  for char in line[minimal_zero_layer*size : (minimal_zero_layer+1)*size]:
    if char == '1':
      number_of_one += 1
    if char == '2':
      number_of_two += 1
  print(number_of_one * number_of_two)

def count_zeros(str):
  sum = 0
  for char in str:
    if char == '0':
      sum += 1
  return sum

def part_two(line):
  width = 25
  height = 6

  size = width * height
  messages = ''

  for i in range(size):
    message = ''
    for char in line[i::size]:
      if char == '2':
        continue
      else:
        message = char
        break
    messages += message

  for i in range(6):
    for j in range(25):
      if messages[i*25+j] == '0':
        print(' ', end =' ')
      if messages[i*25+j] == '1':
        print('#', end =' ')
    print(' ')

if __name__ == '__main__':
  main()