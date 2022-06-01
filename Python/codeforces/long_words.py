num_words=int(input())
new_words=[]
for i in range(num_words):
    word=input()
    if(len(word)>10):
        new_words.append(word[0]+str(len(word)-2)+word[len(word)-1])
    else:
        new_words.append(word)

for i in new_words:
    print (i)