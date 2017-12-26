#encoding:utf-8
from flask import Flask
from flask import request
from db1 import Table_one,db
# from db2 import Table_two
# from db3 import Table_three
# from db4 import Table_four
# from db5 import Table_five
#import hello
app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():
    return '<h1>Home</h1>'

@app.route('/signin', methods=['GET'])
def signin_form():
    return '''<form action="/signin" method="post">
              <p><input name="username"></p>
              <p><input name="password" type="password"></p>
              <p><button type="submit">Sign In</button></p>
              </form>'''

@app.route('/signin', methods=['POST'])
def signin():
    if request.form['username']=='admin' and request.form['password']=='password':
        admin_role = Table_one(sqbh = request.form['username'] ,sqsj = request.form['password'])

        db.session.add(admin_role)

        db.session.commit()

        return '<h3>Hello, admin!</h3>'
    else:
        admin_role = Table_one(sqbh = request.form['username'] ,sqsj = request.form['password'])

        db.session.add(admin_role)
        db.session.commit()
        return '<h3>Bad username or password.</h3>'

if __name__ == '__main__':
    app.run(debug=True)