from system.core.controller import *

class Reviews(Controller):
    def __init__(self, action):
        super(Reviews, self).__init__(action)
        self.load_model('Review')

    def index(self):
        return self.load_view('add_review.html')


    def new_review(self):
        info = {
            "title" : request.form['title'],
            "author" : request.form['author'],
            "review" : request.form['description'],
            "rating" : request.form['rating'],
            "current_user_id" : session['current_user']['id']
        }
        review_status = self.models['Review'].create_review(info)
        # print review_status
        if review_status['status'] == False:
            return self.load_view('add_review.html', errors=review_status['errors'])
        else:
            user_reviews = self.models['Review'].get_user_reviews(session['current_user']['email'])
            return self.load_view('profile.html', user_reviews=user_reviews)



    def get_a_books_reviews(self, book_id):
        print "********** MADE IT TO get_a_books_reviews ****************"
        reviews_for_this_book = self.models['Review'].get_reviews_for_this_book(book_id)



        # get_book_title = "SELECT title FROM books WHERE books.id = '{}'".format(book_id)
        # book_title = self.db.query_db(get_book_title)
        return self.load_view('one_books_reviews.html', reviews=reviews_for_this_book)



    def get_home_reviews(self):
        reviews_for_home = self.models['Review'].get_reviews_for_home()
        all_books = self.models['Review'].get_all()
        return self.load_view('home.html', reviews = reviews_for_home, reviews_all=all_books)


    def delete_review(self, review_id):
        print "************ MADE IT TO DELETE REVIEW ******************"
        # self.models['Review'].delete_this_review(review_id)
        self.models['Review'].delete_this_review(review_id)



        reviews_for_home = self.models['Review'].get_reviews_for_home()
        all_books = self.models['Review'].get_all()
        return self.load_view('home.html', reviews = reviews_for_home, reviews_all=all_books)
