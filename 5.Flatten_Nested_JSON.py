
#5
from typing import Dict, Any

def flatten_json(nested_dict: Dict[str, Any], parent_key: str = '', sep: str = '.') -> Dict[str, Any]:
    flat_dict = {}
    for key, value in nested_dict.items():
        # Create a new key by concatenating parent and current key
        new_key = parent_key + sep + key if parent_key else key
        
        # If the value is a dictionary, recursively flatten it
        if isinstance(value, dict):
            flat_dict.update(flatten_json(value, new_key, sep=sep))
        else:
            flat_dict[new_key] = value
    return flat_dict

# Example usage
nested_dict = {
    "user": {
        "id": 1,
        "details": {
            "name": "Alice",
            "address": {
                "city": "New York",
                "zipcode": 10001
            }
        }
    }
}

output = flatten_json(nested_dict)
print(output)