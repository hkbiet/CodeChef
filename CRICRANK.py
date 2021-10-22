
num_tests = int(input())


def better_player():
	A_R, A_W, A_C = list(map(int, input().split()))
	B_R, B_W, B_C = list(map(int, input().split()))

	A_points = 0
	B_points = 0

	# for each case compute points of each player

	if(A_R > B_R):
		A_points =  A_points + 1
	else:
		B_points = B_points + 1

	if(A_W > B_W):
		A_points =  A_points + 1
	else:
		B_points = B_points + 1

	if(A_C > B_C):
		A_points =  A_points + 1
	else:
		B_points = B_points + 1

	if(A_points > B_points):
		print("A")
	else:
		print("B")


for each_test in range(num_tests):
	better_player()
