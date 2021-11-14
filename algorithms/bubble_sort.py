test_array = [7, 5, 9, 2, 5]
a = 5
b = 3
c = a # c = 5
a = b # a = 3
b = c # b = 5 

swapped = True
while swapped == True:
    swapped = False
    for i in range (0, len(test_array) - 1):
        if test_array[i] > test_array[i + 1]:
            x = test_array[i + 1]
            test_array[i + 1] = test_array[i]
            test_array[i] = x 
            swapped = True
    print(test_array)