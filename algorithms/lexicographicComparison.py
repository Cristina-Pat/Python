list1 = [1, 2, 4]
list2 = [1, 2, 3]

def comparison (list1: list, list2: list) -> bool:
    if len(list1) != len(list2):
        print('The lists have different lenght.')

    for i in range(len(list1)):
        if list1[i] != list2[i]:
            print('The lists have different elements.')
    print('Both list have the same elements.')

comparison(list1, list2)