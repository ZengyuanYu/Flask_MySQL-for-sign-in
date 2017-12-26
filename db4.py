#encoding:utf-8
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:272617@localhost:3306/mysql'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
db = SQLAlchemy(app)

class Table_four(db.Model):#审核、审批情况
    __tablename__ = 'table4'
    id = db.Column(db.Integer,primary_key=True,autoincrement=True)
    jbyj = db.Column(db.Text(50))
    jbr = db.Column(db.String(10))
    jbrdate = db.Column(db.Time)
    shyj = db.Column(db.Text(50))
    shr = db.Column(db.String(10))
    shrdate = db.Column(db.Time)
    spjgyj = db.Column(db.Text)
    fzr = db.Column(db.String(10))
    fzrdate = db.Column(db.Time)
    beizhu = db.Column(db.Text)
    def __init__(self,id,jbyj,jbr,jbrdate,shyj,shr,shrdate,spjgyj,fzr,fzrdate,beizhu):
        self.id = id
        self.jbyj = jbyj
        self.jbr = jbr
        self.jbrdate = jbrdate
        self.shyj = shyj
        self.shr = shr
        self.shrdate = shrdate
        self.spjgyj= spjgyj
        self.fzr = fzr
        self.fzrdate=fzrdate
        self.beizhu = beizhu
db.create_all()