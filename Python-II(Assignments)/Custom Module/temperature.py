def c_f(cel):
    f=((9*cel)/5)+32
    return f
def f_c(f):
    c=(5*(f-32))/9
    return c
def c_k(cel):
    k=cel+273
    return k
def f_k(f):
    c=f_c(f)
    k=c_k(c)
    return k
def k_c(kel):
    c=kel-273
    return c
def k_f(kel):
    c=kel-273
    f=c_f(c)
    return f