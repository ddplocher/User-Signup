from flask import Flask, request, redirect
import cgi
import os
import jinja2

template_dir = os.path.join(os.path.dirname(__file__), 'templates')
jinja_env = jinja2.Environment(loader = jinja2.FileSystemLoader(template_dir))



app = Flask(__name__)
app.config['DEBUG'] = True


@app.route("/")
def display_form():
    template = jinja_env.get_template('form.html')
    return template.render()

def input_length(input):
    if len(str(input)) > 2 and len(str(input)) < 19:
        return True
    else:
        return False


def check_for_space(name): 
    new_name = name.replace(" ", "MM")
    if len(new_name) == len(name):
        return True
    else: 
        return False
            
            
def password_check(password, verify_password):
    if str(password) == str(verify_password):
        return True
    else:
        return False

def check_email(email_address):
    new_email_address = email_address.replace ("@", "")
    end_email_address = new_email_address.replace(".", "")
    if len(end_email_address) == len(email_address)-2:
        return True
    else:
        return False
           

@app.route("/", methods=['POST'])
def validate_form():

    username = request.form['username']
    username_error = ''
    password = request.form['password']
    password_error = ''
    verify_password = request.form['verify_password']
    verify_password_error = ''
    email_address = request.form['email_address']
    email_address_error = ''

    if not check_for_space(email_address):
        email_address_error = 'Not valid email address (spaces)'
    else: 
        if not check_email(email_address):
            email_address_error = 'Not valid email address(must have "@" and ".")'
    
    if not input_length(email_address):
            email_address_error = 'Not valid email length (3-20 charectors)'
    
    if not check_for_space(username):
        username_error = 'Not valid username (spaces)'
    else:
        if not input_length(username):
            username_error = 'Not valid username length (3-20 charectors)'
    
    if not input_length(password):
        password_error = 'Not valid password length (3-20 charectors)'
        password = ''
    else:
        if not check_for_space(password):
            password_error = 'Not valid password (spaces)'
            password= ''

    if not input_length(verify_password):
        verify_password_error = 'Not valid password length (3-20 charectors)'
        verify_password =''
    
    if not password_check(password, verify_password):
        password_error = 'password and verify password did not match'
        verify_password_error = 'password and verify password did not match'
        password = ''
        verify_password = ''

    if not username_error and not password_error and not verify_password_error:
        
        return redirect('/valid_login?username={0}'.format(username))
    else:
        template = jinja_env.get_template('form.html')
        return template.render(email_address_error= email_address_error, email_address= email_address, password= password, password_error= password_error, verify_password= verify_password, verify_password_error= verify_password_error, username_error= username_error, username=username)
    


@app.route("/valid_login")
def valid_login():
    name = request.args.get('username')
    template = jinja_env.get_template('welcome.html')
    return template.render(name=name)


app.run()