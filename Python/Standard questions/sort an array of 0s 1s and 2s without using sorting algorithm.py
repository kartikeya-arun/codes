def Sort012(array):
    count0=0
    count1=0
    count2=0
    for i in array:
        if(i==0):
            count0+=1
        elif(i==1):
            count1+=1
        else:
            count2+=1
    
    return [0]*count0+[1]*count1+[2]*count2

##################################################### MAIN ##########################################################################
n=int(input())
arr=list(map(int,input().split()))

print(Sort012(arr))