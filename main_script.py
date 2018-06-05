import network_generation as net_gen

def main():

    print('''List of Tasks:
        1. Generate Network
    ''')
    
    task = int(input('Choose Task: '))

    if task == 1:
        network_type = net_gen.choose_network()



if __name__ == '__main__':
    main()