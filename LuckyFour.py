# cook your dish here

def luckyFour():
	
	number = int(input())
	count = 0
	temp = number
	while int(temp) > 0:
		rem = temp % 10
		if int(rem) == 4:
			count = count + 1
			#print(count)
		temp = temp / 10
	print(count)
	count = 0





num_tests = int(input())

for test_case in range(num_tests):
	luckyFour()