from datetime import timedelta
from app import app
from app.model.user import User
from app.model.media import Media

import os
import uuid

from app import response, db, uploadConfig
from flask import request
from flask_jwt_extended import *
from werkzeug.utils import secure_filename

# add data
def createAdmin():
    try:
        # if using form data
        name = request.form.get('name')
        email = request.form.get('email')
        password = request.form.get('password')
        
        user = User(name=name, email=email, level=1)
        user.setPassword(password)
        
        # push data
        db.session.add(user)
        db.session.commit()
        
        return response.success('', "success to add lecture data!")
    except Exception as e:
        print(e)


# login
def loginAdmin():
    try:
        email = request.form.get('email')
        password = request.form.get('password')
        
        # get user
        userLogin = User.query.filter_by(email=email).first()
        
        # user check
        if not userLogin:
            return response.badRequest('', 'Email is not registered!')
        
        # password check
        if not userLogin.checkPassword(password=password):
            return response.badRequest('', 'Username/password is incorrect!')
        
        data = User.formatObject(userLogin)
        
        expires = timedelta(days=1)
        expires_refresh = timedelta(days=2)
        
        access_token = create_access_token(identity=data, fresh=True, expires_delta=expires)
        refresh_token = create_access_token(data, expires_delta=expires_refresh)
        
        return response.success({
            "data": data,
            "access_token": access_token,
            "refresh_token": refresh_token
        }, "Success login!")
    except Exception as e:
        print(e)


# upload
def upload():
    try:
        title = request.form.get('title')
        
        # check uploaded file
        if 'file' not in request.files:
            return response.badRequest('', 'no file uploaded!')
        
        file = request.files['file']
        
        # check file name
        if file.filename == '':
            return response.badRequest('', 'no file uploaded!')
        
        # check allowed file
        if file and uploadConfig.allowedFiles(file.filename):
            fileName = secure_filename(file.filename)
            renameFile = 'Flask-' + str(uuid.uuid4()) + fileName
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], renameFile))
            
            # push data
            upload = Media(title=title, path_name=renameFile)
            db.session.add(upload)
            db.session.commit()
            
            return response.success(
                {
                    'title': title,
                    'pathName': renameFile
                }, 'Sucess to upload media!'
            )
        else:
            return response.badRequest('', 'file extensions not allowed!')
    except Exception as e:
        print(e)