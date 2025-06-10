from flask import Flask, request, render_template, redirect, url_for, session
import sqlite3

app = Flask(__name__)
app.secret_key = 'your_secret_key_here'  # Needed for sessions

# Initialize SQLite DB
def init_db():
    conn = sqlite3.connect("users.db")
    c = conn.cursor()
    c.execute("CREATE TABLE IF NOT EXISTS users (username TEXT, password TEXT)")
    c.execute("DELETE FROM users")  # Reset for demo
    c.execute("INSERT INTO users VALUES ('admin', 'admin123')")
    conn.commit()
    conn.close()

@app.route('/', methods=['GET', 'POST'])
def login():
    msg = ''
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        
        # ❗ VULNERABLE SQL
        query = f"SELECT * FROM users WHERE username = '{username}' AND password = '{password}'"

        conn = sqlite3.connect("users.db")
        cursor = conn.cursor()
        cursor.execute(query)
        result = cursor.fetchone()
        conn.close()

        if result:
            session['username'] = username
            return redirect(url_for('welcome'))
        else:
            msg = "❌ Login failed. Try again."
    return render_template("login.html", message=msg)

@app.route('/welcome')
def welcome():
    if 'username' in session:
        return render_template("welcome.html", username=session['username'])
    else:
        return redirect(url_for('login'))

if __name__ == '__main__':
    init_db()
    app.run(host='0.0.0.0', port=5000, debug=True)

