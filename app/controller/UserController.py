from datetime import timedelta
from app.model.user import User

from app import response, db
from flask import request
from flask_jwt_extended import *

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