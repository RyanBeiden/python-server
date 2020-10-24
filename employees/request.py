from models.employee import Employee
from models.location import Location
from models.animal import Animal

import sqlite3
import json

def get_all_employees():
    with sqlite3.connect('./kennel.db') as conn:
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()

        db_cursor.execute("""
        SELECT
            e.id,
            e.name,
            e.address,
            e.locationId,
            e.animalId,
            l.name location_name,
            l.address location_address,
            a.name animal_name,
            a.breed animal_breed,
            a.treatment animal_treatment,
            a.locationId animal_locationId,
            a.customerId animal_customerId
        FROM Employee e
        JOIN Location l
            ON l.id = e.locationId
        JOIN Animal a
            ON a.id = e.animalId
        """)

        employees = []
        dataset = db_cursor.fetchall()

        for row in dataset:
            employee = Employee(row['id'], row['name'], row['address'], row['locationId'], row['animalId'])
            location = Location(row['id'], row['location_name'], row['location_address'])
            animal = Animal(row['id'], row['animal_name'], row['animal_breed'], row['animal_treatment'], row['animal_locationId'], row['animal_customerId'])

            employee.location = location.__dict__
            employee.animal = animal.__dict__

            del employee.location['id']
            del employee.animal['id']

            employees.append(employee.__dict__)
    
    return json.dumps(employees)

def get_single_employee(id):
    with sqlite3.connect('./kennel.db') as conn:
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()

        db_cursor.execute("""
        SELECT
            e.id,
            e.name,
            e.address,
            e.locationId,
            e.animalId,
            l.name location_name,
            l.address location_address,
            a.name animal_name,
            a.breed animal_breed,
            a.treatment animal_treatment,
            a.locationId animal_locationId,
            a.customerId animal_customerId
        FROM Employee e
        JOIN Location l
            ON l.id = e.locationId
        JOIN Animal a
            ON a.id = e.animalId
        WHERE e.id = ?
        """, (id , ))

        data = db_cursor.fetchone()
        
        employee = Employee(data['id'], data['name'], data['address'], data['locationId'])
        location = Location(data['id'], data['location_name'], data['location_address'])
        animal = Animal(data['id'], data['animal_name'], data['animal_breed'], data['animal_treatment'], data['animal_locationId'], data['animal_customerId'])

        employee.location = location.__dict__
        employee.animal = animal.__dict__

        del employee.location['id']
        del employee.animal['id']

        return json.dumps(employee.__dict__)
        

def create_employee(new_employee):
    with sqlite3.connect('./kennel.db') as conn:
        db_cursor = conn.cursor()

        db_cursor.execute("""
        INSERT INTO Employee
            ( name, address, locationId, animalId )
        VALUES
            ( ?, ?, ?, ? );
        """, (new_employee['name'], new_employee['address'], new_employee['locationId'], new_employee['animalId']))

        id = db_cursor.lastrowid

        new_employee['id'] = id
    
    return json.dumps(new_employee)

def delete_employee(id):
    with sqlite3.connect('./kennel.db') as conn:
        db_cursor = conn.cursor()

        db_cursor.execute("""
        DELETE FROM employee
        WHERE id = ?
        """, (id, ))

def update_employee(id, new_employee):
    with sqlite3.connect('./kennel.db') as conn:
        db_cursor = conn.cursor()

        db_cursor.execute("""
        UPDATE employee
            SET
                name = ?,
                address = ?,
                locationId = ?
        WHERE id = ?
        """, (new_employee['name'], new_employee['address'], new_employee['locationId'], id ))

        rows_affected = db_cursor.rowcount

    if rows_affected == 0:
        return False
    else:
        return True

def get_employees_by_location(locationId):
    with sqlite3.connect('./kennel.db') as conn:
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()

        db_cursor.execute("""
        SELECT
            e.id,
            e.name,
            e.address,
            e.locationId
        FROM Employee e
        WHERE e.locationId = ?
        """, ( locationId, ))

        employees = []
        dataset = db_cursor.fetchall()

        for row in dataset:
            employee = Employee(row['id'], row['name'], row['address'], row['locationId'])
            employees.append(employee.__dict__)
    
    return json.dumps(employees)
