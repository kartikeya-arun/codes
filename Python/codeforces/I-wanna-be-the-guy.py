n=int(input())
x=input()
y=input()
p=int(x[0])
a=list(map(int,x[1:].split()))
q=int(y[0])
b=list(map(int,y[1:].split()))

if(len(set(a+b))<n):
        print('Oh, my keyboard!')
else:
    print('I become the guy.')