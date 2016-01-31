"""
    Database Specific Configuration File
"""
""" Put Generic Database Configurations here """
class DBConfig(object):
    """ DB_ON must be True to use the DB! """
    DB_ON = True    #turn database on
    DB_DRIVER = 'mysql'
    DB_ORM = False

""" Put Development Specific Configurations here """
class DevelopmentDBConfig(DBConfig):
    DB_USERNAME = 'root'
    DB_PASSWORD = 'root'
    DB_DATABASE_NAME = 'book_review_red_belt_prep' #change name here
    DB_HOST = 'localhost'
    DB_PORT = 8889      #make sure root is correct
    """ unix_socket is used for connecting with MAMP. Take this out if you aren't using MAMP """
    DB_OPTIONS = {
        'unix_socket': '/Applications/MAMP/tmp/mysql/mysql.sock'
    }

""" Put Staging Specific Configurations here """
class StagingDBConfig(DBConfig):
    DB_USERNAME = 'root'
    DB_PASSWORD = 'root'
    DB_DATABASE_NAME = 'book_review_red_belt_prep' #change name here
    DB_HOST = 'localhost'

""" Put Production Specific Configurations here """
class ProductionDBConfig(DBConfig):
    DB_USERNAME = 'root'
    DB_PASSWORD = 'root'
    DB_DATABASE_NAME = 'book_review_red_belt_prep' #change name here
    DB_HOST = 'localhost'
