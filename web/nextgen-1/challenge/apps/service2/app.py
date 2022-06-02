from flask import Flask, render_template

app = Flask(__name__)

# Human resources department
@app.route("/overview")
def overview():
    return render_template('summary.html')
