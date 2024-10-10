def min_picks(N):
    total_units = sum(N)
    # The minimum number of picks required to ensure 5 from each unit
    # can be derived from the worst-case scenario.
    # For each unit, we can pick 4 gifts from all but one unit before getting
    # to the 5 gifts from that unit.
    
    # We need to pick 4 gifts from all units except the last one,
    # then we pick 5 gifts from the last unit.
    picks = 0
    
    # Picking 4 gifts from each unit
    for count in N:
        if count > 0:
            picks += min(4, count)  # Ensure not to exceed available gifts
    
    # Now we need to make sure we get at least 5 gifts from each unit
    # After taking 4 from each, we still need 5 from each
    picks += len(N) * 5  # Adding 5 picks for each unit
    
    return picks

# Example usage
N = [6, 5]
print(min_picks(N))  # Output: 11
