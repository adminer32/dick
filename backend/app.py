import sqlite3
from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

DB_PATH = 'db/solitaire.db'

# Helper to get database connection

def get_db_connection():
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    return conn

@app.route('/entries', methods=['GET'])
def list_entries():
    conn = get_db_connection()
    cur = conn.execute('SELECT id, name, message, created_at FROM entries ORDER BY id ASC')
    rows = [dict(row) for row in cur.fetchall()]
    conn.close()
    return jsonify(rows)

@app.route('/entries', methods=['POST'])
def add_entry():
    data = request.get_json()
    name = data.get('name')
    message = data.get('message')
    if not name or not message:
        return jsonify({'error': 'name and message required'}), 400
    conn = get_db_connection()
    conn.execute(
        'INSERT INTO entries (name, message) VALUES (?, ?)',
        (name, message)
    )
    conn.commit()
    conn.close()
    return jsonify({'status': 'ok'})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
