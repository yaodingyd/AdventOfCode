import math

def main():
  w = []
  with open('input.txt') as file:
    for line in file:
      l = line.split(',')
      w.append(l)
  wire_one = generate_coords(w[0])
  wire_two = generate_coords(w[1])

  m = math.inf
  m2 = math.inf

  dic_one = get_steps(wire_one)
  dic_two = get_steps(wire_two)


  for i in range(len(wire_one)):
    start = 1
    if i % 2 == 1:
      start = 0
    for j in range(start, len(wire_two), 2):
      if is_crossing(wire_one[i:i+2], wire_two[j:j+2]):
        #part 1
        res = get_distance(wire_one[i:i+2], wire_two[j:j+2])
        if res < m:
          m = res
        #part 2
        res2 = crossing_step(wire_one[i:i+2], wire_two[j:j+2]) + dic_one[wire_one[i]] + dic_two[wire_two[j]]
        if res2 < m2:
          m2 = res2

        
  print(m2)
  return m

def crossing_step(a, b):
  if(a[0][0] == a[1][0]):
    return abs(b[0][0] - a[0][0]) + abs(a[0][1] - b[0][1])
  if(a[0][1] == a[1][1]):
    return abs(a[0][0] - b[0][0]) + abs(b[0][1] - a[0][1])

def get_steps(list):
  steps_dic = {}
  steps_dic[(0,0)] = 0
  last = (0, 0)
  for l in list:
    if steps_dic.get(l):
      continue
    if l == last:
      continue
    if l[0] == last[0]:
      steps_dic[l] = steps_dic[last] + abs(l[1] - last[1])
    elif l[1] == last[1]:
      steps_dic[l] = steps_dic[last] + abs(l[0] - last[0])
    last = l
  return steps_dic


def is_crossing(a, b):
  if len(a) < 2 or len(b) < 2:
    return False 
  if(a[0][0] == a[1][0]):
    if(((a[0][1] > b[0][1] and a[1][1] < b[0][1]) or (a[0][1] < b[0][1] and a[1][1] > b[0][1])) 
    and ((b[0][0] > a[0][0] and b[1][0] < a[0][0]) or (b[0][0] < a[0][0] and b[1][0] > a[0][0]))):
      return True
  if(b[0][0] == b[1][0]):
    if(((b[0][1] > a[0][1] and b[1][1] < a[0][1]) or (b[0][1] < a[0][1] and b[1][1] > a[0][1])) 
    and ((a[0][0] > b[0][0] and a[1][0] < b[0][0]) or (a[0][0] < b[0][0] and a[1][0] > b[0][0]))):
      return True
  return False

def get_distance(a, b):
  if(a[0][0] == a[1][0]):
    return abs(a[0][0]) + abs(b[0][1])
  if(a[0][1] == a[1][1]):
    return abs(a[0][1]) + abs(b[0][0])


def generate_coords(list):
  coords = [(0,0)]
  index = 0
  for l in list:
    cur_x = coords[index][0]
    cur_y = coords[index][1]
    direction = l[0]
    distance = int(l[1:])
    if direction == 'U':
      coords.append((cur_x, cur_y + distance))
    elif direction == 'D':
      coords.append((cur_x, cur_y - distance))
    elif direction == 'L':
      coords.append((cur_x - distance, cur_y))
    elif direction == 'R':
      coords.append((cur_x + distance, cur_y))
    index += 1
  return coords

  
def part1(list):
  pass

def part2(list):
  pass

if __name__ == '__main__':
  main()