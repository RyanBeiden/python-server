from models.location import Location

import sqlite3
import json

def get_all_locations():
    with sqlite3.connect('./kennel.db') as conn:
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()

        db_cursor.execute("""
        SELECT
            l.id,
            l.name,
            l.address
        FROM location l
        """)
        
        locations = []
        dataset = db_cursor.fetchall()

        for row in dataset:
            location = Location(row['id'], row['name'], row['address'])

            locations.append(location.__dict__)

    return json.dumps(locations)

def get_single_location(id):
    with sqlite3.connect('./kennel.db') as conn:
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()

        db_cursor.execute("""
        SELECT
            l.id,
            l.name,
            l.address
        FROM location l
        WHERE l.id = ?
        """, (id, ))

        data = db_cursor.fetchone()

        location = Location(data['id'], data['name'], data['address'])

        return json.dumps(location.__dict__)

def create_location(location):
    pass

def delete_location(id):
    with sqlite3.connect('./kennel.db') as conn:
        db_cursor = conn.cursor()

        db_cursor.execute("""
        DELETE FROM location
        WHERE id = ?
        """, (id, ))

def update_location(id, new_location):
    with sqlite3.connect('./kennel.db') as conn:
        db_cursor = conn.cursor()

        db_cursor.execute("""
        UPDATE location
            SET
                name = ?,
                address = ?
        WHERE id = ?
        """, (new_location['name'], new_location['address'], id ))

        rows_affected = db_cursor.rowcount

    if rows_affected == 0:
        return False
    else:
        return True
