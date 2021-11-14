strand=input("Enter your strand here: ")

def DNA_check(strand: str) -> bool:
    """Return wheter the strand is valid.
    Postconditions: is valid if and only if the strand coitans some of 
    A, C, G, T letters.
    """
    base = ['A', 'C', 'G', 'T']
    for letter in strand:
        if letter in base:
            print ('Strand valid.')
    print('Strand unvalid.')

DNA_check(strand)