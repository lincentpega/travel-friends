from flask import url_for, Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
from werkzeug.utils import redirect


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db/profiles.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


class Profiles(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    age = db.Column(db.Integer)
    country = db.Column(db.String)
    city = db.Column(db.String)
    languages = db.Column(db.String)
    address = db.Column(db.String)
    phone = db.Column(db.String)
    contacts = db.Column(db.String)
    about = db.Column(db.String)
    photo = db.Column(db.String)

    def __repr__(self):
        return f'{self.id} {self.name}'


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
    persons_data_list = Profiles.query.all()
    return render_template("dating.html", persons_list=persons_data_list, size=len(persons_data_list))


@app.route("/about", methods=['GET', 'POST'])
def about():
    return render_template("about.html")


if __name__ == "__main__":
    app.run(host="localhost", port=5000, debug=True)