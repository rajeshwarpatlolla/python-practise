# Reverse whole string
a = 'This is sample string'
b=''

# for i,j in enumerate(a):
#   b+=a[int(len(a)-i-1)]

b = ''.join(reversed(a))
print(b)


# Reverse words in a string
c=a.split(' ')
c=' '.join(reversed(c))
print(c)


# Reverse letters in each word
d=a.split(' ')
e=''
for i in d:
  e+=''.join(reversed(i))+' '

print(e)
