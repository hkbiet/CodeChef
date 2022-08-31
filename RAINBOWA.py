def rainbow():
    try:
        num_elements = int(input())
        array = list(map(int, input().split()))
        master = 1
        flag = 0
        
        for i in range((num_elements//2)+1):
            if (array[i] == array[(num_elements-1)-i] and (array[i] == master or array[i] == master+1)):
                master = array[i]
            else:
                flag = 1
                break
                
        
        if array[num_elements//2] == 7 and flag == 0:
            print("yes")
        else:
            print("no")
    except Exception as e:
        pass





t = int(input())


for i in range(t):
    rainbow()
