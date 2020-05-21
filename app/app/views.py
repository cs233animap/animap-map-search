from app import app
from flask import flash, render_template, request, redirect
from flask import render_template
from search_class import Search 
from search_db import SearchDB

app.config['SECRET_KEY'] = 'any secret string'

@app.route("/", methods=["GET","POST"])
def index():
    
    return render_template('index.html') 

@app.route("/search", methods=["GET","POST"])
def searching(): 
    form = Search()
    if form.validate_on_submit():
        return SearchDB(form.state.data)
    return render_template("search.html",form=form)


@app.route("/about")
def about():
    return render_template("about.html")

