n = int(input("enter the terms"))
a=0
b=1
if n==1:
  print(a,end=" ")
elif n==2: 
  print(a,end=" ")
  print(b,end=" ")
else:
  print(a,end=" ")
  print(b,end=" ")
  for i in range(2,n):
    print(a+b,end=" ")
    b=a+b
    a=b-a