num_tests = int(input())




def compute_diff():
	input_string = input()
	resultant = {i : input_string.count(i) for i in set(input_string)}

	solution_computed= 0
	temp = 0
	for key in resultant.keys():
		if resultant[key]>=2:
			solution_computed = solution_computed + 1
		elif resultant[key]==1:
			temp = temp + 1
	solution_computed = solution_computed + (temp // 2)
	print(solution_computed)
	return


for each_test in range(num_tests):
	compute_diff()