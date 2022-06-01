def is_triangular(k):
    sum=0
    n=1
    if k<0:
        return False
    while (sum<k):
        sum+=n
        if (sum==k):
            return True
        n+=1
    return False
