# cook your dish here

def relative():

	g,c = list(map(float, input().split()))

	result = (c*c) / (2 * g)

	print(int(result))



num_tests = int(input())

for each_test in range(num_tests):
	relative()