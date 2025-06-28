
# 🗓️ Event Scheduler API (Flask)

A simple and lightweight Python REST API for scheduling, updating, and managing events — built using Flask. This backend system allows you to create, retrieve, update, and delete events via Postman. Events are saved persistently to a JSON file.

---

## ✅ Features

- **Create Events** with title, description, start time, and end time
- **List All Events** sorted by start time (earliest first)
- **Update Events** by ID (title, time, description)
- **Delete Events** by ID
- **Persistence** via JSON file — events are saved between restarts
- **Search** events by keyword (in title or description)
- **Reminders** for events starting in the next 1 hour (checked every minute)
- **Unit Tests** using Pytest
- Optional support for **Recurring Events** (`daily`, `weekly`, `monthly`)

---

## 🚀 How to Run

### 1. Clone the Repository

```bash
git clone https://github.com/yourusername/event-scheduler-api.git
cd event-scheduler-api
```

### 2. Create Virtual Environment

```bash
python -m venv venv
```

### 3. Activate Virtual Environment

- **Windows**:
```bash
venv\Scripts\activate
```

- **Linux/macOS**:
```bash
source venv/bin/activate
```

### 4. Install Dependencies

```bash
pip install -r requirements.txt
```

### 5. Run the Application

```bash
python app.py
```

---

## 🧪 Running Tests

```bash
pytest
```

---

## 📬 API Endpoints (Use with Postman)

| Method | Endpoint               | Description               |
|--------|------------------------|---------------------------|
| POST   | `/events`              | Create new event          |
| GET    | `/events`              | Get all events (sorted)   |
| PUT    | `/events/<event_id>`   | Update an event by ID     |
| DELETE | `/events/<event_id>`   | Delete an event by ID     |
| GET    | `/search?q=keyword`    | Search events             |

### 🔁 Sample Event JSON

```json
{
  "title": "Team Meeting",
  "description": "Planning sprint",
  "start_time": "2025-07-01T10:00:00",
  "end_time": "2025-07-01T11:00:00"
}
```

---

## 📂 Postman Collection

A ready-to-use Postman collection is included.

> **Download it here:** [`event_scheduler_postman_collection.json`](./event_scheduler_postman_collection.json)

---

## 🧠 Project Structure

```
.
├── app.py                  # Main Flask app
├── utils.py                # File operations and search
├── reminder_thread.py      # Background reminder logic
├── test_app.py             # Pytest test cases
├── events.json             # Persistent data file
├── requirements.txt        # Dependencies
└── README.md               # Project overview
```

---

## 💡 Future Improvements

- Email notifications for reminders
- Full recurrence logic for daily/weekly events
- Replace JSON with SQLite or PostgreSQL

---

## 👨‍💻 Author

Mohammed Faizan

> [GitHub](https://github.com/im-faix) · [LinkedIn](https://linkedin.com/in/faizan9)


