import sqlite3
import re

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

def import_responses():
    init_db()
    with open('responses.txt', 'r') as f:
        lines = f.readlines()
    with sqlite3.connect('responses.db') as conn:
        cursor = conn.cursor()
        for line in lines:
            match = re.match(r'\[(.*?)\] User (.*?) accepted with jumbo mumbo: (.*)', line.strip())
            if match:
                timestamp, username, response = match.groups()
                cursor.execute('INSERT INTO responses (timestamp, username, response) VALUES (?, ?, ?)',
                              (timestamp, username, response))
        conn.commit()
    print("Imported responses to responses.db")

if __name__ == '__main__':
    import_responses()
