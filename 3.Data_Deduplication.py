#3
from typing import List, Dict

def deduplicate(records: List[Dict[str, str]]) -> List[Dict[str, str]]:
    seen_emails = set()  # To track unique emails
    unique_records = []
    
    for record in records:
        email = record['email']
        if email not in seen_emails:
            seen_emails.add(email)  # Mark email as seen
            unique_records.append(record)  # Keep the first occurrence
    
    return unique_records

# Example usage
records = [
    {"id": "1", "name": "Alice", "email": "alice@example.com"},
    {"id": "2", "name": "Bob", "email": "bob@example.com"},
    {"id": "3", "name": "Alice", "email": "alice@example.com"}  # Duplicate email
]

output = deduplicate(records)
print(output)
