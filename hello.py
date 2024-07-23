from flask import Flask, render_template, request, url_for, flash, redirect
from . import download as d
import os

app = Flask(__name__)
app.config['SECRET_KEY'] = "cce5571008a5ca3c1f5dea43b329642f3b43adb612bbf6cc90ac3ad76a0b862d"

@app.route("/")
def hello_world():
  return render_template('index.html')

# ...
@app.route('/download/',methods=['POST','GET'])
def download():
 if request.method == 'POST':
    replay = d.downloader(request)
    return render_template('replay.html',replay=replay)



if __name__ == '__main__':
  app.run(debug = True)
  
  
  