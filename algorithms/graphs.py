nodes = ['Tom', 'Isa', 'Greg', 'Alex'] #undirected graph

edges_matrix =[ #adjacency matrix
    [False, True, False, True], #neighbours of node 0 (Tom): node 1 and 3
    [True, False, False, True], #neighbours of node 1 (Isa): node 0 and 3
    [False, False, False, False], #neighbours of node 2 (Greg): none
    [True, True, False, False] #neighbours of node 3 (Alex): node 0 and 1
]

edges_list = [  #lookup table of sequences
    [1, 3], #neighbours of node 0 - Tom
    [0, 3], #neighbours of node 1 - Isa
    [],     #neighbours of node 2 - Greg
    [0, 1]  #neighbours of node 3 - Alex
]

hash_table = { #store the undirected graph in dictionary, both the nodes and their neighbours
    'Tom': ['Isa', 'Alex'], 
    'Isa': ['Tom', 'Alex'],
    'Greg': [], 
    'Alex': ['Tom', 'Isa']
}

hash_table_digraph = { # keys - nodes, values - out-neighbours
    1: [2], #out-neighbours of 1: 2
    2: [1], #out-neighbours of 1: 1
    3: [], #out-neighbours of 3: none
    4:[1, 2] #out-neighbours of 4: 1 and 2
}