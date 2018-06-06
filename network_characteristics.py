import network_generation as generate


def choose_network():

    print('''
        ---Generate Network---

        List of supported network types:

        Classic Networks:

            1. Erdős-Rényi
            2. Newman–Watts–Strogatz (Small World)
            3. Dorogovtsev-Goltsev-Mendes

        Lattices:

            4. Triangular
            5. Hexagonal
            6. n-Dimensional Grid
            7. n,m-Dimensional Grid
            8. n-Dimensional Hypercube    
    ''')

    network_type = int(input('Choose Network Type (integer): '))

    return network_type

def get_network(network_type):

    if network_type == 1:
        
        print("-Erdős-Rényi Network (Binomial graph) chosen- \n")

        #Get number of nodes and whether or not the network is directed/weighted:
        num_nodes, directed, weighted, draw_network, is_grid, export = get_network_characteristics()

        #Erdős-Rényi Network's have edge creation that is probabalistic:
        edge_prob = float(input('Probability of Edge Creation (Value between 0 and 1): '))

        #Generate the network and give the nodes an initial position:
        erdo_network, node_position = generate.erdo_network(num_nodes, edge_prob, directed, weighted)

        if draw_network:
            generate.plot_network(erdo_network, node_position)
        
        if export:
            generate.export_network(erdo_network, is_grid)

def get_network_characteristics():

    #Ask for number of nodes:
    num_nodes = int(input('Number of nodes: '))

    #Ask if the network should be directed:
    directed_input = input('Directed Network (True or False): ')
    directed = bool_input(directed_input)

    #Ask if the network should be weighted:
    weighted_input = input('Weighted Network (True or False): ')
    weighted = bool_input(weighted_input)

    #Ask if the network should be drawn:
    draw_network_input = input('Draw Network? (True or False): ')
    draw_network = bool_input(draw_network_input)

    export_input = input('Export network? (True or False): ')
    export = bool_input(export_input)

    grid_input = input('Is this a network a grid? (True or False): ')
    is_grid = bool_input(grid_input)

    return num_nodes, directed, weighted, draw_network, is_grid, export

def bool_input(user_input):

    while True:
        try:
            return {'true':True, 'false':False}[user_input.lower()]
        except KeyError:
            print("Please enter true or false")
        
        