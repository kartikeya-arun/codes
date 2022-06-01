################################################### Comparing each element ##########################################################
def findMinMax(array):
    min=array[0]
    max=array[len(array)-1]
    for i in range(len(array)):
        if array[i]>max:
            max=array[i]
        if array[i]<min:
            min=array[i]
    return (max,min)

################################################### Sorting #########################################################################
# def findMinMax(array):
#     array.sort()
#     return (array[len(array)-1],array[0])

lst=list(map(int,input().split()))
answer=findMinMax(lst)
print("Max: "+str(answer[0])+" Min: "+str(answer[1]))