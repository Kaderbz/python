from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html", row=8, col=8, color_one='red', color_two='black', title='Index')

@app.route('/<int:x>')
def row_route(x):
    return render_template("index.html", row=x, col=8, color_one='red', color_two='black', title=f'Row {x}')

@app.route('/<int:x>/<int:y>')
def row_col_route(x, y):
    return render_template("index.html", row=x, col=y, color_one='red', color_two='black', title=f'Row {x}, Col {y}')

@app.route('/<int:x>/<int:y>/<string:one>')
def row_col_one_route(x, y, one):
    return render_template("index.html", row=x, col=y, color_one=one, color_two='black', title=f'Row {x}, Col {y}, Color {one}')

@app.route('/<int:x>/<int:y>/<string:one>/<string:two>')
def row_col_two_route(x, y, one, two):
    return render_template("index.html", row=x, col=y, color_one=one, color_two=two, title=f'Row {x}, Col {y}, Color {one} and {two}')

if __name__ == "__main__":
    app.run(debug=True)
