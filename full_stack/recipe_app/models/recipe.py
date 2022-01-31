from recipe_app.config import mysqlconnection
from flask import flash

class Recipe:
    db = "recipes_db"

    def __init__(self,data) :
        self.id=data['id']
        self.name=data['name']
        self.description=data['description']
        self.instructions=data['instructions']
        self.under30=data['under30']
        self.users_id=data['users_id']
        self.date_made=data['date_made']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    @classmethod
    def get_all_recipes(cls):
        print("Inside REcipe class")
        query = "SELECT * FROM recipes;"
        results = mysqlconnection.connectToMySQL(cls.db).query_db(query)
        recipes =[]
        for recipe in results:
            recipes.append(cls(recipe))
        return recipes

    @classmethod
    def get_all_recipes_id(cls,id):
        query ="SELECT * FROM recipes WHERE id= %(id)s"
        data={
            'id':id
        }
        results = mysqlconnection.connectToMySQL(cls.db).query_db(query,data)
        print("Results from DB", results)
        if len(results) < 1:
            return False
        return cls(results[0])

    @classmethod
    def get_all_recipes_by_userId(cls,data):
        query ="SELECT * FROM recipes WHERE user_id= %(id)s"
        results = mysqlconnection.connectToMySQL(cls.db).query_db(query,data)
        if len(results) < 1:
            return False
        return cls(results[0])

    @classmethod
    def add_recipe(cls,data):
        query = """INSERT INTO recipes (name, description, instructions, under30, date_made ,users_id) 
        VALUES(%(name)s,%(description)s,%(instructions)s,%(under30)s,%(date_made)s,%(user_id)s)"""
        return mysqlconnection.connectToMySQL(cls.db).query_db(query,data)

    @classmethod
    def update_recipe(cls, data):
        query = """UPDATE recipes SET name=%(name)s, description=%(description)s, instructions=%(instructions)s, 
        under30=%(under30)s, date_made=%(date_made)s,updated_at=NOW() WHERE id = %(id)s;"""
        print("Update Query: ",query)
        return mysqlconnection.connectToMySQL(cls.db).query_db(query,data)
    
    @classmethod
    def delete_recipe(cls,data):
        query = "DELETE FROM recipes WHERE id = %(id)s;"
        return mysqlconnection.connectToMySQL(cls.db).query_db(query,data)