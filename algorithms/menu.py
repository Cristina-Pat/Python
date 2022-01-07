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