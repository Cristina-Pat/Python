list = [8, 6, 2, 10, 5, 7]

min = list[0]
for i in range (0, len(list) - 1): 
    for j in range (i+1, len(list) - 1):
        if list[j] < min:
            min = list[j] 
            x = j
        if list[i] > min:
            y = list[x]
            list[x] = list[i]
            list[i] = y
print(list)          
print(min)
print(x)