import sqlite3
import json

from pathlib import Path
from datetime import datetime

# ---------------------------
# BASE PATHS
# ---------------------------

from utils.paths import BASE_DIR

DATABASE_DIR = BASE_DIR / "database"

DATABASE_DIR.mkdir(
    parents=True,
    exist_ok=True
)

DATABASE_FILE = DATABASE_DIR / "security.db"

# ---------------------------
# CREATE DATABASE DIRECTORY
# ---------------------------

DATABASE_DIR.mkdir(
    parents=True,
    exist_ok=True
)

# ---------------------------
# CONNECT
# ---------------------------

def connect_db():

    connection = sqlite3.connect(
        DB_PATH,
        check_same_thread=False
    )

    return connection
    
# ---------------------------
# CREATE TABLES
# ---------------------------

def create_tables():

    connection = connect_db()

    cursor = connection.cursor()

    # ---------------------------
    # SECURITY EVENTS
    # ---------------------------

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS security_events (

        id INTEGER PRIMARY KEY AUTOINCREMENT,

        timestamp TEXT,

        event_type TEXT,

        severity TEXT,

        source TEXT,

        details TEXT,

        created_at TEXT
    )
    """)

    # ---------------------------
    # INCIDENTS
    # ---------------------------

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS incidents (

        id INTEGER PRIMARY KEY AUTOINCREMENT,

        severity TEXT,

        source TEXT,

        description TEXT,

        status TEXT,

        created_at TEXT
    )
    """)

    # ---------------------------
    # DETECTIONS
    # ---------------------------

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS detections (

        id INTEGER PRIMARY KEY AUTOINCREMENT,

        detection_type TEXT,

        severity TEXT,

        details TEXT,

        created_at TEXT
    )
    """)

    # ---------------------------
    # IOC MATCHES
    # ---------------------------

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS ioc_matches (

        id INTEGER PRIMARY KEY AUTOINCREMENT,

        indicator TEXT,

        source TEXT,

        severity TEXT,

        created_at TEXT
    )
    """)

    # ---------------------------
    # THREAT HUNTING
    # ---------------------------

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS hunting_queries (

        id INTEGER PRIMARY KEY AUTOINCREMENT,

        query TEXT,

        analyst TEXT,

        created_at TEXT
    )
    """)

    connection.commit()

    connection.close()


# ---------------------------
# SAVE SECURITY EVENT
# ---------------------------

def save_security_event(
    event_type,
    severity,
    source,
    raw_log
):

    connection = connect_db()

    cursor = connection.cursor()

    cursor.execute("""
    INSERT INTO security_events (

        timestamp,
        event_type,
        severity,
        source,
        details,
        created_at

    )
    VALUES (?, ?, ?, ?, ?, ?)
    """, (

        datetime.utcnow().isoformat(),
        event_type,
        severity,
        source,
        raw_log,
        datetime.utcnow().isoformat()

    ))

    connection.commit()

    connection.close()


# ---------------------------
# LOAD SECURITY EVENTS
# ---------------------------

def load_security_events():

    connection = connect_db()

    cursor = connection.cursor()

    cursor.execute("""
    SELECT * FROM security_events
    ORDER BY id DESC
    """)

    rows = cursor.fetchall()

    connection.close()

    return rows


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
        status,
        created_at

    )
    VALUES (?, ?, ?, ?, ?)
    """, (

        severity,
        source,
        description,
        status,
        datetime.utcnow().isoformat()

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
    ORDER BY id DESC
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
        details,
        created_at

    )
    VALUES (?, ?, ?, ?)
    """, (

        detection_type,
        severity,
        details,
        datetime.utcnow().isoformat()

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
    ORDER BY id DESC
    """)

    rows = cursor.fetchall()

    connection.close()

    return rows


# ---------------------------
# SAVE IOC MATCH
# ---------------------------

def save_ioc_match(
    indicator,
    source,
    severity
):

    connection = connect_db()

    cursor = connection.cursor()

    cursor.execute("""
    INSERT INTO ioc_matches (

        indicator,
        source,
        severity,
        created_at

    )
    VALUES (?, ?, ?, ?)
    """, (

        indicator,
        source,
        severity,
        datetime.utcnow().isoformat()

    ))

    connection.commit()

    connection.close()


# ---------------------------
# LOAD IOC MATCHES
# ---------------------------

def load_ioc_matches():

    connection = connect_db()

    cursor = connection.cursor()

    cursor.execute("""
    SELECT * FROM ioc_matches
    ORDER BY id DESC
    """)

    rows = cursor.fetchall()

    connection.close()

    return rows


# ---------------------------
# SAVE HUNT QUERY
# ---------------------------

def save_hunting_query(
    query,
    analyst="SOC Analyst"
):

    connection = connect_db()

    cursor = connection.cursor()

    cursor.execute("""
    INSERT INTO hunting_queries (

        query,
        analyst,
        created_at

    )
    VALUES (?, ?, ?)
    """, (

        query,
        analyst,
        datetime.utcnow().isoformat()

    ))

    connection.commit()

    connection.close()


# ---------------------------
# LOAD HUNT QUERIES
# ---------------------------

def load_hunting_queries():

    connection = connect_db()

    cursor = connection.cursor()

    cursor.execute("""
    SELECT * FROM hunting_queries
    ORDER BY id DESC
    """)

    rows = cursor.fetchall()

    connection.close()

    return rows
