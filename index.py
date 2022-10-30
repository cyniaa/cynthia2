from flask import Flask, render_template, request
from datetime import datetime

app = Flask(__name__)

@app.route("/")
def index():
    homepage = "<h1>蕭媛芯的求職資訊</h1>"
    homepage += "<h3><a href=/about>我的個人簡介</a></h3><br>"
    homepage += "<h3><a href=/MIS>MIS相關工作介紹</a></h3><br>"
    homepage += "<h3><a href=/work>興趣何倫碼測驗結果</a></h3><br>"
    homepage += "<h3><a href=/me>自傳履歷</a></h3><br>"
    return homepage



@app.route("/MIS")
def MIS():
    return render_template("公司.html")

@app.route("/work")
def work():
    return render_template("測驗.html")

@app.route("/about")
def about():
    return render_template("abouutme.html")
    
@app.route("/me")
def me():
    return render_template("自傳.html")

if __name__ == "__main__":
    app.run()