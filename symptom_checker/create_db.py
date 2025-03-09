import sqlite3

DATABASE = 'symptoms.db'

def init():
    print("Creating Database...")
    with sqlite3.connect(DATABASE) as connection:
        cursor = connection.cursor()
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS symptoms (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                symptom TEXT NOT NULL
            )
        """)
        connection.commit()
    print("Database created.")

# Call the init function when the script is run
if __name__ == '__main__':
    init()
