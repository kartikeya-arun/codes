t=int(input())
answer=[]
for i in range(t):
    num=int(input())
    # even*even=even
    # even*odd=even
    # odd*even=even
    # odd*odd=odd
    # if a number has no odd divisors, then it must be a power of two.

    # q=num
    # while q%2!=1:
    #     q=q//2
    # if q==1:
    #     answer.append('no')
    # else:
    #     answer.append('yes')

    if num&(num-1)==0:
        answer.append('no')
    else:
        answer.append('yes') # Bitwise AND because if n is a power of two then n-1 will have 0 in exactly the bit in which n will have 1

print('\n'.join(answer))
            