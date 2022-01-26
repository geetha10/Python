import email
from operator import truediv
from email_validation.config import mysqlconnection
import re
from flask import flash

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$') 

class Email:

    def __init__(self,data):
        self.id=data['id']
        self.email_address=data['email_address']
        self.created_at=data['created_at']
        self.updated_at=data['updated_at']

    @classmethod
    def save(cls, data):
        query="INSERT into email (email_address) VALUES (%(email_address)s)"
        return mysqlconnection.connectToMySQL('email').query_db(query,data)

    @classmethod
    def get_one(cls):
        query="SELECT * FROM email ORDER BY email.id desc Limit 1"
        results = mysqlconnection.connectToMySQL('email').query_db(query)
        return results[0]

    @classmethod
    def get_all_emails(cls):
        query="SELECT * FROM email"
        results = mysqlconnection.connectToMySQL('email').query_db(query)
        emails =[]
        for email in results:
            emails.append(cls(email))
        return emails

    @classmethod
    def delete_one(cls,data):
        query="Delete From email where id = %(id)s"
        return mysqlconnection.connectToMySQL('email').query_db(query,data)

    @staticmethod
    def validate_email(data):
        is_valid = True
        query = "SELECT * FROM email WHERE email_address = %(email_address)s;"
        results = mysqlconnection.connectToMySQL('email').query_db(query,data)
        if len(results) >= 1:
            flash("Email already taken.")
            is_valid=False
        if not EMAIL_REGEX.match(data['email_address']):
            flash("Invalid Email : please try again")   
            is_valid=False
        return is_valid