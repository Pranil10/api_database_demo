import sqlite3
import logging

logging.basicConfig(level=logging.INFO, format="%(asctime)s — %(levelname)s — %(message)s")

# connect() creates the database file if it doesn't exist yet
logging.info("Connecting to the database...")



conn = sqlite3.connect("school.db")
cursor = conn.cursor()   # The cursor is like a pen — you use it to write SQL

# --- Create a table ---
logging.info("Creating the 'students' table...")
cursor.execute("""
    CREATE TABLE IF NOT EXISTS students (
        id      INTEGER PRIMARY KEY AUTOINCREMENT,
        name    TEXT    NOT NULL,
        grade   TEXT    NOT NULL,
        score   REAL
    )
""")

# --- Insert a single row ---
logging.info("Inserting a student record...")
cursor.execute(
    "INSERT INTO students (name, grade, score) VALUES (?, ?, ?)",
    ("Alice", "A", 95.5)     # Always use ? placeholders — NEVER put values directly in the string
)

conn.commit()   # Save the changes permanently
logging.info("Record inserted and committed.")

# --- Read it back ---
cursor.execute("SELECT * FROM students")
rows = cursor.fetchall()

print("\n--- Students Table ---")
for row in rows:
    print(f"ID: {row[0]} | Name: {row[1]} | Grade: {row[2]} | Score: {row[3]}")

conn.close()
logging.info("Database connection closed.")