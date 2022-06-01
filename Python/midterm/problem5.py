def dict_invert(d):
    inverse={}
    for i in d.keys():
        if d[i] in inverse:
            inverse[d[i]].append(i)
        else:
            inverse[d[i]]=[i]
    for val in inverse.values():
        val.sort()
    return inverse
############################################
d={4:True, 2:True, 0:True}
print(dict_invert(d))
