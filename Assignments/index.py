
b=list(map(int,input('Enter the elements of the list: ').split()))
a=int(input("Enter the element to find index: "))
try :
    print(f"The element is found at index: {b.index(a)} ")
except (IndexError,ValueError):
    print("Element not in the list")
