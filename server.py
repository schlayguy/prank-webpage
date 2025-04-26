from flask import Flask, request, render_template
import sqlite3
from datetime import datetime

app = Flask(__name__)

# Initialize SQLite database
def init_db():
    with sqlite3.connect('responses.db') as conn:
        cursor = conn.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS responses (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                timestamp TEXT,
                username TEXT,
                response TEXT
            )
        ''')
        conn.commit()

# Call init_db on startup
init_db()

@app.route('/', methods=['GET'])
def index():
    username = request.args.get('user', 'unknown')
    return render_template('index.html', username=username)

@app.route('/submit', methods=['POST'])
def submit():
    username = request.form.get('username', 'unknown')
    response = request.form.get('response', '')
    timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    with sqlite3.connect('responses.db') as conn:
        cursor = conn.cursor()
        cursor.execute('INSERT INTO responses (timestamp, username, response) VALUES (?, ?, ?)',
                      (timestamp, username, response))
        conn.commit()
    # Log to responses.txt for backup
    with open('responses.txt', 'a') as f:
        f.write(f'[{timestamp}] User {username} accepted with jumbo mumbo: {response}\n')
    return 'Response recorded!'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
