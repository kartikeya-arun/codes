def isIn(char, aStr):
    '''
    char: a single character
    aStr: an alphabetized string
    
    returns: True if char is in aStr; False otherwise
    '''
    # Your code here
    if aStr=='':
        return False
    if len(aStr)==1:
        return aStr==char
    m=len(aStr)//2
    midchar=aStr[m]
    if char==midchar:
        return True
    elif char<midchar:
        return isIn(char,aStr[:m])
    else:
        return isIn(char,aStr[m+1:])
