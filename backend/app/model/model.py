from .. import db 
from flask_login import UserMixin
from werkzeug.security import generate_password_hash
from werkzeug.security import check_password_hash


class Role:
	
	PRINCIPAL = 0x0001
	DEPUTY_PRINCIPAL = 0x0002
	
	DEPARTMENT_HEAD = 0x0003
	DEPUTY_DEPARTMENT_HEAD = 0x0004
	
	GRADE_HEAD = 0x0005
	DEPUTY_GRADE_HEAD = 0x0006
	
	CLASS_TEACHER = 0x0007
	DEPUTY_CLASS_TEACHER = 0x0008
	
	TEACHER = 0x0009
	ACTIING_TEACHER = 0x00a
	
	INTERN_TEACHER = 0x00b
	
	STUDENT_BOARD_HEAD = 0X00c
	DEPUTY_STUDENT_BOARD_HEAD _ 0x00d
	
	STUDENT_BOARD = 0x00e
	
	STUDENT = 0x00f


class School(db.Model): 
	
	id = db.Column(db.Integer, primary_key=True)
	name = db.Column(db.String(50), nullable=False)
	location = db.Column(db.String(100), nullable=False)
	emis = db.Column(db.String(8), nullable=False)
	type = db.Column(db.Boolean, default=False, nullable=False)
	started = db.Column(db.DateTime, nullable=False)
	registered = db.Column(db.DateTime, nullable=False)
	uuid = db.Integer(db.Integer, nullable=False, unique=True)
	
	contracts = db.relationship('Contact', backref='contact')
	staff = db.relationship('Staff', backref='staff')
	students = db.relationship('Student', backref='students')


class Staff(db.Model):
	
	id = db.Column(db.Integer, primary_key=True)
	
	school_id = db.Column(db.Integer, db.ForeignKey('school.uuid'))


