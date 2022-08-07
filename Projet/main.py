from flask import Flask
from app import views

app = Flask(__name__, static_url_path="/static")
UPLOAD_FOLDER ='static/uploads/'
# APP CONFIGURATIONS
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
# url

app.add_url_rule('/', 'index', views.index)
app.add_url_rule('/result', 'result', views.result , methods=['GET', 'POST'])
if __name__ == "__main__":
    app.run(threaded=True) 
