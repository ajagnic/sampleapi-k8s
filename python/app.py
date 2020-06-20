from storage.mongo import MongoDB

if __name__ == '__main__':
    print("Running App")
    db_client = MongoDB()
    print(db_client.temp)