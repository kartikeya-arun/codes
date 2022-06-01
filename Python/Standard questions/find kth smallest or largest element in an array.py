import random
# FOR RANDOMLY CHOOSING AN ELEMENT AS PIVOT

############################################## PARTITION LOGIC (SAME AS QUICK SORT) ##########################################
def Partition(array,left,right):
    pivot=array[right]
    i=left
    for j in range(left,right):
        if(array[j]<=pivot):
            array[i],array[j]=array[j],array[i]
            i+=1
    array[i],array[right]=array[right],array[i]
    return i

######################################################## RANDOM PARTITION ####################################################
def RandomPartition(array,left,right):
    randomIndex=int(random.random()*(right-left+1))
    array[left+randomIndex],array[right]=array[right],array[left+randomIndex]
    return Partition(array,left,right)
    
#################################################### QUICK SELECT ALGORITHM ##################################################
def KthSmallest(array,left,right,k):    
    # IF K IS SMALLER THAN THE NUMBER OF ELEMENT IN THE ARRAY-
    if(k > 0 and k <= right - left + 1):                         # WE FOLLOW A SIMILAR APPROACH TO QUICK SORT
        pos=RandomPartition(array,left,right)          # THE DIFFERENCE IS WE DO NOT SORT THE WHOLE ARRAY
        
        # WE FIND THE RIGHT POSITION OF THE PIVOT IN THE ARRAY AND SEE IF IT IS AT THE INDEX OF THE KTH SMALLEST ELEMENT
        if(pos-left==k-1):
            return array[pos]

        # IF THE POSITION OF PIVOT IS AFTER THE INDEX OF Kth SMALLEST ELEMENT WE CONSIDER THE PART OF ARRAY BETWEEN LEFT INDEX AND
        # INDEX POS-1 SINCE IT IS IMPOSSIBLE THAT THE ELEMENT WILL BE IN THE OTHER PART OF THE ARRAY. 
        if(pos-left>k-1):
            return KthSmallest(array,left,pos-1,k)

        # SIMILARLY, IF POSITION OF THE PIVOT IS SMALLER THAN THE INDEX OF Kth SMALLEST ELEMENT WE CONSIDER THE PART OF ARRAY BETWEEN
        # POS+1 AND RIGHT INDEX OF THE ARRAY. 
        return KthSmallest(array,pos+1,right,k-pos+left-1)
        
    # IF K IS GREATER THAN THE NUMBER OF ELEMENTS IN THE ARRAY-
    else:
        return -1

################################################### MAIN PROGRAM (DRIVER CODE) ################################################

lst=list(map(int,input().split()))
k=int(input())
l=0
r=len(lst)-1
print (KthSmallest(lst,l,r,k))