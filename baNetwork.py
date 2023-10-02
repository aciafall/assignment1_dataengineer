import random
import networkx as nx
import collections
import numpy as np
# 从一个叫做seq的list中随机选择m个不重复元素
def random_subset(seq,m):
  targets=set()
  while len(targets)<m:
    x=random.choice(seq)
    targets.add(x)
  return targets

# 为定义带权重的随机选择函数做准备
def weighted_choice_sub(weights):
  rnd = random.random() * sum(weights)
  for i, w in enumerate(weights):
    rnd -= w
    if rnd < 0:
      return i

# 带权重的随机选择函数, gamma为度k的指数，gamma=1即为BA网络，gmma=0为随机网络，gamma=-1为反BA网络
def weightedDegreeSelection(nodeOccurance,m,gamma):
  c = collections.Counter(nodeOccurance)
  w = np.array(list(c.values()))**float(gamma)
  wcs = [weighted_choice_sub(w) for i in range(m)]
  s = [c.keys()[j] for j in wcs]
  return s

# 反BA机制
def rBA(n, m):
  G=nx.empty_graph(m)
  targets=list(range(m))
  repeated_nodes=[]
  source=m
  while source < n:
    G.add_edges_from(zip([source],targets))
    repeated_nodes.extend(targets)
    repeated_nodes.extend([source])
    targets = weightedDegreeSelection(repeated_nodes,m,-1)
    source += 1
  return G

rBA(1000,4)