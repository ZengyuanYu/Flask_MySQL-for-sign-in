from flask import Flask
from flask_sqlalchemy import SQLAlchemy
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:272617@localhost:3306/mysql'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
db = SQLAlchemy(app)

class Table_one(db.Model):
    __tablename__ = 'table1'
    id = db.Column(db.Integer,primary_key=True,autoincrement=True)
    sqbh = db.Column(db.String(20))
    slbh = db.Column(db.String(20))
    sqsj = db.Column(db.String(20))
    slsj = db.Column(db.String(20))
    pshmc = db.Column(db.String(20))
    psxmmc = db.Column(db.String(20))
    tbrq = db.Column(db.String(20))
    #scsq = db.Column(db.Boolean)
    def __init__(self,sqbh='NULL',sqsj='NULL'):
        self.sqbh = sqbh
        self.sqsj = sqsj
db.create_all()