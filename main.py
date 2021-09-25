n = 3
A = [
    [],
    [3,1,2]
]
for i in range(n):
    A[0].append(i+1)
print(A)
B=[
    [],
    [2,3,1]
]
for i in range(n):
    B[0].append(i+1)
print(B)
# X = A o B = id
X=[
    [],
    []
]
for i in range(n):
    X[0].append(i+1)
    j=A[1][i]
    X[1].append(B[1][j-1])
print(X)
# Y = B o A = id
Y=[
    [],
    []
]
for i in range(n):
    Y[0].append(i+1)
    j=B[1][i]
    Y[1].append(A[1][j-1])
print(Y)