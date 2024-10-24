class UnionFind:
    def __init__(self, n):
        # Initialize parent and rank arrays
        self.parent = list(range(n))  # Each node is its own parent initially
        self.rank = [0] * n  # Rank is used to keep the tree flat
        self.network_strength = [i + 1 for i in range(n)]  # Node's signal strength is its 1-based index
    
    def find(self, u):
        # Find the root of the node u with path compression
        if self.parent[u] != u:
            self.parent[u] = self.find(self.parent[u])  # Path compression
        return self.parent[u]
    
    def union(self, u, v):
        # Union by rank: attach the shorter tree under the taller tree
        root_u = self.find(u)
        root_v = self.find(v)
        
        if root_u != root_v:
            # If the roots are different, we merge the two sets
            if self.rank[root_u] > self.rank[root_v]:
                self.parent[root_v] = root_u
                # Update the strength of the root to be the max of both roots
                self.network_strength[root_u] = max(self.network_strength[root_u], self.network_strength[root_v])
            elif self.rank[root_u] < self.rank[root_v]:
                self.parent[root_u] = root_v
                self.network_strength[root_v] = max(self.network_strength[root_u], self.network_strength[root_v])
            else:
                # If the ranks are the same, arbitrarily choose one as root
                self.parent[root_v] = root_u
                self.network_strength[root_u] = max(self.network_strength[root_u], self.network_strength[root_v])
                self.rank[root_u] += 1  # Increase the rank of the new root

    def get_total_strength(self):
        # Compute the sum of strengths of all distinct networks
        total_strength = 0
        seen_roots = set()  # To avoid counting the same network multiple times
        for i in range(len(self.parent)):
            root = self.find(i)  # Find the root of the current node
            if root not in seen_roots:  # If the root has not been counted
                total_strength += self.network_strength[root]
                seen_roots.add(root)
        return total_strength


# Input example based on the problem statement
n = 1  # Number of computers (nodes)
c_from = [1]  # Edges from these computers
c_to = [1]    # Edges to these computers

# Create the UnionFind structure for n nodes
uf = UnionFind(n)

# Process each connection and calculate the total strength after each connection
results = []
for u, v in zip(c_from, c_to):
    uf.union(u - 1, v - 1)  # Adjust for 0-based indexing in Python
    total_strength = uf.get_total_strength()
    results.append(total_strength)

print(results)

# from typing import List

# class DisjointSet:
#     def __init__(self, n: int):
#         self.parent = list(range(n))
#         self.rank = [0] * n
#         self.max_signal = list(range(n))

#     def find(self, x: int) -> int:
#         if self.parent[x] != x:
#             self.parent[x] = self.find(self.parent[x])
#         return self.parent[x]

#     def union(self, x: int, y: int):
#         px, py = self.find(x), self.find(y)
#         if px == py:
#             return
#         if self.rank[px] < self.rank[py]:
#             px, py = py, px
#         self.parent[py] = px
#         if self.rank[px] == self.rank[py]:
#             self.rank[px] += 1
#         self.max_signal[px] = max(self.max_signal[px], self.max_signal[py])

# def networkStrengths(c_nodes: int, c_edges: int, c_from: List[int], c_to: List[int]) -> List[int]:
#     ds = DisjointSet(c_nodes)
#     results = []

#     for i in range(c_edges):
#         # Connect computers
#         ds.union(c_from[i] - 1, c_to[i] - 1)

#         # Calculate sum of network strengths
#         network_strengths = set()
#         for j in range(c_nodes):
#             root = ds.find(j)
#             network_strengths.add(ds.max_signal[root])
        
#         results.append(sum(network_strengths))

#     return results

# # # Example usage
# # c_nodes = 1
# # c_edges = 1
# # c_from = [1]
# # c_to = [1]
# c_nodes = 5
# c_edges = 4
# c_from = [1, 2, 1, 4]
# c_to = [2, 3, 3, 5]

# print(networkStrengths(c_nodes, c_edges, c_from, c_to))