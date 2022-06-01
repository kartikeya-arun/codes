operands=list(map(int,input().split('+')))

operands.sort()

if(len(operands)==1):
    print(str(operands[0]))
else:
    print('+'.join(list(map(str,operands))))