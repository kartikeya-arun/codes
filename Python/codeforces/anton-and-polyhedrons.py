n=int(input())

answer=0
shapes={'Tetrahedron':4,'Cube':6,'Octahedron':8,'Dodecahedron':12,'Icosahedron':20}
for i in range(n):
    answer+=shapes[input()]

print (answer)