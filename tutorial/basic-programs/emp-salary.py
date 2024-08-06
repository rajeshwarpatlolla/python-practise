a = int(input('Enter no.of employees: '))
employees={}

for i in range(a):
  name = input('Enter employee name: ')
  salary = input('Enter employee salary: ')
  employees[name]=salary

print(employees)

while True:
  b=input('Enter empoyee name whose salary you want to know: ')
  print(employees.get(b))
