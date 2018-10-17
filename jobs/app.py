from flask import Flask, render_templete
app = Flask(__name__)
@app.route('/')
@app.route('/jobs')
def jobs():
    return render_templete('index.html')
