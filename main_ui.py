from flask import Flask
import login_operations as login_op

app = Flask(__name__)

# We can render basic HTML from flask methods
# The flag before a function sets the route that will trigger the function
# Whatever is returned by the function will be rendered in the page

@app.route('/')
def index():
    return '<h1>Hello World</h1>'

@app.route('/users')
def users_list():
    login_obj = login_op.LoginPage()
    usernames = login_obj.return_accounts()
    render = '<h1>Users: </h1>'

    render = render + '<ul>'
    for user in usernames:
        render = render + '<li>' + user + '</li>'

    render = render + '</ul>'

    return render
