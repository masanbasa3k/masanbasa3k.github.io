from flask import Blueprint, render_template, send_file
import requests

auth = Blueprint('auth', __name__)

@auth.route('/about')
def about():
    url = "https://api.github.com/users/masanbasa3k/repos"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        return render_template("about.html", repositories=data)
    else:
        return "An error occurred: {}".format(response.text)  
