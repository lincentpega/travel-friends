import main_db_client


db = main_db_client.DB()

ID = 0
Name = "Margot"
Age = 31
Country = "USA"
Languages = "English, Русский"
Address = "San-Francisco, Juvenile str, h. 41"
Phone = "88005553535"
Contacts = "vk.com/blank_page, someaddress@rundex.org"
About = "Australian actress and producer. Has received several accolades throughout her career, including nominations for two Academy Awards, three Golden Globe Awards, five Screen Actors Guild Awards and five British Academy Film Awards. Time magazine named me one of the 100 most influential people in the world in 2017 and I was ranked as one of the world's highest-paid actresses by Forbes in 2019."
Photo = "0.png"


db.insert_data(Name, Age, Country, Languages, Address, Phone, Contacts, About, Photo)

print([record for record in main_db_client.view_records()])
