from flask import redirect, render_template, url_for
from .views import home_view
from app import app


@app.route("/")
def home():
    return home_view()
