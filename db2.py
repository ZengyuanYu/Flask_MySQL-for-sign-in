#encoding:utf-8
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:272617@localhost:3306/mysql'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
db = SQLAlchemy(app)

class Table_two(db.Model):
    __tablename__ = 'table2'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    sqdw = db.Column(db.String(50))
    dz = db.Column(db.String(50))
    fddbr = db.Column(db.String(50))
    yb = db.Column(db.String(50))
    dh1 =db.Column(db.String(50))
    sj1 = db.Column(db.String(50))
    lxr = db.Column(db.String(50))
    dh2 = db.Column(db.String(50))
    sj2 = db.Column(db.String(50))
    psxmmc = db.Column(db.String(50))
    ysl = db.Column(db.Integer)
    psl = db.Column(db.Integer)
    zysl = db.Column(db.Integer)
    zls =  db.Column(db.Integer)
    zbs = db.Column(db.Integer)
    zps = db.Column(db.Integer)
    scwh = db.Column(db.Integer)
    shws =db.Column(db.Integer) #污水处理方式未 写
    wsclgy = db.Column(db.String(50))
    jdmj = db.Column(db.Integer)
    zjzmj = db.Column(db.Integer)
    zzmj = db.Column(db.Integer)
    scmj = db.Column(db.Integer)
    bglmj = db.Column(db.Integer)
    cymj = db.Column(db.Integer)
    zycpfw = db.Column(db.String(50))
    zyyl = db.Column(db.String(50))
    zylc = db.Column(db.String(50))
    wsclgylc = db.Column(db.String(50))
    def __init__(self, id ,sqdw ,dz,fddbr ,yb , dh1 , sj1 ,lxr , dh2 ,sj2,psxmmc ,ysl,psl ,zysl ,zls ,zbs ,zps ,scwh,shws, wsclgy , jdmj ,zjzmj ,zzmj,scmj,bglmj ,cymj ,zycpfw ,zyyl,zylc, wsclgylc):
        self.id = id
        self.sqdw = sqdw
        self.dz = dz
        self.fddbr = fddbr
        self.yb = yb
        self.dh1 = dh1
        self.sj1 = sj1
        self.lxr = lxr
        self.dh2 = dh2
        self.sj2 = sj2
        self.psxmmc = psxmmc
        self.ysl = ysl
        self.psl = psl
        self.zysl = zysl
        self.zls = zls
        self.zbs = zbs
        self.zps = zps
        self.scwh = scwh
        self.shws = shws
        self.wsclgy = wsclgy#jdmj ,zjzmj ,zzmj,scmj,bglmj ,cymj ,zycpfw ,zyyl,zylc, wsclgylc
        self.jdmj = jdmj
        self.zjzmj = zjzmj
        self.zzmj = zzmj
        self.scmj = scmj
        self.bglmj = bglmj
        self.cymj = cymj
        self.zycpfw = zycpfw
        self.zyyl = zyyl
        self.zylc = zylc
        self.wsclgylc= wsclgylc
db.create_all()