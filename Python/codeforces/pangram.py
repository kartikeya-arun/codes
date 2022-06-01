import string
alphabets=set(string.ascii_lowercase)
n=int(input())
print('YES') if set(input().lower())==alphabets else print('NO')