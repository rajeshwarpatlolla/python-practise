a,b,c=1,2,3

# print(a+b,b-c, a*b, c/b, b**c, c//b, c%b)

# print(id(True)==id(True))

x,y=12,11
b=True
# print(x,y, x==y, x>y, x and y, x or y, not b, x==12)

height=5.9
weight=60

# bmi = weight in kg / height in meters * height in meters
heightInMeters = height*0.4536
bmi = weight/ (heightInMeters*heightInMeters)
print(bmi)


# print(1,2, 3,4,sep='++')

# print('one: %s, two is %f and %.2f' %(a,b,c))
# print('one: {}, two is {}'.format(a,c))


# name=input('Enter name: ')
# nums=input('Enter 2 numbers: ')

# for n in nums:
#   print(type(n))


products_list = {'a':1, 'b':2, 'c': 3}

product_1 = input('Enter first product name: ')
quantity_1 = int(input(f'Enter quantity for {product_1}: '))

product_2 = input('Enter first product name: ')
quantity_2 = int(input(f'Enter quantity for {product_2}: '))

sub_total=0
total=0

sub_total += products_list[product_1] * quantity_1
sub_total += products_list[product_2] * quantity_2

tax= sub_total*0.08
total+=sub_total+tax
print(f'Sub total is {sub_total}, tax is {tax} total is {total}')
