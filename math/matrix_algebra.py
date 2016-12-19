# Matrix Algebra - Brian Maimone

import numpy as np

A = np.array([[1, 2, 3], [2, 7, 4]])
B = np.array([[1, -1], [0, 1]])
C = np.array([[5, -1], [9, 1], [6, 0]])
D = np.array([[3, -2, -1], [1, 2, 3]])

u = np.array([6, 2, -3, 5])
v = np.array([3, 5, -1, 4])
w = np.array([[1], [8], [0], [5]])

# 1. Matrix Dimensions

print "Dimensions of: "
print "A: {0}".format(A.shape)
print "B: {0}".format(B.shape)
print "C: {0}".format(C.shape)
print "D: {0}".format(D.shape)
print "u: {0}".format(u.shape)
print "w: {0}".format(w.shape)

# 2. Vector Operations

alpha = 6

print "u + v = {0}".format(np.add(u, v))
print "u - v = {0}".format(np.subtract(u, v))
print "alpha * u = {0}".format(alpha * u)
print "Dot product of u and v is {0}".format(np.dot(u, v))
print "Norm of u is {0}".format(np.linalg.norm(u))

# 3. Matrix Operations

# In case the operation is not defined, numpy will throw an exception

errorMsg = "Not defined!"

try:
    print "A + C = \n{0}".format(np.add(A, C))
except ValueError:
    print "A + C = " + errorMsg
try:
    print "A - CT = \n{0}".format(np.subtract(A, C.transpose()))
except ValueError:
    print "A - CT = " + errorMsg
try:
    print "CT + 3D = \n{0}".format(np.add(C.transpose(), 3 * D))
except ValueError:
    print "CT + 3D = " + errorMsg
try:
    print "BA = \n{0}".format(np.matmul(B, A))
except ValueError:
    print "BA = " + errorMsg
try:
    print "BAT = \n{0}".format(np.matmul(B, A.transpose()))
except ValueError:
    print "BAT = " + errorMsg

# Optional

try:
    print "BC = \n{0}".format(np.matmul(B, C))
except ValueError:
    print "BC = " + errorMsg
try:
    print "CB = \n{0}".format(np.matmul(C, B))
except ValueError:
    print "CB = " + errorMsg
try:
    print "B^4 = \n{0}".format(np.linalg.matrix_power(B, 4))
except ValueError:
    print "B^4 = " + errorMsg
try:
    print "AAT = \n{0}".format(np.matmul(A, A.transpose()))
except ValueError:
    print "AAT = " + errorMsg
try:
    print "DTD = \n{0}".format(np.matmul(D.transpose(), D))
except ValueError:
    print "DTD = " + errorMsg
