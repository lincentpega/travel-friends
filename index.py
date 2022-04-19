from flask import url_for, Flask, render_template, request
from werkzeug.utils import redirect
import main_db_client


app = Flask(__name__)

@app.route("/", methods=['GET', 'POST'])
@app.route("/index", methods=['GET', 'POST'])
def index():
    return render_template("index.html")


@app.route("/registration", methods=['GET', 'POST'])
def registration():
    return render_template("registration.html")


@app.route("/profile", methods=['GET', 'POST'])
def profile():
    return render_template("profile.html")


@app.route("/dating", methods=['GET', 'POST'])
def dating():
    db = main_db_client.DB()
    persons_data_list = db.view_records()
    return render_template("dating.html", persons_list=persons_data_list, size=len(persons_data_list))


@app.route("/about", methods=['GET', 'POST'])
def about():
    return render_template("about.html")


if __name__ == "__main__":
    app.run(host="localhost", port=5000, debug=True)