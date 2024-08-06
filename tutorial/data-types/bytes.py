b = [4,5,6,7,8]

b1 = bytes(b)
# b1[1]=111

b2 = bytearray(b)
b2[1]=2

print(b, b1, b2, type(b), type(b1), type(b2), b1*2, b2*2, b1[2:], b2[:3])
