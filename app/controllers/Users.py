from system.core.controller import *

class Users(Controller):
    def __init__(self, action):
        super(Users, self).__init__(action)
        self.load_model('User')
        self.load_model('Review')

    def index(self):
        return self.load_view('index.html')

    def register(self):
        print "***************** Made it to /users/register ***************"
        info = {
            "first_name" : request.form['first_name'],
            "last_name" : request.form['last_name'],
            "alias" : request.form['alias'],
            "email" : request.form['email'],
            "password" : request.form['password'],
            "confirm_password" : request.form['confirm_password']
        }
        register_status = self.models['User'].create_user(info)
        # print register_status
        if register_status['status'] == False:
            return self.load_view('index.html', errors = register_status['errors'])
        else:
            session['current_user'] = register_status['user']
            return self.load_view('profile.html', user=register_status['user'])


    def login(self):
        info = {
            "email" : request.form['email'],
            "password" : request.form['password']
        }
        login_status = self.models['User'].login_user(info)
        if login_status:
            home_reviews = self.models['Review'].get_reviews_for_home()
            session['current_user'] = login_status
            return self.load_view('home.html', user=login_status, reviews = home_reviews)
        else:
            message = 'We do not have a user with that email and password'
            return self.load_view('index.html', message=message)


    def logout(self):
        print "************ makes it to logout method **************"
        session['current_user'].clear()
        return self.load_view('index.html')


    def go_to_profile(self):
        print "*********** MADE IT TO go_to_profile *****"
        # print session['current_user']
        profile_info = self.models['Review'].get_user_reviews(session['current_user']['email'])
        return self.load_view('profile.html', user_reviews=profile_info)
