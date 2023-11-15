import os
from dotenv import load_dotenv


basedir = os.path.abspath(os.path.dirname(__file__))

load_dotenv(os.path.join(basedir, '.env'))


# class Config():

#     """
#     Set Config variables for our flask app.
#     Using Environment variables where available otherwise
#     Create config variables.

#     """

#     FLASK_APP = os.environ.get('FLASK_APP')
#     FLASK_ENV = os.environ.get('FLASK_ENV')
#     FLASK_DEBUG = True
#     SECRET_KEY = os.environ.get('SECRET_KEY') or "Don't tell secrets"

class Config():

    """
    Create Config class which will setup our configuration variables.
    Using Environment variables where available other create config variables. 
    """

    #regular configuration for Flask App
    FLASK_APP = os.environ.get('FLASK_APP') 
    FLASK_ENV = os.environ.get('FLASK_ENV') 
    FLASK_DEBUG = os.environ.get('FLASK_DEBUG')

    #configuration if you are connecting a database
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'Literally whatever you want as long as its a string. Cool Beans'
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or 'sqlite:///' + os.path.join(basedir, 'app.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False