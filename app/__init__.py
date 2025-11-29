from flask import Flask, Blueprint
import os

app = Flask(__name__)
app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY') or 'a-secret-key' 

from app import routes