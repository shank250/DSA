import java.util.*;

class UnionFind {
    private int[] parent;
    private int[] rank;
    private int[] maxStrength;

    public UnionFind(int n) {
        parent = new int[n];
        rank = new int[n];
        maxStrength = new int[n];

        // Initialize each node as its own parent and its own max signal strength
        for (int i = 0; i < n; i++) {
            parent[i] = i;
            maxStrength[i] = i + 1; // node strength equals node number (1-indexed)
        }
    }

    // Find function with path compression
    public int find(int u) {
        if (parent[u] != u) {
            parent[u] = find(parent[u]);
        }
        return parent[u];
    }

    // Union function with union by rank
    public void union(int u, int v) {
        int rootU = find(u);
        int rootV = find(v);

        if (rootU != rootV) {
            // Union by rank
            if (rank[rootU] > rank[rootV]) {
                parent[rootV] = rootU;
                maxStrength[rootU] = Math.max(maxStrength[rootU], maxStrength[rootV]);
            } else if (rank[rootU] < rank[rootV]) {
                parent[rootU] = rootV;
                maxStrength[rootV] = Math.max(maxStrength[rootU], maxStrength[rootV]);
            } else {
                parent[rootV] = rootU;
                rank[rootU]++;
                maxStrength[rootU] = Math.max(maxStrength[rootU], maxStrength[rootV]);
            }
        }
    }

    // Get the maximum signal strength of a component
    public int getMaxStrength(int u) {
        return maxStrength[find(u)];
    }
}

public class NetworkStrength {
    public static List<Integer> calculateStrengthSum(int c_nodes, int[] c_from, int[] c_to) {
        UnionFind uf = new UnionFind(c_nodes);
        List<Integer> totalSum = new ArrayList<>();

        // Initially, each node is its own network, and we sum their strengths
        int currentSum = 0;
        for (int i = 1; i <= c_nodes; i++) {
            currentSum += i;  // Sum of initial strengths
        }
        totalSum.add(currentSum);

        // Process each connection
        for (int i = 0; i < c_from.length; i++) {
            int u = c_from[i] - 1;  // Convert to 0-indexed
            int v = c_to[i] - 1;    // Convert to 0-indexed

            // Get the maximum strength before union
            int maxU = uf.getMaxStrength(u);
            int maxV = uf.getMaxStrength(v);

            // If they're not already connected
            if (uf.find(u) != uf.find(v)) {
                // Subtract their current max strengths from the sum
                currentSum -= (maxU + maxV);

                // Union the two sets
                uf.union(u, v);

                // Add the new max strength of the merged set
                int newMax = uf.getMaxStrength(u);
                currentSum += newMax;
            }

            // Store the current sum after this connection
            totalSum.add(currentSum);
        }

        return totalSum;
    }

    public static void main(String[] args) {
        int c_nodes = 5;
        int c_edges = 4;
        int[] c_from = {1, 2, 1, 4};
        int[] c_to = {2, 3, 3, 5};

        // Calculate the sum of strengths after each connection
        List<Integer> result = calculateStrengthSum(c_nodes, c_from, c_to);

        // Print results
        for (int i = 0; i < result.size(); i++) {
            System.out.println("After " + i + " second(s), sum of strengths: " + result.get(i));
        }
    }
}