from flask import Flask, redirect, render_template, request, url_for
import random, string


def home_view():
    return render_template("home.html")


