import os
import sqlite3
from flask import Flask, render_template, request, g
import suggestions

app = Flask(__name__, static_url_path='/static')

# Database configuration
app.config['DATABASE'] = os.path.join(os.path.dirname(__file__), 'symptoms.db')


# Function to connect to the database
def connect_db():
    rv = sqlite3.connect(app.config['DATABASE'])
    rv.row_factory = sqlite3.Row
    return rv


# Function to get the database connection
def get_db():
    if not hasattr(g, 'sqlite_db'):
        g.sqlite_db = connect_db()
    return g.sqlite_db


# Function to initialize the database
def init_db():
    with app.app_context():
        db = get_db()

        # Clear existing records from the 'symptoms' table
        db.execute('DELETE FROM symptoms;')
        db.commit()

        # Drop and recreate the 'symptoms' table
        db.execute('DROP TABLE IF EXISTS symptoms;')
        db.execute("""
            CREATE TABLE IF NOT EXISTS symptoms (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                symptom TEXT NOT NULL
            )
        """)
        db.commit()

    print("Database initialized.")
    # To store all entries: create_db.init()


# Close the database connection when the request ends
@app.teardown_appcontext
def close_db(error):
    if hasattr(g, 'sqlite_db'):
        g.sqlite_db.close()


# Routes

# Define the route for the start page ('/')
@app.route('/')
def index():
    return render_template('index.html')


# Define the route for symptom analysis ('/analyze')
@app.route('/analyze', methods=['POST'])
def analyze():
    symptoms = request.form.get('symptoms')

    # Insert symptoms into the database
    db = get_db()
    db.execute('INSERT INTO symptoms (symptom) VALUES (?)', (symptoms,))
    db.commit()

    suggestions_set = suggestions.analyze_symptoms(symptoms)

    # Return a results page using an HTML template and provide the suggestions
    return render_template('results.html', symptoms=symptoms, suggestions=suggestions_set)


# Check if the script is executed directly and not imported as a module
if __name__ == '__main__':
    # Initialize the database
    init_db()

    # Start the application in debug mode
    app.run(debug=True)
