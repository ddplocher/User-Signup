from flask import Flask, request

app = Flask(__name__)
app.config['DEBUG'] = True





form = """
<!doctype html>

<h1><strong> User-Signup<strong></h1>
<html>
    <body>
        <form action ="/welcome">
        <label for = "username">Username</label>
            <input type = "text" name= "username"/>
            <input type = "submit"/>
        </label>
        </form>
    </body>
</html>
    


""" 

password = """
<style>
    .error{{color: purple;}}
</style>

<form method = 'POST'>
    <label> Password 
        <input name= "Password" type = "text"/>
</label>
<input type= "submit" value= "Submit"/>
</form> 
"""

verify_password = """
 <style>
    .error{{color: purple;}}
</style>

<form method = 'POST'>
    <label> Verify Password 
        <input name= "Verify Passord" type = "text"/>
</label>
<input type= "submit" value= "Submit"/>
</form> 
"""

email_address = """
<style>
    .error{{color: purple;}}
</style>

<form method = 'POST'>
    <label> Email Address (Optional) 
        <input name= "Email Address" type = "text"/>
</label>
<input type= "submit" value= "Submit"/>
</form> 
"""


@app.route("/")
def index():

    content = form + password + verify_password + email_address
    return content

@app.route("/welcome")
def welcome():
    username = request.args.get("username")
    return '<h1>Welcome ' + str(username) +'!</h1>'
app.run()