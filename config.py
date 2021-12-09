import os


class Config(object) :
    SECRET_KEY = os.environ.get('SECRET_KEY') or b'AmgadAbbasEricStock12345678@#$%^&*()Elsayed'
    
