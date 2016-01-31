from system.core.router import routes



"""
    routes['GET']['/users'] = 'users#index'
    routes['GET']['/users/new'] = 'users#new'
    routes['POST']['/users'] = 'users#create'
    routes['GET']['/users/<int:id>'] = 'users#show'
    routes['GET']['/users/<int:id>/edit' = 'users#edit'
    routes['PATCH']['/users/<int:id>'] = 'users#update'
    routes['DELETE']['/users/<int:id>'] = 'users#destroy'
"""
routes['default_controller'] = 'Users'

#route for login
routes['POST']['/users/login'] = 'Users#login'

#route for register
routes['POST']['/users/register'] = 'Users#register'



#route for logging out user
routes['/users/logout'] = 'Users#logout'

#route for going to add a book review page
routes['/reviews/go_to_add_review'] = 'Reviews#index'

routes['POST']['/reviews/create_review'] = 'Reviews#new_review'

# routes['/go_to_profile'] = 'Users#render_profile'


routes['/reviews/book_review/<book_id>'] = 'Reviews#get_a_books_reviews'

routes['/users/home'] = 'Reviews#get_home_reviews'



routes['/users/profile'] = 'Users#go_to_profile'


routes['POST']['/reviews/delete/<review_id>'] = 'Reviews#delete_review'
