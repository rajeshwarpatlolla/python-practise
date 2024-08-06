# a = lambda x,y:x+y

# print(a(1,2))


# def fullname (fn):
# 	return lambda ln: fn+ln

# print(fullname('a')('b'))


def getfullname(fn):
	# def x(ln): 
	# 	return fn+ln
	return lambda x:fn+x


# print(getfullname('a')('b'))


# if 2<33 and 2<3:
# 	print('yes')
# elif 3>22 or 22>3:
# 	print('no')
# else:
# 	print('none')

# o = {'a':1,'b':2,'c':3,'d':4}
# for a in o:
# 	print(a, o[a])


# for i in range(1,5):
# 	for j in range(1,5):
# 		print(i*j)



# c=10

# while c>5:
# 	c=c-1

# 	if c==7:
# 		pass
# 	print(c)


# try:
# 	if 2<num:
# 		print('try block')
# except:
# 	print('except block')


# def get_name():
# 	print('test')

# get_name()


# print(dir(1))
# print('TEST'.lower())
a="print(1)"
# print(eval(a))
# print('hello' + '1')
# print(int(1212.12), float(12.123123))

def calculate_factorial(num):
	total=1
	while num>0:
		total = total*num
		num=num-1
	print(total)
              
# calculate_factorial(6)


# class Person:
# 	def __init__(self, name, age):
# 		self.name=name
# 		self.age=age
	
# 	def getName(self):
# 		return self.name
	
# 	def getAge(self):
# 		return self.age

# p = Person('test', 12)

# print(p.getName(), p.getAge())

"""
class Car:
	def __init__(self):
		self.wheels=4
		self.seats=4

	def drive(self):
		print('driving car')

class SportsCar(Car):
	def __init__(self):
		super().__init__()
		self.type = 'sports car'
		self.seats = 2
	
	def drive(self):
		print('driving sports car')

sc = SportsCar()
print(sc.type, sc.seats, sc.wheels, sc.drive())

c = Car()
print(c.wheels, c.seats, c.drive())
"""


# if 2<3:
# 	print('yes')
# else:
# 	print('no')

# a = 5j
# bin = 0B10101
# hex = 0X12f1
# b= True

# print(bin, type(bin), hex, type(hex), b, type(b), (2<3) == True)

# print(int(12.121), float(12), bool('1'), type(float('1.11')), bin(4), hex(1580), oct(10), type(0b10101))
print(type(0b1010) is int, isinstance(1j, complex), float(1))


x=2+4j
print(x, x.real, x.imag)
