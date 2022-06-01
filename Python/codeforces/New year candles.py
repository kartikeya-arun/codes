a,b=list(map(int,input().split()))
count=a
while a>=b:

# You'll die alone Vasily! I hate romance 

    div=int(a/b)
    rem=a%b
    a=div+rem
    count+=div
print(int(count))