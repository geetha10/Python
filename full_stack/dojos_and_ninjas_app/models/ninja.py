from flask import redirect
from config.mysqlconnection import connectToMySQL;

class Ninja:
    def __init__(self,data):
        self.id=data['id']
        self.first_name=data['first_name']
        self.last_name=data['last_name']
        self.age=data['age']
        self.dojo_id=data['dojo_id']
        self.created_at=data['created_at']
        self.updated_at=data['updated_at']

    @classmethod
    def get_all_ninjas_by_id(cls,id):
        query = "SELECT * FROM ninjas where dojo_id=%(id)s;"
        data={'id':id}
        results = connectToMySQL('dojos_and_ninjas').query_db(query,data)
        print(results)
        ninjas=[]
        for ninja in results:
            ninjas.append(cls(ninja))
        return ninjas