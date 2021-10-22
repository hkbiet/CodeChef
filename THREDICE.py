num_tests = int(input())



def find_prob():
	X, Y = list(map(int,input().split()))

	dice_items = [1,2,3,4,5,6]

	desired_outcome = 0

	for each_item in dice_items:
		if ( each_item > ( X + Y) ):
			desired_outcome = desired_outcome + 1
	probability = desired_outcome / 6

	print(probability)



for each_test in range(num_tests):
	find_prob()