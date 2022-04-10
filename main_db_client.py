import sqlalchemy as sa


class DB:
    def __init__(self):
        meta = sa.MetaData()
        self.table = sa.Table('Event', meta,
            sa.Column('id', sa.Integer, primary_key=True),
            sa.Column('name', sa.String, nullable=False),
            sa.Column('age', sa.Integer),
            sa.Column('country', sa.String),
            sa.Column('languages', sa.String),
            sa.Column('address', sa.String),
            sa.Column('phone', sa.String),
            sa.Column('contacts', sa.String),
            sa.Column('about', sa.String),
            sa.Column('photo', sa.String),
            sa.Column('is_watched', sa.Integer))
        
        self.engine = sa.create_engine('sqlite:///db/profiles.db', echo=True)
        self.table.create(self.engine)
        self.conn = self.engine.connect()

    def convert_data(self, record):
        data = {
            "ID": record[0],
            "Name": record[1],
            "Age": record[2],
            "Country": record[3],
            "Languages": record[4],
            "Address": record[5],
            "Phone": record[6],
            "Contacts": record[7],
            "About": record[8],
            "Photo": record[9],
            "IsWatched": record[10],
        }
        return data

    def insert_data(self, name, age, country, languages, address, phone, contacts, about, photo, is_watched):
        self.conn.execute(self.table.insert().values(name, age, country, languages, address, phone, contacts, about, photo, is_watched))

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

    def update_record(self, name, age, country, languages, address, phone, contacts, about, photo, is_watched):
        self.conn.execute(self.table.update().values(name, age, country, languages, address, phone, contacts, about, photo, is_watched))
