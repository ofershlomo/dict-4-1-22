workers=[]
hours=[]

while True:
  name=input("if you wish to stop, type STOP ")
  if(name=="STOP"):
    break
  else:
    workers.append(name)
    # hours.append(input("enter worker name"))
for i in range(len(workers)):
  print("hours for", workers[i],end=" ")
  hour=float(input(":"))
  hours.append(hour)
saldict=dict(zip(workers,hours))
print(saldict)


for x in saldict:
  print("worker name : ",x,saldict[x]*30)