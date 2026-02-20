
def dec_bin():
    a=int(input('Enter the decimal number: '))
    b=[]
    while a>0 :
        c=a%2
        b.append(str(c))
        a=a//2
    b.reverse()
    print(''.join(b))
dec_bin()
