#encoding:utf-8
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:272617@localhost:3306/mysql'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
db = SQLAlchemy(app)

class Table_five(db.Model):#秦淮区排水户废水排放现场勘查意见
    __tablename__ = 'table5'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    dwmc = db.Column(db.String(50))
    dd = db.Column(db.String(50))
    lsgd = db.Column(db.String(50))
    ljgwz = db.Column(db.String(50))
    psgj = db.Column(db.String(50))
    psqx = db.Column(db.String(50))
    num1 = db.Column(db.Text)#排水现状
    num2 = db.Column(db.Text)
    num3 = db.Column(db.Text)
    num4 = db.Column(db.Text)
    yj = db.Column(db.Text)
    fzr = db.Column(db.String(10))
    date = db.Column(db.Time)
    def __init__(self,id,dwmc,dd,lsgd,ljgwz,psgj,psqx,num1,num2,num3,num4,yj,fzr,date):
        self.id = id
        self.dwmc = dwmc
        self.dd = dd
        self.lsgd= lsgd
        self.ljgwz = ljgwz
        self.psgj = psgj
        self.psqx = psqx
        self.num1 = num1
        self.num2 = num2
        self.num3 = num3
        self.num4 = num4
        self.yj = yj
        self.fzr = fzr
        self.date = date
db.create_all()