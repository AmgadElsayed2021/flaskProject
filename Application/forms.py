from flask_wtf import FlaskForm
from wtforms import StringField ,PasswordField,SubmitField,BooleanField
from wtforms.validators import DataRequired

# class LoginForm(FlaskForm):
#     email = StringField("Email", validators=[DataRequired()])
#     password = PasswordField("Password" , validators=[DataRequired()])
#     remember_me = BooleanField("Remember Me")
#     submit = SubmitField("Login")
# class RegisterForm(FlaskForm):
#     pass