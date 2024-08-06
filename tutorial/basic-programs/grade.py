maths = 80
science = 60
social = 70



def getGrade():
  avg = (maths+science+social)/3
  if(avg>=70):
    print('passed with A grade')
  elif(avg<70 and avg>=60):
    print('passed with B grade')
  elif(avg<60 and avg>=50):
    print('passed with C grade')
  else:
    print('passed with D grade')


if (maths<40):
  print('failed in maths')
elif (science<40):
  print('failed in science')
elif (social<40):
  print('failed in social')
else:
  getGrade()
