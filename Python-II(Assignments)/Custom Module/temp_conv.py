import temperature
a=float(input('Enter a temp in celsius:'))
print(f'The temp in fahrenheit:{temperature.c_f(a)}\nThe temp in Kelvin:{temperature.c_k(a)}')
b=float(input('Enter a temp in fahrenheit:'))
print(f'The temp in celsius:{temperature.f_c(b)}\nThe temp in Kelvin:{temperature.f_k(b)}')
c=float(input('Enter a temp in kelvin:'))
print(f'The temp in celsius:{temperature.k_c(c)}\nThe temp in fahrenheit:{temperature.k_f(c)}')