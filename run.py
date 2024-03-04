from pprint import pprint

from db.models.mongoDB.mongoDBConnections.connection import DBConnectionHandler
from db.models.mongoDB.mongoDbRepository.firstCollectionRepository import FirstCollectionRepository


db_handle = DBConnectionHandler()
db_handle.connect_to_db()
db_conn = db_handle.get_db_connection()

first_collection_repository = FirstCollectionRepository(db_conn)
get_order_number = first_collection_repository.select_one({
    "orderNumber": "7000008312"
})

# first_document = get_order_number[0]
pprint(get_order_number.get("updatedAt"))
# pprint(get_order_number)