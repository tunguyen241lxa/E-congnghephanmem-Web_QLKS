from app import app
from flask import render_template
from app.models import *
from flask_admin import BaseView, expose, AdminIndexView, Admin
from flask_login import current_user, logout_user
from werkzeug.utils import redirect
from flask_login import login_user
from app import app, login, dao
from flask import render_template, request, url_for


from app.models import *
import hashlib


# dang nhap dau tien vo gap trang login
@app.route("/")
def index():
    return render_template("/admin/login.html")


@app.route("/login-admin", methods=["post", "get"])
def login_admin():
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password", "")
        password = str(hashlib.md5(password.strip().encode("utf-8")).hexdigest())
        user = User.query.filter(User.username == username.strip(),
                          User.password == password).first()
        if user:
            login_user(user=user)
    return redirect("/admin")




#  lay user
@login.user_loader
def load_user(user_id):
    return User.query.get(user_id)


if __name__ == "__main__":
    from app.admin_view import *

    app.run(debug=True, port=5556)