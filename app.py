from flask import Flask, request, jsonify
from uuid import uuid4
from datetime import datetime
from utils import load_events, save_events, find_event, search_events
from reminder_thread import start_reminder_thread

app = Flask(__name__)
EVENTS_FILE = 'events.json'
events = load_events(EVENTS_FILE)


@app.route('/')
def home():
    return "Hello from Event Scheduler!"


@app.route('/events', methods=['POST'])
def create_event():
    data = request.json
    try:
        event = {
            "id": f"event{len(events) + 1}",
            "title": data['title'],
            "description": data.get('description', ""),
            "start_time": data['start_time'],
            "end_time": data['end_time'],
            "recurrence": data.get('recurrence')
        }
        events.append(event)
        save_events(events, EVENTS_FILE)
        return jsonify(event), 201
    except KeyError:
        return jsonify({"error": "Missing required fields"}), 400

@app.route('/events', methods=['GET'])
def list_events():
    sorted_events = sorted(events, key=lambda x: x['start_time'])
    return jsonify(sorted_events), 200

@app.route('/events/<event_id>', methods=['GET'])
def get_event(event_id):
    event = find_event(events, event_id)
    return jsonify(event if event else {"error": "Not found"}), 200 if event else 404

@app.route('/events/<event_id>', methods=['PUT'])
def update_event(event_id):
    data = request.json
    event = find_event(events, event_id)
    if not event:
        return jsonify({"error": "Not found"}), 404
    for key in ['title', 'description', 'start_time', 'end_time', 'recurrence']:
        if key in data:
            event[key] = data[key]
    save_events(events, EVENTS_FILE)
    return jsonify(event), 200

@app.route('/events/<event_id>', methods=['DELETE'])
def delete_event(event_id):
    global events
    events = [e for e in events if e['id'] != event_id]
    save_events(events, EVENTS_FILE)
    return jsonify({"message": "Deleted"}), 200

@app.route('/search', methods=['GET'])
def search():
    query = request.args.get("q", "")
    return jsonify(search_events(events, query)), 200

if __name__ == '__main__':
    start_reminder_thread(events)
    app.run(host="0.0.0.0", port=9000, debug=True)

