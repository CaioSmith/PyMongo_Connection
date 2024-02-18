from bson.objectid import ObjectId
from typing import List, Dict


class FirstCollectionRepository:
    def __init__(self, db_conn: str) -> None:
        self.__collection_name = "FirstCollection"
        self.__db_conn = db_conn
        
        
    def insert_doc(self, document: Dict) -> Dict:
        collection = self.__db_conn.get_collection(self.__collection_name)
        collection.insert_one(document)
        return document
        
        
    def insert_list_docs(self, doc_list: List[Dict]) -> List[Dict]:
        collection = self.__db_conn.get_collection(self.__collection_name)
        collection.insert_many(doc_list)
        return doc_list
    
    
    def select_many(self, _filter) -> List[Dict]:
        collection = self.__db_conn.get_collection(self.__collection_name)
        data = collection.find(
            _filter,
            {"_id": 0}
        )
        response = [elem for elem in data]
        return response
    
        
    def select_one(self, _filter) -> Dict:
        collection = self.__db_conn.get_collection(self.__collection_name)
        response = collection.find_one(
            _filter, 
            {"_id": 0}
        )
        return response
        
        
    def select_prop(self, _property: str) -> Dict:
        collection = self.__db_conn.get_collection(self.__collection_name)
        data = collection.find(
            {f"{_property}": {"$exists": True}}
        )
        response = [elem for elem in data]
        return response
    
    
    def select_any_prop(self, _propertys: List[Dict] = Dict) -> Dict:
        collection = self.__db_conn.get_collection(self.__collection_name)
        data = collection.find(
            {"$or": _propertys}
        )
        response = [elem for elem in data]
        return response
    
    
    def select_by_id(self, _id: str) -> Dict:
        collection = self.__db_conn.get_collection(self.__collection_name)
        data = collection.find(
            {"_id": ObjectId(_id)},
        )
        for elem in data: return elem
        
