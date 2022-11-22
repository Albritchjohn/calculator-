print ("Enter you operator if + is addition, - is subtraction, * is multiplication, / is divide")

print ("Choice your operator +,-,*,/")
opp = input("Enter your operator: ")

if opp=="+":
	a = int(input("Enter the number: "))
	b = int(input("Enter the number: "))
	result = a+b
	print (result)

elif opp=="-":
	a = int(input("Enter the number: "))
	b = int(input("Enter the number: "))
	result = a-b
	print (result)

elif opp=="*":
	a = int(input("Enter the number: "))
	b = int(input("Enter the number: "))
	result = a*b
	print (result)

elif opp=="/":
	a = int(input("Enter the number: "))
	b = int(input("Enter the number: "))
	result = a/b
	print (result)

else:
	print ("Invalid")