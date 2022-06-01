mat=[]

def idx2d(matrix,element):
    for i,x in enumerate(matrix):
        if element in x:
            return (i,x.index(element))

for i in range(5):
    mat.append(list(map(int,input().split())))

one_location=idx2d(mat,1)
answer=abs(2-one_location[0])+abs(2-one_location[1])
print(answer)