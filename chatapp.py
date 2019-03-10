from flask import Flask, render_template



app = Flask(__name__)
@app.route('/')
def index():
    return '<h1>Hello World</h1>'

@app.route('/home', methods=['GET','POST'])
def home():
    chats = ['Hey guys hows it going','Fine dude, what are you up to?','Working on this Python App man, what else!']
    return render_template('group.html',user_1="*Johnny the Coder Guy*",chats=chats)


if __name__ == "__main__":
    app.run(debug=True)
