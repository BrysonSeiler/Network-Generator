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