from flask import Flask, abort

app = Flask(__name__)

# Task 1: Root route
@app.route('/')
def hello_world():
    return 'Hello World!'

# Task 2: Route for "Dojo!"
@app.route('/dojo')
def dojo():
    return 'Dojo!'

# Task 3: Route for "Hi" and name from URL
@app.route('/say/<string:name>')
def say_hi(name):
    return f'Hi {name}'

# Task 4: Route for repeating a word
@app.route('/repeat/<int:count>/<string:word>')
def repeat_word(count, word):
    return word * count

# Ninja Bonus: Handling non-string names
@app.errorhandler(400)
def bad_request(error):
    return 'Bad Request: Name must be a string', 400

# Ninja Bonus: Handling non-integer count and non-string word
@app.errorhandler(404)
def not_found(error):
    return 'Not Found: Invalid URL structure', 404

# Sensei Bonus: Handling undefined routes
@app.errorhandler(405)
def method_not_allowed(error):
    return 'Sorry! No response. Try again.', 405

if __name__ == '__main__':
    app.run(debug=True)
    