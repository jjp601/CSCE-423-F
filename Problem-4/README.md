# CSCE 423 - Final Problem 4

Your first assignment as a Jet employee is to build an internal dashboard of various order statistics and how they change over time. The 3 most important values that should be calculated are the maximum price, average price and standard deviation.

To observe the evolution of these values in the given list of prices, for the given number n you should consider the following running sets of orders:

the nth order at the end;
the nth and (n - 1)th orders at the end;
the nth, (n - 1)th and (n - 2)th orders at the end;
...
n last orders, from the nth at the end to the most recent one.
For each of the running sets, calculate the required statistics and return them in arrays comprised of three elements.
When it's impossible to calculate the standard deviation, return -1 instead.

# Example

For orders = [4, 2, 5, 9, 2] and n = 5, the output should be

jetDashboard(orders, n) = [[4, 4,       -1], 
                           [4, 3,       1.41421], 
                           [5, 3.66667, 1.52753], 
                           [9, 5,       2.94392],
                           [9, 4.4,     2.88097]]
The values are calculated for the following running sets: [4], [4, 2], [4, 2, 5], [4, 2, 5, 9] and [4, 2, 5, 9, 2].

For orders = [4, 2, 5, 9, 2] and n = 3, the output should be

jetDashboard(orders, n) = [[5, 5,       -1], 
                           [9, 7,       2.82843],
                           [9, 5.333