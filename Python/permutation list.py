import operator
def is_list_permutation(L1, L2):
    '''
    L1 and L2: lists containing integers and strings
    Returns False if L1 and L2 are not permutations of each other. 
            If they are permutations of each other, returns a 
            tuple of 3 items in this order: 
            the element occurring most, how many times it occurs, and its type
    '''
    if L1==L2==[]:
        return (None,None,None)
    elif len(L1)==len(L2):
        D1={i:L1.count(i) for i in L1}
        D2={i:L2.count(i) for i in L2}
        if D1==D2:
            return (max(D1.items(), key=operator.itemgetter(1))[0],D1[max(D1.items(), key=operator.itemgetter(1))[0]],type(max(D1.items(), key=operator.itemgetter(1))[0]))
        else:
            return False
    else:
        return False
