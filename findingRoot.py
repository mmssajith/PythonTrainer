from math import sqrt
import cmath

def find_roots(a, b, c):
    sqrt_comp = b ** 2 - 4 * a * c

    if sqrt_comp == 0:
      solution = -b / (2*a)
      return solution
    
    elif sqrt_comp > 0:
      solution1 = (-b + sqrt(sqrt_comp)) / (2*a)
      solution2 = (-b - sqrt(sqrt_comp)) / (2*a)

      return([solution1, solution2])

    else:
      solution1 = (-b + cmath.sqrt(sqrt_comp)) / (2*a)
      solution2 = (-b - cmath.sqrt(sqrt_comp)) / (2*a)

      return([solution1, solution2])

print(find_roots(2, 10, 8))