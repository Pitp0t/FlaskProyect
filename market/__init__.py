from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager


app = Flask(__name__, template_folder= 'templates')
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///market.db'
app.config['SECRET_KEY']= '742d01ab54a85d066c370dd1'
db = SQLAlchemy(app)
bcrypt= Bcrypt(app)
login_manager= LoginManager(app)


from market import routes


