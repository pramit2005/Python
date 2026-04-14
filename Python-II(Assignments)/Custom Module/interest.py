def si(p,r,t):
    return p*(r/100)*t
def cpi(p,r,t):
    ci=(p*((1+(r/100))**t))-p
    return ci
