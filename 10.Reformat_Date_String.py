#10
from typing import List

def reformat_dates(dates: List[str]) -> List[str]:
    reformatted = []
    for date in dates:
        day, month, year = date.split('-')
        reformatted.append(f"{year}-{month}-{day}")
    return reformatted

# Example usage
dates = ["31-12-2024", "01-01-2024"]
reformatted_dates = reformat_dates(dates)
print(reformatted_dates)