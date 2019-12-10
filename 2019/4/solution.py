def solution():
  print(part_two(138241, 674034))


def part_one(low, high):
  count = 0
  for i in range(low, high+1):
    list = [int(li) for li in str(i)]
    if check_none_decreasing(list) and check_two_same(list):
      count += 1
  return count

def part_two(low, high):
  count = 0
  for i in range(low, high+1):
    list = [int(li) for li in str(i)]
    if check_none_decreasing(list) and check_same(list):
      count += 1
  return count


def check_none_decreasing(list):
  last = -1
  for l in list:
    if last > l:
      return False
    last = l
  return True

def check_two_same(list):
  last = -1
  for l in list:
    if last == l:
      return True
    last = l
  return False

def check_same(list):
  last = -1
  map_dict = {}
  for l in list:
    if last == l:
      if map_dict.get(l):
        map_dict[l] += 1
      else:  
        map_dict[l] = 2
    last = l
  for key, value in map_dict.items():
    if value == 2:
      return True
  return False
  
if __name__ == "__main__":
  solution()