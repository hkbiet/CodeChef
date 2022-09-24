for _ in range(int(input())):
    number = int(input())
    
    result = list(range(number - (number & 1), 0, -2))
    result += list(range(1, number+1, 2))
    print(*result)
