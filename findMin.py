data=[]
numString = 0

while numString < 3:
    numbers = input("Please insert your number: ")
    data.append(numbers)
    numString += 1

def findMin (data: list) -> int:
    """Find a min on a string data.
    """
    min = data[0]
    for i in range(0, len(data)-1):
        if data[i+1] < min:
            min = data[i+1]
    print(min)

findMin(data)