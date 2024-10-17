
#7
from typing import List, Dict, Union

def merge_data(employees: List[Dict[str, Union[str, int]]], departments: List[Dict[str, str]]) -> List[Dict[str, Union[str, int]]]:
    # Create a mapping of department_id to department_name for quick lookup
    department_map = {dept['id']: dept['department_name'] for dept in departments}
    
    # Merge department_name into each employee dictionary
    for employee in employees:
        dept_id = employee['department_id']
        employee['department_name'] = department_map.get(dept_id)
    
    return employees

# Example usage
employees = [
    {"id": 1, "name": "Alice", "department_id": 2},
    {"id": 2, "name": "Bob", "department_id": 1}
]
departments = [
    {"id": 1, "department_name": "Engineering"},
    {"id": 2, "department_name": "Marketing"}
]

merged_data = merge_data(employees, departments)
print(merged_data)