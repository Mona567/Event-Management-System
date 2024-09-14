from flask import Flask, render_template, request, redirect, url_for, flash, session
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)
app.secret_key = 'supersecretkey'

# Load users and roles from the password file
users = {}
roles = {}
with open('passwords.txt') as f:
    for line in f:
        username, password = line.strip().split(':')
        users[username] = generate_password_hash(password)
        roles[username] = 'admin' if username == 'admin' else 'user'

events = []

# Login route
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        if username in users and check_password_hash(users[username], password):
            session['username'] = username
            session['role'] = roles.get(username, 'user')
            return redirect(url_for('index'))
        flash('Invalid username or password.', 'error')
    return render_template('login.html')

# Logout route
@app.route('/logout')
def logout():
    session.pop('username', None)
    session.pop('role', None)
    return redirect(url_for('login'))

# Home page: List all events
@app.route('/')
def index():
    if 'username' not in session:
        return redirect(url_for('login'))
    return render_template('index.html', events=events, role=session.get('role'))

# Create event page
@app.route('/create', methods=['GET', 'POST'])
def create_event():
    if 'username' not in session or session.get('role') != 'admin':
        return redirect(url_for('index'))
    
    if request.method == 'POST':
        name = request.form['name']
        date = request.form['date']
        description = request.form['description']
        events.append({'name': name, 'date': date, 'description': description})
        flash('Event created successfully!', 'success')
        return redirect(url_for('index'))
    
    return render_template('create_event.html')

# View event page
@app.route('/event/<int:event_id>')
def view_event(event_id):
    if 'username' not in session:
        return redirect(url_for('login'))
    
    if event_id >= len(events):
        flash('Event not found.', 'error')
        return redirect(url_for('index'))
    
    event = events[event_id]
    return render_template('event.html', event=event, role=session.get('role'))

# Update an event (Admin only)
@app.route('/update/<int:event_id>', methods=['GET', 'POST'])
def update_event(event_id):
    if 'username' not in session or session.get('role') != 'admin':
        return redirect(url_for('index'))
    
    if event_id >= len(events):
        flash('Event not found.', 'error')
        return redirect(url_for('index'))

    if request.method == 'POST':
        name = request.form['name']
        date = request.form['date']
        description = request.form['description']
        events[event_id] = {'name': name, 'date': date, 'description': description}
        flash('Event updated successfully!', 'success')
        return redirect(url_for('index'))

    event = events[event_id]
    return render_template('update_event.html', event=event)

# Delete an event (Admin only)
@app.route('/delete/<int:event_id>')
def delete_event(event_id):
    if 'username' not in session or session.get('role') != 'admin':
        return redirect(url_for('index'))
    
    if event_id >= len(events):
        flash('Event not found.', 'error')
        return redirect(url_for('index'))
    
    events.pop(event_id)
    flash('Event deleted successfully!', 'success')
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
