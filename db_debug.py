from app import Profiles, db

Name = "Margot"
Age = 31
Country = "USA"
City = "San-Francisco"
Languages = "English, Русский"
Address = "San-Francisco, Juvenile str, h. 41"
Phone = "88005553535"
Contacts = "vk.com/blank_page, someaddress@rundex.org"
About = "Australian actress and producer. Has received several accolades throughout her career, including nominations for two Academy Awards, three Golden Globe Awards, five Screen Actors Guild Awards and five British Academy Film Awards. Time magazine named me one of the 100 most influential people in the world in 2017 and I was ranked as one of the world's highest-paid actresses by Forbes in 2019."
Photo = "0.png"

# me = Profiles(id=ID, name=Name, age=Age, country=Country, city=City,
#               languages=Languages, address=Address, phone=Phone,
#               contacts=Contacts, about=About, photo=Photo)

# db.session.add(me)
# db.session.commit()
while len(Profiles.query.all()) > 0:
    db.session.delete(Profiles.query.first())
    db.session.commit()

print([record for record in Profiles.query.all()])
input()
