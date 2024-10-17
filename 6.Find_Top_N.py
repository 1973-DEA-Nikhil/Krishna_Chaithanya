
#6
from collections import Counter
from typing import List

def top_n_frequent_words(words: List[str], n: int) -> List[str]:
    # Count the frequency of each word
    word_count = Counter(words)
    
    # Sort words by frequency (descending) and lexicographically (ascending)
    sorted_words = sorted(word_count.keys(), key=lambda word: (-word_count[word], word))
    
    # Return the top N words
    return sorted_words[:n]

# Example usage
words = ["apple", "banana", "apple", "orange", "banana", "apple"]
n = 2
output = top_n_frequent_words(words, n)
print(output)