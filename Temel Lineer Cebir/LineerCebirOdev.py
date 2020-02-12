
import numpy as np

#SORU 1

print("\nSORU  -  1\n\n")

A = np.array([[1,2,3],[4,5,6],[7,8,9]])
B = np.array([[1,2],[0,-1],[1,2]])

#a)
print("a) ",A*(-1))
print("\n")
#b)
print("b) ",A*(3))
print("\n")
#c)
try:
    print("c) ",A+2*B)
except:
    print("c) A+2xB shapes don't match!..")
print("\n")
#d)
print("d) ",A.T)
print("\n")
#e)
print("e) ",B.T)
print("\n")
#f)
print("f) ",np.dot(A,B))
print("\n")
#g)
try:
    print("g) ",np.dot(B,A))
except:
    print("g) Shapes don't match!..")

#SORU 3
print("\nSORU  -  3\n\n")

E = [[4,7,8],[3,5,7],[11,4,3]]

F = [[6,12,4],[8,9,1],[13,4,2]]

G = [2,5,9]

if np.dot(np.dot(E,F),G).all() == np.dot(E,np.dot(F,G)).all():
    print("\nMatrix Multiplication is Associative")
else:
    print("Matrix Multiplication is not Associative")

#SORU 5
print("\nSORU  -  5\n\n")

B = np.dot(A,A.T)
B_trans = B.T

if B.all() == B_trans.all():
    print("B is symmetric\n")
else:
    print("B is not symmetric!\n")
print("\nB Transpose =\n",B_trans)
print("\nB =\n",B)

#SORU 7
print("\nSORU  -  7\n\n")

C = A+B
print("A+B =\n",C)

diag1 = sum([C[i][i] for i in range(len(C))])

diag2 = sum([A[i][i] for i in range(len(A))])
diag3 = sum([B[i][i] for i in range(len(B))])

if diag1 == (diag2+diag3):
    print("Rule works!")
else:
    print("Rule is a lie..")