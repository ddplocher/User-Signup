from flask import Flask, request, redirect

app = Flask(__name__)
app.config['DEBUG'] = True


form = """
<!DOCTYPE html>
<html>

<style>
    .error {{ color: purple; }}
</style>

<h1><strong> Signup <strong></h1>
<html>
    <body>
        <form method= 'POST'>
        <label class= "label" for = "username">Username</label>
            <input type = "text" name= "username" value ='{username}'/> 
        </label>
    <p class= 'error'>{username_error}</p>

    

    <label> Password 
        <input name= "password" type = "password" value ='{password}'/>
    </label>
    <p class = "error">{password_error}</p>



    <label> Verify Password 
        <input name= "verify_password" type = "password" value ='{verify_password}'/>
    </label>
    <p class = "error">{verify_password_error}</p>


    <label> Email Address (Optional) 
        <input name= "email_address" type = "text" value ='{email_address}'/><p class = "error"> {email_address_error}</p>
    
    </label>



<input type= "submit" value= "Submit"/>
</body>
</form> 

</html>
"""

@app.route("/validate_form")
def display_form():
    return form.format(username='' ,username_error= '', password='', password_error='', verify_password='', verify_password_error='',email_address='', email_address_error='')

def input_length(input):
    if len(str(input)) > 2 and len(str(input)) < 19:
        return True
    else:
        return False


#not working, fix
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
           

@app.route("/validate_form", methods=['POST'])
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
    else:
        if not check_for_space(password):
            password_error = 'Not valid password (spaces)'

    if not input_length(verify_password):
        verify_password_error = 'Not valid password length (3-20 charectors)'
    
    if not password_check(password, verify_password):
        password_error = 'password and verify password did not match'
        verify_password_error = 'password and verify password did not match'

    if not username_error and not password_error and not verify_password_error:
        
        return redirect('/valid_login')
    else:
        return form.format(email_address_error= email_address_error, email_address= email_address, password= password, password_error= password_error, verify_password= verify_password, verify_password_error= verify_password_error, username_error= username_error, username=username)
    


@app.route('/valid_login')
def valid_login():
    
    return '<h1> Welcome</h1>'


               
    
    

app.run()