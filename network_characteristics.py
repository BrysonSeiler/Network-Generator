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
            5. n,m-Dimensional Grid
            6. Hexagonal
            7. n-Dimensional Hypercube 

        Communities:

            9. Connected Caveman   
    ''')

    network_type = int(input('Choose Network Type (integer): '))

    return network_type

def get_network(network_type):

    if network_type == 1:
        
        print("-Erdős-Rényi Network (Binomial graph) chosen- \n")

        is_grid = False

        #Get number of nodes and whether or not the network is directed/weighted:
        num_nodes, directed, weighted = get_network_characteristics(is_grid)

        draw_network, export = draw_export_info()

        #Erdős-Rényi Network's have edge creation that is probabalistic:
        edge_prob = float(input('Probability of Edge Creation (Value between 0 and 1): '))

        #Generate the network and give the nodes an initial position:
        erdo_network, node_position = generate.erdo_network(num_nodes, edge_prob, directed, weighted)

        if draw_network:
            generate.plot_network(erdo_network, node_position)
        
        if export:
            generate.export_network(erdo_network, is_grid)

    if network_type == 2:
        
        print("-Newman–Watts–Strogatz (Small World) Network Chosen- \n")

        is_grid = False

        #Get number of nodes and whether or not the network is directed/weighted:
        num_nodes, directed, weighted = get_network_characteristics(is_grid)

        draw_network, export = draw_export_info()

        num_neighbors = int(input('Number of neighbors (Integer): '))

        #Newman–Watts–Strogatz Network's have edge creation that is probabalistic:
        edge_prob = float(input('Probability of Edge Creation (Value between 0 and 1): '))

        #Generate the network and give the nodes an initial position:
        newman_network, node_position = generate.newman_network(num_nodes, edge_prob, num_neighbors, directed, weighted)

        if draw_network:
            generate.plot_network(newman_network, node_position)
        
        if export:
            generate.export_network(newman_network, is_grid)

    if network_type == 3:

        print("-Dorogovtsev-Goltsev-Mendes Network Chosen- \n")

        generation = int(input('Generation: '))

        draw_network, export = draw_export_info()

        doro_network = generate.doro_network(generation, weighted)

        if draw_network:
            generate.plot_network(doro_network, node_position)
        
        if export:
            generate.export_network(doro_network, is_grid)

    if network_type == 4:

        print("-Triangular Lattice Chosen- \n")

        is_grid = True

        #Get number of nodes and whether or not the network is directed/weighted:
        m, n, periodic, directed, weighted = get_network_characteristics(is_grid)

        draw_network, export = draw_export_info()

        #Generate the network and give the nodes an initial position:
        triangular_lattice, node_position = generate.triangular_lattice(m, n, periodic, directed, weighted)

        if draw_network:
            generate.plot_network(triangular_lattice, node_position)
        
        if export:
            generate.export_network(triangular_lattice, is_grid)

    if network_type == 5:

        print("-n,m-Dimensional Grid Chosen-")

        is_grid = True

        #Get number of nodes and whether or not the network is directed/weighted:
        m, n, periodic, directed, weighted = get_network_characteristics(is_grid)

        draw_network, export = draw_export_info()

        #Generate the network and give the nodes an initial position:
        grid, node_position = generate.grid_network(m, n, directed, weighted)

        if draw_network:
            generate.plot_network(grid, node_position)
        
        if export:
            generate.export_network(grid, is_grid)


    if network_type == 9:
        
        print("-Caveman Network Chosen- \n")

        num_cliques = int(input('Number of Cliques (Integer): '))

        #Get number of nodes and whether or not the network is directed/weighted:
        draw_network, export = draw_export_info()

        #Newman–Watts–Strogatz Network's have edge creation that is probabalistic:
        size = int(input('Size (Integer): '))

        #Generate the network and give the nodes an initial position:
        caveman_network, node_position = generate.caveman_network(num_cliques, size)

        if draw_network:
            generate.plot_network(caveman_network, node_position)
        
        if export:
            generate.export_network(caveman_network, is_grid)


def get_network_characteristics(is_grid):

    if is_grid:

        dimension = input('Enter network dimension separated by commas: ')
        m,n = map(int, dimension.split(','))

        periodic_input = input('Periodic Network (True or False): ')
        periodic = bool_input(periodic_input)

        #Ask if the network should be directed:
        directed_input = input('Directed Network (True or False): ')
        directed = bool_input(directed_input)

        #Ask if the network should be weighted:
        weighted_input = input('Weighted Network (True or False): ')
        weighted = bool_input(weighted_input)

        return m, n, periodic, directed, weighted


    else:

        #Ask for number of nodes:
        num_nodes = int(input('Number of nodes: '))

        #Ask if the network should be directed:
        directed_input = input('Directed Network (True or False): ')
        directed = bool_input(directed_input)

        #Ask if the network should be weighted:
        weighted_input = input('Weighted Network (True or False): ')
        weighted = bool_input(weighted_input)

        return num_nodes, directed, weighted

def draw_export_info():

    #Ask if the network should be drawn:
    draw_network_input = input('Draw Network? (True or False): ')
    draw_network = bool_input(draw_network_input)

    export_input = input('Export network? (True or False): ')
    export = bool_input(export_input)

    return draw_network, export

def bool_input(user_input):

    while True:
        try:
            return {'true':True, 'false':False}[user_input.lower()]
        except KeyError:
            print("Please enter true or false")
        