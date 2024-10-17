#2
from typing import List, Dict
from datetime import datetime

def process_logs(logs: List[str]) -> Dict[int, int]:
    active_periods = {}

    for log in logs:
        # Extract the timestamp, user_id, and action using string manipulation
        timestamp_str = log[1:20]  # The first 19 characters inside the square brackets
        user_id, action = log[22:].split(" ", 1)  # Extract user_id and action
        
        # Convert the timestamp to a datetime object
        timestamp = datetime.strptime(timestamp_str, "%Y-%m-%d %H:%M:%S")
        user_id = int(user_id)
        
        if action == "start":
            # Store the start time for the user
            active_periods[user_id] = [timestamp, None]
        elif action == "stop":
            # Calculate the duration between start and stop
            if user_id in active_periods and active_periods[user_id][1] is None:
                start_time = active_periods[user_id][0]
                duration = (timestamp - start_time).total_seconds()
                active_periods[user_id] = [start_time, duration]  # Store duration

    # Create final result mapping user_id to total active time
    user_durations = {user_id: duration for user_id, (_, duration) in active_periods.items() if duration is not None}

    return user_durations

# Example usage
logs = [
    "[2024-01-01 10:00:00] 1 start",
    "[2024-01-01 10:05:00] 1 stop",
    "[2024-01-01 10:00:00] 2 start",
    "[2024-01-01 10:10:00] 2 stop"
]

output = process_logs(logs)
print(output)