n, k, l, c, d, p, nl, np=list(map(int,input().split()))
total_lime_pieces=c*d
total_drink=k*l
answer=int(min(int(total_drink/nl),total_lime_pieces,int(p/np))/n)
print(answer)