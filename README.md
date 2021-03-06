
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

# Routes
@app.route("/", methods=['GET', 'POST', 'PUT']) # decorator

# Functions
def home():
    return "Hello World!"

# Execute program
app.run(debug = True)
```

### Replace "home" function with following code block
Below is an example of how to return straight HTML to the browser.
```python
def home():
    # Returning HTML
    return "<html>\
                <body>\
                    <h3><u>Hello YOURNAME!</u></h3>\
                </body>\
            </html>"
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

# Routes
@app.route("/")

# Functions
def home():
    return render_template('index.html')

# Execute program
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
        <link rel="stylesheet" href="/static/index.css">
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
        <link rel="stylesheet" href="/static/index.css">
        <!-- Inject JavaScript here-->
        <script src="/static/index.js"></script>
    </head>
```
If you've been successful up until this point, now is a good time to take a break.
### Dynamic Routes

# Sources: 
[Great Flask Tutorial](https://scoutapm.com/blog/python-flask-tutorial-getting-started-with-flask)
[Python Virtual Environment](https://python.land/virtual-environments/virtualenv)
[Python Documentation](https://flask.palletsprojects.com/en/1.1.x/quickstart/)
[jinja delimiters](https://jinja.palletsprojects.com/en/2.11.x/templates/)
[JavaScript Strict mode](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Strict_mode)