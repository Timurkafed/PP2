import psycopg2
import csv

# Database connection parameters
conn = psycopg2.connect(
    host="localhost",
    database="postgres",
    user="postgres",
    password="Timur260607",
    port="2280"
)
conn.autocommit = True
cur = conn.cursor()

# Create table
cur.execute("""
    CREATE TABLE IF NOT EXISTS phonebook (
        id SERIAL PRIMARY KEY,
        first_name VARCHAR(50) NOT NULL,
        last_name VARCHAR(50),
        phone VARCHAR(20) UNIQUE NOT NULL
    )
""")
conn.commit()

def insert_from_csv(filename):
    """Insert data from CSV file"""
    try:
        with open(filename, 'r') as f:
            reader = csv.reader(f)
            next(reader)  # Skip header
            for row in reader:
                cur.execute(
                    """INSERT INTO phonebook (first_name, last_name, phone)
                    VALUES (%s, %s, %s) ON CONFLICT (phone) DO NOTHING""",
                    (row[0], row[1], row[2])
                )
        conn.commit()
        print("Data uploaded from CSV successfully!")
    except Exception as e:
        print(f"Error: {e}")

def insert_from_console():
    """Insert data from user input"""
    try:
        first_name = input("Enter first name: ")
        last_name = input("Enter last name (optional): ")
        phone = input("Enter phone number: ")
        
        cur.execute(
            """INSERT INTO phonebook (first_name, last_name, phone)
            VALUES (%s, %s, %s)""",
            (first_name, last_name, phone)
        )
        conn.commit()
        print("Data inserted successfully!")
    except Exception as e:
        print(f"Error: {e}")

def update_data():
    """Update existing records"""
    try:
        phone = input("Enter phone number of the entry to update: ")
        print("What do you want to update?")
        choice = input("1. First name\n2. Phone number\nEnter choice: ")
        
        if choice == '1':
            new_name = input("Enter new first name: ")
            cur.execute(
                "UPDATE phonebook SET first_name = %s WHERE phone = %s",
                (new_name, phone)
            )
        elif choice == '2':
            new_phone = input("Enter new phone number: ")
            cur.execute(
                "UPDATE phonebook SET phone = %s WHERE phone = %s",
                (new_phone, phone)
            )
        conn.commit()
        print("Update successful!")
    except Exception as e:
        print(f"Error: {e}")

def query_data():
    """Search records with filters"""
    try:
        search = input("Enter search term (leave empty for all): ")
        if not search:
            cur.execute("SELECT * FROM phonebook")
        else:
            search = f"%{search}%"
            cur.execute(
                """SELECT * FROM phonebook 
                WHERE first_name ILIKE %s OR 
                      last_name ILIKE %s OR 
                      phone ILIKE %s""",
                (search, search, search)
        )
        results = cur.fetchall()
        if not results:
            print("No records found")
            return
        for row in results:
            print(f"ID: {row[0]}, Name: {row[1]} {row[2]}, Phone: {row[3]}")
    except Exception as e:
        print(f"Error: {e}")

def delete_data():
    """Delete records"""
    try:
        choice = input("Delete by:\n1. First name\n2. Phone\nEnter choice: ")
        if choice == '1':
            name = input("Enter first name to delete: ")
            cur.execute("DELETE FROM phonebook WHERE first_name = %s", (name,))
        elif choice == '2':
            phone = input("Enter phone number to delete: ")
            cur.execute("DELETE FROM phonebook WHERE phone = %s", (phone,))
        conn.commit()
        print("Deletion successful!")
    except Exception as e:
        print(f"Error: {e}")

# User interface
while True:
    print("\nPhoneBook Management System")
    print("1. Insert from CSV")
    print("2. Insert from console")
    print("3. Update record")
    print("4. Search records")
    print("5. Delete record")
    print("6. Exit")
    
    choice = input("Enter your choice: ")
    
    if choice == '1':
        filename = input("Enter CSV file path: ")
        insert_from_csv(filename)
    elif choice == '2':
        insert_from_console()
    elif choice == '3':
        update_data()
    elif choice == '4':
        query_data()
    elif choice == '5':
        delete_data()
    elif choice == '6':
        break
    else:
        print("Invalid choice, try again!")

cur.close()
conn.close()