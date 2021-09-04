from flask import Flask, redirect
app = Flask(__name__)

@app.route("/")
def hello():
    return redirect("https://afflat3e1.com/lnk.asp?o=22483&c=918273&a=433607&k=0&l=23309", code=302)
