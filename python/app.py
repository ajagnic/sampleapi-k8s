import storage.dummy_data
from storage.mongo import MongoDB


if __name__ == '__main__':
    conn_str = "mongodb://admin:admin@db:27017"

    client = MongoDB()
