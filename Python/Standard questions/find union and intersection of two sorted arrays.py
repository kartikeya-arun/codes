def union(set1,set2):
    union=[]+set1
    for i in set2:
        if i not in union:
            union.append(i)
    return union

def intersection(set1,set2):
    intersection=[]
    for i in set1:
        if i in set2:
            intersection.append(i)
    return intersection

n1,n2=list(map(int,input().split()))
set1=list(map(int,input().split()))
set2=list(map(int,input().split()))
u=union(set1,set2)
i=intersection(set1,set2)

print (u)
print (i)