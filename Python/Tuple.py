def oddTuples(aTup):
    '''
    aTup: a tuple
    
    returns: tuple, every other element of aTup. 
    '''
    # Your Code Here
    newTup=()
    length=len(aTup)
    for i in range(length):
        if i%2==0:
            newTup+=(aTup[i],)
            
    print (newTup)

''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
################################################################################
################################################################################

''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
aTup=('I', 'am', 'a', 'test', 'tuple')
oddTuples(aTup)
