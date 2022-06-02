from flask import Flask, render_template

app = Flask(__name__)

# Accounting department

@app.route("/overview")
def overview():
    return render_template('summary.html')
