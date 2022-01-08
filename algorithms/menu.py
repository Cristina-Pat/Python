def free_from (menu: list, ingredient: str) -> bool:
    """Search the ingredient given in each dish of menu.
    Preconditions: true
    Postconditions: the menu is free_from the ingredient is true if and only if there's no match for 
    the ingredient in the menu.
    """
    for i in range (0, len(menu)):
        dish = menu[i]
        for j in range (0, len(dish)):
            if dish[j] == ingredient:
                return False
    return True     



menu = [
         ['soup','onion','potato','leek','celery'],
         ['pizza','bread','tomato','cheese','cheese'],
         ['banana']
       ]

# This code tests the implementation
test_menu = [ ['potato'],
              ['cheese'],
              ['apple'] ]
expected_result = True
if free_from(test_menu, 'water') == expected_result:
    print('Working')
else:
    print('Failure')

test_menu2 = [['stew', 'onion', 'potato', 'oil'],
              ['soup','dill', 'carrot', 'ckichen', 'parsley'],
              ['orange']]
expected_result2 = True
if free_from(test_menu2, 'water') == expected_result2:
    print('Test 2: Working')
else:
    print('Test 2: Failure')

test_menu3 = [['butter'],
              ['bread', 'flour', 'water', 'yeast'],
              ['pancakes', 'flour', 'milk', 'sugar']]
expected_result3 = False
if free_from(test_menu3, 'water') == expected_result3:
    print('Test 3: Working')
else:
    print('Test 3: Failure')
    
test_menu4 = [['water'],
              ['bread', 'flour', 'butter', 'yeast'],
              ['pancakes', 'flour', 'milk', 'sugar']]
expected_result4 = False
if free_from(test_menu4, 'water') == expected_result4:
    print('Test 4: Working')
else:
    print('Test 4: Failure')