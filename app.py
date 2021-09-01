from flask import Flask, redirect
app = Flask(__name__)

@app.route("/")
def hello():
    return redirect("https://www.tvc-mall.com/", code=302)
