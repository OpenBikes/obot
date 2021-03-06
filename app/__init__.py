from flask import Flask, url_for

NAMESPACE = 'obot'

app = Flask(NAMESPACE)

# Setup the application
app.config.from_object('app.config')

# Add the top level to the import path
import sys
sys.path.append('..')

# import dotenv
# dotenv.load_dotenv(dotenv.find_dotenv())

from app import api
