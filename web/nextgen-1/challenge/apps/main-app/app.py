from flask import Flask, request, render_template
from urllib.request import urlopen

# acc -> accounting
# hr -> human resources

ACCOUNTING_DEP_LINK = "http://acc.dep.nextgen.org"
HR_DEP_LINK = "http://hr.dep.nextgen.org"


app = Flask(__name__)

@app.route("/")
def hello_world():
    return render_template('index.html', accLink=ACCOUNTING_DEP_LINK, hrLink=HR_DEP_LINK)

@app.route("/request", methods=['POST'])
def serve():
    with urlopen(request.form['service']) as response:
        html = response.read()
    return html

@app.errorhandler(404)
def not_found(e):
    return render_template("error-404.html"), 404

@app.errorhandler(500)
def server_error(e):
    return render_template("error-500.html"), 500
