# def min_total_cost(x, y, premium):
#     # Sort the x and y coordinates to find the medians
#     sorted_x = sorted(x)
#     sorted_y = sorted(y)
    
#     # For odd number of coordinates, median is the middle element
#     # For even number, take any of the middle ones (we'll take the lower one)
#     cx = sorted_x[len(x) // 2]
#     cy = sorted_y[len(y) // 2]
    
#     # Calculate the total cost
#     total_cost = 0
#     for i in range(len(x)):
#         distance = abs(x[i] - cx) + abs(y[i] - cy)
#         total_cost += premium[i] * distance
    
#     return total_cost
def weighted_median(data, weights):
    # Sort data and weights based on data values
    sorted_data = [d for _, d in sorted(zip(data, data))]
    sorted_weights = [w for _, w in sorted(zip(data, weights))]
    
    # Calculate total weight
    total_weight = sum(sorted_weights)
    
    # Find the weighted median: the point where cumulative weight crosses half the total weight
    cumulative_weight = 0
    for i in range(len(sorted_data)):
        cumulative_weight += sorted_weights[i]
        if cumulative_weight >= total_weight / 2:
            return sorted_data[i]

def min_total_cost_weighted(x, y, premium):
    # Compute the weighted medians for x and y coordinates
    cx = weighted_median(x, premium)
    cy = weighted_median(y, premium)
    
    # Calculate the total cost
    total_cost = 0
    for i in range(len(x)):
        distance = abs(x[i] - cx) + abs(y[i] - cy)
        total_cost += premium[i] * distance
    
    return total_cost

# Example case
x = [2, 3, 5]
y = [1,1, 1]
premium = [1, 1, 1]
# Example case
# x = [5, 2, 3]
# y = [3, 4, 7]
# premium = [1, 1, 1]


result = min_total_cost_weighted(x, y, premium)
print("Minimum total cost:", result)


# result = min_total_cost(x, y, premium)
# print("Minimum total cost:", result)
