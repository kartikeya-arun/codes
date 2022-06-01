n=int(input())

def findPlaces(n):
    return(n*n*(n*n-1)-8-24-((n-4)*16)-16-((n-4)*24)-(8*(n-4)*(n-4)))
    #This expression is found after considering every case in the 8*8 chessboard
    # Think for yourself

for i in range(1,n+1):
    print(findPlaces(i)//2)