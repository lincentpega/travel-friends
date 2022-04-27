from flask import Flask, render_template, request, redirect, flash, url_for
from flask_login import login_user, login_required, logout_user
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import check_password_hash, generate_password_hash

app = Flask(__name__)
app.secret_key = 'secret_key'
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


@app.route("/profile", methods=['GET', 'POST'])
def profile():
    return render_template("profile.html")


@app.route("/dating", methods=['GET', 'POST'])
@login_required
def dating():
    persons_data_list = Profiles.query.all()
    return render_template("dating.html", persons_list=persons_data_list, size=len(persons_data_list))


@app.route("/about", methods=['POST'])
def about():
    return render_template("about.html")


@app.route("/login", methods=['GET', 'POST'])
def login_page():
    login = request.form.get('login')
    password = request.form.get('password')

    if login and password:
        user = Profiles.query.filter_by(login=login).first()
        if check_password_hash(user.password, password):
            login_user(user)

            # next_page = request.args.get('next_page')
            # redirect('next_page')
            redirect('dating')
        else:
            flash('Неверный пароль!')
    else:
        flash('Введите логин и пароль!')
        return render_template('login.html')


@app.route("/registration", methods=['GET', 'POST'])
def registration():
    if request.method == 'POST':
        email = request.form['email']
        username = request.form['username']
        password = request.form['password']
        password2 = request.form['password2']
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

        if not(username or password or password2):
            flash('Пожалуйста, заполните поля: Имя пользователя, Пароль, Повторите пароль')
        elif password != password2:
            flash('Пароли отличаются, повторите ввод!')
        else:
            pass_hash = generate_password_hash(password)
            new_profile = Profiles(email=email, username=username, password=pass_hash, name=name, age=age,
                                   country=country,
                                   city=city, languages=languages, address=address,
                                   contacts=contacts, about=about_text, phone=phone,
                                   photo=photo)
            try:
                db.session.add(new_profile)
                db.session.commit()
                return redirect(url_for('login_page'))
            except:
                return "Ошибка при добавлении пользователя"

    else:
        return render_template("registration.html")


@app.route("/logout", methods=['GET', 'POST'])
@login_required
def logout():
    logout_user()
    redirect(url_for('index'))


if __name__ == "__main__":
    app.run(host="localhost", port=5000, debug=True)
