from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///market.db'
db = SQLAlchemy(app)

app = Flask(__name__)

print(__name__)


@app.route("/")
def BinoCent():
  return render_template('home.html')

@app.route('/about_me')
def about_me():
    return render_template('AboutMe.html')

if __name__ == '__main__':
  app.run(host='0.0.0.0', debug=True)
  
