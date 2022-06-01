import random
import string
key=string.ascii_letters
shift=random.randint(1,25)
shift_dict={}
for i in range(len(key)):
    try:
        shift_dict[key[i]]=key[i+shift]
    except IndexError:
        shift_dict[key[i]]=key[i+shift-52]
#print( shift_dict)


word='Fuck You!!!'
cyphWord=''
for l in word:
    try:
        cyphWord+=shift_dict[l]
    except KeyError:
        cyphWord+=l
print(cyphWord)

        
