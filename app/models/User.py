
from system.core.model import Model
import re
from flask import Flask
from flask.ext.bcrypt import Bcrypt
app = Flask(__name__)
bcrypt = Bcrypt(app)

class User(Model):
    def __init__(self):
        super(User, self).__init__()

    def create_user(self, info):
        EMAIL_REGEX = re.compile(r'^[a-za-z0-9\.\+_-]+@[a-za-z0-9\._-]+\.[a-za-z]*$')
        errors = []
        if not info['first_name']:
            errors.append('First name cannot be blank!')
        elif len(info['first_name']) < 2:
            errors.append('Name must be at least 2 characters long')

        if not info['last_name']:
            errors.append('Last name cannot be blank')
        elif len(info['last_name']) < 2:
            erorrs.append('Last name must be at least 2 characters long')


        if not info['alias']:
            errors.append('Please provide an alias')
        elif len(info['alias']) < 6:
            errors.append('Alias must be longer than 5 characters')


        if not info['email']:
            errors.append('Email cannot be blank')
        elif not EMAIL_REGEX.match(info['email']):
            errors.append('Email must be valid!')

        if not info['password']:
            errors.append('Password cannt be blank')
        elif len(info['password']) < 8:
            errors.append('Password must be greater than 7 characters')
        elif info['password'] != info['confirm_password']:
            errors.append('Password and confirmation must match!')


        if errors:
            return {"status" : False, "errors" : errors}
        else:
            encrypted_password = bcrypt.generate_password_hash(info['password'])
            insert_query = "INSERT INTO users (first_name, last_name, alias, email, encrypted_password, created_at, updated_at) VALUES ('{}', '{}', '{}', '{}', '{}', NOW(), NOW())".format(info['first_name'], info['last_name'], info['alias'], info['email'], encrypted_password)
            self.db.query_db(insert_query)
            get_user_query = "SELECT * FROM users ORDER BY id DESC LIMIT 1"
            users = self.db.query_db(get_user_query)
            return {"status" : True, "user" : users[0]}

    def login_user(self, info):
        password = info['password']
        user_query = "SELECT * FROM users WHERE email = '{}' LIMIT 1".format(info['email'])
        users = self.db.query_db(user_query)
        print "printing users *************"
        # print users
        if users:
            if self.bcrypt.check_password_hash(users[0]['encrypted_password'], password):
                return users[0]
        return False


    def get_user_reviews(self, info):
        "********************** GETTTING ALL REVIEWS FOR CURRENT USER ******************"
        get_reviews_for_user_query = "SELECT reviews.id as review_primary_id, reviews.review, reviews.created_at as review_created_at, reviews.book_id, reviews.user_id, users.first_name, users.last_name, users.id as user_primary_id, books.id as book_primary_id, books.title, books.author_id,  authors.id as author_primary_id, authors.name FROM reviews LEFT JOIN users ON users.id = reviews.user_id LEFT JOIN books ON books.id = reviews.book_id LEFT JOIN authors ON authors.id = books.author_id WHERE users.email = '{}'".format(info['email'])
        reviews_for_current_user = self.db.query_db(get_reviews_for_user_query)
        print "******************* PRINTING THE REVIEWS FOR THE CURRENT USER *******************"
        # print reviews_for_current_user
        return reviews_for_current_user







