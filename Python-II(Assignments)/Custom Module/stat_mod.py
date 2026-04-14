def mean(l):
    s=sum(l)
    m=s/len(l)
    return m
def median(l):
    l.sort()
    x=len(l)
    if x%2==0:
        n1=int((x/2))
        n2=int((x/2)+1)
        m=(l[n1-1]+l[n2-1])/2
        return m
    else:
        n=int((x+1)/2)
        return l[n-1]
def mode(l):
    a={}
    for i in l:
        a[i]=a.setdefault(i,0)+1
    max=-1
    m=None
    for k,v in a.items():
        if v>max:
            max=v
            m=k
    return m