import sqlalchemy as sa


class DB:
    def __init__(self):
        meta = sa.MetaData()
        self.table = sa.Table('Profiles', meta,
            sa.Column('id', sa.Integer, primary_key=True),
            sa.Column('name', sa.String, nullable=False),
            sa.Column('age', sa.Integer),
            sa.Column('country', sa.String),
            sa.Column('city', sa.String),
            sa.Column('languages', sa.String),
            sa.Column('address', sa.String),
            sa.Column('phone', sa.String),
            sa.Column('contacts', sa.String),
            sa.Column('about', sa.String),
            sa.Column('photo', sa.String))
        
        self.engine = sa.create_engine('sqlite:///db/profiles.db', echo=True)
        meta.create_all(self.engine)
        self.conn = self.engine.connect()

    def convert_data(self, record):
        data = {
            "ID": record[0],
            "Name": record[1],
            "Age": record[2],
            "Country": record[3],
            "City": record[4],
            "Languages": record[5],
            "Address": record[6],
            "Phone": record[7],
            "Contacts": record[8],
            "About": record[9],
            "Photo": record[10],
        }
        return data

    def insert_data(self, name, age, country, city, languages, address, phone, contacts, about, photo):
        self.conn.execute(self.table.insert().values(name=name, age=age, country=country,
            city=city, languages=languages, address=address, phone=phone, contacts=contacts, about=about, photo=photo))
    # Make the same everywhere

    def get_record(self, id: int):
        record = self.conn.execute(self.table.select().where(sa.table.c.id == id))
        return self.convert_data(record)

    def view_records_of(self, k):
        records = self.conn.execute(self.table.select().where(sa.table.c.id < k))
        data_list = []
        for id in range(k):
            record = records[id - 1]
            data_list.append(self.convert_data(record))
        return data_list

    def view_records(self):
        records = self.conn.execute(self.table.select())
        data_list = []
        for record in records:
            data_list.append(self.convert_data(record))
        return data_list

    def delete_record(self, id):
        self.conn.execute(self.table.delete().where(sa.table.c.id == id))

    def update_record(self, name, age, country, city, languages, address, phone, contacts, about, photo):
        self.conn.execute(self.table.update().values(name=name, age=age, country=country,
            city=city, languages=languages, address=address, phone=phone, contacts=contacts, about=about, photo=photo))
