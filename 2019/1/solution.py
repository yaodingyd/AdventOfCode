
def main():
  masses = []
  with open('input.txt') as file:
    for line in file:
      masses.append(int(line))
  part1(masses)
  part2(masses)
  
def part1(list):
  sum = 0
  for mass in list:
    sum += findFuel(mass)
  print(sum)

def part2(list):
  sum = 0
  for mass in list:
    while True:
      mass = findFuel(mass)
      if (mass > 0):
        sum += mass
      else:
        break
  print(sum)

def findFuel(mass):
  return (mass // 3) - 2

if __name__ == '__main__':
  main()