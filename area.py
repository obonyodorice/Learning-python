# radius=20
# length= 17
# area=3.142*int(radius)**2
# volume=area*length
# print('The area is:',area,'and volume is:',volume)
# import random
# print(random.randrange(0,10))

radius=input('Enter the radius: ')
height=input('Enter the height: ')
base_area=3.142*int(radius)**2
Total_area=2*base_area + 2*3.142*int(radius)*int(height)
Total_volume=base_area*int(height)
print ('The area of a cylinder is :', Total_area, 'and Volume is:', Total_volume)