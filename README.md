#  Job Application Management API

A simple REST API built with **Flask** and **SQLite** to manage job applications.

## Features

* Add Application
* View All Applications
* Get Application By ID
* Update Application
* Delete Application

## Technologies

* Python 3
* Flask
* SQLite3

## Project Structure

```text
job-application-api/
│
├── app.py
├── jobs.db
├── README.md
└── requirements.txt
```

## Installation

```bash
pip install flask
```

Run the project:

```bash
python app.py
```

Server:

```text
http://127.0.0.1:5000
```

## API Endpoints

| Method | Endpoint             |
| ------ | -------------------- |
| POST   | `/applications`      |
| GET    | `/applications`      |
| GET    | `/applications/<id>` |
| PUT    | `/applications/<id>` |
| DELETE | `/applications/<id>` |

## Sample JSON

```json
{
    "applicant_name": "Maheen",
    "job_title": "Python Developer",
    "company_name": "ABC Software",
    "status": "Applied"
}
```

## Database

```sql
CREATE TABLE applications(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    applicant_name TEXT,
    job_title TEXT,
    company_name TEXT,
    status TEXT
);
```

## Requirements

```text
Flask==3.1.0
```

# Authur:
Maheen Asad
