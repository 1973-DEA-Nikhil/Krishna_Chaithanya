#9
from typing import List, Dict, Union

def rename_fields(data: List[Dict[str, Union[str, int]]]) -> List[Dict[str, Union[str, int]]]:
    for record in data:
        # Rename the 'location' field to 'city'
        if 'location' in record:
            record['city'] = record.pop('location')
    return data

# Example usage
data = [
    {"name": "Alice", "age": 25, "location": "New York"},
    {"name": "Bob", "age": 30, "location": "San Francisco"}
]

renamed_data = rename_fields(data)
print(renamed_data)