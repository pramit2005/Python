import pandas as pd
from geopy.geocoders import Nominatim
df=pd.read_csv(r"D:\Datasets\Zomato_Kolkata_Restaurants.csv\Zomato_Kolkata_Restaurants.csv")
df1=df[["Name","Area","Full_Address"]]
x=list(df1["Full_Address"])
y=[]
geolocator=Nominatim(user_agent="tourism")
for i in x:
    location=geolocator.geocode(i)
    if location != None:
        print(f"{i}:{location}")
        break