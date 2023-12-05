from flask_app.config.mysqlconnection import connectToMySQL, DATABASE
from flask import flash
from flask_app import app
from flask_bcrypt import Bcrypt
bcrypt =Bcrypt(app)

import re

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

class User:
    def __init__(self , data):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.email = data['email']
        self.password = data['password']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    @staticmethod
    def validate_register(data):
        is_valid = True
        if len(data['first_name'] ) < 3 or not data['first_name'].isalpha():
            flash("First Name | Must be atleast 2 characters long | Contains only letters")
            is_valid = False
        if len(data['last_name'] ) < 3 or not data['last_name'].isalpha():
            flash("Last Name | Must be atleast 2 characters long | Contains only letters")
            is_valid = False
        if not EMAIL_REGEX.match(data['email']):
            flash("Email | None Valid Email Address")
            is_valid = False
        if len(data['password']) < 8:
            flash("Password | Must be atleast 8 characters long")
            is_valid = False
        if not data['password'] == data['confirm_password'] or len(data['confirm_password']) < 8:
            flash("Confirm Password | Must match password field")
            is_valid = False

        if not User.get_by_email(data) == False:
            flash("Email | This Email already exists")
            is_valid = False
        return is_valid
    
    @staticmethod
    def validate_login(data):
        is_valid = True
        if not EMAIL_REGEX.match(data['email']):
            flash("Email (Login) | None Valid Email Address")
            is_valid = False
        elif User.get_by_email(data) == False:
            flash("Email (Login) | No user exists with this email ")
            is_valid = False
        if len(data['password']) < 8 or not User.authenticate(data):
            flash("Password (Login) | Invalid Password ")
            is_valid = False
        return is_valid
    
    @classmethod
    def authenticate(cls , data):
        user = User.get_by_email(data)
        if bcrypt.check_password_hash(user.password , data['password']):
            return True
        return False

    @classmethod
    def create(cls , data):
        query = """
            INSERT INTO users (first_name , last_name, email, password) VALUES (%(first_name)s , %(last_name)s, %(email)s, %(password)s);
        """
        result = connectToMySQL(DATABASE).query_db(query , data)
        return result
    
    @classmethod
    def get_by_email(cls , data):
        query = """
            SELECT * FROM users WHERE email = %(email)s;
        """

        result = connectToMySQL(DATABASE).query_db(query , data)
        if result:
            return cls(result[0])
        return False