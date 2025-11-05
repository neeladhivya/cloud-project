import os
from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

# --- DATABASE CONFIGURATION ---
# 1. Get the DATABASE_URL from the environment variable you just set
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL')
# 2. Disable a feature we don't need
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# 3. Create the database connection object
db = SQLAlchemy(app)

# --- DATABASE MODEL ---
# This class defines the "guestbook" table in our database
class Guestbook(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    message = db.Column(db.String(500), nullable=False)

    def __repr__(self):
        return f'<Message {self.id}>'

# --- ROUTES ---
@app.route('/', methods=['GET', 'POST'])
def index():
    # If the user is submitting the form (POST)
    if request.method == 'POST':
        # Get data from the form
        name = request.form['name']
        message = request.form['message']
        
        # Create a new message object
        new_entry = Guestbook(name=name, message=message)
        
        # Add it to the database
        try:
            db.session.add(new_entry)
            db.session.commit()
            # Redirect back to the homepage
            return redirect(url_for('index'))
        except:
            return "There was an error adding your message."

    # If the user is just visiting the page (GET)
    else:
        # Get all messages from the database
        all_messages = Guestbook.query.order_by(Guestbook.id.desc()).all()
        
        # Render the HTML page and send it the messages
        return render_template('index.html', messages=all_messages)

# This is a one-time command to create your database tables
# We need to run this *once* after the app starts
with app.app_context():
    db.create_all()

if __name__ == '__main__':
    app.run()
