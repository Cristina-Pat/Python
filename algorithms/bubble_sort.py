test_array=[]
num_elements = 0

while num_elements < 5:
    numbers = input("Please insert your number: ")
    test_array.append(numbers)
    num_elements += 1

def bubble_sort (test_array: list) -> list:
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

bubble_sort(test_array)