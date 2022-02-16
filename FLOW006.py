#num_tests = list(map(int, input().split()))
num_tests = int(input())

def find_digits():
	number = int(input())

	sum = 0
	
	if number < 10 :
	    print(number)
	    return

	while(number >= 10 ):
		remainder = number % 10
		sum = sum + remainder
		number = number // 10

		if number < 10 :
			sum = sum + number

	print(sum)
	
	return
		




for each_test in range(num_tests):
	find_digits()