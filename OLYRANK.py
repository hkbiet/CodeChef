# cook your dish here

def winner():
    G1, S1, B1, G2, S2, B2 = list(map(int, input().split()))
    country_one_tally = G1 + S1 + B1
    country_two_tally = G2 + S2 + B2
    
    if(country_one_tally > country_two_tally):
        print(1)
    else:
        print(2)
    return



num_tests = int(input())

for each_test in range(num_tests):
    winner()
