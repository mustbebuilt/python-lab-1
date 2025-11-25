# Import the flask class and create an instance of it
from flask import Flask, render_template, jsonify
from config import db_config
import mysql.connector

app = Flask(__name__)

# Define a route and view function
@app.route('/')
def index():
    return render_template('index.html', name='Flask Demos')

@app.route('/about')
def about():
    return render_template('about.html', title='About Us', description='Template example with multiple strings passed to it.')

@app.route('/fruits')
def fruits():
    fruit_list  = ["apple", "banana", "cherry", "Apples"]
    return render_template('fruits.html', title='List Example', fruits = fruit_list)

@app.route('/profile')
def show_profile():
    user = {"name": "Alice", "age": 30}
    return render_template("profile.html", title='Dictionary Example', user=user)

@app.route('/db_data')
def db_data():
    # Establish database connection
    conn = mysql.connector.connect(**db_config)
    
    # Create a cursor that returns results as dictionaries
    cursor = conn.cursor(dictionary=True)
    
    # Execute SQL query
    cursor.execute("SELECT * FROM staff")
    
    # Fetch all rows from the query result
    data = cursor.fetchall()
    
    # Clean up resources
    cursor.close()
    conn.close()
    
    # Pass data to template
    return render_template('db_data.html', data=data)

@app.route('/api/staff')
def get_staff_json():
    conn = mysql.connector.connect(**db_config)
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM staff")
    rows = cursor.fetchall()
    cursor.close()
    conn.close()
    return jsonify(rows)

# Run the app in debug mode
if __name__ == '__main__':
    app.run(debug=True)