from pymongo import MongoClient


class MongoDB:

    def try_connect(self, conn_str):
        self.client = MongoClient(conn_str)
        db_ok = True
        try:
            self.client.admin.command('ismaster')
        except:
            db_ok = False
        else:
            self.db = self.client.app
        return db_ok

    def close(self):
        self.client.close()
    
    def insert(self, table_name, records_list):
        update = self.db[table_name].insert_many(records_list)
        return update.inserted_ids

    def get(self, table_name, query_dict):
        records = []
        for row in self.db[table_name].find(query_dict):
            records.append(row)
        return records

    def update(self, table_name, query_dict, new_record):
        update = self.db[table_name].update_one(query_dict, {'$set': new_record})
        return update.raw_result

    def delete(self, table_name, query_dict):
        delete = self.db[table_name].delete_many(query_dict)
        return delete.raw_result
