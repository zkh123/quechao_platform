# coding:utf8
from flask import Flask, render_template
from models import User, db

import sys

reload(sys)
sys.setdefaultencoding("utf8")

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello World!'

@app.route('/hs')
def hello():
    return 'ok'

# http://127.0.0.1:5000/index
@app.route('/index')
def toIndex():
    return render_template('index.html', name='上海')

# http://127.0.0.1:5000/add
@app.route('/add')
def addData():
    admin = User(username='admin', email='admin@example.com')
    guest = User(username='guest', email='guest@example.com')
    db.session.add(admin)
    db.session.add(guest)
    db.session.commit()
    return 'ok'

# http://127.0.0.1:5000/selectAll
@app.route('/selectAll')
def select():
    for user in User.query.all():
        print('id:{},username:{}, email:{}'.format(user.id, user.username, user.email))
    return 'ok'

# http://127.0.0.1:5000/selectById/2
@app.route('/selectById/<int:id>')
def selectById(id):
    user = User.query.filter_by(id)
    print('id:{},username:{}, email:{}'.format(user.id,user.username, user.email))
    return 'ok'

# http://127.0.0.1:5000/selectByUsername/guest
@app.route('/selectByUsername/<username>')
def selectByUsername(username):
    user = User.query.filter_by(username=username).first()
    print('id:{},username:{}, email:{}'.format(user.id, user.username, user.email))
    return 'ok'

# http://127.0.0.1:5000/selectLike
@app.route('/selectLike')
def selectLike():
    list_users = User.query.filter(User.username.endswith('t')).all()
    for user in list_users:
        print('id:{},username:{}, email:{}'.format(user.id, user.username, user.email))
    return 'ok'


# http://127.0.0.1:5000/delete
@app.route('/delete')
def delete():
    user = User.query.first()
    db.session.delete(user)
    db.session.commit()
    return 'ok'


# http://127.0.0.1:5000/update
@app.route('/update')
def update():
    user = User.query.first()
    user.username = 'sb'
    db.session.commit(user)
    return 'ok'

if __name__ == '__main__':
    app.run(debug=True)
