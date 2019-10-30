from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField
from wtforms.validators import DataRequired, Length, Email

class RegForm(FlaskForm):
	team = StringField('Team name*', validators = [DataRequired(),Length(min=2,max=50)])

	name1 = StringField('Name', validators = [DataRequired(),Length(min=2,max=50)])
	uni1 = StringField('Institution', validators = [DataRequired(),Length(max=50)])
	email1 = StringField('Email', validators = [DataRequired(),Email()])
	phone1 = StringField('Phone number', validators = [DataRequired()])


	name2 = StringField('Name')
	uni2 = StringField('Institution')
	email2 = StringField('Email')
	phone2 = StringField('Phone number')


	name3 = StringField('Name')
	uni3 = StringField('Institution')
	email3 = StringField('Email')
	phone3 = StringField('Phone number')


	name4 = StringField('Name')
	uni4 = StringField('Institution')
	email4 = StringField('Email')
	phone4 = StringField('Phone number')


	trxid = StringField('Transaction ID*', validators = [DataRequired()])

	submit= SubmitField('Submit')

class login(FlaskForm):
	pwd = PasswordField('Password', validators=[DataRequired()])
	submit = SubmitField('Login')