from geometry import shapes,volumes
a=float(input('Enter the length of the rectangle:'))
b=float(input('Enter the breadth of the rectangle:'))
r=float(input('Enter the radius of the circle:'))
x=int(input('Enter the side of the cube:'))
print('The rectangle area:',shapes.rectangle_area(a,b))
print('The circle area:',shapes.circle_area(r))
print('The cube volume:',volumes.cube_volume(x))
print('The sphere radius:',volumes.sphere_volume(r))