import networkx as nx
import matplotlib.pyplot as plt
import network_characteristics as net_char

import simplejson as json
from networkx.readwrite import json_graph

import random

def erdo_network(num_nodes, edge_prob, directed, weighted):

    #Generate the network:
    erdo_network = nx.erdos_renyi_graph(num_nodes, edge_prob, directed=directed)

    #Give the nodes an initial position:
    node_position = position_nodes(erdo_network)

    #If the network is weighted, add edge weights:
    #if weighted:
    #    weight_edges(erdo_network)

    return erdo_network, node_position

def newman_network(num_nodes, edge_prob, num_neighbors, directed, weighted):

    #Generate Network:
    newman_network = nx.newman_watts_strogatz_graph(num_nodes, num_neighbors, edge_prob)

    #Give the nodes an initial position:
    node_position = position_nodes(newman_network)

    #If the network is weighted, add edge weights:
    #if weighted:
    #    weight_edges(erdo_network)

    return newman_network, node_position

def doro_network(generation, weighted):

    #Generate Network:
    doro_network = nx.dorogovtsev_goltsev_mendes_graph(generation)

    #Give the nodes an initial position:
    node_position = position_nodes(doro_network)

    #If the network is weighted, add edge weights:
    #if weighted:
    #    weight_edges(erdo_network)

    return doro_network, node_position

#----------------------------------------------------------------------------------

def triangular_lattice(m, n, periodic, directed, weighted):

    #Generate Network:
    triangular_lattice = nx.triangular_lattice_graph(m, n, periodic=periodic)

    #Give the nodes an initial position:
    node_position = position_nodes(triangular_lattice)

    #If the network is weighted, add edge weights:
    #if weighted:
    #    weight_edges(erdo_network)

    return triangular_lattice, node_position





def caveman_network(num_cliques, size):

    #Generate Network:
    caveman_network = nx.connected_caveman_graph(num_cliques, size)

    #Give the nodes an initial position:
    node_position = position_nodes(caveman_network)

    #If the network is weighted, add edge weights:
    #if weighted:
    #    weight_edges(erdo_network)

    return caveman_network, node_position




#-----------------------------------------------------------------------------------------------------------------------------
def position_nodes(network):

    initial_pos = {i: (random.random(), random.random()) for i in network.nodes()}
    position = nx.spring_layout(network, k=0.35, dim=2, weight='weight', pos=initial_pos, iterations=50, scale=2.0, center=None)

    return position

#-----------------------------------------------------------------------------------------------------------------------------
def plot_network(network, position):
    label_input = input('Draw Edge/Node Labels (True or False): ')
    
    #grid = net_char.bool_input(grid_input)
    labeled = net_char.bool_input(label_input)
    #export = get_bool(export_input)

    #if export:
    #    export_network(network, grid)

    if labeled:
        nx.draw(network, node_size=25, pos=position, node_color='grey', with_labels=True)
        labels = nx.get_edge_attributes(network,'weight')
        #nx.draw_networkx_edge_labels(graph, pos=position, edge_color='#99a3b2', edge_labels=labels, with_labels=False)
        plt.figure(1)
        plt.show()
    else:
        nx.draw(network, node_size=25, pos=position, edge_color='#99a3b2', node_color='grey', with_labels=False)
        plt.figure(1)
        plt.show()

#-----------------------------------------------------------------------------------------------------------------------------
def export_network(network, is_grid):

    print('''
        List of supported file types:

        1. gml
        2. json    
    ''')

    file_type = int(input('Choose File Type (integer): '))

    network_name_input = input('Enter Network Name For Export: ')

    #Export as gml:
    if file_type == 1:

        network_name = network_name_input + ".gml"

        if is_grid:
            #If the network is a grid, we have to relabel it:
            relabled_grid = nx.convert_node_labels_to_integers(network, first_label=0, ordering="default")
            nx.write_gml(relabled_grid, network_name)

        else:
            nx.write_gml(network, network_name)
        
    #Export as json:
    if file_type == 2:
        network_name = network_name_input + ".json"

        if is_grid:

            #If the network is a grid, we have to relabel it:
            relabled_grid = nx.convert_node_labels_to_integers(network, first_label=0, ordering="default")

            #Create a dictionary in a node-link format:
            node_data = json_graph.node_link_data(network, {'link': 'edges', 'source': 'from', 'target': 'to'})

            with open(network_name, 'w') as net_file:
                json.dump(node_data, net_file)

        else:

            #Create a dictionary in a node-link format:
            node_data = json_graph.node_link_data(network)

            with open(network_name, 'w') as net_file:
                json.dump(node_data, net_file)
