def new_item(d):
    a=input('Enter the name of the item:')
    b=int(input('Enter the price of the item:'))
    d[a]=b
def discount(d,x):
    for k,v in d.items():
        d[k]=v-(v*(x/100))
def invoice(d):
    total=0
    for v in d.values():
        total=total+v
    return total