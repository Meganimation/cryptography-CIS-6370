from flask import Flask, request, jsonify
import sqlite3
import os

app = Flask(__name__)

# Database file path
DB_PATH = 'greeting.db'

def init_database():
    """Initialize the database and create the greeting table if it doesn't exist"""
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    
    # Create table if it doesn't exist
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS greeting (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            message TEXT NOT NULL,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    ''')
    
    # Check if there's already a greeting message
    cursor.execute('SELECT COUNT(*) FROM greeting')
    count = cursor.fetchone()[0]
    
    # If no greeting exists, insert the default one
    if count == 0:
        cursor.execute('INSERT INTO greeting (message) VALUES (?)', ('hello world!',))
    
    conn.commit()
    conn.close()

def get_current_greeting():
    """Get the current greeting message from the database"""
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    
    cursor.execute('SELECT message FROM greeting ORDER BY created_at DESC LIMIT 1')
    result = cursor.fetchone()
    
    conn.close()
    
    if result:
        return result[0]
    return 'hello world!'

def update_greeting(new_message):
    """Update the greeting message in the database"""
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    
    cursor.execute('INSERT INTO greeting (message) VALUES (?)', (new_message,))
    
    conn.commit()
    conn.close()

@app.route('/hello', methods=['GET'])
def get_hello():
    """GET endpoint to retrieve the current greeting message"""
    try:
        greeting_msg = get_current_greeting()
        return jsonify({'greetingMsg': greeting_msg}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/hello', methods=['POST'])
def post_hello():
    """POST endpoint to update the greeting message"""
    try:
        data = request.get_json()
        
        if not data or 'greetingMsg' not in data:
            return jsonify({'error': 'greetingMsg is required in request body'}), 400
        
        new_message = data['greetingMsg']
        
        if not isinstance(new_message, str) or not new_message.strip():
            return jsonify({'error': 'greetingMsg must be a non-empty string'}), 400
        
        update_greeting(new_message.strip())
        
        return jsonify({'message': 'Greeting updated successfully', 'greetingMsg': new_message.strip()}), 200
        
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/health', methods=['GET'])
def health_check():
    """Health check endpoint"""
    return jsonify({'status': 'healthy'}), 200

if __name__ == '__main__':
    # Initialize database on startup
    init_database()
    
    # Run the Flask app
    app.run(debug=True, host='0.0.0.0', port=5000)
