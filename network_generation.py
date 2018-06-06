import networkx as nx
import matplotlib.pyplot as plt
import network_characteristics as net_char

import random

def erdo_network(num_nodes, edge_prob, directed, weighted):

    #Generate the network:
    erdo_network = nx.erdos_renyi_graph(num_nodes, edge_prob, directed=directed)

    #If the network is weighted, add edge weights:
    if weighted:
        weight_edges(erdo_network)

    #Give the nodes an initial position:
    node_position = position_nodes(erdo_network)

    #Ask if the network should be drawn:
    draw_network_input = input('Draw Network? (True or False): ')
    draw_network = net_char.bool_input(draw_network_input)

    if draw_network:
        plot_network(erdo_network, node_position)

    return erdo_network


#-----------------------------------------------------------------------------------------------------------------------------
def position_nodes(network):
    initial_pos = {i: (random.random(), random.random()) for i in network.nodes()}
    position = nx.spring_layout(network, k=0.35, dim=2, weight='weight', pos=initial_pos, iterations=50, scale=2.0, center=None)
    #position = graphviz_layout(graph, prog='neato')
    
    #adj_matrix = nx.adjacency_matrix(graph, weight='weight')
    #force_class = force.ForceAtlas2(graph=adj_matrix, iterations=100)
    #position = force_class.run_algo()
    
    return position


#-----------------------------------------------------------------------------------------------------------------------------
def plot_network(network, position):
    label_input = input('Draw Edge/Node Labels (True or False): ')
    #export_input = input('Export network as gml? (True or False): ')
    #grid_input = input('Is this a grid? (True or False): ')

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