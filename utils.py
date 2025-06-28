import json
import os

def load_events(file_path):
    if not os.path.exists(file_path):
        return []
    with open(file_path, 'r') as f:
        try:
            return json.load(f)
        except json.JSONDecodeError:
            return []

def save_events(events, file_path):
    with open(file_path, 'w') as f:
        json.dump(events, f, indent=2)

def find_event(events, event_id):
    for event in events:
        if event['id'] == event_id:
            return event
    return None

def search_events(events, keyword):
    return [e for e in events if keyword.lower() in e['title'].lower() or keyword.lower() in e['description'].lower()]
