#4
from typing import List

def sliding_window_sum(transactions: List[int], k: int) -> List[int]:
    window_sums = []
    # Iterate over the list and calculate sum for each sliding window of size k
    for i in range(len(transactions) - k + 1):
        # Sum the current window of size k
        window_sum = sum(transactions[i:i+k])
        window_sums.append(window_sum)
    
    return window_sums

# Example usage
transactions = [10, 20, 30, 40, 50]
k = 3
output = sliding_window_sum(transactions, k)
print(output)