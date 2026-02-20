def bi_dec():
    a=list(input("Enter the binary number: "))
    dec=0
    l=len(a)
    for i,j in zip(a,range(l-1,-1,-1)):
        i = int(i)
        dec = dec + i * (2 ** j)
    print(f'The decimal equivalent is:{dec}')
bi_dec()