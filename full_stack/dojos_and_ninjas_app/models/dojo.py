from flask import redirect
from config.mysqlconnection import connectToMySQL;

class Dojo:
    def __init__(self,data):
        self.id=data['id']
        self.name=data['name']
        self.created_at=data['created_at']
        self.updated_at=data['updated_at']
    

    @classmethod
    def get_all_dojos(cls):
        query = "SELECT * FROM dojos;"
        results = connectToMySQL('dojos_and_ninjas').query_db(query)
        print(results)
        dojos=[]
        for dojo in results:
            print("Current element", dojo)
            dojos.append(cls(dojo))
        print("Final Dojos sfter For loop: ", dojos)
        return dojos
    
    @classmethod
    def get_all_dojo_names(cls):
        query = "SELECT * from dojos join ninja on ninjas.dojo_id=dojo.id group by dojo.id"
        results = connectToMySQL('dojos_and_ninjas').query_db(query)
        dojos=[]
        for dojo in results:
            dojos.append(cls(dojo))
        return dojo