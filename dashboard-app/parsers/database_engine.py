import sqlite3
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

DB_PATH = BASE_DIR / "database" / "security.db"


# ---------------------------
# CONNECT
# ---------------------------

def connect_db():

    connection = sqlite3.connect(DB_PATH)

    return connection


# ---------------------------
# CREATE TABLES
# ---------------------------

def create_tables():

    connection = connect_db()

    cursor = connection.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS incidents (

        id INTEGER PRIMARY KEY AUTOINCREMENT,

        severity TEXT,

        source TEXT,

        description TEXT,

        status TEXT
    )
    """)

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS detections (

        id INTEGER PRIMARY KEY AUTOINCREMENT,

        detection_type TEXT,

        severity TEXT,

        details TEXT
    )
    """)

    connection.commit()

    connection.close()


# ---------------------------
# SAVE INCIDENT
# ---------------------------

def save_incident(
    severity,
    source,
    description,
    status
):

    connection = connect_db()

    cursor = connection.cursor()

    cursor.execute("""
    INSERT INTO incidents (
        severity,
        source,
        description,
        status
    )
    VALUES (?, ?, ?, ?)
    """, (
        severity,
        source,
        description,
        status
    ))

    connection.commit()

    connection.close()


# ---------------------------
# LOAD INCIDENTS
# ---------------------------

def load_incidents():

    connection = connect_db()

    cursor = connection.cursor()

    cursor.execute("""
    SELECT * FROM incidents
    """)

    rows = cursor.fetchall()

    connection.close()

    return rows


# ---------------------------
# SAVE DETECTION
# ---------------------------

def save_detection(
    detection_type,
    severity,
    details
):

    connection = connect_db()

    cursor = connection.cursor()

    cursor.execute("""
    INSERT INTO detections (
        detection_type,
        severity,
        details
    )
    VALUES (?, ?, ?)
    """, (
        detection_type,
        severity,
        details
    ))

    connection.commit()

    connection.close()

# ---------------------------
# LOAD DETECTIONS
# ---------------------------

def load_detections():

    connection = connect_db()

    cursor = connection.cursor()

    cursor.execute("""
    SELECT * FROM detections
    """)

    rows = cursor.fetchall()

    connection.close()

    return rows
