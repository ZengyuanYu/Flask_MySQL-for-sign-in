from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import config

app = Flask(__name__)
app.config.from_object(config)

db = SQLAlchemy(app)

class Article(db.Model):
    __tablename__ = 'article'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.String(100), nullable=False)
    content = db.Column(db.Text, nullable=False)

db.create_all()

@app.route('/')
def index():
    #增加
    # article1 = Article(title='aaa', content='bbb')
    # db.session.add(article1)
    # db.session.commit()

    #查找
    # result = Article.query.filter(Article.title == 'aaa').all()
    # print(result)

    #修改
    # #1.查找需要更改的数据
    # article1 = Article.query.filter(Article.title == 'aaa').first()
    # #2.修改值
    # article1.title = 'new title'
    # #3.做事务提交
    # db.session.commit()

    #删除数据库
    # #1.把需要删除的数据查找出来
    # article1 = Article.query.filter(Article.content == 'bbb').first()
    # #2.把该数据删除掉
    # db.session.delete(article1)
    # #3.做事务提交
    # db.session.commit()
    return 'index'


if __name__ == '__main__':
    app.run()
