import random
import matplotlib.pyplot as plt

def initialize_network(num_nodes):
    # 创建一个包含所有节点的初始连接字典
    network = {node: set(range(num_nodes)) - {node} for node in range(num_nodes)}
    return network


def process_network(network, p):
    # 对每一对可能的节点执行处理步骤
    nodes = list(network.keys())
    removed_edge = False  # 用于跟踪是否移除了边

    for i in range(len(nodes)):
        for j in range(i + 1, len(nodes)):
            if random.random() < p:
                # 移除边
                # print(random.random())
                network[nodes[i]].discard(nodes[j])
                network[nodes[j]].discard(nodes[i])
                removed_edge = True
                # print(network)

    # 移除孤立节点
    isolated_nodes = [node for node, neighbors in network.items() if not neighbors]
    for node in isolated_nodes:
        del network[node]
    return removed_edge

def simulate_network(num_nodes, p):
    network = initialize_network(num_nodes)
    # nodes = list(network.keys())
    # processed = set()  # 用于跟踪已处理的节点对
    # removed_edge = True

    process_network(network, p)

    return network

def calculate_degree_distribution(network):
    degrees = [len(neighbors) for neighbors in network.values()]
    degree_counts = {degree: degrees.count(degree) for degree in set(degrees)}
    return degree_counts

# 指定节点数和概率
num_nodes = 10000
p = 0.5



final_network = simulate_network(num_nodes, p)
print("最终网络结构:")
print(final_network)

# 计算度分布
degree_distribution = calculate_degree_distribution(final_network)

# 绘制度分布图
degrees = list(degree_distribution.keys())
counts = list(degree_distribution.values())

plt.bar(degrees, counts)
plt.xlabel('degree')
plt.ylabel('number of nodes')
plt.title('degree distribution')
plt.show()