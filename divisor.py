x = int(input("Please enter an integer for which you want to know the divisors: "))
print("The divisors of the integer you entered are: ")

for i in range(1, x+1):
	if(x%i == 0):
		print(i)
