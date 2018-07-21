# coding:utf8
from flask import Flask, render_template
from models import User, db

import sys

reload(sys)
sys.setdefaultencoding("utf8")

app = Flask(__name__)
app.config['SECRET_KEY']="1234"


@app.route('/')
def hello_world():
    return 'Hello World!'


def hello():
    return 'ok'


@app.route('/index')
def toIndex():
    return render_template('index.html', name='上海')


@app.route('/add')
def addData():
    admin = User(username='admin', email='admin@example.com')
    guest = User(username='guest', email='guest@example.com')
    db.session.add(admin)
    db.session.add(guest)
    db.session.commit()
    return 'ok'


if __name__ == '__main__':
    app.run(debug=True)
