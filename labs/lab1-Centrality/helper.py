#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Lab 1 - Centrality
"""
from numbers import Number
from math import isclose
import matplotlib.pyplot as plt
import networkx as nx
import numpy as np

def dictsAlmostEqual(dict1, dict2, rel_tol=1e-8):
    """
    If dictionary value is a number, then check that the numbers are almost equal, otherwise check if values are exactly equal
    """
    if len(dict1) != len(dict2):
        return False
    for key, item in dict1.items():
        if isinstance(item, dict):
            if not dictsAlmostEqual(dict1[key], dict2[key], rel_tol=rel_tol):
                return False
        else:
            if isinstance(item, Number):
                if not isclose(dict1[key], dict2[key], rel_tol=rel_tol):
                    return False
            else:
                if not (dict1[key] == dict2[key]):
                    return False
    return True


def visualize(graph, values, node_size=100):
    '''
    :param graph:
    :param node_list: dictionary keyed by node
    :return:
    '''
    nodes = graph.nodes()
    colors = [values[node] for node in nodes]
    
    pos = nx.spring_layout(graph)
    nx.draw_networkx_edges(graph, pos, alpha=0.2)
    nc = nx.draw_networkx_nodes(graph, pos, nodelist=nodes, node_color=colors, 
                                node_size=node_size, cmap=plt.cm.jet)
    plt.colorbar(nc)
    plt.axis('off')
    
    plt.show()


def assign_random_values(graph, min_value=0, max_value=None, replace=False):
    
    if max_value is None:
        max_value = graph.number_of_nodes()
    
    values = np.random.choice(range(min_value, max_value), 
                                    size=graph.number_of_nodes(), replace=replace)
    
    node2values = {node: values[i] for i, node in enumerate(graph.nodes())}                     
    
    return node2values