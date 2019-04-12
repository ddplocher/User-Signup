from flask import Flask, request

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
        <form action = "/validate" method= "post">
        <label class= "label" for = "username">Username</label>
            <input type = "text" name= "username" value ='{username}'/> 
        </label>
    <p class= 'error'>{username_error}</p>
<br>
    

    <label> Password 
        <input name= "password" type = "password" value ='{password}'/>
    </label>
    <p class = "error">{password_error}</p>

<br>

    <label> Verify Password 
        <input name= "verify_password" type = "password" value ='{password}'/>
    </label>
    <p class = "error">{verify_password_error}</p>
<br>

    <label> Email Address (Optional) 
        <input name= "email_address" type = "text" value ='{email_address}'/>
    </label>
    <p class = "error"> {email_address_error}</p>

<br>

<input type= "submit" value= "Submit"/>
</body>
</form> 

</html>
"""

@app.route("/validate")
def display_form():
    return form.format(username='' ,username_error= '', password= '', password_error= '', verify_password= '', verify_password_error= '', email_address = '', email_address_error= '')

def input_length(input):
    if len(input) > 3 and len(input) < 20:
        return True
    else:
        return False

def check_for_space(input):
    if i in range(len(input)) == '':
        return False
    else:
        return True

@app.route("/validate", methods=['POST'])
def validate_form():

    username = request.form['username']
    password = request.form['password']
    verify_password = request.form['verify_password']
    email_address = request.form['email_address']

    username_error = ''
    password_error = ''
    verify_password_error = ''
    email_address_errror = ''

    if not input_length(username):
        username_error = 'Not a valid username'

    if not input_length(password):
        password_error = 'Not a valid password'

    if not input_length(verify_password):
        validate_password_error = 'not valid password'
    if not username_error and not password_error and not validate_password_error:
        return SUCCESS
    else:
            return form.format(username_error=username_error, password_error = password_error, validate_password_error= validate_password_error)





app.run()