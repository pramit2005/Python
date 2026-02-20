#Create a shopping cart program where users can add items along with their prices and calculate the total bill.
#Implement exception handling to manage invalid price inputs and attempts to access items that do not exist in the cart.
#[Invalid price input → ValueError, Accessing non-existing item → KeyError ]
shop={}
c='start'
while(True):
    c=input("Enter the name of the product(Enter 'stop' to exit): ")
    if c.lower()=='stop':
        break
    try:
        d=int(input('Enter the price of the item: '))
        e = int(input('Enter the number of items: '))
        if d<0 or e<0:
            raise ValueError
    except ValueError:
        print('Invalid input! Enter positive numbers only.')
        continue
    else:
        shop[c]=[d,e]
while(True):
    x=input("Enter the name of the item to update price(Enter 'no' to exit): ")
    if x.lower()=='no':
        break
    try:
        y=int(input('Enter the price to update: '))
        shop[x][0]=y
    except ValueError:
        print('Invalid input! Enter positive numbers only.')
        continue
    except KeyError:
        print('Item does not exist in shopping list')
        continue
total=0
for k,v in shop.items():
    total=v[0]*v[1]+total
print('The total cost is:',total)