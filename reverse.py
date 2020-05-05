x=int(input("Enter 3 digit number"))
y=0
y+=x%10*100
y+=int(x/10) % 10 *10 
y+=int(x/100)*1

print(y)