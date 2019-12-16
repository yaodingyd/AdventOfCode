def main():
  l = []
  with open('input.txt') as file:
    for line in file:
      l.append(line.strip('\n').split(')'))

  #print(part_one(l))

  print(part_two(l)-2) 

def part_one(l):
  d = {}
  for orbit in l:
    if orbit[0] in d:
      d[orbit[0]].append(orbit[1])
    else:
      d[orbit[0]] = [orbit[1]]
  
  cur = 'COM'
  sum = 0

  def find(cur, d, distance):
    nonlocal sum
    if cur in d:
      satelites = d[cur]
      for satelite in satelites:
        sum += distance
        find(satelite, d, distance+1)

  find(cur, d, 1)

  return sum

  def part_two(d):
    cur = 'COM'

    def find(cur, d, distance):
      nonlocal sum
      if cur in d:
        satelites = d[cur]
        for satelite in satelites:
          if satelite == 'SAN':
            break
          sum += distance
          find(satelite, d, distance+1)

    find(cur, d, 1)

    return sum

def part_two(l):
  d = {}
  for orbit in l:
    d[orbit[1]] = orbit[0]

  p1 = 'YOU'
  p2 = 'SAN'

  d1 = {}
  d1[p1] = 0
  d2 = {}
  d2[p2] = 0
  
  while True:
    if p1 in d:
      t1 = d[p1]
      d1[t1] = d1[p1] + 1
      if t1 in d2:
        return d1[t1] + d2[t1]
      p1 = t1
    if p2 in d:
      t2 = d[p2]
      d2[t2] = d2[p2] + 1
      if t2 in d1:
        return d1[t2] + d2[t2]
      p2 = t2
    if p1 not in d and p2 not in d:
      return
  
if __name__ == '__main__':
  main()