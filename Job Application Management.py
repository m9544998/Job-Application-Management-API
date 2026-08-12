from flask import Flask, request, jsonify
import sqlite3

app = Flask(__name__)

# Create database
conn = sqlite3.connect("jobs.db")
conn.execute("""
CREATE TABLE IF NOT EXISTS applications(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    applicant_name TEXT,
    job_title TEXT,
    company_name TEXT,
    status TEXT
)
""")
conn.commit()
conn.close()


# POST - Add Application
@app.route("/applications", methods=["POST"])
def add_application():
    data = request.get_json()

    conn = sqlite3.connect("jobs.db")
    conn.execute("""
        INSERT INTO applications
        (applicant_name, job_title, company_name, status)
        VALUES (?, ?, ?, ?)
    """, (
        data["applicant_name"],
        data["job_title"],
        data["company_name"],
        data["status"]
    ))

    conn.commit()
    conn.close()

    return jsonify({"message": "Application Added Successfully"}), 201


# GET - All Applications
@app.route("/applications", methods=["GET"])
def get_applications():
    conn = sqlite3.connect("jobs.db")
    conn.row_factory = sqlite3.Row

    applications = conn.execute(
        "SELECT * FROM applications"
    ).fetchall()

    conn.close()

    return jsonify([dict(app) for app in applications])


# GET - Application By ID
@app.route("/applications/<int:id>", methods=["GET"])
def get_application(id):
    conn = sqlite3.connect("jobs.db")
    conn.row_factory = sqlite3.Row

    application = conn.execute(
        "SELECT * FROM applications WHERE id=?",
        (id,)
    ).fetchone()

    conn.close()

    if application is None:
        return jsonify({"message": "Application Not Found"}), 404

    return jsonify(dict(application))


# PUT - Update Application
@app.route("/applications/<int:id>", methods=["PUT"])
def update_application(id):
    data = request.get_json()

    conn = sqlite3.connect("jobs.db")

    conn.execute("""
        UPDATE applications
        SET applicant_name=?, job_title=?, company_name=?, status=?
        WHERE id=?
    """, (
        data["applicant_name"],
        data["job_title"],
        data["company_name"],
        data["status"],
        id
    ))

    conn.commit()
    conn.close()

    return jsonify({"message": "Application Updated Successfully"})


# DELETE - Delete Application
@app.route("/applications/<int:id>", methods=["DELETE"])
def delete_application(id):
    conn = sqlite3.connect("jobs.db")

    conn.execute(
        "DELETE FROM applications WHERE id=?",
        (id,)
    )

    conn.commit()
    conn.close()

    return jsonify({"message": "Application Deleted Successfully"})


if __name__ == "__main__":
    app.run(debug=True)