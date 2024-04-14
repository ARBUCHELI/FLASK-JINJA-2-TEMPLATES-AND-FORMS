from flask import Flask, render_template
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField

app = Flask(__name__)
app.config["SECRET_KEY"] = "my_secret"

class MyForm(FlaskForm):
    my_textfield = StringField("TextLabel")
    my_submit = SubmitField("SubmitName")

@app.route("/")
def my_route():
    flask_form = MyForm()
    return render_template("my_template", template_form=flask_form)