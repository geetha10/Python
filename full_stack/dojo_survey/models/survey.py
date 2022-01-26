from config.mysqlconnection import connectToMySQL

from flask import flash

class Survey:

    def __init__(self,data):
        self.name=data['name']
        self.location=data['location']
        self.language=data['language']
        self.comment=data['comment']

    @classmethod
    def save(cls,data):
        query = "INSERT into dojos (name,location,language,comment) VALUES (%(name)s,%(location)s,%(language)s,%(comment)s);"
        return connectToMySQL('dojo_survey').query_db(query,data)

    @classmethod
    def get_last_survey(cls):
        query = "SELECT * FROM dojos ORDER BY dojos.id DESC LIMIT 1;"
        results = connectToMySQL('dojo_survey').query_db(query)
        print("result is: ",results)
        return cls(results[0])

    @staticmethod
    def validate_survey(survey):
        is_valid = True
        if len(survey['name']) < 3:
            flash("Name must be at least 3 characters.")
            is_valid = False
        
        if len(survey['location']) < 3:
            flash("Location must be at least 3 characters.")
            is_valid = False

        if len(survey['language']) < 1:
            flash("Language must be at least 1 character.")
            is_valid = False

        if len(survey['comment']) < 3:
            flash("Comment must be at least 3 characters.")
            is_valid = False
        return is_valid