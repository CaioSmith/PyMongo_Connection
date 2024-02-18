from pprint import pprint

from db.models.mongoDB.mongoDBConnections.connection import DBConnectionHandler
from db.models.mongoDB.mongoDbRepository.firstCollectionRepository import FirstCollectionRepository


db_handle = DBConnectionHandler()
db_handle.connect_to_db()
db_conn = db_handle.get_db_connection()

first_collection_repository = FirstCollectionRepository(db_conn)
