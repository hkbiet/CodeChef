num_tests = int(input())

def compute_blindness():
	N, M, L = list(map(int,input().split()))

	list_of_M_lists = []

	for each_M_list in range(M):
		list_of_M_lists.append(list(map(int,input().split())))
	
	L_list = list(map(int,input().split()))

	visible_pair = 0


	for each_color in L_list:
		color_1 = each_color
		print("COLOR ONE: ", color_1)

		if((L_list.index( color_1 ) + 1) < len(L_list) ):
			print("INSIDE")
			color_2 = L_list [ L_list.index( color_1 ) + 1 ]
			print("COLOR TWO: ", color_2)
			each_M_list = 0
			for each_M_list in list_of_M_lists:
				if ( (color_1 in each_M_list) and (color_2 in each_M_list)):
					flag = True
					print("FLAG = TRUE")
			if (not flag):
				visible_pair = visible_pair + 1
	
	print(visible_pair + 1)


for each_test in range(num_tests):
	compute_blindness()