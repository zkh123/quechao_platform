# coding:utf8
import sys

from flask import Flask
from flask_sqlalchemy import SQLAlchemy

reload(sys)
sys.setdefaultencoding("utf8")

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:@192.168.1.114:3306/quechao_flask'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
db = SQLAlchemy(app)


class User(db.Model):
    def __init__(self,id, username, email):
        self.id = id
        self.username = username
        self.email = email

    """定义数据模型"""
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)

    def __repr__(self):
        return '<User %r>' % self.username


if __name__ == '__main__':
    print(db)
    db.create_all()
