import sqlite3
from flask import Flask, jsonify, request

app = Flask(__name__)

# Connect to the database
connection = sqlite3.connect('entries.db')

# Create the entries table if it doesn't exist
connection.execute('''CREATE TABLE IF NOT EXISTS entries
    (title TEXT, description TEXT, category TEXT)''')

@app.route('/entries', methods=['POST'])
def create_entry():
    # Get the data from the request body
    data = request.get_json()
    title = data.get('title')
    description = data.get('description')
    category = data.get('category')

    # Insert the data into the database
    connection.execute(f"INSERT INTO entries (title, description, category) VALUES ('{title}', '{description}', '{category}')")
    connection.commit()

    return jsonify({'message': 'entry created successfully'}), 201

@app.route('/entries', methods=['GET'])
def get_entries():
    # Retrieve all entries from the database
    cursor = connection.execute("SELECT * FROM entries")
    entries = cursor.fetchall()

    # Convert the entries to a list of dictionaries
    entries = [{'title': entry[0], 'description': entry[1], 'category': entry[2]} for entry in entries]

    return jsonify(entries)

if __name__ == '__main__':
    app.run(debug=True)
