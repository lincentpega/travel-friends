from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db/profiles.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


class Profiles(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String, nullable=False)
    password = db.Column(db.String, nullable=False)
    email = db.Column(db.String, nullable=False)
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
    if request.method == 'POST':
        email = request.form['email']
        username = request.form['username']
        password = request.form['password']
        name = request.form['name']
        age = request.form['age']
        country = request.form['country']
        city = request.form['city']
        languages = request.form['languages']
        address = request.form['address']
        contacts = request.form['contacts']
        about_text = request.form['about_text']
        phone = request.form['phone']
        photo = request.form['photo']

        new_profile = Profiles(email=email, username=username, password=password, name=name, age=age, country=country,
                               city=city, languages=languages, address=address,
                               contacts=contacts, about=about_text, phone=phone,
                               photo=photo)

        # try:
        db.session.add(new_profile)
        db.session.commit()
        return redirect('/')
        # except:
        #     return "Ошибка при добавлении пользователя"
    else:
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
