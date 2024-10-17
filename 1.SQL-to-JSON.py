#1
from typing import List, Dict, Union

def transform_data(rows: List[Dict[str, Union[str, int]]]) -> Dict[int, Dict[str, Union[str, int]]]:
    transformed_data = {}
    for row in rows:
        user_id = row['user_id']
        transformed_data[user_id] = {
            "name": row["name"],
            "age": row["age"],
            "city": row["city"]
        }
    return transformed_data

# Example usage:
rows = [
    {"user_id": 1, "name": "Alice", "age": 25, "city": "New York"},
    {"user_id": 2, "name": "Bob", "age": 30, "city": "San Francisco"}
]

output = transform_data(rows)
print(output)


