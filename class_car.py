class Car:
    def  __init__(self,brand,year):
        self.brand=brand
        self.year=year
    def display_info(self):
        print(f'The brand of the car is {self.brand} & {self.year}')
c1=Car('Hyundai',2010)
c2=Car('Tata',2019)
c1.display_info()
c2.display_info()
