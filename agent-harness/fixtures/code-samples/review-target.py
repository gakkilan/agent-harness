# Sample Code for Review
# This file contains intentional issues for testing code review capabilities

import sqlite3
from flask import Flask, request, jsonify

app = Flask(__name__)

def get_user_data(user_id):
    """Get user data from database."""
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()
    
    # Security Issue: SQL Injection
    query = f"SELECT * FROM users WHERE id = {user_id}"
    cursor.execute(query)
    
    result = cursor.fetchone()
    conn.close()
    return result

def calculate_sum(numbers):
    """Calculate sum of numbers."""
    # Performance Issue: O(n²) algorithm
    total = 0
    for i in range(len(numbers)):
        for j in range(len(numbers)):
            if i == j:
                total += numbers[i]
    return total

def process_items(items):
    """Process list of items."""
    # Logic Error: Off-by-one
    for i in range(1, len(items)):
        print(items[i])
    
    # Error Handling: Missing try-catch
    with open('output.txt', 'w') as f:
        f.write(str(items))

@app.route('/api/users/<user_id>')
def get_user(user_id):
    # No input validation
    user = get_user_data(user_id)
    return jsonify({'user': user})

if __name__ == '__main__':
    app.run(debug=True)
