from flask import Flask,render_template
app=Flask(__name__)
@app.route('/hello/')
@app.route('/hello/<username>')
def hello(username=None):
    return render_template("hello.html",username=username)

@app.route('/predict')
def predict():
    a=None+0
    return "Prediction: 0"