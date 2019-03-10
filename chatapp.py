from flask import Flask

app = Flask(__name__)
@app.route('/')
def index():
    return '<h1>Hello World</h1>'

@app.route('/homt')
def home():
    return '<h3>Welcome to the ChatApp Home Page</h3>'
if __name__ == "__main__":
    app.run(debug=True)
