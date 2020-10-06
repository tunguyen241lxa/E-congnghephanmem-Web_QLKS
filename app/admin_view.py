from flask_admin import BaseView, expose
from flask import redirect, url_for, request
from app import db, admin, dao
from flask_login import current_user, logout_user
from flask_admin.contrib.sqla import ModelView
from app.models import HotelCategory, HotelProduct, ManageCategory, ManageProduct
from flask import render_template

class AuthenticatedBaseView(BaseView):
    def is_accessible(self):
        return current_user.is_authenticated \
               and current_user.active == True

    def inaccessible_callback(self, name, **kwargs):
        # redirect to login page if user doesn't have access
        logout_user()
        return redirect(url_for('admin/login.html', next=request.url))


class AuthenticatedModelView(ModelView):
    def is_accessible(self):
        return current_user.is_authenticated \
               and current_user.active == True

    def inaccessible_callback(self, name, **kwargs):
        # redirect to login page if user doesn't have access
        logout_user()
        return redirect(url_for('admin/login.html', next=request.url))


class AboutUsView(AuthenticatedBaseView):
    @expose("/")
    def index(self):
        return self.render("admin/about-us.html")


# them loai phong
class HotelProductModelView(AuthenticatedModelView):
    column_display_pk = True
    can_create = True


class HotelCategoryModelView(AuthenticatedModelView):
    column_display_pk = True
    can_create = True


# them chuc vu nhan vien
class ManageProductModelView(AuthenticatedModelView):
    column_display_pk = True
    can_create = True


class ManageCategoryModelView(AuthenticatedModelView):
    column_display_pk = True
    can_create = True


class LogoutView(BaseView):
    @expose("/")
    def index(self):
        logout_user()

        return render_template("admin/login.html")

    def is_accessible(self):
        return current_user.is_authenticated


class PositionModelView(AuthenticatedModelView):
    column_display_pk = True
    can_export = True
    form_columns = ('position_name',)
    form_filters = ('position_name',)
    page_size = 10


admin.add_view(AboutUsView(name="About-us"))
admin.add_view(HotelCategoryModelView(HotelCategory, db.session))
admin.add_view(HotelProductModelView(HotelProduct, db.session))
admin.add_view(ManageCategoryModelView(ManageCategory, db.session))
admin.add_view(ManageProductModelView(ManageProduct, db.session))
admin.add_view(LogoutView(name="Đăng Xuất"))
