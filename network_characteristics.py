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

def get_network_characteristics(network_type):

    if network_type == 1:
        
        print("-Erdős-Rényi Network (Binomial graph) chosen- \n")

        num_nodes = int(input('Number of nodes: '))
        edge_prob = float(input('Probability of Edge Creation (Value between 0 and 1): '))
        
        directed_input = input('Directed Network (True or False): ')
        directed = bool_input(directed_input)

        weighted_input = input('Weighted Network (True or False): ')
        weighted = bool_input(weighted_input)

        erdo_network = generate.erdo_network(num_nodes, edge_prob, directed, weighted)



def bool_input(user_input):

    while True:
        try:
            return {'true':True, 'false':False}[user_input.lower()]
        except KeyError:
            print("Please enter true or false")
        
        