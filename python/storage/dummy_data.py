from random import randint
from time import time

from storage.mongo import MongoDB

records = []
names = [
    'Kitchen','Animal','State', 'Tastey', 'Big','City','Fish', 
    'Pizza','Goat', 'Salty','Sandwich','Lazy', 'Fun'
    ]
company_cuisine = [
    'Pizza', 'Bar Food', 'Fast Food', 'Italian', 'Mexican', 
    'American', 'Sushi Bar', 'Vegetarian'
    ]
company_type = ['LLC','Inc','Company','Corporation']

for x in range(501):
    record = {
        '_id': str(time()),
        'name': names[randint(0, (len(names)-1))] +' '+ names[randint(0, (len(names)-1))] +' '+ company_type[randint(0, (len(company_type)-1))],
        'rating': str(randint(1, 5)),
        'cuisine': company_cuisine[randint(0, (len(company_cuisine)-1))]
    }
    records.append(record)

def insert_dummy_data(conn_str):
    table_name = 'dummy'
    client = MongoDB()
    db_ok = client.try_connect(conn_str)

    if db_ok:
        res = client.insert(table_name, records)
        client.close()
        print("Inserted {0} records".format(len(res)))
