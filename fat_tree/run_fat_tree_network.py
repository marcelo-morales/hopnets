import networkx as nx
import matplotlib.pyplot as plt
import random


'''
Let k be the number of ports that each switch contains. Switches with k number of ports in a Fat tree topology is called 
k-ary or k-port Fat tree network topology.
From the value of k, we’ll derive the number of core switches, aggregation switches, edge switches and the maximum number of 
servers that can be attached.
A set of (k/2) number of aggregation switches and (k/2) number of edge switches are combined together and that is known as a Pod.
'''

FatTree = nx.Graph()

def create_fat_tree(k):
  num_core_swithces = int((k/2)**2)
  num_pods = k

  agg_switch_list = []
  core_switch_list = []
  edge_switch_list = []
  server_list = []

  for core in range(num_core_swithces):
    FatTree.add_node(core)
    core_switch_list.append(core_name)

  #each pod consits of...
  num_agg_switches = int(k/2)
  num_edge_switches = int(k/2)

  aggregation_switch_count = 0
  edge_switch_count = 0

  num_servers = int((k**3)/4)

  for pod in range(num_pods):
    while aggregation_switch_count < num_agg_switches and edge_switch_count < num_edge_switches:
      FatTree.add_node(aggregation_switch_count)
      agg_switch_list.append(agg_switch_name)
      FatTree.add_node(edge_switch_count)
      edge_switch_list.append(edge_switch_name)

      aggregation_switch_count = aggregation_switch_count + 1
      edge_switch_count = edge_switch_count + 1


  for agg_switch in agg_switch_list:
    for i in range(num_edge_switches):
      random_core_switch = random.randint(0, len(core_switch_list))

      # restriction: core switch has max k edges coming out of it
      # also core switch cannot already be connected to the same node
      # if this is correct, create edge
      if (random_core_switch is not used):
        FatTree.add_edge(edge_switch, random_core_switch)
      # mark core switch as connected

      random_edge_switch = random.randint(0, len(edge_switch_list))
      if (random_edge_switch is not used):
        FatTree.add_edge(edge_switch, random_edge_switch)


  #step 4 from website

  #add servers
  for server in num_servers:
    # somehow label node that this is a server node
    # SERVER - COUNT[0, 1, 2, ...] , unique UUID
    FatTree.add_node(server)


  for edge_switch in edge_switch_list:
    for i in range(num_agg_switches):
    random_server = random.randint(0, len(server_list))
      

      if (random_server is not used):
        FatTree.add_edge(edge_switch, random_server)
      # mark core switch as connected

      random_agg_switch = random.randint(0, len(agg_switch_list))
      if (random_agg_switch is not used):
        FatTree.add_edge(edge_switch, random_agg_switch)

  





  # each aggregation switch within pod is connected to...
  num_core_switches = int(k/2)
  num_agg_switch_edges = int(k/2)

  # each edge switch within a pod is connected to ...
  num_servers = int(k/2)
  num_edge_agg_switches = int(k/2)

  max_num_servers = int((k**3)/4)





'''
Visual representation of Fat Tree Graph: https://www.researchgate.net/figure/Fat-Tree-structure-with-n-4-It-has-three-levels-of-switches_fig1_220429211

'''

FatTree = nx.Graph()

# opens a worksheet by its name/title
# worksht = spreadsht.worksheet("hopnet graph topology analysis", "Sheet1")

'''
spreadsheet formatted like


| Path Length | Number of Hops |
|             |                |
|             |

'''

# lowest level
#servers


# set k = 4, can manually check if works correctly


# parametrize, fat ree paper, kparameter k

#define as arrays based on value k
FatTree.add_nodes_from([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16])

# 2nd from bottom level
FatTree.add_nodes_from([17, 18, 18, 20, 21, 22, 23, 24])

# 3rd from bottom level
FatTree.add_nodes_from([25, 26, 27, 28, 29, 30, 31, 32])

# top level
FatTree.add_nodes_from([33, 34, 35, 36])

# add edges
# why so close together? A reader cannot see an edge between the nodes?
FatTree.add_edges_from([(1, 13), (2, 13), (13, 21), (13, 22),(3, 14), (4, 14), 
                        (14, 21), (14, 22),(21, 29), (21, 30), (22, 31), (22, 32), 
                        (23, 29), (23, 30), (23, 16), (23, 15), (15, 24), (15, 5), 
                        (15, 6), (16, 7), (16, 8), (16, 24), (24, 31), (24, 32), 
                        (32, 26), (26, 17), (26, 18), (26, 31), (18, 11), (18, 12), 
                        (17, 9), (17, 10), (17, 25), (25, 29) , (25, 30) , (32, 28), (28, 19), (19, 27), 
                        (27, 20), (20, 35), (20, 36), (19, 33), (19, 34)])

# I am trying to change color of node here but does successfully change
# FatTree.add_nodes_from([
#     (70, {"color" : "red"}),
#     (71, {"color" : "orange"}),
# ])

nx.draw(FatTree, with_labels=True, font_weight='bold')

FatTree.nodes.data()

shortest_path_list = []

print("this is shortest path length " + str(len(nx.shortest_path(FatTree, source=3, target=10))))
shortest_path_list.append(len(nx.shortest_path(FatTree, source=3, target=10)))

print("this is shortest path length " + str(len(nx.shortest_path(FatTree, source=3, target=9))))
shortest_path_list.append(len(nx.shortest_path(FatTree, source=3, target=9)))

print("this is shortest path length " + str(len(nx.shortest_path(FatTree, source=4, target=10))))
shortest_path_list.append(len(nx.shortest_path(FatTree, source=4, target=10)))

print("this is shortest path length " + str(len(nx.shortest_path(FatTree, source=4, target=9))))
shortest_path_list.append(len(nx.shortest_path(FatTree, source=4, target=9)))

print("this is shortest path length " + str(len(nx.shortest_path(FatTree, source=1, target=10))))
shortest_path_list.append(len(nx.shortest_path(FatTree, source=1, target=10)))

print("this is shortest path length " + str(len(nx.shortest_path(FatTree, source=1, target=9))))
shortest_path_list.append(len(nx.shortest_path(FatTree, source=1, target=9)))

print("this is shortest path length " + str(len(nx.shortest_path(FatTree, source=35, target=10))))
shortest_path_list.append(len(nx.shortest_path(FatTree, source=35, target=10)))

print("this is shortest path length " + str(len(nx.shortest_path(FatTree, source=35, target=9))))
shortest_path_list.append(len(nx.shortest_path(FatTree, source=35, target=9)))

print("this is shortest path length " + str(len(nx.shortest_path(FatTree, source=36, target=10))))
shortest_path_list.append(len(nx.shortest_path(FatTree, source=36, target=10)))

print("this is shortest path length " + str(len(nx.shortest_path(FatTree, source=36, target=9))))
shortest_path_list.append(len(nx.shortest_path(FatTree, source=36, target=9)))

print("this is shortest path length " + str(len(nx.shortest_path(FatTree, source=12, target=10))))
shortest_path_list.append(len(nx.shortest_path(FatTree, source=12, target=10)))

print("this is shortest path length " + str(len(nx.shortest_path(FatTree, source=12, target=9))))
shortest_path_list.append(len(nx.shortest_path(FatTree, source=12, target=9)))

print("this is shortest path length " + str(len(nx.shortest_path(FatTree, source=11, target=10))))
shortest_path_list.append(len(nx.shortest_path(FatTree, source=11, target=10)))

print("this is shortest path length " + str(len(nx.shortest_path(FatTree, source=11, target=9))))
shortest_path_list.append(len(nx.shortest_path(FatTree, source=11, target=9)))

print("this is shortest path length " + str(len(nx.shortest_path(FatTree, source=8, target=10))))
shortest_path_list.append(len(nx.shortest_path(FatTree, source=8, target=10)))

print("this is shortest path length " + str(len(nx.shortest_path(FatTree, source=8, target=9))))
shortest_path_list.append(len(nx.shortest_path(FatTree, source=8, target=9)))

print("this is shortest path length " + str(len(nx.shortest_path(FatTree, source=7, target=10))))
shortest_path_list.append(len(nx.shortest_path(FatTree, source=7, target=10)))

print("this is shortest path length " + str(len(nx.shortest_path(FatTree, source=7, target=9))))
shortest_path_list.append(len(nx.shortest_path(FatTree, source=7, target=9)))

avg = 0

for length in shortest_path_list:
  avg = avg + length

avg = avg / len(shortest_path_list)

print("this is final average " + str(avg))


# print("this is average path length " + str(nx.average_shortest_path_length(FatTree)))


if __name__ == "__main__":
    print("Hello, World!")
    