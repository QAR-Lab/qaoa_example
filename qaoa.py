# -------------
# Listing 1.1 |
# ------------- 
import pennylane as qml
from pennylane import numpy as np
import networkx as nx
from matplotlib import pyplot as plt
import random


# -------------
# Listing 1.2 |
# ------------- 
random.seed(42)
np.random.seed(42)
n = 6
G = nx.fast_gnp_random_graph(n, 0.5)
plt.figure(figsize=(5, 3))
pos = nx.spring_layout(G)
nx.draw(G, with_labels=True, node_size=700, pos=pos)
plt.savefig("example_graph.png")


# -------------
# Listing 1.3 |
# ------------- 
depth = 10
wires = range(n)

H_C, H_M = qml.qaoa.maxcut(G)
def U_M(beta):
    qml.qaoa.mixer_layer(beta, H_M/G.number_of_edges())
def U_C(gamma):
    qml.qaoa.cost_layer(gamma, H_C/G.number_of_edges())

# define a single qaoa layer
def qaoa_layer(gamma, beta):
    U_C(gamma)
    U_M(beta)

# define the qaoa circuit
def qaoa_circuit(params):
    # Initialize ground state of mixer Hamiltonian
    for wire in wires:
        qml.Hadamard(wires=wire)
    # Apply qaoa layers
    qml.layer(qaoa_layer, depth, params[0], params[1])


# -------------
# Listing 1.4 |
# ------------- 
dev = qml.device("default.qubit", wires=wires)

@qml.qnode(dev)
def cost_fun(params):
    qaoa_circuit(params)
    return qml.expval(H_C)


# -------------
# Listing 1.5 |
# ------------- 
optimizer = qml.AdamOptimizer()
steps = 1000
T = 7.5
beta = [- (1 - i/depth)* T/depth for i in range(depth)]
gamma = [(i/depth)*T/depth for i in range(depth)]
params = np.array([beta, gamma], requires_grad=True)
cost_list = []
initial = True

# start optimization
for step in range(steps):
    params, cost = optimizer.step_and_cost(cost_fun, params)
    cost_list.append(cost)
    if initial:
        print(f"Initial cost: {cost}")
        initial = False
    print(f"Cost at step {step}: {cost}", end="\r")
plt.figure(figsize=(7, 4))
plt.plot(cost_list)
plt.ylabel("Cost")
plt.xlabel("Iteration")
plt.savefig("cost_minimization.png")

# -------------
# Listing 1.6 |
# ------------- 
@qml.qnode(dev)
def probability_circuit(gamma, beta):
    qaoa_circuit([gamma, beta])
    return qml.probs(wires=wires)

probs = probability_circuit(params[0], params[1])
plt.figure(figsize=(7, 4))
plt.style.use('seaborn-v0_8')
plt.bar(range(2 ** len(wires)), probs)
plt.ylabel("Probability")
plt.xlabel("Bitstrings")
plt.savefig("measurement_probabilities.png")