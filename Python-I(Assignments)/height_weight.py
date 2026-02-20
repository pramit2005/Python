h=float(input('Enter the height(ft-inch): '))
h_inch=(h-int(h))*10
h_ft=int(h)
w=int(input('Enter the weight(lbs): '))
print(f' The height is:{(h_ft*12*2.54)+(h_inch*2.54)}cm\n The weight is:{w*0.453}kg')