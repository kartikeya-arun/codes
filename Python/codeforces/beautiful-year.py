y=int(input())
beautifulYearFound=False

while not beautifulYearFound:
    y+=1
    if len(set(str(y)))==4:
        beautifulYearFound=True

print(y)