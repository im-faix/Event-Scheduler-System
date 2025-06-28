import threading
import time
from datetime import datetime, timedelta

def check_reminders(events):
    now = datetime.now()
    upcoming = []
    for event in events:
        try:
            start_time = datetime.fromisoformat(event['start_time'])
            if now <= start_time <= now + timedelta(hours=1):
                upcoming.append(event)
        except Exception as e:
            continue
    return upcoming

def reminder_loop(events):
    while True:
        due = check_reminders(events)
        for event in due:
            print(f"🔔 Reminder: '{event['title']}' starts at {event['start_time']}")
        time.sleep(60)

def start_reminder_thread(events):
    thread = threading.Thread(target=reminder_loop, args=(events,), daemon=True)
    thread.start()
