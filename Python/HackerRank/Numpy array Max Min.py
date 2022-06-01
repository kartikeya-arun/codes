import numpy
n,m=map(int,input().split())
A=numpy.array([input().split() for _ in range(n)],int)
print (numpy.max(numpy.min(A,axis=1)))