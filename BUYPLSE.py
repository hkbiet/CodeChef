def compute():
	test_case = input()

	splitted = test_case.split()


	cost_a = int(splitted[0])
	cost_b = int(splitted[1])

	quantity_a = int(splitted[2])
	quantity_b = int(splitted[3])

	total_cost = cost_a * quantity_a + cost_b * quantity_b

	print(total_cost)


compute()