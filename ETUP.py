num_tests = int(input())



def count_tuples():
	array_length , num_of_queries = list(map(int,input().split()))
	input_array = list(map(int,input().split()))

	for query in range(num_of_queries):
		L, R = list(map(int,input().split()))

		k = R - 1
		i = L - 1

		tuple_count = 0

		while(k):
			for j in range(k-1, i , -1):
				for i in range(j-1, -1, -1):
					if(L-1 <= i < j < k <= R-1):
						sum_tuple = input_array[i] + input_array[j] + input_array[k]
						if ((sum_tuple % 2) == 0):
							tuple_count = tuple_count + 1

			k = k - 1

		print(tuple_count)



for each_test in range(num_tests):
	count_tuples()