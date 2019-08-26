from flask import Flask, render_template, request, flash
from flask_wtf import Form
from wtforms import TextField, IntegerField, TextAreaField, SubmitField, RadioField, SelectField, PasswordField
from wtforms import validators, ValidationError
app = Flask(__name__)
app.secret_key = 'development key'

class ContactForm(Form):
   name = TextField("Name Of Student",[validators.DataRequired("Please enter your name.")])
   Gender = RadioField("Gender", [validators.Optional()], choices = [("M","Male"),("F","Female")])
   Address = TextAreaField("Address", [validators.Optional()])   
   email = TextField("Email",[validators.DataRequired("Please enter your email address."),validators.Email("Please enter a valid email address.")])
   Age = IntegerField("age", [validators.Optional()])
   Password = PasswordField('New Password', [validators.DataRequired(),validators.EqualTo('Confirm', message='Passwords must match'), validators.Length(min=2, max=25, message='Minimum 2 characters')])
   Confirm = PasswordField('Repeat Password', [validators.DataRequired()])
   submit = SubmitField("Send")



@app.route('/contact', methods = ['GET', 'POST'])
def contact():
   form = ContactForm()
   
   if request.method == 'POST':
      if form.validate() == False:
         flash('All fields are required.')
         return render_template('contact.html', form = form)
      else:
         return render_template('success.html')
   elif request.method == 'GET':
         return render_template('contact.html', form = form)

if __name__ == '__main__':
   app.run(debug = True)
