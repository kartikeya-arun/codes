import math
x=int(input())
rev=0
upperLimit=2147483647
lowerLimit=-2147483648
while x:
    pop=int(math.fmod(x,10))
    x=int(x/10)
    if rev>upperLimit//10 or (rev==upperLimit//10 and pop>=upperLimit%10):
        print(0)
    if (rev<lowerLimit//10 or (rev==lowerLimit//10 and pop<=lowerLimit%10)):
        print(0)
    rev=(rev*10)+pop
print(rev)