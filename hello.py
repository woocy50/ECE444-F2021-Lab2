from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
#    return '<h1>Hello World!</h1>'
    return render_template('index.html')

@app.route('/user/<name>')
def user(name):
#    return f'<h1>Hello, {name}!</h1>'
    return render_template('user.html', name=name)

if __name__ == '__main__':
    app.run(debug=True)
