ip=list(map(int,input().split()))
ip.sort()
remaining=(ip[1]-ip[0])//2
print(ip[0],remaining)