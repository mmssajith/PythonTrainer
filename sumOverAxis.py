"""
# FInd Summation over axis in a Matrix
"""

import numpy as np

m, n = map(int, input().split())

matrix = []
for i in range (m):
  a = np.array(input().split(), int)
  matrix.append(a)

matrix = np.array(matrix)
# print(np.prod(np.sum(matrix, axis=0)))

print(np.mean(matrix, axis=1))
print(np.var(matrix,axis=0))
print(np.std(matrix, axis=None))