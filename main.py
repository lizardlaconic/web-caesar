from flask import Flask, request
from caesar import rotate_string

app = Flask(__name__)
app.config['DEBUG'] = True

#page_header = """
#<!DOCTYPE html>
#<html>
#    <head>
#        <title>FlickList</title>
#    </head>
#    <body>
#        <h1>FlickList</h1>
#"""

#page_footer = """
#    </body>
#</html>
#"""

#add_form = """
#    <form action="/add" method="post">
#        <label>
#            I want to add
#            <input type="text" name="new-movie"/>
#            to my watchlist.
#        </label>
#        <input type="submit" value="Add It"/>
#    </form>
#"""

form="""
<!DOCTYPE html>

<html>
    <head>
        <style>
            form {{
                background-color: #eee;
                padding: 20px;
                margin: 0 auto;
                width: 540px;
                font: 16px sans-serif;
                border-radius: 10px;
            }}
            textarea {{
                margin: 10px 0;
                width: 540px;
                height: 120px;
            }}
        </style>
    </head>
    <body>
      <!-- create your form here -->
      
    <form action="/" method="post">
        <label>Rotate by:
            <input type="text" name="rot" value="0"/>
        </label>
        <label>
            <textarea type="text" name="text">{0}</textarea>
        </label>
        <input type="submit" value="Submit Query"/>
    </form>

    </body>
</html>
"""

#@app.route("/crossoff", methods=['POST'])
#@app.route("/encrypt", methods=['POST'])
@app.route("/", methods=['POST'])
def encrypt():
    #crossed_off_movie = request.form['crossed-off-movie']
    crypt_text=request.form['text']
    crypt_rot=int(request.form['rot'])

    #def rotate_string(text, rot):
    encrypt_text=rotate_string(crypt_text,crypt_rot)

    return "<h1>"+form.format(encrypt_text)+"</h1>"


@app.route("/")
def index():
    return form.format("")

app.run()