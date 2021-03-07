
## Configure Flask
```bash
# Install virtual environment
python3 -m pip install virtualenv

# Create directory
mkdir flask-tutorial
cd flask-tutorial

# Create virtual environment
virtualenv .
source bin/activate

# In (virtual enviornment)
# Install Flask
python3 -m pip install Flask
```

### Some items to point out
```python
# GET    - ideal for retrieving data
# POST   - ideal for submitting data, resulting in modification of state
# PUT    - replacing server's target resource with request resource
# DELETE - deleting a server's resource
# Note: PUT and DELETE are typically handled using specialized code in the back-end side... But worth mentioning nonetheless.
```

### Baseline code with added "route"
```python
# Filename: app.py
# Libraries
from flask import Flask  

# Initialization
app = Flask(__name__)

# Webpages
@app.route('/', methods=['GET', 'POST', 'PUT']) # decorator
def home():
    return 'Hello World!'

# Execute program
if __name__ == '__main__':
    app.run(debug = True) 
```

### Replace "home" function with following code block
Below is an example of how to return straight HTML to the browser.
```python
def home():
    # Returning HTML
    return '<html>\
                <body>\
                    <h3><u>Hello YOURNAME!</u></h3>\
                </body>\
            </html>'
```
Additionally, you can see the HTML within the web page pressing F12, while in the browser, to open the console.
Is this method practical for real-world scenarios... No not really. Lets start working with templates now.

### Adding templates
First, add a "templates" folder to the projects main directory. Then, add file "index.html" that resides within.
```html
<!-- Filename: index.html -->
<html>
<body>
    <h3><u>Hello YOURNAME!</u></h3>
    <p>I'm a rendered webpage from the templates folder.</p>
</body>
</html>
```
Now modify the "app.py" file previously made.
```python
# Filename: app.py
# Libraries
from flask import Flask, render_template 

# Initialization
app = Flask(__name__)

# Webpages
@app.route('/')
def home():
    return render_template('index.html')

# Execute program
if __name__ == '__main__':
    app.run(debug = True) 
```
Something thats really cool about the "render_template" functionality is that you can pass variables to the HTML template. Lets take a look below.

### Dynamic data for templates
Replace below function within the "app.py" file
```python
def home():
    return render_template('index.html', name = 'YOURNAME')
```
Then within the "templates/index.html" file, make the below change.
```HTML
<h3><u>Hello {{name}}</u></h3>
```

### Conditionals
Not only can you pass variables, but you can perform conditional operations by using variables passed into template.
Make the following changes in the next two code blocks.
```python
# app.py
def home():
    return render_template('index.html', name = 'YOURNAME', gender = 'Female')
```
```HTML
<!-- index.html -->
<body>
    {% if gender == 'Female' %}
      <h3><u>Hello Miss {{name}}!</u></h3>
    {% else %}
      <h3><u>Hello Mr. {{name}}!</u></h3>
    {% endif %}
    <p>I'm a rendered webpage from the templates folder.</p>
</body>
```
Some typical mechanisms provided by the jinja template engine are as follows:
* {% ... %} for code statements
* {{ ... }} for printing an expression to the template
* {# ... #} for comments not included in the template output
* \# ... ## for line statements

Note: See [jinja delimiters](https://jinja.palletsprojects.com/en/2.11.x/templates/) for more information.

### Static Assets
Note: CSS, JavaScript, images, gifs, etc... all fall within this category.

First create a new directory called "static" within the projects main directory.

#### Adding CSS styling
Add the following CSS file within the "static" directory.
```css
/* Filename: index.css */
body {
    background: lightblue;
}
h3 {
    color: purple;
}
```
Now lets modify our "index.html" template to inject the previously created CSS file.
```html
<!-- Filename: index.html -->
<html>
    <head>
        <!-- Inject CSS here-->
        <link rel='stylesheet' href='/static/index.css'>
    </head>
    <body>
        {% if gender == 'Female' %}
          <h3><u>Hello Miss {{name}}!</u></h3>
        {% else %}
          <h3><u>Hello Mr. {{name}}!</u></h3>
        {% endif %}
        <p>I'm a rendered webpage from the templates folder.</p>
    </body>
</html>
```
#### Adding JavaScript logic
```js
// Filename: index.js
'use strict'; // Ensures clean code
console.log('Greetings,');
console.log('I am so glad you made your way here.');
```
See [JavaScript Strict mode](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Strict_mode) for more details on this.

Append invokation of that previously created JavaScript file to the templates/index.html \<HEADER\> element.
```html
<!-- Filename: index.html -->
    <head>
        <!-- Inject CSS here-->
        <link rel='stylesheet' href='/static/index.css'>
        <!-- Inject JavaScript here-->
        <script src='/static/index.js'></script>
    </head>
```
If you've been successful up until this point, now is a good time to take a break.
### Dynamic Routes
Lets add another webpage to this web application. 
Ensure your "app.py" looks similar to the below code block.
```python
# Filename: app.py
# Libraries
from flask import Flask, render_template 

# Initialization
app = Flask(__name__)

# Webpages
@app.route('/')
def home():
    return render_template('index.html', name = 'YOURNAME', gender = 'Female')

@app.route('/employee/<id>')
def employee(id):
    return render_template('employee.html', id = id)

# Execute program
if __name__ == '__main__':
    app.run(debug = True) 
```
Additionally add the two following pages.
HTML employee webpage
```html
<!-- Filename: employee.html -->
<html>
    <head>
        <link rel='stylesheet' href='/static/employee.css'>
    </head>
    <body>
        <h3><u>Hello Employee # {{id}}!</u></h3>
    </body>
</html>
```
CSS employee page
```css
/* Filename: employee.css */
body {
    background: green;
}
h3 {
    color: red;
}
```
Now when you key the following into the browser's URL, you'll land on the new page.
URL = 127.0.0.1:5000/employee/1234
Experiment with different numbers.

### Add user form
Add the following files
HTML
```html
<!-- Filename: contact.html -->
<html>
    <body>
        <form action="/form-handler" method="POST">
            <div>
                Name: <input type="text" name="name"><br>
            </div>
            <div>
                Gender: <input type="text" name="gender"><br>
            </div>
            <input type="submit" value="Submit">
          </form>
    </body>
</html>
```
CSS
```css
/* Filename: contact.css */
body {
    background: rgb(69, 166, 196);
}
h3 {
    color: goldenrod;
}

form {
    margin: 2%;
}

div {
    margin: 2% 0;
}
```
Append route / function for rendering the contact form within "app.py"
```py
@app.route('/contact')
def contact():
    return render_template('contact.html')
```
Now when you key the following into the browser's URL, you'll land on the new page.
http://127.0.0.1:5000/contact

Only issue now, is that when you hit submit... You hit the dreaded "Not Found" web page. We still need to define an end-point for the form submission.

### Define the end-point for our form
Add to the "app.py" file.
```py
@app.route('/form-handler', methods=['POST'])
def handle_data():
    return "Request received successfully!"
```
Now go back to this page and hit "Submit". You should see "Request received successfully!". You may wondering, is that all? Well, the answer is no. We still need to write code to unpack the "POST" request data, process it, then return the appropriate message to the user.

In order to unpack the POST request, we'll need to rely on the "request" library, go back to "app.py" and include this in the libraries section.
```py
# Libraries
from flask import Flask, render_template, request
```
Now, within the "handle_data" function, add the following.
```py
@app.route('/form-handler', methods=['POST'])
def handle_data():
    # Print messages to terminal
    print('Name: ', request.form['name'])
    print('Gender: ', request.form['gender'])
    
    # Append submitted values to web page.
    return 'Request received successfully!\
            <p>Name = ' + request.form['name'] + '</p>\
            <p> Gender = ' + request.form['gender'] + '</p>\
    '
```
With this added into the "handle_data" function, we can see the submission values both in Terminal and in the web page itself.

#### Pretty up the response
The prior way of building this function is fine for illustrative purposes. However, we really need to stay away from written HTML inside of the "return". (See below for example).
```py
def handle_data():
    # Collect POST request data values
    name = request.form['name']
    gender = request.form['gender']

    # Initialize response message
    submission_response = 'Greetings, '

    # Format response message
    if gender == 'Female':
        submission_response += 'Mrs. ' + name
    elif gender == 'Male':
        submission_response += 'Mr. ' + name
    else:
        submission_response += name

    # Print messages to terminal
    print('Name: ', request.form['name'])
    print('Gender: ', request.form['gender'])

    # Append submitted values to web page.
    return submission_response
```
#### Conforming to real-world scenarios
JSON is todays standard model of exchanging information between the front-end and the back-end.

Let's return to the "app.py" file and add the follow code blocks.
```py
# Libraries
from flask import Flask, render_template, request, jsonify
```
```py
@app.route('/form-handler', methods=['POST'])
def handle_data():
    return jsonify(request.form)
```

What we have now, is a JSON object containing KEY-VALUE pairs. This makes iterating through the submission values very easy.

### Final notes
At this point, this is essentially a boilerplate template anyone can use to have a quick start in developing a Python Flask web project.

# Sources: 
[Great Flask Tutorial](https://scoutapm.com/blog/python-flask-tutorial-getting-started-with-flask)
[Python Virtual Environment](https://python.land/virtual-environments/virtualenv)
[Python Documentation](https://flask.palletsprojects.com/en/1.1.x/quickstart/)
[jinja delimiters](https://jinja.palletsprojects.com/en/2.11.x/templates/)
[JavaScript Strict mode](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Strict_mode)
[JSON (technical stuff)](https://www.json.org/json-en.html)
[JSON for layman's with a dash of technical](https://www.infoworld.com/article/3222851/what-is-json-a-better-format-for-data-exchange.html)