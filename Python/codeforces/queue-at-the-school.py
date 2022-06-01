n,t=list(map(int,input().split()))
list1=[]
list1[:0]=input()

while t>0:
    j=0
    while j<n-1:
        if(list1[j]=='B' and list1[j+1]=='G'):
            list1[j],list1[j+1]=list1[j+1],list1[j]
            j+=1
        j+=1
    t-=1
print (''.join(list1))