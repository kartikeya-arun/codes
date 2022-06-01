shoes=list(map(int,input().split()))
unique_shoes=set(shoes)
# answer-
print(4-len(unique_shoes))

# One-liner because who doesn't love a good headache trust me it doesn't kill to declare variables
# print(4-len(set(list(map(int,input().split())))))