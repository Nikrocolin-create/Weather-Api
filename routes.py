from app import app
from forms import CityForm
from controllers import ResultMaker
from flask import render_template, redirect, url_for, jsonify
import json

@app.route('/', methods=["GET", "POST"])
def welcome():
    form = CityForm()
    if form.validate_on_submit():
        result = ResultMaker().call(form.city.data)
        return redirect(url_for('information', city=result))
    return render_template("welcome.html", form=form)

@app.route("/information/<city>", methods=["GET", "POST"])
def information(city):
    a = json.loads(city.replace("'",'"'))
    return render_template("information.html", info=a)

@app.route('/test')
def test():
    return render_template("test.html")