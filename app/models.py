from sqlalchemy.orm import relationship
from app import db, admin
from flask_login import UserMixin
from datetime import datetime
from sqlalchemy import Column, String, Float, Integer, ForeignKey, Boolean, DateTime, Date, Enum
import enum


class EmployeeRole(enum.Enum):
    ADMIN = 1
    EMPLOYEE = 2


class Gender(enum.Enum):
    MALE = 1
    FEMALE = 2
    OTHER = 3


class Position(db.Model):
    __tablename__ = "position"

    id = Column(Integer, primary_key=True, autoincrement=True)
    position_name = Column(String(50), nullable=False)
    employees = relationship('Employee', backref='position', lazy=True)

    def __str__(self):
        return self.position_name


# them loai phong
class HotelCategory(db.Model):
    __tablename__ = "hcategory"
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(255), nullable=False)
    products = relationship('HotelProduct', backref='hcategory', lazy=True)

    def __str__(self):
        return self.name


class HotelProduct(db.Model):
    __tablename__ = "hproduct"
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(255), nullable=False)
    quantity = Column(Integer, nullable=False)
    price = Column(Float, default=0)
    image = Column(String(255), nullable=True)
    # hotelcategory_id = Column(Integer, ForeignKey(Hotelcategory.id), autoincrement=True)
    hotelcategory_id = Column(Integer, ForeignKey(HotelCategory.id))

    def __str__(self):
        return self.name


# them loai nhan vien
class ManageCategory(db.Model):
    __tablename__ = "mcategory"
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(255), nullable=False)
    kinds = relationship('ManageProduct', backref='mcategory', lazy=True)

    def __str__(self):
        return self.name


class ManageProduct(db.Model):
    __tablename__ = "mproduct"
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(255), nullable=False)
    quantity = Column(Integer, nullable=False)
    salary = Column(Float, default=0)
    # hotelcategory_id = Column(Integer, ForeignKey(Hotelcategory.id), autoincrement=True)
    mcategory_id = Column(Integer, ForeignKey(ManageCategory.id))

    def __str__(self):
        return self.name


# loc loai nhan vien


# login
class Employee(db.Model, UserMixin):
    __tablename__ = "employee"

    id = Column(Integer, primary_key=True, autoincrement=True)
    username = Column(String(50), nullable=False)
    password = Column(String(255), nullable=False,
                      default="4dff4ea340f0a823f15d3f4f01ab62eae0e5da579ccb851f8db9dfe84c58b2b37b"
                              "89903a740e1ee172da793a6e79d560e5f7f9bd058a12a280433ed6fa46510a")
    name = Column(String(50), nullable=False)
    gender = Column(Enum(Gender), nullable=True)
    date_of_birth = Column(Date, nullable=True)
    phone = Column(String(30), nullable=True)
    address = Column(String(100), nullable=True)
    active = Column(Boolean, nullable=False, default=True)
    employee_role = Column(Enum(EmployeeRole), default=EmployeeRole.EMPLOYEE)
    start_work_date = Column(Date, nullable=True, default=datetime.now())
    position_id = Column(Integer, ForeignKey(Position.id), nullable=False)
    activity_logs = relationship('ActivityLog', backref='employee', lazy=True)
    transaction_slips = relationship('TransactionSlip', backref='employee', lazy=True)

    def __str__(self):
        return self.username


class User(db.Model, UserMixin):
    __tablename__ = "user"
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(50), nullable=False)
    active = Column(Boolean, default=True)
    username = Column(String(50), nullable=False)
    password = Column(String(50), nullable=False)
    staff_role = Column(String(10), nullable=False)
    employee_id = Column(Integer, ForeignKey(Employee.id), nullable=False)

    def __str__(self):
        return self.name


class ActivityLog(db.Model):
    __tablename__ = "activity_log"

    id = Column(Integer, primary_key=True, autoincrement=True)
    employee_id = Column(Integer, ForeignKey(Employee.id), nullable=False)
    activity_time = Column(DateTime, nullable=False, default=datetime.now())
    activity = Column(String(50), nullable=False)
    description = Column(String(300), nullable=True)

    def __str__(self):
        return self.id


if __name__ == "__main__":
    db.create_all()
