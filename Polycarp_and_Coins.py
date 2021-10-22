import math


num_tests = int(input())



def compute_diff():
	total_money = int(input())
	if(total_money == 1):
		print("1 0")
		return
	Q = total_money // 2
	R = 0
	Q_major = 0
	R_major = 0
	diff = math.inf

	while(Q):
		R = total_money - (2 * Q)
		temp_diff = abs(Q-R)

		if(temp_diff < diff ):
			diff = temp_diff
			Q_major = Q
			R_major = R
			Q = Q - 1
		elif (temp_diff > diff):
			print(str(R_major) + " " + str(Q_major))
			return
		else:
			Q = Q - 1
	return






for each_test in range(num_tests):
	compute_diff()