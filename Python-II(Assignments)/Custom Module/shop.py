import bill
a={}
bill.new_item(a)
bill.new_item(a)
bill.new_item(a)
b=int(input('Enter the discount rate:'))
bill.discount(a,b)
print(f'The total bill is:{bill.invoice(a)}')