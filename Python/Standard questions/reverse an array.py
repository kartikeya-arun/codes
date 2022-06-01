#################################################### RECURSIVE METHOD ############################################################
def reverse(array,start,end):
    if start>=end:
        return
    array[start],array[end]=array[end],array[start]
    reverse(array,start+1,end-1)

#################################################### ITERATIVE METHOD ############################################################
# def reverse(array,start,end):
#     while start<end:
#         array[start],array[end]=array[end],array[start]
#         start+=1
#         end-=1

lst=list(map(int,input().split()))
start=0
end=len(lst)-1
reverse(lst,start,end)
print (lst)