from app import app
from forms import CityForm
from controllers import ResultMaker
from flask import render_template, redirect, url_for
import json


@app.route('/', methods=["GET", "POST"])
def welcome():
    form = CityForm()
    if form.validate_on_submit():
        obj = ResultMaker()
        result = obj.call(form.city.data)
        clothes = obj.clothes()
        if form.degrees.data == True:
            result['temperature'] -= 273
        print(type(clothes))
        print(type(result))
        return redirect(url_for('.information', clothes=clothes, city=result))
    return render_template("welcome.html", form=form)


@app.route("/information/<city>/<clothes>", methods=["GET", "POST"])
def information(city,clothes):
    if city == "not_found":
        return redirect(url_for('wrong_name'))
    a = json.loads(city.replace("'", '"'))
    b = json.loads(clothes.replace("'", '"'))
    return render_template("information.html", info=a, clothes=b)


@app.route("/wrong_name")
def wrong_name():
    return render_template("wrong_name.html")


@app.route('/test')
def test():
    return render_template("test.html")
