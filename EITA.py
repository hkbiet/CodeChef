def max_work():
	test_case_data = list(map(int, input().split()))
	d,x,y,z = test_case_data

	regular_work_max = 7 * x
	varying_work_max = d * y + ((7-d) * z)

	if(regular_work_max > varying_work_max):
		print(regular_work_max)
	else:
		print(varying_work_max)
	return




num_tests = int(input())

for each_test in range(num_tests):
	max_work()