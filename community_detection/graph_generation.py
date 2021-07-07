import numpy as np
import networkx as nx

'''
input: time series data over WE as np array
ouput: graph that contains gridcells as nodes and an edge if correllation is sufficiently high
'''
threshold = 0.5

def build_graph(data): 
    t, lon, lat = data.shape[0], data.shape[1], data.shape[2]
    print(f"dimensions: longitude={lon}, latitude={lat}, timeseries={t}")
    graph = nx.Graph()
    
    # create nodes that consist of grid cell coordinates
    for i in range(lon):
        for j in range(lat):
            graph.add_node((i, j))
    add_edges(graph, data)
    return graph

'''
compute correlation coefficient between the two given time series
'''
def add_edges(graph, data): 
    for n1 in graph.nodes():
        t1 = data[:, n1[0], n1[1]]
        for n2 in graph.nodes():
            t2 = data[:, n2[0], n2[1]]
            corr = np.corrcoef(t1, t2)
            print(f"first timeseries={t1}, second timeseries={t2}, shape correlation coefficient{corr.shape}")
            if corr >= threshold: 
                graph.add_edge(n1, n2)