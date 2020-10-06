from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_admin import Admin

app = Flask(__name__)

app.secret_key = "123456"
app.config["SQLALCHEMY_DATABASE_URI"] = "mysql+pymysql://root:1111@localhost/db_khachsan?charset=utf8mb4"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db = SQLAlchemy(app)
admin = Admin(app=app, name="Trang Quản Trị", template_mode="bootstrap3")
# app.config['MYSQL_HOST'] = 'localhost'
login = LoginManager(app=app)