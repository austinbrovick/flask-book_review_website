
from system.core.model import Model
import re
from flask import Flask
from flask.ext.bcrypt import Bcrypt
app = Flask(__name__)
bcrypt = Bcrypt(app)

class Review(Model):
    def __init__(self):
        super(Review, self).__init__()


    def create_review(self, info):
        errors = []
        if not info['title']:
            errors.append('Review must have book title')
        elif len(info['title']) < 2:
            errors.append('Book title must be at least 2 characters')

        if not info['author']:
            errors.append('There must be an author for the book')
        elif len(info['author']) < 4:
            errors.append('Author name must be at least 4 total characters')

        if not info['review']:
            errors.append('Review must have a description')
        elif len(info['review']) < 5:
            errors.append('Review must be at least 5 characters')

        if errors:
            return {"status" : False, "errors" : errors}
        else:
            find_author_query = "SELECT * FROM authors WHERE name = '{}'".format(info['author'])
            authors = self.db.query_db(find_author_query)
            print "********************** PRINTING AUTHORS *******************************"

            # print authors
            find_book_query = "SELECT * FROM books WHERE title = '{}'".format(info['title'])
            books = self.db.query_db(find_book_query)
            print "********************** PRINTING BOOKS *******************************"
            # print books
            print "********************** PRINTING CURRENT USER **********************"
            # print info['current_user_id']
            if authors:
                if books:
                    create_review_query = "INSERT INTO reviews (review, user_id, book_id, created_at, updated_at) VALUES ('{}', '{}', '{}', NOW(), NOW())".format(info['review'], info['current_user_id'], books[0]['id'])
                    self.db.query_db(create_review_query)
                    return {"status" : True}
                else:
                    create_book_query = "INSERT INTO books (title, author_id, created_at, updated_at) VALUES ('{}', '{}', NOW(), NOW())".format(info['title'], authors[0]['id'])
                    self.db.query_db(create_book_query)
                    create_review_query_for_new_book = "INSERT INTO reviews (review, user_id, book_id, created_at, updated_at) VALUES ('{}', '{}', '{}', NOW(), NOW())".format(info['review'], info['current_user_id'], info['title'])
                    self.db.query_db(create_review_query_for_new_book)
                    return {"status" : True}
            else:
                # creates author
                create_author_query = "INSERT INTO authors (name, created_at, updated_at) VALUES ('{}', NOW(), NOW())".format(info['author'])
                self.db.query_db(create_author_query)
                # gets the author of the current book by using a SELECT statement
                get_current_author = "SELECT * FROM authors WHERE name = '{}'".format(info['author'])
                current_author = self.db.query_db(get_current_author)
                #creates the book in the database
                create_current_book_query = "INSERT INTO books (title, author_id, created_at, updated_at) VALUES ('{}', '{}', NOW(), NOW())".format(info['title'], current_author[0]['id'])
                self.db.query_db(create_current_book_query)
                #gets book from database query
                get_current_book_query = "SELECT * FROM books WHERE title = '{}'".format(info['title'])
                current_book = self.db.query_db(get_current_book_query)



                create_review_query_for_new_book = "INSERT INTO reviews (review, user_id, book_id, created_at, updated_at) VALUES ('{}', '{}', '{}', NOW(), NOW())".format(info['review'], info['current_user_id'], current_book[0]['id'])
                self.db.query_db(create_review_query_for_new_book)
                return {"status" : True}


    def get_user_reviews(self, email):
        "********************** GETTTING ALL REVIEWS FOR CURRENT USER ******************"
        get_reviews_for_user_query = "SELECT reviews.id as review_primary_id, reviews.review, reviews.created_at as review_created_at, reviews.book_id, reviews.user_id, users.first_name, users.last_name, users.id as user_primary_id, books.id as book_primary_id, books.title, books.author_id,  authors.id as author_primary_id, authors.name FROM reviews LEFT JOIN users ON users.id = reviews.user_id LEFT JOIN books ON books.id = reviews.book_id LEFT JOIN authors ON authors.id = books.author_id WHERE users.email = '{}'".format(email)
        reviews_for_current_user = self.db.query_db(get_reviews_for_user_query)
        print "******************* PRINTING THE REVIEWS FOR THE CURRENT USER *******************"
        # print reviews_for_current_user
        return reviews_for_current_user




    def get_reviews_for_this_book(self, book_id):
        print "************** GETTTING THE REVIEWS FOR THIS CURRENT BOOK *************"
        get_reviews_for_user_query = "SELECT reviews.id as review_primary_id, reviews.review, reviews.created_at as review_created_at, reviews.book_id, reviews.user_id, users.first_name, users.last_name, users.id as user_primary_id, books.id as book_primary_id, books.title, books.author_id,  authors.id as author_primary_id, authors.name FROM reviews LEFT JOIN users ON users.id = reviews.user_id LEFT JOIN books ON books.id = reviews.book_id LEFT JOIN authors ON authors.id = books.author_id WHERE books.id = '{}'".format(book_id)
        reviews_for_current_book = self.db.query_db(get_reviews_for_user_query)
        return reviews_for_current_book




    def get_reviews_for_home(self):
        get_reviews_for_home_query = "SELECT reviews.id as review_primary_id, reviews.review, reviews.created_at as review_created_at, reviews.book_id, reviews.user_id, users.first_name, users.last_name, users.id as user_primary_id, books.id as book_primary_id, books.title, books.author_id,  authors.id as author_primary_id, authors.name FROM reviews LEFT JOIN users ON users.id = reviews.user_id LEFT JOIN books ON books.id = reviews.book_id LEFT JOIN authors ON authors.id = books.author_id ORDER BY reviews.created_at DESC LIMIT 3"
        reviews_for_home = self.db.query_db(get_reviews_for_home_query)
        return reviews_for_home



    def get_all(self):
         get_books = "SELECT reviews.id as review_primary_id, reviews.review, reviews.created_at as review_created_at, reviews.book_id, reviews.user_id, users.first_name, users.last_name, users.id as user_primary_id, books.id as book_primary_id, books.title, books.author_id,  authors.id as author_primary_id, authors.name FROM reviews LEFT JOIN users ON users.id = reviews.user_id LEFT JOIN books ON books.id = reviews.book_id LEFT JOIN authors ON authors.id = books.author_id"
         books = self.db.query_db(get_books)
         return books

    def delete_this_review(self, review_id):
        delete_query = "DELETE FROM reviews WHERE reviews.id = '{}' LIMIT 1".format(review_id)
        self.db.query_db(delete_query)
        return True








