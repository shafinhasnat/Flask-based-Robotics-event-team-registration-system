from flask import Flask, render_template,redirect,url_for,flash
from forms import RegForm, login
from flask_sqlalchemy import SQLAlchemy 
from flask_login import login_user,logout_user, login_required,current_user,LoginManager,UserMixin
import os

app=Flask(__name__)
app.config['SECRET_KEY'] = 'mieisthebestmiedaytekhubmojahobe'

ENV = 'prod'
if ENV == 'dev':
	app.debug = True
	app.config['SQLALCHEMY_DATABASE_URI'] = 'postgres://postgres:19971904@localhost/miereg'
else:
	app.debug=False
	app.config = "postgres://aazmqvtooyrcmu:56e1c61f87f6e6cbed71ed4c0413c4441cbcdf08e12b71a040286714a41ceda3@ec2-174-129-253-27.compute-1.amazonaws.com:5432/def8rb96r96eld"

# app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
login_manager = LoginManager(app)

class Register(db.Model):
	__tablename__ = 'teams'
	id = db.Column(db.Integer, primary_key=True)
	team = db.Column(db.String(120), nullable=False)
	name1 = db.Column(db.String(120), nullable=False)
	name2 = db.Column(db.String(120))
	name3 = db.Column(db.String(120))
	name4 = db.Column(db.String(120))
	uni1 = db.Column(db.String(120), nullable=False)
	uni2 = db.Column(db.String(120))
	uni3 = db.Column(db.String(120))
	uni4 = db.Column(db.String(120))
	email1 = db.Column(db.String(120), nullable=False)
	email2 = db.Column(db.String(120))
	email3 = db.Column(db.String(120))
	email4 = db.Column(db.String(120))
	phone1 = db.Column(db.String(120), nullable=False)
	phone2 = db.Column(db.String(120))
	phone3 = db.Column(db.String(120))
	phone4 = db.Column(db.String(120))
	trxid = db.Column(db.String(120), nullable=False)
	def __repr__(self):
		return f"Register('self.id','self.team','self.name1','self.email1','self.phone1','self.trxid')"

class User(UserMixin):
  def __init__(self,id):
    self.id = id

@login_manager.user_loader
def load_user(user_id):
    return User(user_id)

@app.route('/')
def home():
	title='Home'
	return render_template('index.html',title=title)

@app.route('/regisration', methods = ['GET', 'POST'])
def regisration():
	form=RegForm()
	title='Registration'
	if form.validate_on_submit():
		print('###########################validate###########################################')
		team= Register(team=form.team.data,name1=form.name1.data,name2=form.name2.data,
					   name3=form.name3.data,name4=form.name4.data,
					   uni1=form.uni1.data,uni2=form.uni2.data,uni3=form.uni3.data,uni4=form.uni4.data,
					   email1=form.email1.data,email2=form.email2.data,email3=form.email3.data,email4=form.email4.data,
					   phone1=form.phone1.data,phone2=form.phone2.data,phone3=form.phone3.data,phone4=form.phone4.data,
					   trxid=form.trxid.data)
		db.session.add(team)
		db.session.commit()
		flash(f'Your response has been recorded! Please wait for confirmation.','success')
		return redirect(url_for('home'))
	else:
		print('###########################not validate###########################################')
	return render_template('reg.html',title=title,form=form)


@app.route('/admin/teams')
@login_required
def teams():
	teams = Register.query.all()
	title = 'teams'
	return render_template('admin.html', teams=teams, title=title)

@app.route('/admin', methods = ['GET', 'POST'])
def admin():
	form = login()
	title='admin'
	if form.validate_on_submit():
		if form.pwd.data == 'mieshera':
			login_user(User(1))
			return redirect(url_for('teams'))
	return render_template('login.html',title=title,form=form)

@app.route('/logout')
@login_required
def logout():
	logout_user()
	return redirect(url_for('home'))


if __name__=='__main__':
	app.run()