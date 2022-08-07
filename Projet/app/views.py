from flask import render_template, request
from flask import redirect, url_for
import os
from PIL import Image
from app.utils import prediction
#from app.utils import Linear_Svc_model
#from app.utils import Kneighbors_model

UPLOAD_FLODER = 'static/uploads'
SAVE_FOLDER = 'static/files'

def index():
    return render_template('index.html')

   

def result():
 
    if request.method == "POST":
        f = request.files['fichier']
        filename=  f.filename
        path = os.path.join(UPLOAD_FLODER,filename)
        f.save(path)
        ch=prediction(path,filename)
        # prediction (pass to pipeline model)
        return render_template('result.html',fileupload=True,inf=ch)

    return render_template('result.html',fileupload=False,img_name="freeai.png")

