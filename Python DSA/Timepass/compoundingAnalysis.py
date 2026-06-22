def compound_interest(principal, rate, time, n=1):
    """
    Calculate compound interest.

    :param principal: Initial amount of money
    :param rate: Annual interest rate (in decimal, e.g., 5% = 0.05)
    :param time: Time in years
    :param n: Number of times interest is compounded per year (default is 1 for yearly compounding)
    :return: Final amount after interest
    """
    amount = principal * (1 + rate / n) ** (n * time)
    return amount

# Example usage:
p = 900_000  # Principal amount
r = 0.16  # Annual interest rate (5%)
t = 13    # Time in years
n = 1    # Compounded quarterly

single_principal = []
for year in range(1, t+1):
    single_principal.append(compound_interest(p, r, year, n))

print(single_principal)
p = 25000  # Principal amount

added_principal = []
for year in range(1, t+1):
    if year == 1:
        added_principal.append(compound_interest(p, r, year, n))
    else:
        added_principal.append(compound_interest(added_principal[-1] + 24000, r, 1, n))
print(added_principal)

# Plotting the results
import matplotlib.pyplot as plt

plt.plot(range(1, t+1), single_principal, label='Single Investment')
plt.plot(range(1, t+1), added_principal, label='Annual Investment')
plt.xlabel('Years')
plt.ylabel('Amount')
plt.title('Compound Interest Analysis')
plt.legend()
plt.show()