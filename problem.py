import math


num_tests = int(input())


# computing money here
def compute_diff():
	total_money = int(input())

	if total_money % 3 == 0:
		c1=c2=total_money//3
		#prinitng answers
		print(str(c1) + " " +str(c2))
		return
	elif ( total_money - 1 ) % 3==0:
		c2 = ( total_money-1)//3
		c1 = c2+1
		#prinitng answers
		print(str(c1)+" "+str(c2))
		return
	elif ( total_money - 2 ) % 3 == 0:
		c1 = ( total_money - 2 ) // 3
		c2 = c1 + 1
		#prinitng answers
		print(str(c1)+ " " + str(c2))
		return






for each_test in range(num_tests):
	compute_diff()