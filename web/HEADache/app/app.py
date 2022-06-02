from flask import Flask,url_for,request,render_template

app = Flask(__name__)

@app.route("/")
def hello_world():
    polite=False
    if request.headers.get('wanna-something')=="can-i-have-a-flag-please":
        polite=True
    return render_template('index.html',static=url_for('static', filename='bulma.min.css'),polite=polite)


if __name__ == '__main__':
      app.run(host='0.0.0.0', port=1337)