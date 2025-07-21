item={149:5,249:3,399:3,299:5,199:4}
total=0
for k,v in item.items():
    x=int(input(f'Enter the quantity of item priced {k}: '))
    if x>v:
        x=v
    total=total+(x*k)
if total<1500:
    disc=total*0
    print(f'Your discount amount is {disc} & total amount payable is {total-disc}')
elif 2000>total>=1500:
    disc = total * 0.05
    print(f'Your discount amount is {disc} & total amount payable is {total - disc}')
elif 2500>total>=2000:
    disc = total * 0.1
    print(f'Your discount amount is {disc} & total amount payable is {total - disc}')
elif 3000>=total>2500:
    disc = total * 0.12
    print(f'Your discount amount is {disc} & total amount payable is {total - disc}')
else:
    disc = total * 0.15
    print(f'Your discount amount is {disc} & total amount payable is {total - disc}')