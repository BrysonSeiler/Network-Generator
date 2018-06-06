import network_characteristics as net_char

def main():

    print('''List of Tasks:
        1. Generate Network
    ''')
    
    task = int(input('Choose Task: '))

    if task == 1:
        network_type = net_char.choose_network()
        net_char.get_network(network_type)



if __name__ == '__main__':
    main()