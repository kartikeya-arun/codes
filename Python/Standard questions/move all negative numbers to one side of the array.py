##################################################### USING QUICK SORT PARTITION ####################################################
def rearrange(array):
    j=0
    for i in range(len(array)):
        if array[i]<0:
            array[i],array[j]=array[j],array[i]
            j+=1
    return array

################################################################# MAIN ##############################################################
n=int(input())
arr=list(map(int,input().split()))
print(rearrange(arr))