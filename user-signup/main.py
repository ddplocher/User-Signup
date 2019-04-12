from flask import Flask, request

app = Flask(__name__)
app.config['DEBUG'] = True

form = """
<!doctype html>
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


@app.route("/")
def index():
    return form

@app.route("/welcome")
def welcome():
    username = request.args.get("username")
    return '<h1>Hello ' + str(username) +'</h1>'
app.run()