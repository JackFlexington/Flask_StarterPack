# Filename: app.py
# Libraries
from flask import Flask, render_template, request, jsonify

# Initialization
app = Flask(__name__)

# Webpages
@app.route('/')
def home():
    return render_template('index.html', name = 'JackFlex', gender = 'Female')

@app.route('/employee/<id>')
def employee(id):
    return render_template('employee.html', id = id)

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/form-handler', methods=['POST'])
def handle_data():
    return jsonify(request.form)

# Execute program
if __name__ == '__main__':
    app.run(debug = True) 