# remove duplicates from an array
a = [1,2,3,4,1,2,4,456,7,686,7867,8678,543,12,2,3,4,5, 'a', 'b','a']
b=[]

# approach 1
# for i in a:
#   if i not in b:
#     b.append(i)

# approach 2
b = set(a)
print(b)

# remove duplicate characters from a string
c="This is a sample string"
d=[]

for i in c:
  if i not in d:
    print(i)
    d.append(i)

print(''.join(d))

