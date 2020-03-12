import os
from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
db = SQLAlchemy(app)

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///quotes.db"

if "DATABASE_URL" in os.environ:
    app.config["SQLALCHEMY_DATABASE_URI"] = os.environ["DATABASE_URL"]

app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

port = "5000"
if "PORT" in os.environ:
    port = os.environ["PORT"]

class Quote(db.Model):
    __tablename__ = "quotes"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    quote = db.Column(db.String(120), unique=True, nullable=False)


@app.route("/")
def index():
    quotes = Quote.query.filter().all()
    return render_template("index.html", quotes = quotes)

@app.route("/", methods = ["POST"])
def handle_quote():
    text = request.form["quote"]
    quote = Quote(quote = text)
    db.session.add(quote)
    db.session.commit()
    return redirect(url_for("index"))


app.run(port = port, host = "0.0.0.0")
